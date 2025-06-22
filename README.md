🔍 AI Agent Dashboard
A powerful Streamlit-based web application that automates the extraction of specific information about entities from data. It integrates Google Generative AI (Gemini) for natural language querying and supports both CSV and Google Sheets data sources.

Ideal for analysts and teams working with large datasets for tasks such as:

✅ Data enrichment

✅ Entity extraction

✅ AI-powered information retrieval

📚 Table of Contents
Project Summary

Setup Instructions

Usage Guide

Key Features

Third-Party APIs and Tools

Project Structure

License

Contact

📌 Project Summary
AI Agent Dashboard is a web-based dashboard designed to query and retrieve relevant information about entities listed in a dataset. It leverages Google Gemini (Generative AI) to process user-defined prompts and extract data based on natural language queries.

Key use cases:

Contact info extraction

Company insights

Web-based data enrichment

⚙️ Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2. Install Dependencies
Make sure Python 3.8+ is installed.

bash
Copy
Edit
pip install -r requirements.txt
3. Configure Environment Variables
Create a .env file in the root directory:

env
Copy
Edit
GEMINI_API_KEY=your_gemini_api_key
GOOGLE_APPLICATION_CREDENTIALS=path/to/your-service-account-file.json
Ensure the Google service account file (credentials.json) has the required permissions.

4. Run the Application
bash
Copy
Edit
streamlit run app.py
🧠 Usage Guide
1. Input Options
Upload CSV: Upload a .csv file with the entities to be queried.

Google Sheets URL: Provide the shareable URL of a Google Sheet.

2. Query Information
Choose the entity column.

Enter a natural language query (e.g., "Find contact information for each company").

Click Process to run the query.

3. Output Options
Download CSV: Save enriched data to your device.

Update Google Sheet: Write results directly back to the provided Google Sheet.

✨ Key Features
📊 Streamlit UI: Clean, user-friendly dashboard interface.

📂 Multi-Source Input: CSV upload & Google Sheets support.

🧠 AI-Powered: Natural language queries using Google Gemini.

⚡ High Performance: Concurrency support with ThreadPoolExecutor.

📤 Export Options: CSV download & Google Sheets write-back.

🔌 Third-Party APIs and Tools
Tool / API	Purpose	Library
Google Generative AI (Gemini)	Information extraction via AI prompts	google-generativeai
Google Sheets API	Data reading and writing	gspread, oauth2client
SerpAPI	External search engine querying (optional)	serpapi
Streamlit	Frontend web app	streamlit
Pandas	Data processing and manipulation	pandas
python-dotenv	Manage environment variables	python-dotenv

🗂️ Project Structure
bash
Copy
Edit
project-folder/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (excluded from repo)
├── credentials.json        # Google service account (excluded from repo)
└── README.md               # Project documentation
📄 License
This project is licensed under the MIT License.
Feel free to use, modify, and distribute as per the license terms.

📬 Contact
Chilamkurthi Bhuvansai
📧 Email: chbhuvansai522@gmail.com
🔗 LinkedIn: linkedin.com/in/bhuvansaich
