from tkinter import *
from http.client import *
from json import *

#The Application class extends the TK class and creates a Frame
class Application(Tk):

    def __init__(self):
        super(Application,self).__init__()
        self.minsize(500,500)
        self.resizable(False,False)
        self.iconbitmap("logo.ico")
        self.title("Imgur API Tool")
        self.usernameLabel = Label(self)
        self.usernameLabel["text"]="Please type in an Imgur username into the box below:"
        self.usernameLabel.place(x=100,y=40)
        self.entryBox = Entry(self)
        self.textVar = StringVar()
        self.textVar.set("brandonrninefive")
        self.entryBox["textvariable"]=self.textVar
        self.entryBox.place(x=92,y=80,width=300)
        self.goButton = Button(self)
        self.goButton["text"]="Request JSON associated with the given username"
        self.goButton["command"]=self.requestJSON
        self.goButton.place(x=102,y =120)
        self.outputLabel = Label(self)
        self.outputLabel["text"]="Output:"
        self.outputLabel.place(x=215,y=180)
        self.nameLabel = Label(self)
        self.nameLabel["text"]="Username: "
        self.nameLabel.place(x=10,y=210)
        self.statusLabel = Label(self)
        self.statusLabel["text"]="Server Response Code: "
        self.statusLabel.place(x=10,y=240)
        self.statusMessageLabel = Label(self)
        self.statusMessageLabel["text"]="Server Error Message: "
        self.statusMessageLabel.place(x=10,y=270)
        self.idLabel = Label(self)
        self.idLabel["text"]="Account ID: "
        self.idLabel.place(x=10,y=300)
        self.urlLabel = Label(self)
        self.urlLabel["text"]="Account URL: "
        self.urlLabel.place(x=10,y=330)
        self.creationLabel = Label(self)
        self.creationLabel["text"]="Account Creation Timestamp: "
        self.creationLabel.place(x=10,y=360)
        self.reputationLabel = Label(self)
        self.reputationLabel["text"]="Account Reputation: "
        self.reputationLabel.place(x=10,y=390)
        self.proLabel = Label(self)
        self.proLabel["text"]="Account Pro Expiration: "
        self.proLabel.place(x=10,y=420)
        self.bioLabel = Label(self)
        self.bioLabel["text"]="Account Bio: "
        self.bioLabel.place(x=10,y=450)
        self.mainloop()
    #requestJSON() uses an HTTPSConnection to make a HTTP GET request based on the supplied username.
    #The function then displays the retrieved data via labels.
    def requestJSON(self):
       username = self.textVar.get()
       api_key = "ab8422c63a280b9"
       connection = HTTPSConnection("api.imgur.com")
       connection.putrequest("GET","/3/account/" + username +".json")
       connection.putheader("Authorization","Client-ID " + api_key)
       connection.endheaders()
       response = connection.getresponse().read().decode("utf-8")
       decoder = JSONDecoder()
       decodedResponse = decoder.decode(response)
       self.nameLabel["text"]="Username: "+username
       self.statusLabel["text"]="Server Response Code: " +str(decodedResponse["status"])
       if(decodedResponse["status"] != 200):
           self.statusMessageLabel["text"]="Server Error Message: "+ decodedResponse["data"]["error"]
           self.idLabel["text"]="Account ID: "
           self.urlLabel["text"]="Account URL: "
           self.creationLabel["text"]="Account Creation Timestamp: "
           self.reputationLabel["text"]="Account Reputation: "
           self.proLabel["text"]="Pro Expiration: "
           self.bioLabel["text"]="Account Bio: "
       else:
           self.statusMessageLabel["text"]="Server Error Message: None"
           self.idLabel["text"]="Account ID: " + str(decodedResponse["data"]["id"])
           self.urlLabel["text"]="Account URL: " + str(decodedResponse["data"]["url"]) +".imgur.com"
           self.creationLabel["text"]="Account Creation Timestamp: "+ str(decodedResponse["data"]["created"])
           self.reputationLabel["text"]="Account Reputation: " + str(decodedResponse["data"]["reputation"])
           self.proLabel["text"]="Pro Expiration: " + str(decodedResponse["data"]["pro_expiration"])
           self.bioLabel["text"]="Account Bio: " + str(decodedResponse["data"]["bio"]).replace("\n"," ")

#Creates an Application instance which displays the Frame
Application()
