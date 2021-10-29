import keyboard                                                 ######      Keyboard library to simulate keyboard                                
import speech_recognition                                       ######      Speech Recognition to convert speech to text              
from nltk.tokenize import word_tokenize                         ######      NLTK to tokenize command
import os                                                       ######      to import os functions
import pyttsx3                                                  ######      pyttsx3 for elsa to reply
import subprocess                                               ######      to start application as a subprocess
#import threading                                               ######      for multi threading 

# init_voice class
# for defining properties of voice and speed
# pyttsx3 as engine
# create an object to use voice as per the properties and run engine
class init_voice() :
    engine = pyttsx3.init()  # object creation
    voices = engine.getProperty('voices')  # getting details of current voice
    #engine.setProperty('voice', voices[0].id)  # changing index, changes voices. 0 for male
    engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female
    engine.setProperty('rate', 140)

# listenit function
# for listen command
# no arguments or parameter passing
# initialises the speech reoigniser and convert it to text
# return the text of the command
def listenit():
    # creates an boject for recognizer in speech recognition module
    r = speech_recognition.Recognizer()
    # make microphone as source
    with speech_recognition.Microphone() as source:
        print("Listening : ")
        # adjust for ambient noise
        r.adjust_for_ambient_noise(source)
        # get audio of the command from the user                                      
        audio = r.listen(source,timeout=3)  
        # use google api to convert the audio to text                                            
        value = r.recognize_google(audio)   
    # return the text command as value           
    return value

# listen text function
# for listening text to insert
# no arguments or parameter passing
# initialises the speech reoigniser and convert it to text
# return the text to be inserted
def listentext():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening text : ")
        r.adjust_for_ambient_noise(source)                                              
        audio = r.listen(source,timeout=3)                                              
        text = r.recognize_google(audio)              
    return text

