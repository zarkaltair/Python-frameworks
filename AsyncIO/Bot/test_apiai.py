import json
import apiai

from config import TOKEN_DIALOGFLOW


def test_apiai(text):
    request = apiai.ApiAI(TOKEN_DIALOGFLOW).text_request()
    request.lang = 'ru'
    request.session_id = 'Test_session_2'
    request.query = text
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech']
    return response

print(test_apiai('How are you?'))