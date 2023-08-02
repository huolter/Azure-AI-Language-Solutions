# Azure Text Services Example

This repository contains a Python script that demonstrates how to use Azure Text Analytics services to perform language detection, sentiment analysis, key phrase extraction, and entity recognition on text documents. Azure Text Analytics is a powerful service that allows you to extract insights and valuable information from text data.

## Prerequisites

Before running the code, make sure you have the following:

1. An Azure account: If you don't have one, you can sign up for a free trial at [azure.com/free](https://azure.com/free).

2. Azure Text Analytics service: Set up the Text Analytics service in your Azure portal and obtain the endpoint and key credentials. You can find the endpoint and key in your Azure Text Analytics resource.

3. Python environment: Make sure you have Python installed on your system. You can download it from the official website: [python.org/downloads](https://www.python.org/downloads/).

4. Required libraries: Install the necessary libraries using pip by running the following command in your terminal:

   ```
   pip install azure-ai-textanalytics python-dotenv
   ```

## Getting Started

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/azure-text-services-example.git
   cd azure-text-services-example
   ```

2. Set up environment variables:

   The script uses the `python-dotenv` library to read the Azure Text Analytics endpoint and key from the environment. Create a `.env` file in the project directory and add the following lines:

   ```
   COG_SERVICE_ENDPOINT=your_cog_service_endpoint
   COG_SERVICE_KEY=your_cog_service_key
   ```

   Replace `your_cog_service_endpoint` and `your_cog_service_key` with the actual values from your Azure Text Analytics resource.

3. Run the script:

   Execute the Python script to analyze the text files located in the 'texts' folder. The script will output language detection results, sentiment analysis, key phrases, and recognized entities for each text document.

   ```
   python main.py
   ```

## Sample Texts

The 'texts' folder contains sample text files that the script will analyze. You can add your own text files to this folder for testing different texts.

## Results

The script will output the following information for each text document:

- Language: The primary language detected in the text.
- Sentiment: The sentiment analysis result, which can be positive, neutral, or negative.
- Key Phrases: A list of important phrases extracted from the text.
- Entities: Recognized entities (e.g., person names, locations, organizations) with their respective categories.

## Notes

- The script uses sequential calls to Azure Text Analytics for each text file. However, you can optimize this process by passing a list of documents for batch processing, which is more efficient for large-scale operations.

- Remember to use your Azure Text Analytics credentials responsibly and securely. Avoid sharing sensitive information such as keys and endpoints publicly.

