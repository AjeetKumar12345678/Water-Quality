💧 AI-Powered Water Quality Assessment System

An AI-powered Water Quality Assessment System that evaluates water quality using Fuzzy Logic and generates an expert analysis report using Google Gemini AI through LangChain.

The system takes three important water-quality parameters — pH, Turbidity, and Total Dissolved Solids (TDS) — and calculates a Water Quality Index (WQI) from 0 to 100 using Fuzzy Logic. It then uses Google Gemini to generate an AI-based interpretation and recommendations.

---

👨‍🎓 Student Details

- Name: Ajeet Kumar Saroj
- Roll Number: 19045
- Class: TYBSC-IT
- College: S.I.W.S College
- Project Type: Individual Project
- Academic Year: 2026

---

📌 Project Overview

Water quality is an important factor for human health, agriculture, and the environment. Traditional water-quality assessment can require manual analysis and interpretation of multiple parameters.

This project provides a simple AI-assisted system where users can enter:

- pH Level
- Turbidity (NTU)
- Total Dissolved Solids (TDS in mg/L)

The system processes these values using Fuzzy Logic and produces a Water Quality Index score.

The calculated score is classified into:

- Good / Safe
- Fair / Moderate
- Poor / Unsafe

After the fuzzy assessment, Google Gemini AI generates an expert-style water analysis report containing possible impacts, safety considerations, and suggested actions.

---

🎯 Objectives

The main objectives of this project are:

1. To assess water quality using pH, Turbidity, and TDS.
2. To implement Fuzzy Logic for water-quality evaluation.
3. To calculate a Water Quality Index (WQI) score from 0–100.
4. To classify the water into different quality categories.
5. To integrate an LLM using LangChain.
6. To generate an AI-based water analysis report using Google Gemini.
7. To provide understandable recommendations based on the entered parameters.

---

✨ Main Features

- 💧 Water Quality Assessment
- 📊 Fuzzy Logic based WQI calculation
- 🧪 pH, Turbidity and TDS inputs
- 📈 WQI score from 0–100
- 🟢 Good / Safe classification
- 🟠 Fair / Moderate classification
- 🔴 Poor / Unsafe classification
- 🤖 Google Gemini AI integration
- 🔗 LangChain prompt processing
- 📋 AI-generated water analysis report
- 🔐 Secure Gemini API key configuration using Streamlit Secrets
- 🌐 Streamlit web interface

---

🛠️ Technologies Used

Programming Language

- Python

Framework

- Streamlit

AI / LLM

- Google Gemini

AI Framework

- LangChain
- LangChain Google GenAI

Fuzzy Logic

- scikit-fuzzy

Numerical / Scientific Computing

- NumPy
- SciPy

Other Libraries

- Pydantic
- NetworkX

The project dependencies are listed in "requirements.txt".

---

🧠 How the System Works

The system follows these main steps:

User Input
   ↓
pH + Turbidity + TDS
   ↓
Fuzzy Logic Processing
   ↓
Water Quality Index (0–100)
   ↓
Quality Classification
   ↓
LangChain Prompt
   ↓
Google Gemini AI
   ↓
AI Water Analysis Report

---

🔬 Fuzzy Logic Methodology

The system uses three input parameters:

1. pH

The pH value is divided into fuzzy categories:

- Acidic
- Optimal
- Alkaline

2. Turbidity

Turbidity is classified as:

- Low
- Moderate
- High

3. TDS

Total Dissolved Solids are classified as:

- Low
- Moderate
- High

The system applies fuzzy rules to these parameters and calculates a WQI score.

Example Fuzzy Rules

If pH is optimal AND turbidity is low AND TDS is low
→ Water Quality is Good

If pH is acidic OR alkaline
→ Water Quality is Poor

If turbidity is high OR TDS is high
→ Water Quality is Poor

If turbidity is moderate OR TDS is moderate
→ Water Quality is Fair

The project implements these fuzzy rules using "scikit-fuzzy".

---

🤖 AI / LangChain Component

After calculating the Fuzzy Logic WQI score, the system sends the water parameters and assessment category to Google Gemini through LangChain.

The AI receives:

- pH
- Turbidity
- TDS
- Fuzzy Logic WQI Score
- Preliminary Assessment Category

It generates a report covering:

1. Potential health and environmental impacts
2. Water safety considerations
3. Consumption or irrigation considerations
4. Possible treatment or corrective actions

