import google.generativeai as genai
import pandas as pd
import os

# Set your Gemini API Key here
genai.configure(api_key="AIzaSyC0nLVJvGIIEv2pNsfLR6pXzi-B-KLTn8g")

model = genai.GenerativeModel('gemini-1.5-pro-latest')

# Load all CSVs as strings
def load_data():
    sales_data = pd.read_csv("total_sales.csv").to_string()
    ads_data = pd.read_csv("ad_sales.csv").to_string()
    eligibility_data = pd.read_csv("eligibility.csv").to_string()
    return f"Sales Data:\n{sales_data}\n\nAd Sales Data:\n{ads_data}\n\nEligibility Data:\n{eligibility_data}"




# Send the question + data to Gemini
def handle_query(question):
    data_string = load_data()
    prompt = f"""
    You are an AI data assistant for e-commerce. Given the following datasets and a question, respond accurately and clearly.

    {data_string}

    Question: {question}
    """

    response = model.generate_content(prompt)
    return response.text, prompt
