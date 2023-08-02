# Azure Text Services Example

This folder contains a Python script that demonstrates how to use Azure Text Analytics services to perform language detection, sentiment analysis, key phrase extraction, and entity recognition on text documents. Azure Text Analytics is a powerful service that allows you to extract insights and valuable information from text data.

## Sample Texts

The 'texts' folder contains sample text files that the script will analyze. You can add your own text files to this folder for testing different texts.

## Results

The script will output the following information for each text document:

- Language: The primary language detected in the text.
- Sentiment: The sentiment analysis result, which can be positive, neutral, or negative.
- Key Phrases: A list of important phrases extracted from the text.
- Entities: Recognized entities (e.g., person names, locations, organizations) with their respective categories.

Check output.txt for a sample of expected output

## Notes

- The script uses sequential calls to Azure Text Analytics for each text file. However, you can optimize this process by passing a list of documents for batch processing, which is more efficient for large-scale operations.
