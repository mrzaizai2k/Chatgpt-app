# chatgpt-app
chatgpt call API to do things... Boost productivity app

This Flask application utilizes OpenAI's powerful language model for generating answers to user-submitted questions. The app features two main routes: the home route for initial page rendering and the generate route for answering questions.

## Setup

To set up the OpenAI API credentials, ensure you have an environment variable (`OPENAI_API_KEY`) containing your OpenAI API key.

## Usage

1. Visit the home route ("/") to access the initial page.
2. Ask a question using the provided form on the page.
3. Submit the form to the generate route ("/generate").
4. The app utilizes the OpenAI API to generate answers and displays them on the "answer.html" template.

## Important Note

Before running the application, replace the placeholder "OPENAI_API_KEY" in the code with your actual OpenAI API key.

## Running the Application

Ensure you have Flask installed. You can install it using:

```bash
pip install Flask

