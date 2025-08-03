
# 🤖 AI Doctor with Vision and Voice

This project is a proof-of-concept multimodal AI application that simulates a medical consultation. Users can speak to an AI doctor and upload a medical image for analysis. The application processes both audio and visual inputs to generate a spoken diagnosis and recommendation.

## ⚙️ Technical Workflow

The application operates through a sequential pipeline that integrates several AI models and services:

1.  [cite\_start]**User Input**: The user interacts with a **Gradio** web interface to record audio from their microphone and upload an image file[cite: 1].

2.  [cite\_start]**Speech-to-Text (STT)**: The recorded audio is processed by the `tts` function [cite: 4][cite\_start], which uses the **Groq API** to access the `whisper-large-v3` model for fast and accurate transcription[cite: 1, 4].

3.  [cite\_start]**Image Encoding**: The uploaded image is converted into a Base64 string by the `sext` function[cite: 2]. [cite\_start]This format is required for inclusion in the API request to the vision model[cite: 2].

4.  [cite\_start]**Multimodal Analysis**: The transcribed text and the encoded image are sent to the **Groq API** to be analyzed by the `meta-llama/llama-4-scout-17b-16e-instruct` model[cite: 1, 2]. [cite\_start]A detailed system prompt instructs the model to act as a professional doctor, analyze the image in a medical context, and provide a concise, two-sentence response in a single paragraph[cite: 1].

5.  [cite\_start]**Text-to-Speech (TTS)**: The AI's text response is passed to the `texi` function [cite: 3][cite\_start], which uses the **Google Text-to-Speech (gTTS)** library to convert the text into a natural-sounding audio file[cite: 1, 3].

6.  [cite\_start]**Output**: The Gradio interface is updated to display the user's transcribed question, the AI doctor's text response, and an audio player to listen to the spoken diagnosis[cite: 1].

-----

## 🛠️ Technology Stack

  * [cite\_start]**UI Framework**: Gradio [cite: 1]
  * [cite\_start]**AI Service Provider**: Groq API [cite: 2, 4]
  * [cite\_start]**Vision & Reasoning LLM**: Meta Llama 4 Scout [cite: 1, 2]
  * [cite\_start]**Speech-to-Text Model**: Whisper V3 [cite: 1, 4]
  * [cite\_start]**Text-to-Speech Engine**: gTTS (Google Text-to-Speech) [cite: 3]
  * [cite\_start]**Audio Libraries**: pydub, speechrecognition [cite: 4]
  * **Core Language**: Python

-----

## 🚀 Getting Started

Follow these instructions to set up and run the project locally.

### Prerequisites

  * Python 3.7+
  * A Groq API Key

### Installation

1.  **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/ai-doctor-vision-voice.git
    cd ai-doctor-vision-voice
    ```

2.  **Create and activate a virtual environment:**

    ```sh
    # Windows
    python -m venv venv && venv\Scripts\activate
    # macOS / Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:** Create a `requirements.txt` file with the content below and run the installation command.

    *`requirements.txt`*:

    ```
    gradio
    groq
    gtts
    pydub
    speechrecognition
    ```

    *Installation command*:

    ```sh
    pip install -r requirements.txt
    ```

4.  [cite\_start]**Set up Environment Variables:** The application requires a Groq API key to function[cite: 1, 2, 4]. Create a file named `.env` in the root directory of the project and add your API key:

    *`.env` file*:

    ```
    GROQ_API_KEY="your-groq-api-key-here"
    ```

    *Note: To load this variable automatically, you may need to install and use a library like `python-dotenv` in your main script.*

-----

## 🏃‍♀️ How to Run

1.  Make sure your `GROQ_API_KEY` is set in your environment.

2.  Run the main application script:

    ```sh
    python grad.py
    ```

3.  The console will output a local URL (e.g., `http://127.0.0.1:7860`). Open this URL in your web browser to use the application.
