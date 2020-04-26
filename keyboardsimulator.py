###################################################################################### Imports ###############################################################################
import keyboard                                   """pip install keyboard"""            ## imports Keyboard package     
import speech_recognition                         """pip install speechrecognition"""   ## speech recognition over google ___ requires internet access  
from nltk.tokenize import word_tokenize           """pip install nltk"""                ## for word tokenization ___ Advanced program can bring Natural Language processing

################################################################################## Voice Recognition #########################################################################
def listenit():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening : ")
        r.adjust_for_ambient_noise(source)                                              ## cancels noise
        audio = r.listen(source,timeout=3)                                              ## listens for 3 sec.
        value = r.recognize_google(audio)                                               ## uses google speech recognition online
        #value = r.recognize_sphinx(audio)       """pip install pocketsphinx"""      ##  # Untag for Offline ___ in that case, install pocketsphinx 
    return value

#################################################################################### Main Program ###########################################################################
flag = "start"
while flag == "start" :
    try:
        command = listenit()
        tokens = word_tokenize(command)
        key=["up", "down", "right", "tab" ,"left","next","stop", "enter","back","open"]
        for i in tokens:
            if i in key:
                if i=="up":
                    keyboard.press_and_release('up')                                   ## simulates keyboard up key
                    print(i)
                elif i=="down":
                    keyboard.press_and_release('down')                                 ## simulates keyboard down key
                    print(i)
                elif i=="tab":
                    keyboard.press_and_release('tab')                                  ## simulates keyboard tab key
                    print(i)
                elif i=="enter":
                    keyboard.press_and_release('enter')                                ## simulates keyboard enter key
                    flag= "stop"
                    print(i)
                elif i=="right" or i=="next":
                    keyboard.press_and_release('right')                                ## simulates keyboard right key
                    print(i)
                elif i=="left":
                    keyboard.press_and_release('left')                                 ## simulates keyboard left key
                    print(i)
                elif i=="back":
                    keyboard.press_and_release('backspace')                            ## simulates keyboard backspace key
                    print(i)
                elif i=="open":
                    keyboard.press_and_release('enter')                                ## simulates keyboard enter key
                    flag= "stop"
                    print(i)
                elif i== "stop":                                                       ## stop means close the program
                    flag ="stop"
    except speech_recognition.WaitTimeoutError :
        print ("try again")
    except speech_recognition.UnknownValueError :
        print ("try again")

"""

Simple Voice Control your Computer,  

"""

