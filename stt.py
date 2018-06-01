#!/usr/bin/python3
import speech_recognition as sr
import os
sample_rate = 48000
chunk_size = 2048
r = sr.Recognizer()
with sr.Microphone() as source:

	r.adjust_for_ambient_noise(source)
	print ("say something")
	audio = r.listen(source)
	try:
		text = r.recognize_google(audio)
		x=list(text.split(' '))
		size_x=len(x)
		if x[0] =='make' and size_x < 3:
    			os.system("mkdir "+x[1])
		elif x[0]=='remove':
			os.system("rmdir "+x[1])
		print ("you said:"+text)
	
	except sr.UnknownValueError:
		print("google speech Recognition could not understand audio")
	except sr.RequestError as e:
		print("could not request results from Google")
