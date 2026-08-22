"""
Flask server implementation for the Emotion Detection application.
This script routes requests to the Watson NLP emotion detection service
and handles the presentation of data or error states to the user.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask application
app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emot_detector():
    """
    Analyze the text argument and return the formatted emotion scores
    or an error message for invalid entries.
    """
    # Retrieve the text input from the web interface request
    text_to_analyze = request.args.get("textToAnalyze")

    # Pass the text to the emotion detection package function
    response = emotion_detector(text_to_analyze)

    # Extract dominant_emotion to verify if the text entry was valid
    dominant_emotion = response["dominant_emotion"]

    # Task 7 Error Handling: Check if the text input was blank
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Return the successful response matching the user interface template criteria
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is **{dominant_emotion}**."
    )


@app.route("/")
def render_index_page():
    """
    Render the main application HTML user interface page.
    """
    return render_template("index.html")


if __name__ == "__main__":
    # Deploy the application to run locally on port 5000
    app.run(host="0.0.0.0", port=5000)
