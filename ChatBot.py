import random
import time
import tkinter
from tkinter import *
import sympcheck
import growthRate
import cUpdates

##Color Table
c1 = '#263238'
c2 = '#faa21f'
c3 = '#1e282d'
c6 = '#577e75'

c4 = '#faa21f'
c5 = '#577e75'

c7 = '#1e282d'
c8 = '#faa21f'
"""
getting data from entry of
    'Enter Name' page
"""

def info() :
    global myname
    myname = entry_user.get('1.0', 'end-1c')
                                                                        
    global chatbot                           
    chatbot = entry_chat.get('1.0', 'end-1c')
    
    if myname == "" or chatbot == "":
        Label(frame_info , text = "Please fill in both fields" , bg = "red" , fg = "white" , font = 'Verdana 11 bold').place( x = 182 , y = 96)
        return 

    entry_user.delete('1.0' , END)
    entry_chat.delete('1.0' , END)

    frame_info.pack_forget ()
    frame_topic.pack ()
    
#------------------------------------------------------------------------------------------

"""
opening files after selection of
        topic in topic selestion
                    page
"""

def topic_1():
    global no_topic
    no_topic = 1
    
    global top
    top = 'chat.txt'

    global a
    a = open(top , 'r')

    global doc
    doc = a.readlines()

    frame_topic.pack_forget()
    frame_chat.pack()    

    topic = "CoVID-19"
    label_topic.config(text = topic)

    refresh_screen()

#----------------------------------------------------------------------------------------------------------

"""
functions for writing in files
        for writing in files in chat screen

"""

def write_ans () :

    enter1 = entry_feed.get('1.0' , END)

    b.write(enter1)
    b.close()

    window.destroy()

    """           
        Reopening of files after
           changes are saved
    """

    if no_topic == 1 :
        topic_1()
    
    elif no_topic == 2 :
        topic_2()          
    
    elif no_topic == 3 :
        topic_3()
    
    elif no_topic == 4 :
        topic_4()
    
    elif no_topic == 5 :
        topic_5()
    
def feed_answer () :

    """
a seperate window for writing answer
            on file

    """

    global window
    window=Tk()

    frame_root = Frame(window , bg = c1)
    frame_root.pack()
                                                                                            
    label = Label (frame_root , text = 'Enter your answer to the Question here ...' , bg = c1 , fg = 'white' )
    label.pack()

    global entry_feed
    entry_feed = Text (frame_root , height = 3 , width = 30 , fg = 'white' , bg = c2)
    entry_feed.bind ('<Return>' , write_ans)
    entry_feed.pack()

    button = Button (frame_root , text = 'Add answer' , command  = write_ans , bg = c3 , fg = 'white' )
    button.pack()
    
def write_file () :

    """
opening file for appending in
exsisting  files

    """

    global b
    b = open ( top , 'a')
    
    b.write(chat_raw)
    b.write('\n')

    button_write.place_forget()
    feed_answer ()

#----------------------------------------------------------------------------------------------

def refresh_screen () :

    for widget in frame_chats.winfo_children():
        widget.destroy()

    button_write.place_forget()
    label_space = Label (frame_chats , bg = c1 ,  text = '')
    label_space.pack()

#------------------------------------------------------------------------------------------
def submit() :

    """
function for producing response of
        request of user

    """

    button_write.place_forget ()
    global chat_raw
    chat_raw = entry.get('1.0', 'end-1c')
                        
    entry.delete('1.0' , END)
    
    chat = chat_raw.lower()
    chat = chat.replace(" ","")

    global label_request
    label_request = Label(frame_chats ,text=chat_raw , bg = c4 , fg= c7  , justify = LEFT , wraplength = 300, font = 'Verdana 10 bold')
    
    label_request.pack(anchor = 'w')   
    
    global answer
    
    if chat == 'groupmembers' or chat == 'group' or chat == 'developers' or chat == 'groupmember':
          answer = "William Anstey \n Demetrious Economous"

    elif chat == "what'smyname?" or chat == "whatsmyname?" or chat == "whatismyname?" or chat == "whatsmyname" or chat == 'myname?' or chat =='myname' :
          answer = myname

    elif chat == "what'syourname?" or chat == "whatisyourname?" or chat == "whatsyourname?" or chat == "whatsyourname" or chat == 'yourname?' or chat =='yourname' :
          answer = chatbot

    elif chat == 'bye' or chat == 'goodbye' or chat == 'exit' or chat == 'close' or chat == 'end' :
          answer = 'Bye'

    ## TODO add other functionalities
    elif chat == "growthrate" or chat == "covid-19growth" or chat == "coronavirusgrowthrate" or chat == "ncov-19growthrate":        
        answer = "Here is a graph showing the estimated growth rate of the SARS-CoV-2 virus"
        growthRate.showGraph()

    elif chat == "help":
        answer = """
        Try these commmands:
        growthrate
        symptomscheck
        update + your country (currently only Japan Singapore and Australia are working)
        Also feel free to ask me any questions you have about the virus, like when was the first case etc.
        """

    elif chat == "hello!" or chat == "hello":
        x = random.randint(1, 3)
        if x == 1:
            answer = "Hey there!"
        elif x == 2:
            answer = "Hi!"
        elif x == 3:
            answer = "Heyo"

    elif chat == "updatejapan":
        placeHolder = cUpdates.cUpdate("Japan")
        answer = f"Current CoVID-19 statistics in Japan:\n{placeHolder}"
    
    elif chat == "updatesingapore":
        placeHolder = cUpdates.cUpdate("Singapore")
        answer = f"Current CoVID-19 statistics in Singapore:\n{placeHolder}"
    
    elif chat == "updateaustralia":
        placeHolder = cUpdates.cUpdate("Australia")
        answer = f"Current CoVID-19 statistics in Australia:\n{placeHolder}"
        

    elif chat == "sympcheck" or chat == "symptomcheck":
        simp = sympcheck.sympcheck()
        answer = simp

    else:
        i = 0
        j = 0
        for lines in doc:
             stats = lines [:-1]
             stats = stats.lower()
             stat = stats.replace(' ','')
             i += 1
             if stat == chat :
                    answer = doc[i]
                    break
             else:
                 j += 1
                 
        if i == j :
              blurb = random.randint(1, 4)
              if blurb == 1:
                answer = "I see"
              elif blurb == 2:
                answer = "Interesting"
              elif blurb == 3:
                answer = "Indeed"
              elif blurb == 4:
                answer == "I comprehend"
              elif chat.endswith("?"):
                answer = "I'm sorry but I can't answer that"
              button_write.place(x=430,y=3)


    get_response()
        
