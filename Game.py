from tkinter import *
from tkinter import messagebox
import tkinter.font as font
from PIL import Image, ImageTk
import random
import re


class Game(Exception):
    
    
    def __init__(self,rt):
        self.root=rt
        self.ip=StringVar()
        self.guess=""
    
        #A list containing words
        self.li=["earn","cure","silk","omit","calm","true","bent","grip","crib","bead","sore","half","view","chat","lift","surf","sire","rise","drag","slim"]
            
        #An extra list to change the words if user needs to play again
        self.li1=["coil","seat","stay","copy","cute","nail","size","gold","joke","shit"]
    
    
        self.window()
        self.buttons()
        self.root.mainloop()
        
        
    def window(self):
        #Root window
        self.root.title("GUESS MY WORD")
        self.root.wm_iconbitmap()
        self.root.geometry("1000x1000")
        
        #1st Frame
        self.frame=Frame(self.root,bg="#0accc2")
        self.frame.pack(fill=BOTH,expand=1)
        
        #Background Image
        """load = Image.open("de.jpg")
        s=load.resize((1000, 1000))
        render= ImageTk.PhotoImage(s)
        img =Label(self.frame, image=render)
        img.image = render
        img.place(x=0, y=0)"""
        
        
    #Menu Buttons
    def buttons(self):
        myFont = font.Font(family='Helvetica', weight='bold')
        
        self.button1=Button(self.frame,text="START",padx=25,pady=8,fg="black",bg="#ccc610",activebackground="#7be000",font=myFont,command=self.Start)
        self.button1.place(x=440, y=150)
        
        self.button2=Button(self.frame,text="HELP",padx=30,pady=8,fg="black",bg="#ccc610",activebackground="#7be000",font=myFont,command=self.Help)
        self.button2.place(x=440, y=230)
        
        self.button3=Button(self.frame,text="EXIT",padx=34,pady=8,fg="black",bg="#ccc610",activebackground="#7be000",font=myFont,command=self.Exit)
        self.button3.place(x=440, y=310)
        
        
    #Help Option   
    def Help(self):
        messagebox.showinfo("HOW TO PLAY", "1. In this,you have to guess a 4-letter word,so start with any random 4-letter word.\n\n2. If the letters in your guess are present in the word and are at exact position as that of the word than you will hit a bull.\n\n3. If the letters in your words are present but not in their fixed position then you will hit a bear.\n\n4. NOTE: You will have 10 attempts to guess the word including the starting guess.\n\n5. There are no same letters in the word.Each letter is unique.eg.make")
        
    #To Exit    
    def Exit(self):
        if(messagebox.askyesno('VERIFY', 'DO YOU REALLY WANT TO QUIT?')):
            self.root.destroy()
        
        
        
    #To Start The Game    
    def Start(self):
            #Another frame to play the game
            self.frame1=Frame(self.root,bg="#0accc2",width=1000,height=1000)
            self.frame1.pack(fill=BOTH,expand=1)
        
            #A random number will be generated
            self.r=random.randint(0,19)
            
            #The selected word is stored in variable "word"
            self.word=self.li[self.r]
        
            self.li[self.r]=self.li1[0]
            self.li1.pop(0)
            
        
            #To count number of attempts
            self.count=10
            
            #To place the words
            self.y1=0
            
            myFont = font.Font(family=' Comic Sans MS',size=15)
            myFont1 = font.Font(family=' Helvetica', weight='bold',size=25,underline=True)
            
            lbl1=Label(self.frame1,text="!!!!LET'S PLAY!!!!",font=myFont1,bg="#0accc2",fg="#c9720e")
            lbl1.place(x=130, y=25)
            
            lbl1=Label(self.frame1,text="THE WORD IS:",font=myFont,bg="#0accc2",fg="#c9720e")
            lbl1.place(x=180, y=105)
            
            lbl1=Label(self.frame1,text="__ __ __ __",font=myFont,bg="#0accc2",fg="#c9720e")
            lbl1.place(x=200, y=145)
            
            lblg=Label(self.frame1,text="Enter your guess:",font=myFont,bg="#0accc2",fg="#c9720e")
            lblg.place(x=180, y=215)
            
            
            #To take input from user
            self.gue=Entry(self.frame1,textvariable=self.ip,width=30)
            self.gue.place(x=345, y=222)
                       
             
            myFont2 = font.Font(family=' Comic Sans MS') 
            #The "OK" Button
            btn1=Button(self.frame1,text="OK",padx=7,pady=1,fg="black",bg="#ccc610",activebackground="#7be000",font=myFont2,command=self.Guess)
            btn1.place(x=360, y=255)
            
            #The "CLEAR" Button
            btn2=Button(self.frame1,text="CLEAR",padx=7,pady=1,fg="black",bg="#ccc610",activebackground="red",font=myFont2,command=self.Reset)
            btn2.place(x=440, y=255)
                        
       
    #To clear the input for next use.Works on the press of "CLEAR" Button                 
    def Reset(self):
        self.gue.delete(0, 'end')


    #Works on the press of "OK" Button          
    def Guess(self):
        self.ch=0
        self.guess=str(self.ip.get())
        self.guess=self.guess.lower()
        self.ss=[]
        
        #To check the ERRORS!!
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if(len(self.guess)>4 or len(self.guess)<4):
            self.ch=1
            messagebox.showerror("ERROR!!!","Need to input exactly 4 characters.")
        else:
            for i in range(0,len(self.guess)):
                #To check the input
                if(regex.search(self.guess[i]) == None): 
                    x=0
                else:
                    x=1
                if(self.guess[i].isdigit() or x==1):
                    self.ch=1
                    messagebox.showerror("ERROR!!!","WRONG INPUT!!!\nDigits or special characters are not allowed.\nRe-enter your guess")
                    break
        
        
        if(self.ch==0):
            myFont = font.Font(family=' Comic Sans MS',size=15)
        
            self.lbword=Label(self.frame1,text="WORD",font=myFont,bg="#0accc2",fg="#c9720e")
            self.lbword.place(x=650, y=100)
        
            self.lbbull=Label(self.frame1,text="IT CONTAINS:",font=myFont,bg="#0accc2",fg="#c9720e")
            self.lbbull.place(x=750, y=100)
        
            #self.lbbear=Label(self.frame1,text="BEAR",font=myFont,bg="#0accc2",fg="#c9720e")
            #self.lbbear.place(x=830, y=100)
        
            self.ss=self.Execute(self.guess)
        
        
            self.word1=self.ss[0]
            self.bull=self.ss[1]
            self.bear=self.ss[2]
            self.con=self.ss[3]
            
            
            if(self.bull!=4):
                self.lbword1=Label(self.frame1,text=self.guess,width=5,font=myFont,bg="#0accc2",fg="#c9720e")
                self.lbword1.place(x=655, y=135+self.y1)
            
            
            if(self.bull!=4):
                self.lbbull1=Label(self.frame1,text=self.con,font=myFont,bg="#0accc2",fg="#c9720e")
                self.lbbull1.place(x=770, y=135+self.y1)
        
            #self.lbbear1=Label(self.frame1,text=self.bear,font=myFont,bg="#0accc2",fg="#c9720e")
            #self.lbbear1.place(x=855, y=135+self.y1)
        
            self.y1+=35
    
        
            self.lblg=Label(self.frame1,text=self.word1,font=myFont,bg="#0accc2",fg="#c9720e")
            self.lblg.place(x=200, y=145)
        
        
            self.count-=1 
            if(self.count!=0 and self.bull!=4):
                self.strcount=str(self.count)
                self.att="You have "+ self.strcount +" attempts left."
                self.attempt=Label(self.frame1,text=self.att,font=myFont,bg="#0accc2",fg="#c9720e")
                self.attempt.place(x=240, y=340)
            else:
                self.attempt=Label(self.frame1,text="",width=30,height=2,bg="#0accc2")
                self.attempt.place(x=240, y=340)
            
            
        
            if(self.bull==4 or (self.bull==4 and self.count==0)):
                messagebox.showinfo("RESULT","CONGRATULATIONS!!\nYou have successfully guessed the word.\n*****Thank you for playing*****")
                self.gue.delete(0, 'end')
                self.frame1.destroy()
            
            
            if(self.count==0 and self.bull!=4):
                wordres=self.word
                wordres=wordres.upper()
                wordres="''"+wordres+"''"
                res="UNLUCKY!!\nBetter luck next time.\nThe word was "+wordres+"\n*****Thank you for playing*****"
                messagebox.showinfo("RESULT",res)
                self.gue.delete(0, 'end')
                self.frame1.destroy()
          
            
    #To execute the entered input    
    def Execute(self,guess):
        guess=guess
        length=len(self.word)
        s=""
        use=[]
        iden=[]    
        bull=0
        bear=0
    
        #This is use to check the entered guess
        for i in range(0,len(guess)):
            if(self.word.find(guess[i])>=0):
                ind=self.word.index(guess[i])
                s=s+guess[i]+","
                if(ind==i):
                    bull+=1
                    iden.append(" "+guess[i]+"   ")
                else:
                    bear+=1
                    iden.append("__ ")
            else:
                iden.append("__ ")
        if(not s):
            s=s+"- - - -"

        ss = ' '.join(map(str,iden))
        use.extend([ss,bull,bear,s])
        
        return(use)
                    
    
rt=Tk()
g=Game(rt)





