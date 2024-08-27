import speech_recognition as sr
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import pyttsx3 as tt
load_dotenv()
# This function return the output from the voice text by using llm
def model_output(text):
    model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')
    # Creating prompt to answer in two sentence
    template = '''answer the following  in 2 sentences:
    {user_input}'''
    
    prompt = PromptTemplate(template=template, input_variables=['user_input'])
    formatted_prompt = prompt.format(user_input=text)
    print(formatted_prompt)
    
    result = model.invoke(formatted_prompt).content
    return result
# this fuction takes in audio input of user
def detect_input():

    try:
        # Initialize recognizer class (for recognizing the speech)
        r = sr.Recognizer()

        # Use the microphone as the audio source
        with sr.Microphone(sample_rate=16000) as source:
            print("Say something!")
            
            try:
                # Listen for the first phrase and extract it into audio data
                audio_data = r.listen(source, timeout=2)
                
                # Recognize speech using Google Speech Recognition
                text = r.recognize_google(audio_data)
                print("You said: " + text)
                return text
            
            except sr.UnknownValueError:
                print("Your audio wasn't clear")
            except sr.WaitTimeoutError:
                print("Please speak something, listening timed out")
    except OSError:
        print('Connect your input Device')
# assigning the respective voice and audio rate
def output_audio(result,speed,voice):
    speaker = tt.init()
    
    rate = speaker.getProperty('rate')  
    speaker.setProperty('rate', speed)
    voices=speaker.getProperty('voices') 
    # select voice based on user choice
    if voice=='Male':
        speaker.setProperty('voice',voices[0].id)
    else:
        speaker.setProperty('voice',voices[1].id)

    # Speak the result
    speaker.say(result)

    # Run the speech engine to actually speak the text
    speaker.runAndWait()



    

