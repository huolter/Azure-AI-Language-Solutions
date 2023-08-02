from dotenv import load_dotenv  # using dotenv to store credentials
import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


def main():
    try:
        # Get Configuration Settings - endpoint and key
        load_dotenv()
        cog_endpoint = os.getenv('COG_SERVICE_ENDPOINT')
        cog_key = os.getenv('COG_SERVICE_KEY')

        # Create client using endpoint and key
        text_analytics_client = TextAnalyticsClient(
            endpoint=cog_endpoint, credential=AzureKeyCredential(cog_key))

        # Analyze each text file in the text folder
        # Here we will make sequential calls, but this can also be done
        # passing a list of documents
        text_folder = 'texts'
        for file_name in os.listdir(text_folder):
            # Read the file contents
            print('\n-------------\n' + file_name)
            text = open(os.path.join(text_folder, file_name),
                        encoding='utf8').read()
            print('\n' + text)

            # Get language
            lang_result = text_analytics_client.detect_language([text])[0]
            print("\n", lang_result.primary_language.name)

            # Get sentiment
            sentimentAnalysis = text_analytics_client.analyze_sentiment(documents=[text])[
                0]
            print("\nSentiment: {}".format(sentimentAnalysis.sentiment))

            # Get key phrases
            phrases = text_analytics_client.extract_key_phrases(documents=[text])[
                0].key_phrases
            if len(phrases) > 0:
                print("\nKey Phrases:")
                for phrase in phrases:
                    print('\t{}'.format(phrase))

            # Get entities
            entities = text_analytics_client.recognize_entities(documents=[text])[
                0].entities
            if len(entities) > 0:
                print("\nEntities")
                for entity in entities:
                    print('\t{} ({})'.format(entity.text, entity.category))

    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()
