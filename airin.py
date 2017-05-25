
import speech_recognition  as sr
import webbrowser
# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
	print("Say Something!")
	audio = r.listen(source)

# Speech recognition using Google Speech Recognition
try:
	# for testing purposes, we're just using the default API key
	# to use another API key, use 'r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_KEY)'
	# instead of 'recognize_google(audio)'
	perintah = r.recognize_google(audio)
except sr.UnknownValueError:
	print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
	print("Could not request results from Google Speech Recognition service; {0}".format(e))

if perintah == "open":
	webbrowser.open("http://www.tokopedia.com")
elif perintah == "store":
	webbrowser.open("http://www.tokopedia.com/izakjenie")
elif perintah == "add product":
	webbrowser.open("https://www.tokopedia.com/product-add.pl?ref=addpdside")