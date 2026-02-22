from flask import Flask, request, jsonify
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return "Emotion Detection API is running!"

@app.route("/emotionDetector")
def detect_emotion():
    text = request.args.get("textToAnalyze")
    result = emotion_detector(text)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) 