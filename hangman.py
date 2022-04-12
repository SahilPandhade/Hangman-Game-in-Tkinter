#TO DO TASKS: 1)CHANGE THE READFILE FUNCTION TO ONLY PICK ONE RANDOM COUNTRY 
#             2)CORRECT THE WIDGETS
#             3)ADD A HOW TO PLAY BUTTON AND WRITE INSTRUCTIONS FOR PLAYING
#             4)GUESSES SHOULD NOT BE CASE SENSITIVE.  -----DONE
#             5)MAKE SURE TO CONSIDER ONLY SINGLE CHARACTER AS INPUT FROM USER -----DONE
#             6)ADD MORE WORDS TO THE DICTIONARY FILE

from tkinter import *
import random
from PIL import Image,  ImageTk
class Hangman:
    count=0
    words = set()
    word = str()
    asterisk = str()
    def __init__(self,window):
        self.readFile()
        #word = str(random.choice(tuple(dict)))
        #self.asterisk = "*" * len(self.word)
        #print(word)
        #print(asterisk)

        #Creating the main window
        self.window = window
        window.title('Hangman')
        window.geometry("400x400+10+10")

        #Title
        self.lbl=Label(window, text="Hangman", fg='black', font=("Times", 15,"bold"))
        self.lbl.place(x=150, y=10)

        self.lbl=Label(window, text="Guess this word:", fg='black', font=("Times", 10,"bold"))
        self.lbl.place(x=150, y=60)
        

        #Create a label to print the asterisk string to guess
        #(THIS STRING NEEDS TO BE UPDATED WITH EACH GUESS)
        self.ast = Label(window, text=self.asterisk,fg='black', font=("Times", 15,"bold"))
        self.ast.place(x=160, y=90)

        #Create a label to print whether guess is correct or not
        #Create a textbox to read the user input
        self.txtbox = Text(window,height=1,width=3)
        self.txtbox.place(x=175, y=120)

        #Here I used lambda function to read each guess and call hang method and also clear out the textbox for next guess
        self.btn = Button(window, text="Guess",command=lambda:[self.hang(),self.ast.config(text=self.asterisk),self.txtbox.delete('1.0',END)])
        self.btn.place(x=165,y=150)

        #self.img = Text(window,height=10,width=15)
        #self.img.place(x=140,y=200)
        

    #Main game method
    def hang(self):
        guess = self.txtbox.get(1.0,"end-1c").lower()[0]
        #print(guess)
        tempans = str()

        for i in range(len(self.word)):

            if self.word[i]==guess:
                tempans+=guess

            elif self.asterisk[i] != str('*'):
                tempans += self.word[i]

            else:
                tempans+=str("*")
        
        if self.asterisk==tempans:
            self.count+=1
            self.printImage()
        else:
            self.asterisk = tempans
        
        if(self.asterisk == self.word):
            self.callMethod()

    @classmethod
    def readFile(cls):
        fileobj = open('C:\\Users\\HP\\Desktop\\workspace\\Hangman\\dictionary.txt','r')
        
        while True:
            line = fileobj.readline()

            if not line:
                break

            #dict.add(line.strip())
            cls.words.add(line.strip())

        cls.word = str(random.choice(tuple(cls.words)))
        cls.asterisk = "*" * len(cls.word)
        #print(dict)


    #Method to print the Hangman Image
    def printImage(self):
        if self.count==1:
            # Create a photoimage object of the image in the path
            image1 = Image.open("C:\\Users\\HP\\Desktop\\workspace\\Hangman\\img1.PNG") 
            

        if self.count==2:
            image1 = Image.open("C:\\Users\\HP\\Desktop\\workspace\\Hangman\\img2.PNG")
            

        if self.count==3:
            image1 = Image.open("C:\\Users\\HP\\Desktop\\workspace\\Hangman\\img3.PNG")
            

        if self.count==4:
            image1 = Image.open("C:\\Users\\HP\\Desktop\\workspace\\Hangman\\img4.PNG")
            

        if self.count==5:
            image1 = Image.open("C:\\Users\\HP\\Desktop\\workspace\\Hangman\\img5.PNG")
            

        if self.count==6:
            # Create a photoimage object of the image in the path
            image1 = Image.open("C:\\Users\\HP\\Desktop\\workspace\\Hangman\\img6.PNG")
            

        if self.count==7:
            image1 = Image.open("C:\\Users\\HP\\Desktop\\workspace\\Hangman\\img7.PNG")
            self.callMethod()

        image1 = image1.resize((100,100), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(image1)

        label1 = Label(image=test)
        label1.image = test

        # Position image
        label1.place(x=150, y=200)
        return

    #Stuff to do after winning
    def callMethod(self):
        msg = "You Won !!"
        if(self.count==7):
            msg = "You Lost,The word was : "+self.word
        winlabel = Label(window, text=msg, fg='black', font=("Times", 10,"bold"))
        winlabel.place(x=155,y=330)
        self.btn["state"] = "disabled"
        return    







window = Tk()

obj = Hangman(window)
window.mainloop()
        