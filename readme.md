# Website Scraper with AI

## Overview
This is a Python-based web application built with Streamlit that allows users to scrape content from a website and extract specific information using AI-powered analysis. The program uses BeautifulSoup to parse website HTML, extracts text, and sends it to the Groq API (using the llama-3.3-70b-versatile model) to answer user-defined queries about the scraped content. The application provides a simple, interactive user interface where users can input a website URL and specify what information they want to extract.

## Features
- Web Scraping: Fetches and parses HTML content from a user-provided URL using requests and BeautifulSoup.
- AI-Powered Analysis: Uses the Groq API to process the scraped text and answer user queries about the content.
- Streamlit Interface: Provides an intuitive, web-based UI for entering URLs and queries, with real-time feedback.
- Error Handling: Includes robust error handling for invalid URLs, HTTP errors, and API issues.
- Customizable Queries: Users can specify what information to extract (e.g., "What is the main topic?" or "List all product names").

## Prerequisites
To run this program, you need the following:
- Python 3.8+: Ensure Python is installed on your system.
- Groq API Key: Obtain an API key .
- Internet Connection: Required for fetching website content and accessing the Groq API.

## Dependencies
The program relies on the following Python libraries:
- streamlit: For building the web-based user interface.
- requests: For making HTTP requests to fetch website content.
- beautifulsoup4: For parsing HTML and extracting text.
- groq: For interacting with the Groq API.

Install the dependencies using pip:
```
pip install streamlit requests beautifulsoup4 groq
```

## Setup Instructions
1. Clone or Download the Code:
   - Save the main.py file to your local machine.

2. Set Up the Groq API Key:
   - Obtain a Groq API key from xAI's API service 
   - Set the API key as an environment variable:
     - On Windows (Command Prompt):
       ```
       set GROQ_API_KEY=your-api-key-here
       ```
     - On macOS/Linux:
       ```
       export GROQ_API_KEY=your-api-key-here
       ```
     - Alternatively, you can add the API key to a .env file and load it using a library like python-dotenv (not included in the current code).

3. Install Dependencies:
   - Run the following command to install the required Python libraries:
     ```
     pip install streamlit requests beautifulsoup4 groq
     ```

4. Run the Application:
   - Navigate to the directory containing main.py.
   - Start the Streamlit app:
     ```
     streamlit run main.py
     ```
   - This will launch a local web server, and a browser window will open (typically at http://localhost:8501).

## Usage
1. Access the Application:
   - Open the Streamlit app in your browser (default: http://localhost:8501).

2. Enter a URL:
   - In the "Enter the URL to scrape" field, input a valid website URL (e.g., https://example.com).
   - Ensure the URL starts with http:// or https://.

3. Specify a Query:
   - In the "What do you want to extract?" field, enter a question or instruction about what information to extract from the website (e.g., "What is the main topic?", "List all headlines", or "Summarize the content").

4. Scrape and Extract:
   - Click the "Scrape and Extract" button.
   - The app will fetch the website content, parse it, and use the Groq API to analyze the text based on your query.
   - The extracted information will be displayed below the button.

5. Error Handling:
   - If the URL is invalid or the website cannot be accessed, an error message will appear.
   - If the Groq API fails to process the query, an error message will be displayed.

## Example
- URL: https://example.com
- Query: "What is the main topic?"
- Output: The app might return: "The main topic of the website is to provide a sample webpage for testing purposes."

## Limitations
- Website Compatibility: Some websites may block scraping or use dynamic content (e.g., JavaScript-rendered pages) that BeautifulSoup cannot fully parse. For such cases, consider using a tool like selenium (not included in this code).
- API Quotas: The Groq API may have usage limits depending on your subscription plan. Refer to xAI's API documentation (https://x.ai/api) for details.
- Text Extraction: The program extracts text using BeautifulSoup's get_text() method, which may include irrelevant content (e.g., navigation menus, footers). Advanced parsing logic could improve results.
- Single Model: The program uses the llama-3.3-70b-versatile model. Other Groq models are not currently supported in this code.

## Troubleshooting
- Error: "Error fetching the URL":
  - Check if the URL is valid and accessible.
  - Ensure you have an active internet connection.
- Error: "Error with AI extraction":
  - Verify that your Groq API key is set correctly.
  - Check if the Groq API service is operational.
- Streamlit Not Running:
  - Ensure all dependencies are installed (pip install streamlit requests beautifulsoup4 groq).
  - Run streamlit run main.py from the correct directory.

## Future Improvements
- Add support for dynamic content scraping using tools like selenium or playwright.
- Allow users to select different Groq models or customize API parameters.
- Enhance text parsing to filter out irrelevant content (e.g., ads, navigation).
- Add caching to store scraped results locally and reduce API calls.
- Include advanced error recovery mechanisms for robust scraping.

## License
This project is provided as-is for educational purposes. Ensure compliance with the terms of service of the websites you scrape and the Groq API.





