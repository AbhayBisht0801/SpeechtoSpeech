import streamlit as st
import numpy as np
from voice_to_audio import detect_input, model_output, output_audio

audio_rate = [x * 0.25 for x in range(0, 13)] 
#For selection the type of voice
voice_gender = st.selectbox('Select the Audio Type', ('Male', 'Female'))



# selecting the speed for the audio
default_index = audio_rate.index(1.0)
speed = st.selectbox('Select the audio rate', tuple(audio_rate), index=default_index)

if st.button('Click Here to Ask'):
    with st.spinner('Hearing'):
        text = detect_input()
        result = model_output(text=text)
        
        # The audio rate start from 50 here as 50 refer to 0.25 speed and we have the values till 400 as it refers to 2 x speed
        # as audio rate ranges from 0.25 to 2 in put so we multiple with 200.
        # eg: for we can want the audio to be at speed 1X the its converted for pyttsx3 we multiple 1 * 200 to get 1X speed in it.
        output_audio(result=result, speed=speed*200, voice=voice_gender)
