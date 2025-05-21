import streamlit as st
import requests
from bs4 import BeautifulSoup
from groq import Groq
import os

# Initialize the Groq client with the API key from environment variable
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Streamlit app interface
st.title("Website Scraper with AI")
st.write("Enter a URL and specify what information you want to extract from the website.")

# Input fields for URL and query
url = st.text_input("Enter the URL to scrape:", value="https://example.com")
query = st.text_input("What do you want to extract?", value="What is the main topic?")

# Button to trigger scraping and extraction
if st.button("Scrape and Extract"):
    with st.spinner("Scraping and extracting..."):
        # Fetch the website HTML
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for bad HTTP status codes
            html = response.text
        except Exception as e:
            st.error(f"Error fetching the URL: {e}")
            st.stop()

        # Parse HTML and extract text
        try:
            soup = BeautifulSoup(html, 'html.parser')
            text = soup.get_text(separator=' ', strip=True)

            # Create a prompt for the Groq language model
            prompt = f"Based on the following text, {query}\n\nText: {text}"

            # Send the prompt to Groq API
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model="llama-3.3-70b-versatile",
            )

            # Display the extracted information
            result = chat_completion.choices[0].message.content
            st.write("**Extracted Information:**")
            st.write(result)

        except Exception as e:
            st.error(f"Error with AI extraction: {e}")