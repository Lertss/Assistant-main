import tkinter

import pyttsx3
import speech_recognition as sr


def RunGlos(zdanie):
    tts = pyttsx3.init()
    voices = tts.getProperty('voices')

    # Set the default voice

    tts.setProperty('voice', 'ruя')

    # Try to set your preferred voice

    for voice in voices:
        if voice.name == 'Microsoft Irina Desktop':
            tts.setProperty('voice', voice.id)
            tts.setProperty('rate', 135)

    tts.say(zdanie)
    tts.runAndWait()

    #The command() function is used to track the microphone.
	#Running the function we will listen to what the user will say,

def command():

    r = sr.Recognizer()

    # Start listening to the microphone and write the data to the source
    with sr.Microphone() as source:
        # Just a conclusion so we know when to talk

        RunGlos("Говорите")
        # Setting a pause to listen
        # started only after 1 second
        r.pause_threshold = 1
        # use adjust_for_ambient_noise to delete
        # extraneous noise from the audio track
        r.adjust_for_ambient_noise(source, duration=1)
        # We write the received data to the audio variable
        # so far we have received only mp3 sound
        audio = r.listen(source)

    try:
        """ 
        		We recognize the data from the mp3 track.
        		We indicate that the monitored language is Russian.
        		Thanks to lower(), we put everything in lower case.
        		Now we have received data in string format,
        		which we can safely check in the conditions
        """
        zadanie = r.recognize_google(audio, language="ru-RU").lower()

    # If you could not recognize the text, this error will be caused
    except sr.UnknownValueError:
        # Voice input of the request
        # if the voice is not recognized, the question is displayed
        # repeat input or not
        RunGlos("Я вас не поняла")
        question = tkinter.messagebox.askquestion(title="Вопрос", message="Повторить ввод?")
        if question == 'yes':
            zadanie = command()
        elif question == "no":
            pass
    return zadanie
