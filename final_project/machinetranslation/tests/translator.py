from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

authenticator = IAMAuthenticator('OxlXPrtD-M2tTsugJZtMLLecbke0jQBNq2O_zlRus0QA')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/95900c38-a4b8-475a-ab74-61bd5c93affd')

def english_to_french(english_text):
    '''Translation of english to french'''
    french_translation = language_translator.translate(
        text= english_text,model_id='em-fr').get_result()
    french_text=french_translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    '''Translation of french to english'''
    eng_translation = language_translator.translate(
        text=french_text,model_id ='fr-en').get_result()
    english_text=eng_translation['translations'][0]['translation']
    return english_text