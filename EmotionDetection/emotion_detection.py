import requests

URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict";

def emotion_detector(text_to_analyze):
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"};
    json = { "raw_document": { "text": text_to_analyze } };
    response = requests.post(URL, json = json, headers = headers);
    response_dict = response.json();
    emotion = response_dict["emotionPredictions"][0]["emotion"];
    dominant_emotion = max(emotion, key=emotion.get);
    emotion["dominant_emotion"] = dominant_emotion;
    return emotion;