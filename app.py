import streamlit as st
import pandas as pd
import os
import google.generativeai as genai
from dotenv import load_dotenv
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from time import sleep
from concurrent.futures import ThreadPoolExecutor
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
SERVICE_ACCOUNT_FILE = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Authenticate Google Sheets
def authenticate_google_sheets():
    scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, scopes)
    return gspread.authorize(credentials)

# Fetch data from Google Sheets
def get_sheet_data(sheet_url):
    client = authenticate_google_sheets()
    sheet = client.open_by_url(sheet_url)
    worksheet = sheet.get_worksheet(0)
    data = worksheet.get_all_records()
    return pd.DataFrame(data)

# Update data in Google Sheets
def update_google_sheet(sheet_url, data):
    client = authenticate_google_sheets()
    sheet = client.open_by_url(sheet_url)
    worksheet = sheet.get_worksheet(0)
    worksheet.clear()
    worksheet.append_row(data.columns.tolist())  # Add column headers
    for row in data.values.tolist():  # Add each row
        worksheet.append_row(row)

# Query LLM with rate limiting
def query_entity(entity, query_type):
    try:
        query = f"Provide only the {query_type.lower()} for {entity}."
        response = genai.GenerativeModel("gemini-1.5-flash").generate_content(query)
        return {"Entity": entity, "Extracted Information": response.text.strip()}
    except Exception as e:
        logging.error(f"Error processing entity {entity}: {e}")
        return {"Entity": entity, "Extracted Information": f"Error: {e}"}

# Process entities with concurrency
def process_concurrently(entities, query_type, max_workers=5):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(lambda x: query_entity(x, query_type), entities))
    return results

# Streamlit UI
st.title("AI Agent Dashboard")

input_option = st.radio("Select Input Method", ("Upload CSV", "Use Google Sheets URL"))

if input_option == "Upload CSV":
    uploaded_file = st.file_uploader("Upload your CSV file", type="csv")
    if uploaded_file:
        try:
            # Read and display CSV data
            df = pd.read_csv(uploaded_file)
            st.write("Preview of Uploaded CSV Data:")
            st.write(df)

            # Select primary column and query type
            primary_column = st.selectbox("Select the column for queries", df.columns)
            query_type = st.text_input("Enter the type of information to fetch (e.g., 'Find contact information')")

            if st.button("Fetch Information"):
                if not query_type:
                    st.error("Please enter a query type.")
                else:
                    entities = df[primary_column]
                    st.info("Processing data, please wait...")
                    results = process_concurrently(entities, query_type)
                    results_df = pd.DataFrame(results)

                    st.write("Extracted Information:")
                    st.write(results_df)

                    csv = results_df.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        label="Download Updated Data as CSV",
                        data=csv,
                        file_name="updated_data.csv",
                        mime="text/csv",
                    )
        except Exception as e:
            st.error(f"Error reading CSV file: {e}")

elif input_option == "Use Google Sheets URL":
    sheet_url = st.text_input("Enter the Google Sheets URL:")
    if sheet_url:
        try:
            # Fetch and display Google Sheets data
            df = get_sheet_data(sheet_url)
            st.write("Preview of Google Sheet Data:")
            st.write(df)

            # Select primary column and query type
            primary_column = st.selectbox("Select the column for queries", df.columns)
            query_type = st.text_input("Enter the type of information to fetch (e.g., 'Find contact information')")

            if st.button("Fetch and Update Information"):
                if not query_type:
                    st.error("Please enter a query type.")
                else:
                    entities = df[primary_column]
                    st.info("Processing data, please wait...")
                    results = process_concurrently(entities, query_type)
                    results_df = pd.DataFrame(results)

                    st.write("Extracted Information:")
                    st.write(results_df)

                    try:
                        update_google_sheet(sheet_url, results_df)
                        st.success("Google Sheet updated successfully! Reload the sheet to see changes.")
                    except Exception as e:
                        st.error(f"Error updating Google Sheet: {e}")

            if st.button("Fetch and Download"):
                if not query_type:
                    st.error("Please enter a query type.")
                else:
                    entities = df[primary_column]
                    st.info("Processing data, please wait...")
                    results = process_concurrently(entities, query_type)
                    results_df = pd.DataFrame(results)

                    st.write("Extracted Information:")
                    st.write(results_df)

                    csv = results_df.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        label="Download Processed Data as CSV",
                        data=csv,
                        file_name="processed_google_sheet_data.csv",
                        mime="text/csv",
                    )
        except Exception as e:
            st.error(f"Error fetching data from Google Sheets: {e}")
