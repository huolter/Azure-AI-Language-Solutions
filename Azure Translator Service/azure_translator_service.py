from dotenv import load_dotenv  # using dotenv to store credentials
import os
from azure.ai.translation.text import TextTranslationClient, TranslatorCredential
from azure.ai.translation.text.models import InputTextItem
from azure.core.exceptions import HttpResponseError


def main():
    load_dotenv()
    endpoint = os.getenv('COG_SERVICE_ENDPOINT')
    key = os.getenv('COG_SERVICE_KEY')
    region = os.getenv("COG_SERVICE_REGION")

    credential = TranslatorCredential(key, region)
    text_translator = TextTranslationClient(
        endpoint=endpoint, credential=credential)

    try:
        target_languages = ["en", "es", "fr"]
        file_path = 'text.txt'
        text = open(file_path, 'r', encoding='utf-8').read()
        print(text)

        input_text_elements = [InputTextItem(text=text)]

        response = text_translator.translate(
            content=input_text_elements, to=target_languages)
        translation = response[0] if response else None

        if translation:
            detected_language = translation.detected_language
            if detected_language:
                print(
                    f"Detected languages of the input text: {detected_language.language} with score: {detected_language.score}.")
            for translated_text in translation.translations:
                print(
                    f"Text was translated to: '{translated_text.to}' and the result is: '{translated_text.text}'.")
                # Save the text in a .txt file with the name of the detected language
                file_name = f"{translated_text.to}.txt"
                with open(file_name, 'w', encoding='utf-8') as file:
                    file.write(translated_text.text)

    except HttpResponseError as exception:
        print(f"Error Code : {exception.error.code}")
        print(f"Message: {exception.error.message}")


if __name__ == "__main__":
    main()
