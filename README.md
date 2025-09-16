<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">

</head>
<body>

<h1>📊 Financial Document Q&A Assistant</h1>

<p>
A <b>Streamlit web application</b> that allows users to upload company financial statements (PDF & Excel), 
extracts structured data from them, and answers natural language questions such as <i>"What was the revenue in 2023?"</i> 
or <i>"Show the net profit in 2022"</i>. This project is developed as part of the Data Science Internship assignment from 
<b>Soothsayer Analytics India Private Limited</b>.
</p>

<hr>
<h2>🔗 Live Demo</h2>
<p>
Try the app and view its code on GitHub: 
<a href="https://financial-document-q-a-assistant-git-lvbp9tw3du2ygpgpgvkxfk.streamlit.app/" target="_blank">
Click here to open the demo
</a>
</p>


<img src="https://github.com/pratiksutar841/Financial-Document-Q-A-Assistant-/blob/01f14c9715a690e67a533c959a1bf2d16d349ff2/Financial-Output-Photo.png" alt="Financial Q&A App Demo" style="width:80%; border-radius:10px; box-shadow:0px 4px 10px rgba(0,0,0,0.2);">

<hr>

<h2>📌 Project Objective</h2>
<ul>
    <li>Allow uploading of PDF and Excel financial documents</li>
    <li>Extract tables and text from uploaded files</li>
    <li>Enable natural-language question answering on financial data</li>
    <li>Answer queries like revenue, profit, assets, liabilities, cash flow, etc.</li>
    <li>Work completely offline as a local Streamlit app</li>
</ul>

<hr>

<h2>🛠️ Tools & Technologies</h2>
<ul>
    <li>Python, Pandas, NumPy, PDFPlumber, OpenPyXL, FuzzyWuzzy</li>
    <li>Frontend: Streamlit for interactive UI</li>
    <li>Environment: VS Code / Jupyter Notebook</li>
    <li>Version Control: Git & GitHub</li>
</ul>

<hr>

<h2>📂 Project Structure</h2>
<pre>
Financial_QA_Assignment/
│── app.py               # Main Streamlit app
│── helpers.py            # File extraction and QA logic
│── requirements.txt      # Dependencies
│── README.in              # Project documentation (HTML)
│── sample_files/          # Sample financial Excel/PDF files
</pre>

<hr>

<h2>📊 Methodology</h2>
<ol>
    <li><b>Data Ingestion</b>
        <ul>
            <li>Upload PDF or Excel statements</li>
            <li>Read tables and text from PDFs using pdfplumber</li>
            <li>Read tabular sheets from Excel using pandas</li>
        </ul>
    </li>
    <li><b>Data Processing</b>
        <ul>
            <li>Search for financial keywords (revenue, profit, expenses, etc.)</li>
            <li>Extract corresponding numeric values from tables and text</li>
        </ul>
    </li>
    <li><b>Question Answering</b>
        <ul>
            <li>Take user input question</li>
            <li>Match keywords and return related financial values</li>
            <li>Show results with their source location (sheet/page)</li>
        </ul>
    </li>
</ol>

<hr>

<h2>📌 Features</h2>
<ul>
    <li>Upload financial statements in PDF or Excel</li>
    <li>Automatic extraction of text and tables</li>
    <li>Ask questions like "Revenue in 2023" or "Total Assets in 2022"</li>
    <li>Displays answers and source references</li>
    <li>Clean and interactive Streamlit UI</li>
    <li>Works completely offline</li>
</ul>

<hr>

<h2>🚀 How to Run Locally</h2>
<ol>
    <li>Clone the repository
        <pre>git clone https://github.com/your-username/Financial_QA_Assignment.git</pre>
    </li>
    <li>Navigate to the project folder
        <pre>cd Financial_QA_Assignment</pre>
    </li>
    <li>Create a virtual environment
        <pre>python -m venv venv</pre>
    </li>
    <li>Activate the virtual environment
        <pre>
<!-- Windows -->
venv\Scripts\activate

<!-- Linux / Mac -->
source venv/bin/activate
        </pre>
    </li>
    <li>Install dependencies
        <pre>pip install -r requirements.txt</pre>
    </li>
    <li>Run the Streamlit app
        <pre>streamlit run app.py</pre>
    </li>
</ol>

<hr>

<h2>🙋‍♂️ Author</h2>
<p>
<b>Pratik Sutar</b><br>
B.Tech in Computer Science & Engineering (Data Science)<br>
GitHub: <a href="https://github.com/pratiksutar841">pratiksutar841</a><br>
LinkedIn: <a href="https://www.linkedin.com/in/pratik-sutar-/">Pratik Sutar</a>
</p>

</body>
</html>
