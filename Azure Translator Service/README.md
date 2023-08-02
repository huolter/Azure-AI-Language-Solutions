# Azure Translator Service

The Translator Azure Cognitive Service provides an API for translating text between 90 supported languages.

To use the Translator service, you must provision a resource for it in your Azure subscription. You can provision a single-service Translator resource, or you can use the Text Analytics API in a multi-service Cognitive Services resource.

You can perform language detection, translation and transliteration (for example to render a japanese text in Latin script) with the translator service. 

This script demonstrates how to use the Azure Translation Text service to translate text into multiple target languages. The objective is to translate the contents of a text file specified by 'text.txt' into the languages specified in the 'target_languages' list.

Read the documentation here [https://learn.microsoft.com/en-us/azure/ai-services/translator/]


## How the Script Works

The script loads the Azure credentials (endpoint, key, and region) from a .env file using the dotenv library.

It initializes the TextTranslationClient with the provided credentials.

The script reads the text to be translated from the file 'text.txt' using UTF-8 encoding.

The script then translates the text into the languages specified in the 'target_languages' list. For each translation, the detected language of the input text is displayed along with the translated text.

The translated text for each target language is saved in a .txt file with the name of the corresponding language. For example, if the translation is in English, the script will create a file named 'en.txt' containing the translated text.


## Note
The script demonstrates translation into English, Spanish, and French, but you can modify the 'target_languages' list to include other languages supported by the Azure Translation Text service.

If you encounter any errors during translation, the script will display the error code and message.

Check more examples here [https://github.com/MicrosoftTranslator/Text-Translation-Code-Samples/tree/main/Python-Code-Samples]