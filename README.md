# Stock Analysis and Reporting Application

## Overview
This Flask application offers an automated stock analysis and reporting service. It fetches financial data for specified stocks, calculates simple returns, and utilizes OpenAI's GPT-3 to generate insightful stock performance analyses. The application aims to make financial data more accessible and understandable, especially for users who are not experts in the stock market.

## Features
- **Stock Symbol Translation**: Translates company names to their stock symbols.
- **Financial Data Fetching**: Retrieves financial data for stocks using the Alpha Vantage API.
- **Return Calculation**: Calculates the simple return of a stock over the last two days.
- **Automated Analysis with GPT-3**: Generates a natural language analysis of stock performance.
- **User-Friendly API**: Provides a simple and intuitive API for users to interact with the service.

## How It Works
1. **Symbol Resolution**: Users can query the application with a company name. The application translates this into the corresponding stock symbol.
2. **Data Retrieval**: It then fetches the financial data for the specified stock symbol from Alpha Vantage.
3. **Analysis Preparation**: The application processes this data to calculate the simple return and prepares a prompt for GPT-3.
4. **GPT-3 Analysis**: Using OpenAI's GPT-3, the application generates a detailed analysis report based on the stock's performance.
5. **Result Delivery**: The analysis is returned to the user in an easily understandable format.

## Setup and Installation
### Prerequisites
- Python 3.x
- Flask
- OpenAI API Key
- Alpha Vantage API Key

### Installation Steps
1. Clone the repository:

   git clone https://github.com/lutfulh/Stock-Analysis-and-Reporting.git

   pip install -r requirements.txt

.env
 ALPHA_VANTAGE_API_KEY='your_alpha_vantage_api_key'
 OPENAI_API_KEY='your_openai_api_key'

python run.py

### Usage

Analyze Stock Endpoint:

POST /analyze
Content-Type: application/json
{
    "name": "Apple Inc."
}

Response:

{
    "analysis": "Based on the information provided, the stock 0R2V.LON experienced a simple return of -2.19% on 2024-01-03. This indicates that the stock's value decreased by 2.19% on that particular day. \n\nA negative return suggests that investors may have sold off shares, causing the stock price to decline. This could be due to various factors such as unfavorable market conditions, poor company performance, or negative news surrounding the stock. \n\nWhen considering the implications for future trading sessions, it is important to note that a single day's performance may not be indicative of long-term trends. It is essential to analyze the stock's performance over a longer period to gain a more comprehensive understanding. Monitoring the stock"
}

![llm1](https://github.com/lutfulh/Stock-Analysis-and-Reporting/assets/25671509/d66f57ef-7fb4-4ba7-9dd5-269f61afd6cf)



Direct GPT-3 Interaction Endpoint:


POST /gpt3
Content-Type: application/json
{
    "prompt": "Your custom prompt for GPT-3"
}



License
MIT License

