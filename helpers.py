import io
import re
import pandas as pd
import pdfplumber
from fuzzywuzzy import fuzz
from dateutil import parser

NUM_RE = re.compile(r'([+-]?\d{1,3}(?:[,.\s]\d{3})*(?:\.\d+)?|\d+(?:\.\d+)?)')

FIN_KEYWORDS = {
    'revenue': ['revenue', 'sales', 'turnover', 'total revenue'],
    'profit': ['profit', 'net income', 'net profit', 'profit after tax', 'PAT', 'net earnings'],
    'expense': ['expense', 'expenses', 'operating expenses', 'cost of sales', 'cost of goods'],
    'assets': ['asset', 'assets', 'total assets'],
    'liabilities': ['liabilities','liability','total liabilities'],
    'cash': ['cash', 'cash flow', 'net cash', 'cash and cash equivalents'],
}

def extract_from_pdf(file_bytes):
    texts = []
    tables = []
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""
            texts.append((i, text))
            try:
                page_tables = page.extract_tables()
            except Exception:
                page_tables = []
            for t_idx, table in enumerate(page_tables, start=1):
                df = pd.DataFrame(table)
                df = df.dropna(axis=0, how='all').dropna(axis=1, how='all')
                if not df.empty:
                    tables.append({'page': i, 'table_index': t_idx, 'df': df})
    return texts, tables

def extract_from_excel(file_bytes):
    excel_io = io.BytesIO(file_bytes)
    xls = pd.ExcelFile(excel_io)
    sheets = []
    for sheet in xls.sheet_names:
        try:
            df = xls.parse(sheet_name=sheet, header=None)
            df = df.dropna(how='all', axis=0).dropna(how='all', axis=1)
            if not df.empty:
                sheets.append({'sheet': sheet, 'df': df})
        except Exception:
            continue
    return sheets

def find_numbers_near_keyword(text, keyword):
    results = []
    for m in re.finditer(re.escape(keyword), text, flags=re.I):
        start = max(0, m.start() - 150)
        end = m.end() + 150
        snippet = text[start:end]
        nums = NUM_RE.findall(snippet)
        results.extend(nums)
    return results

def df_search_for_keyword(df, keywords):
    found = []
    str_df = df.fillna('').astype(str)
    rows, cols = str_df.shape
    for r in range(rows):
        for c in range(cols):
            cell = str_df.iat[r, c]
            for kw in keywords:
                if kw.lower() in cell.lower():
                    for cc in range(c+1, min(c+6, cols)):
                        candidate = str_df.iat[r, cc]
                        m = NUM_RE.search(candidate)
                        if m:
                            found.append((m.group(0), (r, cc), kw))
                    for rr in range(r+1, min(r+6, rows)):
                        candidate = str_df.iat[rr, c]
                        m = NUM_RE.search(candidate)
                        if m:
                            found.append((m.group(0), (rr, c), kw))
    return found

def answer_question(question, pdf_texts, pdf_tables, excel_sheets):
    q = question.lower()
    detected = []
    for field, kws in FIN_KEYWORDS.items():
        for kw in kws:
            if kw in q:
                detected.append((field, kw))

    answers = []
    sources = []

    for t in pdf_tables:
        df = t['df']
        page = t.get('page')
        for field, kw in detected:
            finds = df_search_for_keyword(df, FIN_KEYWORDS[field])
            for val, pos, matched_kw in finds:
                answers.append(f"{field.title()}: {val} (PDF page {page})")
                sources.append({'pdf_page': page})

    for s in excel_sheets:
        df = s['df']
        sheet = s.get('sheet')
        for field, kw in detected:
            finds = df_search_for_keyword(df, FIN_KEYWORDS[field])
            for val, pos, matched_kw in finds:
                answers.append(f"{field.title()}: {val} (Excel sheet {sheet})")
                sources.append({'excel_sheet': sheet})

    for page_no, text in pdf_texts:
        for field, kw in detected:
            nums = find_numbers_near_keyword(text, kw)
            if nums:
                answers.append(f"{field.title()}: {nums[0]} (PDF page {page_no})")
                sources.append({'pdf_page': page_no})

    if not answers:
        return {'answer': "No matching financial data found.", 'sources': []}

    return {'answer': "\n".join(dict.fromkeys(answers)), 'sources': sources}
