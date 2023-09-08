import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser

import sys
from PIL import Image
from tkinter import*


def run():
    engine = pyttsx3.init(driverName='sapi5',debug=False)
    voices = engine.getProperty('voices')
    # print(voices[1].id)
    engine.setProperty('voice', voices[0].id)


    def speak(audio):
        engine.say(audio)
        engine.runAndWait()
        


    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Good Morning!")

        elif hour>=12 and hour<18:
            speak("Good Afternoon!")   

        else:
            speak("Good Evening my master!")  

        speak("I am Charlie  Sir. Please tell me how may I help you")       

    def takeCommand():
        #It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening your voice...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-IN')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please...")  
            return "None"
        return query



    if __name__ == "__main__":
        wishMe()
        while True:
        # if 1:
            query = takeCommand().lower()

            #Logic for executing tasks based on query
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'youtube' in query:
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                webbrowser.open("google.com")

            elif 'stackoverflow' in query:
                webbrowser.open("stackoverflow.com")   


            
            elif  'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")

            elif 'please stop' in query:
                speak("I will stop now O K , Bye Bye see you next time.")
                sys.exit()  

            elif 'fool' in query:
                speak("you are fool also.")

            elif 'are you' in query:
                speak("I am Ankit Badhani Chatbot  And my name is Aakash Badhaani. And Ankit Badhani created me.")

            elif 'car' in query:
                speak("my   favourite  car  is  the Volks wagen ,B M W")
            # img=Image.open("C:\\Users\\ACER\Downloads\\ABT Amps Up Volkswagen's Touareg TDI SUV _ Man of Many.jpg")
            # img.show()  

            elif 'favourite song' in query:
                speak('My favourite song is Blue eyes by Honey singh')  

            elif 'monday time table' in query:
                speak('First lecture COA . Second lecture Electronics Engineering. Third lecture Data Structures. Fourth lecture Technical Communication . Then Lunch Break. Fifth lecture Personal Development. Sixth lecture Mini Project Lab')   

            elif 'tuesday time table' in query:
                speak('First lecture D S T L. Second lecture Electronics Engineering. Third lecture Mini project . Fourth lecture Personal Development. Then Lunch Break. Fifth and sixth both are D S T L  Lab. ')

            elif 'wednesday time table' in query:
                speak('First lecture D S T L. Second lecture Electronics Engineering. Third lecture Data Structures. Fourth lecture Technical Communication. Then Lunch Break. Fifth  and sixth lecture C O A Lab. ')

            elif 'thursday time table' in query:
                speak('First lecture C O A. Second lecture Electronics Engineering. Third lecture Data Structures. Fourth lecture Technical Communication. Then Lunch Break. Fifth  lecture C S S . Sixth lecture Personal Development.')

            elif 'friday time table' in query:
                speak('First lecture C O A. Second lecture Electronics Engineering. Third lecture Data Structures. Fourth lecture D S T L. Then Lunch Break. Fifth and sixth lecture Data Structures using C Lab.')

            elif 'saturday time table' in query:
                speak('First lecture C O A. Second lecture Personal Development. Third lecture D S T L. Fourth lecture  Personal development. Then Lunch Break. Fifth and sixth lecture ACTIVITY . ')   

            elif 'data structures teacher'  in query:
                speak('Mister Devesh Malik is your Data Structures Teacher.') 

            elif 'electronics teacher' in query:
                speak('Miss Indu Chauhan is your Electronics Engineering Teacher.') 

            elif 'computer organization teacher.' in query:
                speak('sharad Lamba is your C O A teacher.')

            elif 'discrete mathematics teacher' in query:
                speak('Mister Ravi Baliyaan is your discrete mathematics teacher.')

            else:
                speak("Can you say that again please.")    
            

                    

root=Tk()
root.geometry("788x400")
root.title("Chatbot CHARLIE")
root.iconbitmap('Chatbot Image.ico')
l1=Label(root,bg="white",font="comicsansms 50 bold",fg='yellow',text="AUTO BOT",relief=RAISED)
l1.pack(fill='x')
l3=Label(root,bg="light blue",relief=RAISED,fg="black",text="Here is your Auto Bot.\n\nPOINT NUMBER 1:-Click below button to start the Time Table Bot.\n\nPOINT NUMBER 2:-Ask him about time table of specific day.       \n\nPOINT NUMBER 3:-Just say 'PLEASE STOP' to stop the bot otherwise it\n\n will not stop listening.\n\nPOINT NUMBER 4:-Now you are ready to ask question to the Bot.\n\nPOINT NUMBER 5:-You have to surely say 'PLEASE STOP ' if you wants to stop\n\n the Bot from listening whatever you are saying ,otherwise it will not stop. ",font="comicsansms 20 bold")
l3.pack(fill="x")
l2=Label(root,bg="blue",fg='red',relief=RAISED)
l2.pack(padx=40,pady=40)
b1=Button(l2,bg="grey",text="Click here to run the bot",relief=RAISED,font="comicsansms 10 bold",command=run)
b1.pack()
root.mainloop()