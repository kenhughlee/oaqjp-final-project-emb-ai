import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze }}
    response = requests.post(url, json = myobj, headers=header)

    formatted_response = json.loads(response.text)
    
    emotion_res = formatted_response['emotionPredictions'][0]['emotion']

    # Extracting sentiment label and score from the response
    anger_score = emotion_res['anger']
    disgust_score = emotion_res['disgust']
    fear_score = emotion_res['fear']
    joy_score = emotion_res['joy']
    sadness_score = emotion_res['sadness']
    
    high_score = 0
    
    #loop through emotions to find dominant emotion
    for emotion, score in emotion_res.items():
        if (score > high_score):
            high_score = score
            dom_emotion = emotion 

    # Returning a dictionary containing sentiment analysis results
    return {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score,'sadness': sadness_score, 'dominant_emotion': dom_emotion}