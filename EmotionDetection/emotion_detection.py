import requests
import json

def emotion_detector(text_to_analyse):
    URL =  'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input = { "raw_document": { "text": text_to_analyse } }
    response =  requests.post(URL, json = Input, headers = Headers )
    formatted_response = json.loads(response.text)
    emotion_predictor = formatted_response["emotionPredictions"][0]["emotion"]
    emotion_predictor["dominant_emotion"] = max(emotion_predictor, key=emotion_predictor.get)
    return emotion_predictor