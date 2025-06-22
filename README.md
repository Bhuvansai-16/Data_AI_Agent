
# 🤖 AI Agent Dashboard

> A web-based AI-powered tool for **automated information extraction** from datasets — powered by **Google Generative AI (Gemini)** and **Streamlit**.

---

## 🗂️ Table of Contents

- [📌 Project Summary](#-project-summary)  
- [⚙️ Setup Instructions](#-setup-instructions)  
- [🚀 Usage Guide](#-usage-guide)  
- [✨ Key Features](#-key-features)  
- [🔌 Third-Party APIs & Tools](#-third-party-apis--tools)  
- [📁 Project Structure](#-project-structure)  
- [📄 License](#-license)  
- [📬 Contact](#-contact)

---

## 📌 Project Summary

The **AI Agent Dashboard** is a **Streamlit-based** application that helps you **automate the retrieval of specific information** (e.g., contact details, descriptions, etc.) from datasets like CSV files or Google Sheets. It supports **natural language querying** using **Google Generative AI (Gemini)** and integrates with **Google Sheets** for real-time updates.

This tool is ideal for:
- 🧠 Entity extraction  
- 🏢 Company information enrichment  
- 📊 AI-driven data retrieval  

---

## ⚙️ Setup Instructions

### 🔁 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 📦 2. Install Dependencies

Ensure **Python 3.8+** is installed.

```bash
pip install -r requirements.txt
```

### 🔐 3. Configure Environment Variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_gemini_api_key
GOOGLE_APPLICATION_CREDENTIALS=path/to/your-service-account-file.json
```

> ⚠️ Make sure your Google Cloud credentials file is correctly set up and has the required permissions.

### ▶️ 4. Run the Application

```bash
streamlit run app.py
```

---

## 🚀 Usage Guide

### 📁 Input Options

- **Upload CSV** – Upload a `.csv` file containing the entities you want to query.  
- **Google Sheets URL** – Paste the shareable link to your Google Sheet.

### 🧠 Querying

1. Select the column containing your entities (e.g., names or domains).  
2. Enter your query in natural language (e.g., _"Find LinkedIn URLs"_).  
3. Click **Process** to let the AI work its magic. ✨

### 💾 Output Options

- **Download CSV** – Save enriched data to your device.  
- **Update Google Sheet** – Push results directly to your sheet.

---

## ✨ Key Features

✅ **User-Friendly Interface** — Interactive dashboard built with Streamlit  
✅ **Multi-Source Input** — Accepts CSV files & Google Sheets  
✅ **AI Integration** — Uses Gemini to extract structured info  
✅ **Concurrency Enabled** — Fast processing via `ThreadPoolExecutor`  
✅ **Export Options** — Save locally or update online in real time

---

## 🔌 Third-Party APIs & Tools

| Tool / API | Purpose | Library |
|------------|---------|---------|
| 🧠 **Google Gemini** | Natural language info extraction | `google-generativeai` |
| 📄 **Google Sheets API** | Read/write from Sheets | `gspread`, `oauth2client` |
| 🔍 **SerpAPI** | External data enrichment (optional) | `serpapi` |
| 🖥️ **Streamlit** | Web app framework | `streamlit` |
| 🐼 **Pandas** | Data processing | `pandas` |
| 🧪 **Dotenv** | Environment variable manager | `python-dotenv` |

---

## 📁 Project Structure

```
AI-Agent-Dashboard/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Dependency list
├── .env                    # Environment variables (ignored in git)
├── credentials.json        # Google credentials (ignored in git)
└── README.md               # This file
```

---

## 📄 License

Licensed under the **MIT License**.  
You’re free to use, modify, and distribute it for both personal and commercial purposes.

---

## 📬 Contact

**Chilamkurthi Bhuvansai**  
📧 Email: [chbhuvansai522@gmail.com](mailto:chbhuvansai522@gmail.com)  
🔗 LinkedIn: [linkedin.com/in/bhuvansaich](https://www.linkedin.com/in/bhuvansaich)

---
