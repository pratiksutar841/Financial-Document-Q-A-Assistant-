import streamlit as st
from helpers import extract_from_pdf, extract_from_excel, answer_question

# Page config
st.set_page_config(page_title="Financial Q&A", layout="wide")

# Page header
st.markdown("""
    <h1 style='text-align: center; color: #1f77b4;'>📊 Financial Document Q&A Assistant</h1>
    <p style='text-align: center; font-size: 16px;'>Upload your financial PDFs or Excel files and ask questions</p>
""", unsafe_allow_html=True)

# Initialize session state
if 'pdf_texts' not in st.session_state:
    st.session_state['pdf_texts'] = []
    st.session_state['pdf_tables'] = []
    st.session_state['excel_sheets'] = []

# File uploader section
with st.expander("📂 Upload Files", expanded=True):
    uploaded_files = st.file_uploader(
        "Upload PDF or Excel files",
        type=['pdf', 'xls', 'xlsx'],
        accept_multiple_files=True
    )

if uploaded_files:
    st.session_state['pdf_texts'] = []
    st.session_state['pdf_tables'] = []
    st.session_state['excel_sheets'] = []

    for file in uploaded_files:
        data = file.read()
        with st.spinner(f"Processing {file.name}..."):
            if file.name.lower().endswith('.pdf'):
                texts, tables = extract_from_pdf(data)
                st.session_state['pdf_texts'].extend(texts)
                st.session_state['pdf_tables'].extend(tables)
                st.success(f"✅ Extracted {len(tables)} tables from {file.name}")
            else:
                sheets = extract_from_excel(data)
                st.session_state['excel_sheets'].extend(sheets)
                st.success(f"✅ Extracted {len(sheets)} sheets from {file.name}")

# Question input
with st.container():
    st.markdown("### ❓ Ask a Question")
    question = st.text_input("E.g., 'What is total revenue in 2023?'", key="question_input")
    get_answer = st.button("Get Answer", key="get_answer")

# Answer section
if get_answer:
    if question:
        with st.spinner("Generating answer..."):
            result = answer_question(
                question,
                st.session_state['pdf_texts'],
                st.session_state['pdf_tables'],
                st.session_state['excel_sheets']
            )
        st.markdown("### 💡 Answer")
        st.success(result['answer'])
        
        if result['sources']:
            with st.expander("📑 Sources", expanded=False):
                for src in result['sources']:
                    st.write(f"- {src}")
    else:
        st.warning("⚠️ Please enter a question before requesting an answer.")

# Optional: Show extracted content
with st.expander("🗂 View Extracted Content", expanded=False):
    if st.session_state['pdf_texts']:
        st.markdown("**PDF Texts:**")
        for idx, text in enumerate(st.session_state['pdf_texts']):
            st.write(f"{idx+1}. {text[:150]}{'...' if len(text) > 150 else ''}")
    
    if st.session_state['pdf_tables']:
        st.markdown("**PDF Tables:**")
        for idx, table in enumerate(st.session_state['pdf_tables']):
            st.write(f"Table {idx+1}")
            st.dataframe(table)
    
    if st.session_state['excel_sheets']:
        st.markdown("**Excel Sheets:**")
        for idx, sheet in enumerate(st.session_state['excel_sheets']):
            st.write(f"Sheet {idx+1}")
            st.dataframe(sheet)
