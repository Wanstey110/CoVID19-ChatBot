import random
import time
import tkinter
from tkinter import *
import sympcheck
import growthRate
import cUpdates
count = 0

##Main function
def main():
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
        myname = entryUser.get('1.0', 'end-1c')
                                                                            
        global chatbot                           
        chatbot = entryChat.get('1.0', 'end-1c')
        
        if myname == "" or chatbot == "":
            Label(frameInfo , text = "Please fill in both fields" , bg = "red" , fg = "white" , font = 'Verdana 11 bold').place(x = 182 , y = 96)
            return 

        entryUser.delete('1.0' , END)
        entryChat.delete('1.0' , END)

        frameInfo.pack_forget()
        frameChat.pack()
        
    #------------------------------------------------------------------------------------------

    """
    opening files after selection of
            topic in topic selestion
                        page
    """

    def topic1():
        global noTopic
        noTopic = 1
        
        global top
        top = 'chat.txt'

        global a
        a = open(top , 'r')

        global doc
        doc = a.readlines()

        frameInfo.pack_forget()
        frameChat.pack()    

        topic = "CoVID-19"
        labelTopic.config(text = topic)

        refreshScreen()

    #----------------------------------------------------------------------------------------------------------

    """
    functions for writing in files
            for writing in files in chat screen

    """

    def writeAns() :

        enter1 = entryFeed.get('1.0' , END)

        b.write(enter1)
        b.close()

        window.destroy()

        """           
            Reopening of files after
            changes are saved
        """

        if noTopic == 1 :
            topic1()
        
    def feedAnswer() :

        """
    a seperate window for writing answer
                on file

        """

        global window
        window=Tk()

        frameRoot = Frame(window , bg = c1)
        frameRoot.pack()
                                                                                                
        label = Label(frameRoot , text = 'Enter your answer to the Question here ...' , bg = c1 , fg = 'white' )
        label.pack()

        global entryFeed
        entryFeed = Text (frameRoot , height = 3 , width = 30 , fg = 'white' , bg = c2)
        entryFeed.bind ('<Return>' , writeAns)
        entryFeed.pack()

        button = Button(frameRoot , text = 'Add answer' , command  = writeAns , bg = c3 , fg = 'white' )
        button.pack()
        
    def writeFile() :

        """
    opening file for appending in
    exsisting  files

        """

        global b
        b = open (top , 'a')
        
        b.write(chatRaw)
        b.write('\n')

        buttonWrite.place_forget()
        feedAnswer()

    #----------------------------------------------------------------------------------------------

    def refreshScreen() :

        for widget in frameChats.winfo_children():
            widget.destroy()

        buttonWrite.place_forget()
        labelSpace = Label(frameChats , bg = c1 ,  text = '')
        labelSpace.pack()

    #------------------------------------------------------------------------------------------
    def submit() :
        global count
        count += 1
        """
    function for producing response of
            request of user

        """
        global noTopic
        noTopic = 1

        global top
        top = 'chat.txt'

        global a
        a = open(top, 'r')

        global doc
        doc = a.readlines()

        frameInfo.pack_forget()
        frameChat.pack()

        topic = "CoVID-19"
        labelTopic.config(text=topic)
        if count == 0:
            refreshScreen()

        buttonWrite.place_forget()
        global chatRaw
        chatRaw = entry.get('1.0', 'end-1c')
                            
        entry.delete('1.0' , END)
        
        chat = chatRaw.lower()
        chat = chat.replace(" ","")

        global labelRequest
        labelRequest = Label(frameChats ,text=chatRaw , bg = c4 , fg= c7  , justify = LEFT , wraplength = 300, font = 'Verdana 10 bold')
        
        labelRequest.pack(anchor = 'w')   
            
        if chat == 'groupmembers' or chat == 'group' or chat == 'developers' or chat == 'groupmember':
            answer = "William Anstey \n Demetrios Economou"

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
            update + your country
            updateworld
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
        
        elif chat == 'updateworld':
            answer = cUpdates.cUpdateWorld()
        
        elif chat == 'updateusa' or chat == 'updatecanada' or chat == 'updatechina':
            specialChat = chat.replace("update", "")
            answer = cUpdates.cUpdateSpecial(specialChat)

        elif 'update' in chat: 
            upc = chat.find('update')
            upc = chat.replace('update','')
            ascii1 = ord(upc[0])
            ascii2 = chr(ascii1-32)
            rep = upc.replace(upc[0],ascii2)
            answer = cUpdates.cUpdate(rep)
        
        elif chat == "sympcheck" or chat == "symptomcheck":
            getResponse("Check your terminal to answer the questions!")
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
                    answer = "I comprehend"
                elif chat.endswith("?"):
                    answer = "I'm sorry but I can't answer that"
                buttonWrite.place(x=430,y=3)

        getResponse(answer)
            
    def getResponse(answer) :

        global labelResponse
        labelResponse = Label(frameChats ,text= answer ,bg= c5 , fg = c8 , justify = LEFT , wraplength = 300, font = 'Verdana 10 bold')

        labelResponse.pack(anchor = 'e')

        if answer ==  'Bye':
            root.destroy()


    #------------------------------------------------------------------------------------------------------------------

    """

    moving from one page to another
        by help of button

    """

    def welcomeToInfo():
        frameWelcome.pack_forget()
        frameInfo.pack()
        
    def infoToTopic():
        frameInfo.pack_forget()
        frameChat.pack()
        topic1()


    def chatToTopic():
        frameChat.pack_forget()
        frameInfo.pack()

    def infoToWelcome():
        frameInfo.pack_forget()
        frameWelcome.pack()

    ##Initialize TKinter
    root = Tk()  

    """  Images used in window  """

    back = PhotoImage(file = 'arrow_behind.png')
    front = PhotoImage(file = 'arrow_ahead.png')
    exitt = PhotoImage(file = 'exit.png')
    screen1 = PhotoImage(file = 'image_5.png')
    submitImg = PhotoImage(file = 'image_8.png')

    #---------------------------------------------------------------------------------------------------------------------

    """     WELCOME FRAME    """
    """    first frame containing time date and welcome messages """

    frameWelcome = Frame(root , bg = c1 , height = '670' , width = '550')
    frameWelcome.pack_propagate(0)
    frameWelcome.pack()                 

    
    welcome = Label(frameWelcome , text = 'Welcome' , font = "Vardana 40 bold" , bg = c1 , fg = "white")
    welcome.place(x = 160 , y = 200)

    welcomeChatbot = Label(frameWelcome , text = 'I am your CoVID-19 friendly chatbot!' , font = "Helvetica 15 bold italic" , bg = c1 , fg = c6)
    welcomeChatbot.place(x = 125 , y = 270)

    pic1 = Label(frameWelcome , image = screen1)
    pic1.place(x = -2 , y = 357 )

    buttonFront = Button(frameWelcome , image = front , relief = "flat" , bg = c1 , bd = "3px solid black" , command = welcomeToInfo ).place(x=470 , y=10)

    #__________________________________________________________________

    """  time option  """

    def clock() :
        current = time.strftime("%H:%M:%S")
        labelTime = Label(frameWelcome , bd = 5 ,  text = current , height = 1 , width = 8 , font = 'Ariel 11 bold' ,  fg = "white" , relief = 'groove' , bg = c3)
        labelTime.place(x= 120 , y = 63)

        labelTime.after(1000 , clock )
    
    buttonTime = Button(frameWelcome , text = 'Time' , height = 1 , font = 'Vardana 10 bold' ,  width = 8 , bg = c2 , fg = c1 ,  command = clock)
    buttonTime.place(x=30 , y = 63)

    #_____________________________________________________________________________

    """    date option   """

    def date() :
        
        try:
            date = time.strftime("%d %B , 20%y")
            labelDate = Label(frameWelcome , bd = 5 , relief = 'groove' ,  text = date , bg = c3 , fg = "white"  , height = 1 , font = 'Ariel 11 bold')
            labelDate.place(x= 400 , y = 63)

            labelDate.after(86400000 , date)
            
        except AttributeError:
            print('')        
            
            
    buttonDate = Button(frameWelcome , text = 'Date' ,height = 1 , font = 'Vardana 10 bold' ,  width = 8 , bg = c2 , fg= c1 , command = date)
    buttonDate.place(x = 310 , y = 63)

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    """     INFO FRAME   """
    """     frame of entering names    """

    frameInfo = Frame(root , bg = c1 , height = '670' , width = '550')
    frameInfo.pack_propagate(0)

    spacer1 = Label(frameInfo , bg = c1)
    spacer1.pack()

    spacer2 = Label(frameInfo , bg = c1)
    spacer2.pack()

    labelSub = Label(frameInfo ,text = "Enter name information" , bg = c1 , fg = "white" , font = 'Verdana 30 italic')
    labelSub.pack()
                                
    username = Label(frameInfo , text = 'What should the chatbot call you? ' , bg = c1 , fg = c2 , font = 'Ariel 15')
    username.place(x = 80,y=130)

    entryUser = Text (frameInfo , bg = c6, fg = "white" , height ='1'  , width ='40' , font = 'Ariel 15')
    entryUser.focus()
    entryUser.place(x = 80 , y = 170)

    chatbotName = Label(frameInfo , text = 'What do you want to call the chatbot? ' , bg = c1 , fg = c2 , font = 'Ariel 15')
    chatbotName.place(x = 80 , y = 220)

    entryChat = Text (frameInfo , bg = c6, fg = "white" , height ='1'  , width ='40' , font = 'Ariel 15')
    entryChat.place(x = 80 , y = 260)

    button1 = Button(frameInfo , text ='submit' , font = 'Vardana 10 bold' , bg = c2 , fg = c1 , command = info )
    button1.place(x = 470 , y = 330)

    buttonBack = Button(frameInfo , image =  back , relief = "flat" , bg = c1 , command = infoToWelcome).place(x=10 , y = 10)

    #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    """     TOPIC FRAME   """
    """"   frame for topic selection     """
    """
    frameTopic = Frame(root , bg = c1 , height = '670' , width = '550')
    frameTopic.pack_propagate(0)
                                
    spacer3 = Label(frameTopic , bg = c1)
    spacer3.pack()

    spacer4 = Label(frameTopic , bg = c1)
    spacer4.pack()

    spacer5 = Label(frameTopic , bg = c1)
    spacer5.pack()

    option1 = Label(frameTopic , text = """ """
        Make sure you type in lowercase without spaces! 
        E.g. whatisyourname?
        If you're stuck, type help
        Press the arrow to proceed to the chat
        """ """, font = 'Verdana 15 italic' , bg = c1 , fg= c2)
    option1.place(x = 0 , y = 100)

    buttonOpt1 = Button(frameTopic , text = 'Proceed' , image = front , relief = "flat" , bg = c1 ,command = topic1)
    buttonOpt1.place(x = 350 , y = 50)

    buttonBack = Button(frameTopic , image = back , relief = "flat", bg = c1 , command = topicToInfo).place(x=10 , y = 10)
    """

    """         CHAT FRAME   """
    """"       Main Chat Screen   """
    frameChat = Frame(root , bg = c1 , height = '670' , width = '550')
    frameChat.pack_propagate(0)

    frameTop = Frame(frameChat , bg = c3 , height = '100' , width = '550')
    frameTop.pack()

    labelTopic = Label(frameTop , bg = c3 , fg = 'white' , font = 'Verdana 20 bold ')
    labelTopic.pack(pady = '40')

    frameSpacer = Frame(frameTop , bg = c2 , height = "10" , width = "550" )
    frameSpacer.pack()

    bottomFrame = Frame(frameChat , bg = c2 , height = '100' , width = '550')
    bottomFrame.pack_propagate(0)
    bottomFrame.pack(side = BOTTOM)

    button = Button(bottomFrame , image = submitImg , relief = "flat", font = 'Vardana 10 bold' , bg = c3 , command = submit )
    button.place(x = 410 , y = 27)
                                    
    entry = Text (bottomFrame , bg = c3 , fg = c6 , height = '5'  , width ='45' , font  ='Verdana 10')
    entry.bind ('<Return>' , submit)
    entry.place(x = 30, y = 10)

    frameChats = Frame(frameChat , bg = c1 , height = '450' , width = '500' )
    frameChats.pack_propagate (0)
    frameChats.pack()

    labelSpace = Label(frameChats , bg = c1).pack()

    buttonRefresh = Button(frameChat , bg = c3 , fg = c2 ,  text = 'refresh' , font = 'Vardana 10 bold' ,  command =refreshScreen)
    buttonRefresh.place(x = 440 , y = 80)

    buttonWrite = Button(bottomFrame , text = 'write' ,bg = c3 ,fg = c2 , font = 'Vardana 8' ,  command = writeFile )

    buttonBack = Button(frameChat , image = back , relief = "flat" , bg = c3 , command = chatToTopic).place(x=10 , y = 10)
    buttonFront = Button(frameChat , image = exitt , relief = "flat" , bg = c3 , command = root.destroy ).place(x=440 , y = 10)
    
    getResponse("""
        Make sure you type in lowercase without spaces! 
        E.g. whatisyourname?
        If you're stuck, type help
        """)


    root.mainloop()

if __name__ == "__main__":
    main()
##Well done you made it!
