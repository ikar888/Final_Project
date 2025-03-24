import requests
import json

def emotion_detector(text_to_analyze, document_key="raw_document"):
    # URL of the emotion analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Constructing the request payload in the expected format
    myobj = { document_key: { "text": text_to_analyze } }

    # Custom header specifying the model ID for the emotion analysis service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    #POST request to the emotion analysis API
    response = requests.post(url, json=myobj, headers=header)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    
    # Extracting the emotion data from the response
    emotion_data = formatted_response['emotionPredictions'][0]['emotion']
    
    # Extracting the emotion scores from the response
    emotion_scores = {emotion: round(float(score), 11) for emotion, score in emotion_data.items()}
    
    # Checking the the highest scoring emotion
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Returning a dictionary containing emotion analysis results
    return {
        'anger': emotion_scores["anger"],
        'disgust': emotion_scores["disgust"],
        'fear': emotion_scores["fear"],
        'joy': emotion_scores["joy"],
        'sadness': emotion_scores["sadness"],
        'dominant_emotion': dominant_emotion
    }