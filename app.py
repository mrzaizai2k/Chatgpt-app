from flask import Flask, render_template, request
import openai
import os

# set up OpenAI API credentials
openai.api_key = os.environ.get("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")

# initialize Flask app
app = Flask(__name__)

# define home route
@app.route("/")
def home():
    return render_template("index.html")

# define route for generating answers
@app.route("/generate", methods=["POST"])
def generate():
    # get question from form data
    question = request.form["question"]

    # generate answer using OpenAI API
    response = openai.Completion.create(
        engine="davinci", prompt=question, max_tokens=1024, n=1, stop=None, temperature=0.7
    )

    # get answer from API response
    answer = response.choices[0].text.strip()

    # render answer template with generated answer
    return render_template("answer.html", question=question, answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