The application uses "ChatPromptTemplate", "ChatGoogleGenerativeAI", and "StrOutputParser" for the LangChain-based AI workflow.

---

📊 Water Quality Classification

The project uses the following WQI classification:

WQI Score| Category
70 – 100| Good / Safe
40 – 69.99| Fair / Moderate
0 – 39.99| Poor / Unsafe

The classification is implemented directly in the application code.

---

💻 Installation and Setup

Step 1: Clone the Repository

git clone YOUR_GITHUB_REPOSITORY_URL

Step 2: Open the Project Folder

cd YOUR_PROJECT_FOLDER

Step 3: Create a Virtual Environment

python -m venv venv

Step 4: Activate the Virtual Environment

Windows

venv\Scripts\activate

macOS / Linux

source venv/bin/activate

Step 5: Install Dependencies

pip install -r requirements.txt

The required packages include Streamlit, NumPy, SciPy, scikit-fuzzy, LangChain, and LangChain Google GenAI.

---

🔑 API Key Configuration

The project requires a Google Gemini API key for AI report generation.

Local Testing

The application provides an API-key input field if the Streamlit secret is not configured.

Streamlit Deployment

For deployment, add the API key to Streamlit Secrets.

Use the following placeholder:

GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"

Do not upload your real API key to GitHub.

The application is designed to read "GEMINI_API_KEY" from Streamlit Secrets.

---

▶️ How to Run the Project

Run the following command:

streamlit run app.py

After starting the application, open the Streamlit URL shown in the terminal.

---

🧪 How to Use

1. Open the application.
2. Enter/select the pH Level.
3. Enter/select Turbidity in NTU.
4. Enter/select TDS in mg/L.
5. Click Run Water Assessment.
6. The system calculates the Fuzzy Logic WQI score.
7. The system displays the water-quality category.
8. Google Gemini generates an AI-based analysis report.
9. Read the generated recommendations.

The application provides sliders for pH, turbidity, and TDS and processes them when the Run Water Assessment button is selected
---
Water Quality Assessment Result
AI Expert Analysis Report
«Create a "screenshots" folder in the repository and place the corresponding screenshots inside it.»

---

📁 Project Structure

AI-Water-Quality-Assessment/
│
├── app.py
├── requirements.txt
├── README.md
│
└── screenshots/
    ├── home.png
    ├── result.png
    └── ai-report.png

---

🌐 Live Deployment

Live Project:
"YOUR_STREAMLIT_DEPLOYMENT_LINK"

GitHub Repository:
"YOUR_GITHUB_REPOSITORY_LINK"

«Replace the above placeholders with your actual links before submission.»

---

🔐 Security

- API keys should not be hard-coded in the source code.
- Gemini API keys should be stored using Streamlit Secrets.
- Do not upload passwords, tokens, or private credentials to GitHub.

The submission instructions specifically require that API keys, passwords, tokens, and other private credentials are not exposed.

---

⚠️ Limitations

1. The assessment is based only on pH, Turbidity, and TDS.
2. The system does not perform physical laboratory testing.
3. AI-generated recommendations should be treated as informational.
4. The accuracy of the AI report depends on the input values and availability of the Gemini API.
5. The project does not replace certified laboratory water-quality testing.

---

🚀 Future Scope

Possible future improvements include:

- Adding more water-quality parameters such as dissolved oxygen, hardness, nitrate, and chlorine.
- Connecting the system with IoT water-quality sensors.
- Storing previous assessment results in a database.
- Adding graphical reports and historical analysis.
- Adding user authentication.
- Providing downloadable assessment reports.
- Supporting multiple water-quality standards.
- Improving the fuzzy rule base with a larger expert-validated dataset.

---

📚 References

- Streamlit Documentation
- Python Documentation
- scikit-fuzzy Documentation
- LangChain Documentation
- Google Gemini API Documentation
- Water-quality reference materials used for defining assessment parameters

---

👨‍💻 Author

Ajeet Kumar Saroj
Roll No.: 19045
TYBSC-IT
S.I.W.S College

---

📌 Project Submission Checklist

- [ ] GitHub repository is accessible
- [ ] Complete source code uploaded
- [ ] "README.md" included
- [ ] "requirements.txt" included
- [ ] Live deployment link added
- [ ] Screenshots added
- [ ] No API keys or passwords exposed
- [ ] Documentation PDF completed
- [ ] IKS connection explained in documentation
- [ ] Project ready for individual viva