def get_response() :

    global label_response
    label_response = Label(frame_chats ,text= answer ,bg= c5 , fg = c8 , justify = LEFT , wraplength = 300, font = 'Verdana 10 bold')

    label_response.pack(anchor = 'e')

    if answer ==  'Bye':
        root.destroy()


#------------------------------------------------------------------------------------------------------------------

"""

moving from one page to another
    by help of button

"""

def welcome_to_info ():
    frame_welcome.pack_forget ()
    frame_info.pack ()
    
def info_to_topic ():
    frame_info.pack_forget ()
    frame_topic.pack ()

def topic_to_chat ():
    frame_topic.pack_forget ()
    frame_chat.pack()

def chat_to_topic ():
    frame_chat.pack_forget ()
    frame_topic.pack ()

def topic_to_info ():
    frame_topic.pack_forget ()
    frame_info.pack ()

def info_to_welcome ():
    frame_info.pack_forget ()
    frame_welcome.pack ()

##Initialize TKinter
root = Tk ()  

"""  Images used in window  """

back = PhotoImage(file = 'arrow_behind.png')
front = PhotoImage(file = 'arrow_ahead.png')
exitt = PhotoImage(file = 'exit.png')
screen_1 = PhotoImage(file = 'image_5.png')
submit_img = PhotoImage(file = 'image_8.png')

#---------------------------------------------------------------------------------------------------------------------

"""     WELCOME FRAME    """
"""    first frame containing time date and welcome messages """

frame_welcome = Frame (root , bg = c1 , height = '670' , width = '550')
frame_welcome.pack_propagate(0)
frame_welcome.pack()                 

  
welcome = Label (frame_welcome , text = 'Welcome' , font = "Vardana 40 bold" , bg = c1 , fg = "white")
welcome.place(x = 160 , y = 200)

welcome_chatbot = Label (frame_welcome , text = 'I am your CoVID-19 friendly chatbot!' , font = "Helvetica 15 bold italic" , bg = c1 , fg = c6)
welcome_chatbot.place(x = 125 , y = 270)

pic_1 = Label (frame_welcome , image = screen_1)
pic_1.place(x = -2 , y = 357 )

button_front = Button (frame_welcome , image = front , relief = "flat" , bg = c1 , bd = "3px solid black" , command = welcome_to_info ).place(x=470 , y=10)

#__________________________________________________________________

"""  time option  """

def clock () :
    current = time.strftime("%H:%M:%S")
    label_time = Label (frame_welcome , bd = 5 ,  text = current , height = 1 , width = 8 , font = 'Ariel 11 bold' ,  fg = "white" , relief = 'groove' , bg = c3)
    label_time.place(x= 120 , y = 63)

    label_time.after( 1000 , clock )
   
button_time = Button (frame_welcome , text = 'Time' , height = 1 , font = 'Vardana 10 bold' ,  width = 8 , bg = c2 , fg = c1 ,  command = clock)
button_time.place(x=30 , y = 63)

#_____________________________________________________________________________

"""    date option   """

def date () :
    
    try:
        date = time.strftime("%d %B , 20%y")
        label_date = Label (frame_welcome , bd = 5 , relief = 'groove' ,  text = date , bg = c3 , fg = "white"  , height = 1 , font = 'Ariel 11 bold')
        label_date.place(x= 400 , y = 63)

        label_date.after(86400000 , date)
        
    except AttributeError:
        print('')        
        
        
