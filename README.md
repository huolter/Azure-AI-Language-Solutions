# Azure AI Solutions Examples

This repository provides examples and code samples demonstrating how to leverage Azure Language Solutions to solve natural language processing (NLP) tasks using various Azure services.

## Introduction

Azure Language Solutions offer a wide range of powerful NLP capabilities that enable developers to build intelligent applications for language understanding and processing. This repository aims to guide you through the usage of different Azure services for language-related tasks. You can use it as a quick guide to start running a service fast.

## Prerequisites

Before you get started with the examples, ensure you have the following prerequisites:

1. An Azure account: If you don't have one, you can sign up for a free trial at [azure.com/free](https://azure.com/free).

2. Azure Text Analytics service and Azure Translator service: To explore translation capabilities, set up the services in your Azure portal. Obtain the endpoint and key credentials. You can also use the Azure Cognitive Services multi-service instance. Cognitive Services is a product bundle that enables customers to access multiple services with a single API key. [https://azure.microsoft.com/en-us/products/ai-services]

3. Required libraries: Install the necessary libraries using pip by running the following command in your terminal:

   ```
   pip install azure-ai-textanalytics azure-ai-translation python-dotenv
   ```

## Repository Structure

The repository is organized into different directories, each representing a specific use case or language service. Here's an overview of what you'll find in each directory:

1. **TextAnalytics**: This directory contains Python code samples for using Azure Text Analytics to perform tasks such as sentiment analysis, key phrase extraction, and entity recognition.

2. **Translation**: In this directory, you'll find examples showcasing Azure Translator for text translation in various languages.

3. *(Other directories)*: In the future, we plan to expand the repository to include additional language services, such as Speech-to-Text, Language Understanding, and more.

## Getting Started

1. Clone the repository, and set up environment variables:

   For each example directory (e.g., TextAnalytics or Translation), create a `.env` file and add the necessary credentials:

   ```
   # Text Analytics
   COG_SERVICE_ENDPOINT=your_cog_service_endpoint
   COG_SERVICE_KEY=your_cog_service_key

   # Translator
   TRANSLATOR_ENDPOINT=your_translator_endpoint
   TRANSLATOR_KEY=your_translator_key
   ```

   Replace `your_cog_service_endpoint`, `your_cog_service_key`, `your_translator_endpoint`, and `your_translator_key` with the actual values from your Azure services.

2. Have fun :-)

