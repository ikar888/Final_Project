import requests
import json

def emotion_detector(text_to_analyze, document_key="raw_document"):
    # URL of the emotion analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {document_key: {"text": text_to_analyze}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    try:
        # POST request to the emotion analysis API
        response = requests.post(url, json=myobj, headers=header)
        response.raise_for_status()  # Raise an error for bad HTTP responses

        # Parsing the JSON response
        formatted_response = response.json()

        # Validate and extract emotion data
        if 'emotionPredictions' in formatted_response and len(formatted_response['emotionPredictions']) > 0:
            emotion_data = formatted_response['emotionPredictions'][0].get('emotion', {})
            emotion_scores = {emotion: round(float(score), 11) for emotion, score in emotion_data.items()}
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        else:
            emotion_scores = {}
            dominant_emotion = None

    except requests.exceptions.RequestException as e:
        print(f"HTTP request error: {e}")
        return None
    except (KeyError, IndexError, ValueError, json.JSONDecodeError) as e:
        print(f"Error processing the response: {e}")
        return None

    # Returning the emotion analysis results
    return {
        'anger': emotion_scores.get("anger", 0),
        'disgust': emotion_scores.get("disgust", 0),
        'fear': emotion_scores.get("fear", 0),
        'joy': emotion_scores.get("joy", 0),
        'sadness': emotion_scores.get("sadness", 0),
        'dominant_emotion': dominant_emotion
    }