button_date = Button (frame_welcome , text = 'Date' ,height = 1 , font = 'Vardana 10 bold' ,  width = 8 , bg = c2 , fg= c1 , command = date)
button_date.place(x = 310 , y = 63)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""     INFO FRAME   """
"""     frame of entering names    """

frame_info = Frame (root , bg = c1 , height = '670' , width = '550')
frame_info.pack_propagate(0)

spacer1 = Label(frame_info , bg = c1)
spacer1.pack()

spacer2 = Label(frame_info , bg = c1)
spacer2.pack()

label_sub = Label (frame_info ,text = "Enter name information" , bg = c1 , fg = "white" , font = 'Verdana 30 italic')
label_sub.pack()
                            
user_name = Label (frame_info , text = 'What should the chatbot call you? ' , bg = c1 , fg = c2 , font = 'Ariel 15')
user_name.place(x = 80,y=130)

entry_user = Text (frame_info , bg = c6, fg = "white" , height ='1'  , width ='40' , font = 'Ariel 15')
entry_user.focus()
entry_user.place(x = 80 , y = 170)

chatbot_name = Label (frame_info , text = 'What do you want to call the chatbot? ' , bg = c1 , fg = c2 , font = 'Ariel 15')
chatbot_name.place(x = 80 , y = 220)

entry_chat = Text (frame_info , bg = c6, fg = "white" , height ='1'  , width ='40' , font = 'Ariel 15')
entry_chat.place(x = 80 , y = 260)

button_1 = Button (frame_info , text ='submit' , font = 'Vardana 10 bold' , bg = c2 , fg = c1 , command = info )
button_1.place(x = 470 , y = 330)

button_back = Button (frame_info , image =  back , relief = "flat" , bg = c1 , command = info_to_welcome).place(x=10 , y = 10)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""     TOPIC FRAME   """
""""   frame for topic selection     """

frame_topic = Frame (root , bg = c1 , height = '670' , width = '550')
frame_topic.pack_propagate(0)
                            
spacer3 = Label(frame_topic , bg = c1)
spacer3.pack()

spacer4 = Label(frame_topic , bg = c1)
spacer4.pack()

spacer5 = Label(frame_topic , bg = c1)
spacer5.pack()

option_1 = Label (frame_topic , text = """
    Make sure you type in lowercase without spaces! 
    E.g. whatisyourname?
    If you're stuck, type help
    Press the arrow to proceed to the chat
    """ , font = 'Verdana 15 italic' , bg = c1 , fg= c2)
option_1.place(x = 0 , y = 50)

button_opt_1 = Button (frame_topic , text = 'Proceed' , image = front , relief = "flat" , bg = c1 ,command = topic_1)
button_opt_1.place(x = 350 , y = 50)

button_back = Button (frame_topic , image = back , relief = "flat", bg = c1 , command = topic_to_info).place(x=10 , y = 10)

"""         CHAT FRAME   """
""""       Main Chat Screen   """

frame_chat = Frame (root , bg = c1 , height = '670' , width = '550')
frame_chat.pack_propagate(0)

frame_top = Frame( frame_chat , bg = c3 , height = '100' , width = '550')
frame_top.pack()

label_topic = Label ( frame_top , bg = c3 , fg = 'white' , font = 'Verdana 20 bold ')
label_topic.pack(pady = '40')

frame_spacer = Frame( frame_top , bg = c2 , height = "10" , width = "550" )
frame_spacer.pack()

bottom_frame = Frame (frame_chat , bg = c2 , height = '100' , width = '550')
bottom_frame.pack_propagate(0)
bottom_frame.pack(side = BOTTOM)

button = Button (bottom_frame , image = submit_img , relief = "flat", font = 'Vardana 10 bold' , bg = c3 , command = submit )
button.place(x = 410 , y = 27)
                                   
entry = Text (bottom_frame , bg = c3 , fg = c6 , height = '5'  , width ='45' , font  ='Verdana 10')
entry.bind ('<Return>' , submit)
entry.place(x = 30, y = 10)

frame_chats = Frame (frame_chat , bg = c1 , height = '450' , width = '500' )
frame_chats.pack_propagate (0)
frame_chats.pack()

label_space = Label(frame_chats , bg = c1).pack()

button_refresh = Button (frame_chat , bg = c3 , fg = c2 ,  text = 'refresh' , font = 'Vardana 10 bold' ,  command =refresh_screen)
button_refresh.place(x = 440 , y = 80)

button_write = Button (bottom_frame , text = 'write' ,bg = c3 ,fg = c2 , font = 'Vardana 8' ,  command = write_file )

button_back = Button (frame_chat , image = back , relief = "flat" , bg = c3 , command = chat_to_topic).place(x=10 , y = 10)
button_front = Button (frame_chat , image = exitt , relief = "flat" , bg = c3 , command = root.destroy ).place(x=440 , y = 10)

root.mainloop ()
##Well done you made it!