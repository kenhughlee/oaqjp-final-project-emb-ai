"""this file is the server for the emotion detector"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")

def sent_analyzer():
    """function to retrieve text and return result""" 
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion detector function and store the response
    response = emotion_detector(text_to_analyze)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if response['dominant_emotion'] is None:
        return "<b>Invalid text! Please try again!</b>"
    return f"For the given statement, the system response is 'anger': {anger},\
    'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, and 'sadness': {sadness}. \
    The dominant emotion is <b>{dominant_emotion}</b>."

@app.route("/")
def render_index_page():
    """render the landing page"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
