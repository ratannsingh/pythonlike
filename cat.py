#!/usr/bin/python3
#Python 2.x program for Speech Recognition
import os 
from gtts import gTTS
import speech_recognition as sr
 

#Sample rate is how often values are recorded
sample_rate = 48000
#Chunk is like a buffer. It stores 2048 samples (bytes of data)
#here. 
#it is advisable to use powers of 2 such as 1024 or 2048
chunk_size = 2048
#Initialize the recognizer
r = sr.Recognizer()
with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source)
	print ("Say Something")
	#listens for the user's input
	audio = r.listen(source)
         
	try:
		text = r.recognize_google(audio)
		x=list(text.split(' '))
		size_x=len(x)
		if x[0] =='copy' and size_x < 4:
    			os.system('cp x[1] x[2]  ')
		print ("you said:"+text)
	
     
    #error occurs when google could not understand what was said
     
	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")
     
	except sr.RequestError as e:
        	print("Could not request results from Google") 
                         




