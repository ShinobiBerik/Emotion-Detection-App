import requests  # Import the requests library to handle HTTP requests

def emotion_detector(text_to_analyze):
    # The URL specifically assigned for Watson Emotion Detection
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Structure the input data dictionary required by the API
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Configure the mandatory model ID header mapping for emotion prediction
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Execute the POST network request to the embedded service
    response = requests.post(url, json=myobj, headers=header)
    
    # Extract and return the raw text attribute from the response block
    return response.text