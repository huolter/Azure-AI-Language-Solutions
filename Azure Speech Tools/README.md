# Azure Speech Services

## Speech Command Transcription and Time Telling

This script demonstrates a simple functionality using the Azure Cognitive Services Speech API to transcribe spoken commands and respond with the current time.

## Prerequisites

Before running the script, make sure you have the following:

1. Python environment with the required packages installed (e.g., `dotenv` and `azure.cognitiveservices.speech`).
2. An Azure Cognitive Services Speech API key and region, which should be stored in a `.env` file with the following variables:

```
COG_SERVICE_KEY=your_cognitive_services_key
COG_SERVICE_REGION=your_cognitive_services_region
```

## How it Works

The script uses the `dotenv` library to load the environment variables containing the Cognitive Services API key and region. It then sets up the speech configuration using the provided API key and region.

1. `TranscribeCommand()` function:
   - Configures speech recognition using the default microphone.
   - Waits for the user to speak a command.
   - Transcribes the spoken command and returns it as text.

2. `TellTime()` function:
   - Retrieves the current time.
   - Uses text-to-speech synthesis to respond with the current time in the format "The time is HH:MM".

3. `main()` function:
   - Loads environment variables using `dotenv.load_dotenv()`.
   - Initializes the speech service with the provided API key and region.
   - Waits for a spoken command using `TranscribeCommand()`.
   - If the command is "what time is it?", it calls `TellTime()` to tell the current time.

## Running the Script

To run the script:

1. Ensure you have the required prerequisites mentioned above.
2. Save the script in a file, e.g., `speech_time_teller.py`.
3. Create a `.env` file in the same directory with your Cognitive Services API key and region, as shown in the prerequisites section.
4. Open a terminal or command prompt and navigate to the script's directory.
5. Run the script using the command: `python speech_time_teller.py`.

The script will listen for your spoken command and respond with the current time if you ask "what time is it?". Make sure your microphone is properly configured and accessible to the script.

Please note that this is a basic example to demonstrate speech recognition and synthesis functionality. You can extend and customize the script according to your specific use case and requirements.
```