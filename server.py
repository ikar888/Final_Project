''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask framework package
# Import the Emotion Detector function from the package created
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector", methods=["GET"])

def emotion_analyzer():
    """
    Analyzes the emotions in a given text.

    This function retrieves the text to analyze from the request arguments,
    sends it to the emotion_detector function, and extracts the emotion data
    from the response. It then returns the results or an appropriate error message.

    Returns:
        str: A string with the emotion analysis results or an error message.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    if response is None:
        return "Invalid input! Try again."

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
    """
    Renders the main index page.

    This function renders the 'index.html' template, which serves as the homepage
    of the web application. It does not take any arguments and simply returns the
    rendered template.

    Returns:
        str: Rendered HTML content of 'index.html'.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
