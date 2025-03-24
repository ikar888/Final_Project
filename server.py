# Import Flask, render_template, request from the flask framework package
# Import the Emotion Detector function from the package created
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector", methods=["GET"])

def emotion_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the label and score from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Return the extracted emotions as a string to display in the HTML
    return f"""
        Anger: {anger}<br>
        Disgust: {disgust}<br>
        Fear: {fear}<br>
        Joy: {joy}<br>
        Sadness: {sadness}<br>
        Dominant Emotion: {dominant_emotion.capitalize()}
    """
    

@app.route("/")
# Renders the HTML page
def render_index_page():
    # Renders the HTML page
    return render_template('index.html')    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)