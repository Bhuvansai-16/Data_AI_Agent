AI Agent Dashboard

1.Table of Contents

2.Project Summary

3.Setup Instructions

4.Usage Guide

5.Key Features

6.Third-Party APIs and Tools

7.Project Structure

8.License

9.Contact

----------------------------------------------------------
Project Summary

The AI Agent Dashboard is a powerful web-based tool for automating the extraction of specific information about entities from data. Built with Streamlit, it integrates Google Generative AI (Gemini) for natural language queries and supports both CSV file uploads and Google Sheets integration.This project is designed for tasks like data enrichment, entity extraction, or AI-powered information retrieval, making it ideal for analysts and teams working with large datasets.

----------------------------------------------------------
1. Clone the Repository

    git clone https://github.com/your-username/your-repo-name.git

    cd your-repo-name

2. Install Dependencies

    Ensure you have Python 3.8+ installed. Run the following to install the required libraries:

    pip install -r requirements.txt

3. Configure Environment Variables
Create a .env file in the root directory

   GEMINI_API_KEY=your_gemini_api_key

   GOOGLE_APPLICATION_CREDENTIALS=path/to/your-service-account-file.json

4. Run the Application

   Start the Streamlit app with:

   streamlit run app.py

----------------------------------------------------------
Usage Guide
1. Input Options

Upload CSV: Use a CSV file containing entities you want to query.
Google Sheets URL: Provide the URL of a Google Sheet with appropriate sharing permissions.

2. Query Information

Select a column containing entities to query.
Enter the type of information to extract (e.g., "Find contact information").
Process the data to retrieve results.

3. Output Results

Download CSV: Save the enriched data locally.
Update Google Sheets: Directly write results back to the Google Sheet.

----------------------------------------------------------
Key Features

Streamlit Interface: Easy-to-use, interactive web dashboard.

Multi-Source Input: Support for CSV uploads and Google Sheets URLs.

AI-Powered Queries: Uses Google Generative AI for natural language information extraction.

Concurrency: Efficiently processes large datasets using ThreadPoolExecutor.

Export Options: Download results as a CSV or update Google Sheets in real time.

----------------------------------------------------------
Third-Party APIs and Tools
Google Generative AI (Gemini):
Used for querying information.
Extracting information
Library: google-generativeai.

Google Sheets API:
For data fetching and updates.
Libraries: gspread, oauth2client.
Serpapi:
Used for fetching information

Other Python Libraries:

Streamlit: Web app framework.

Pandas: Data manipulation.

Python-Dotenv: Manage environment variables.

----------------------------------------------------------
Project Structure

project-folder/

├── app.py                  # Main Streamlit app

├── requirements.txt        # Python dependencies

├── .env                    # Environment variables (not included in repo)

├── credentials.json        # Google Service Account file (not included in repo)

└── README.md               # Project documentation

----------------------------------------------------------
License

This project is licensed under the MIT License. Feel free to use and modify it.

----------------------------------------------------------

Contact
For questions, suggestions, or contributions:

Name:Chilamkurthi Bhuvansai

Email:chbhuvansai522@gmail.com

Linkedin: www.linkedin.com/in/bhuvansaich