# Main Function
# the program starts here
if __name__ == "__main__" :

    # initializes a flag to keep the program running
    flag = "start"
    
    # create an object of init_voice as reply
    reply = init_voice()
    
    # loop that depends on the flag that keeps the program alive
    while flag == "start" :
        
        # try to catch exceptions in voice recognition
        try:
            
            # store the command and print the same
            command = listenit()
            print (command)
            
            # convert the command to tokens
            tokens = word_tokenize(command)
            
            # initializing a list to store the keywords
            key=["up", "down", "right", "tab" ,"left","next","stop","start","enter","undo","redo","back","okey","quit","open","insert", "add","select","ok","hello", "hai", "hey","hi", "hay"]
            
            # for each token in tokens
            for i in tokens:
                
                # for every token in key
                if i in key:
                    
                    # reply to simple hi
                    if i=="hai" or i=="hey" or i=="hay" or i=="hello"  or i=="hi" :   
                        # initializes the reply
                        reply.engine.say("hi I am elsa, i am your voice assistant, i can do what ever you say!")
                        # runs the reply engine
                        reply.engine.runAndWait()                               
                        #print(i)
                    
                    # up arrow key command
                    if i=="up":
                        reply.engine.say("moving up")
                        reply.engine.runAndWait()
                        # specify the button to be pressed
                        # keyboard press and release simulates the function
                        keyboard.press_and_release('up')                                   
                        print(i)
                        
                    # down arrow key command
                    elif i=="down":
                        reply.engine.say("moving down")
                        reply.engine.runAndWait()
                        keyboard.press_and_release('down')                                                               
                        print(i)
                        
                    # simulates tab press
                    elif i=="tab":
                        reply.engine.say("moving tab")
                        reply.engine.runAndWait()
                        keyboard.press_and_release('tab')                                 
                        print(i)
                        
                        
                    # simulates tab press
                    elif i=="escape":
                        reply.engine.say("moving tab")
                        reply.engine.runAndWait()
                        keyboard.press_and_release('esc')                                 
                        print(i)
                        
                    # simulates enter key
                    elif i=="enter" or i=="ok" or i=="okey" or i =="select":
                        if i=="enter" or i =="select": 
                            reply.engine.say(i + "ing")
                            reply.engine.runAndWait()     
                        keyboard.press_and_release('enter')                       
                        #flag= "stop"
                        print(i)
                        
                    # right arrow key command
                    elif i=="right" or i=="next":
                        reply.engine.say("next")
                        reply.engine.runAndWait()
                        keyboard.press_and_release('right')                               
                        print(i)
                    
                    # left arrow key command
                    elif i=="left":
                        reply.engine.say("moving left")
                        reply.engine.runAndWait()
                        keyboard.press_and_release('left')          
                        print(i)
                    
                    # simulates backspace key stroke 
                    elif i=="back":
                        keyboard.press_and_release('backspace')                          
                        print(i)
                
                    # execute a command to open a specific application
                    # if no application specified simulates enter stroke
                    elif i=="open" or i=="start":
                        
                        # converts the command to upper case for propper opertion
                        command = command.upper()
                        
                        # checks for the specified app in command : Google-Chrome
                        if ("GOOGLE" in command) or ("SEARCH" in command) or ("WEB BROWSER" in command) or ("CHROME" in command) or ("BROWSER" in command): 
                            #print(command)
                            reply.engine.say("opening google chrome")
                            reply.engine.runAndWait()
                            # runs the binary form the specified location in the system
                            # not in every case to provide the location, directly specify the app name (refer line 154)
                            # Python code continues executing as soon as the process is spawned
                            open_process = (subprocess.Popen("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT))
                    
                        # checks for the specified app in command : Microsoft-Edge
                        elif ("IE" in command) or ("MSEDGE" in command) or ("EDGE" in command): 
                            print(command)
                            reply.engine.say("opening microsoft egde browser")
                            reply.engine.runAndWait()
                            # microsoft egde is a direct distribution of microsoft. so one can directly open the app by execcuting the command 'msegde'
                            open_process = (subprocess.Popen("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL))

                        # checks for the specified app in command : notepad
                        elif ("NOTE" in command) or ("NOTES" in command) or ("NOTEPAD" in command) or ("EDITOR" in command): 
                            print(command)
                            reply.engine.say("opening notepad")
                            reply.engine.runAndWait()
                            open_process = subprocess.Popen("Notepad", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

                        # checks for the specified app in command : VLC media player
                        elif ("VLCPLAYER" in command) or ("PLAYER" in command) or ("VIDEO PLAYER" in command): 
                            print(command)
                            reply.engine.say("opening VLC player")
                            reply.engine.runAndWait()
                            open_process = subprocess.Popen("VLC", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    
                        # checks for the specified app in command : Adobe illustrator
                        elif ("ILLUSTRATOR" in command) or ("AI" in command): 
                            print(command)
                            reply.engine.say("opening adobe illustrator")
                            reply.engine.runAndWait()
                            open_process = subprocess.Popen("illustrator", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    
                        # checks for the specified app in command : Adobe Photoshop
                        elif ("PHOTOSHOP" in command) or ("PS" in command) or ("PHOTOSHOP CC" in command): 
                            print(command)
                            reply.engine.say("opening adobe photoshop")
                            reply.engine.runAndWait()
                            open_process = subprocess.Popen("photoshop", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) 
                    
                        # checks for the specified app in command : telegram
                        elif ("TELEGRAM" in command) or ("TG" in command) : 
                            print(command)
                            reply.engine.say("opening telegram")
                            reply.engine.runAndWait()
                            open_process = subprocess.Popen("telegram", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    
                        # checks for the specified app in command : Microsoft Excel
                        elif ("EXCEL" in command) or ("MSEXCEL" in command) or ("SHEET" in command) or ("WINEXCEL" in command) :
                            print(command)
                            reply.engine.say("opening microsoft EXCEL")
                            reply.engine.runAndWait()
                            open_process = (subprocess.Popen("excel", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL))
                            print (open_process)
                        # checks for the specified app in command : Microsoft PowerPoint
                        elif ("SLIDE" in command) or ("POWERPOINT" in command) or ("MSPOWERPOINT" in command) or ("PPT" in command) or ("POWERPNT" in command): 
                            print(command)
                            reply.engine.say("opening microsoft powerpoint")
                            reply.engine.runAndWait()
                            open_process = (subprocess.Popen("powerpnt", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL))
                        # checks for the specified app in command : Microsoft Word
                        elif ("WORD" in command) or ("MSWORD" in command) or ("1" in command): 
                            print(command)
                            reply.engine.say("opening microsoft word")
                            reply.engine.runAndWait()
                            open_process = subprocess.Popen("winword", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) 
                    
                        # else the application is not found
                        else :
                            if i=="start":
                                keyboard.press_and_release('windows') 
                            else : 
                                reply.engine.say("Sorry i cant help you in this moment, Make sure application is insalled, If installed sorry for the inconvnience, soon we will find a solution.")
                                reply.engine.runAndWait()
                    
                    # a condition to add or insert text or command directly in to the text field
                    # check for insert or add token        
                    elif i=="insert" or i == "add" :
                        # check for text command
                        if ("text" in command) :
                            reply.engine.say(" Now say the text to be inserted soon after this message ")
                            reply.engine.runAndWait() 
                            # call listen text function       
                            text = listentext()
                            print("inserting text ", text)
                            # write the text directly by keyboard write method
                            # pass in the text to be inserted
                            keyboard.write(text)
                    
                    # Undo command ctrl + z                             ######### to be tested
                    elif i=="undo":
                        reply.engine.say("stepping back")
                        reply.engine.runAndWait()
                        keyboard.press_and_release('ctrl+z')          
                        print(i)
                    
                    # Redo command ctrl + shift + z                     ######### to be tested
                    elif i=="redo":
                        reply.engine.say("step forward")
                        reply.engine.runAndWait()
                        keyboard.press_and_release('ctrl+shift+z')          
                        print(i)
                    
                    # comand to kill  or terminate all processes started
                    elif i== "stop":   
                        reply.engine.say("All applications clossing")
                        reply.engine.runAndWait() 
                        # terminates the process
                        open_process.terminate()                                                  
                    
                    # comand to kill  or terminate all processes started as well as Elsa    
                    elif i== "quit":  
                        reply.engine.say("All applications clossing")
                        reply.engine.runAndWait() 
                        open_process.terminate()    
                        reply.engine.say("Elsa Closing, Nice meeting you, Bye")
                        reply.engine.runAndWait()    
                        # reset flag to get out of the loop and end the  Elsa Program                                           
                        flag ="stop"
        
        # exception Handler    
        # for timeout error                                       
        except speech_recognition.WaitTimeoutError :
            print ("try again")
        # for Unknown value error
        except speech_recognition.UnknownValueError :
            print ("try again")
            
            
#####   to be added            
#####   Add text select
#####   Copy and Paste text objects


#####   Deep Learning model based controlling
