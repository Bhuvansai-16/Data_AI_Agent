AI Agent Dashboard:

Project Summary:
The AI Agent Dashboard is a web-based application built with Streamlit that enables users to extract specific information about entities using Google Generative AI models. The app supports processing data from uploaded CSV files or Google Sheets, allowing users to download the results or directly update the Google Sheet.
This project uses concurrency and rate-limiting techniques to efficiently query multiple entities and is ideal for scenarios requiring large-scale data enrichment or AI-powered information retrieval.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Setup Instructions:

1. Clone the Repository
Clone the repository to your local machine:
git clone https://github.com/Bhuvansai-16/Ai_agent_.git
--------------------------------------------------------------------------------------------------
2. Install Dependencies
Install the required libraries listed in requirements.txt:

pip install -r requirements.txt
---------------------------------------------------------------------------------------------------
3. Set Up Environment Variables
Create a .env file in the root directory with the following content:
env:
GEMINI_API_KEY=your_gemini_api_key
GOOGLE_APPLICATION_CREDENTIALS=path/to/your-service-account-file.json
GEMINI_API_KEY: Your API key for Google Generative AI.
GOOGLE_APPLICATION_CREDENTIALS: Path to your Google service account credentials file (JSON format).
--------------------------------------------------------------------------------------------------
4. Run the Application
Start the Streamlit app:
"streamlit run app.py"
--------------------------------------------------------------------------------------------------
Usage Guide:
1. Input Data
Choose an input method:
Upload CSV: Upload a CSV file containing the entities you want to query.
Google Sheets URL: Provide the URL of a Google Sheet (ensure appropriate sharing permissions).
--------------------------------------------------------------------------------------------------
2. Query Entities
Select the primary column in your data containing entities.
Enter the type of information you want to query (e.g., "Find contact information").
Start the process to extract information using Google Generative AI.
--------------------------------------------------------------------------------------------------
3. Output Results
Download CSV: Save the processed data as a CSV file.
Update Google Sheets: Directly update the original Google Sheet with the processed data.
--------------------------------------------------------------------------------------------------
Third-Party APIs and Tools:
1. Google Generative AI
Purpose: To query information about entities using a language model (Gemini).
Library: google-generativeai
Documentation: Google Generative AI
--------------------------------------------------------------------------------------------------
2. Google Sheets API
Purpose: To fetch and update data in Google Sheets.
Libraries: gspread, oauth2client
Documentation: Google Sheets API
--------------------------------------------------------------------------------------------------
3. Python Libraries
Streamlit: For creating the interactive web application.
Pandas: For data manipulation and processing.
Python-Dotenv: For managing environment variables.
Concurrent Futures: For handling concurrency while querying multiple entities.
--------------------------------------------------------------------------------------------------
Project Structure:

project-folder/
│
├── app.py                
├── requirements.txt    
├── .env                
├── credentials.json      
└── README.md       
--------------------------------------------------------------------------------------------------
Key Features:
1)Streamlit Dashboard: Interactive and user-friendly web-based interface.
2)Multi-source Input: Supports data input via CSV upload or Google Sheets URL.
3)I Querying: Uses Google Generative AI to extract information efficiently.
3)Concurrency: Processes multiple entities simultaneously with thread pooling.
4)Data Export: Download processed data as CSV or update Google Sheets in real-time.
--------------------------------------------------------------------------------------------------
License:
This project is licensed under the MIT License.
--------------------------------------------------------------------------------------------------
Author
Chilamkurthi Bhuvansai
Linkedin: www.linkedin.com/in/bhuvansaich
Email: chbhuvansai522@gmail.com
