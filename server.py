""" Routes for web app deployment """
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion detector")

@app.route("/emotionDetector")
def emot_detector():
    """ query incoming argument to NPL emotion detector API, 
    and return emotional values of the argument """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    if response is None:
        return "Invalid text! Please try again."

    anger =  response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]
    return f"For the given statement, the system response is 'anger': {anger}, " \
            f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. " \
            f"The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    """ render index.html template """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
