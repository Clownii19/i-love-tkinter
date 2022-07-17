from tkinter import *
from PIL import Image, ImageTk
import random 
from tkinter import messagebox
names = []
global questions_answers
asked = []
score=0
global choice 
choice=0 
import sys
import os 


def selector(): 
   global qnum
   qnum = random.randint(1,5) 
   if qnum not in asked:
      asked.append(qnum)
   elif qnum in asked:
      selector()

class Homescreen:
    def __init__(self, parent):
 
        background_color="white"
      
        self.heading_label=Label(parent, text="General Knowledge Quiz", font=("Tw Cen MT","35","bold"), bg="#FFE3D8", pady=80)
        self.heading_label.place(x=22, y=20) 
        
        self.blue_bar=Label(parent, text="‎ ‎ ‎ ", font=("Tw Cen MT","15","bold"), bg="#0A043C", padx=314, pady=5)
        self.blue_bar.place(x=22, y=20) 

        #label for username
        self.user_label=Label(parent, text="", font=("Tw Cen MT","1"),bg=background_color)
        self.user_label.place(x=50,y=230)
        
        #entry box
        self.entry_box=Entry(parent, width= 7, font=('Arial', 27))
        self.entry_box.place(x=270,y=251) 
        
        #continue button
        self.continue_button = Button(parent, text="Start", font=("Monoid", "35", "bold"), bg="#FFE3D8",height= 2, width= 6, command=self.name_error)
        self.continue_button.place(x=240,y=310)       
       
    def name_error(self):
      entry = self.entry_box.get()
      if entry == "":
        messagebox.showerror('Oops!', "Please enter your username.")
      else:
        self.name_collection()

    def name_collection(self): 
    #deletes everything from homescreen
     name=self.entry_box.get() 
     names.append(name) 
     self.heading_label.destroy()
     self.user_label.destroy()
     self.entry_box.destroy()
     self.continue_button.destroy()
     self.blue_bar.destroy()
     questions(root)  
    
     
           
class questions: 
  def __init__(self, parent):
        selector()
        background_color="#FFE3D8"
        

          #dictionary 
        self.questions_answers = {
        1:  ["‎ ‎ ‎ ‎ ‎ ‎ The thumb has the fastest growing nail.‎ ‎ ‎ ‎ ‎ ‎ ", 
               'True', 'False', 2, "False", "thumb.PNG"], 
      
        2: ["There are 193 countries recognised by the UN", 'True', 
               'False', 1, "True", "UN.png"], 
      
        3: ["Jeff Bezos is the richest person in the world.‎ ‎ ‎ ‎ ‎ ‎", 'True', 'False', 2, "False", "jeffbezos.png"],
      
        4: ["‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ The number 1 is a prime number‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ", 'True', 'False', 2, "False", "1.png"],
      
        5: ["‎ ‎ ‎ ‎ ‎ ‎ The Film 'Titanic' has won the most Oscars‎ ‎ ‎ ‎ ‎ ‎ ", 'True', 'False', 1, "True", "titanic.PNG"],
      
      }

        
        self.true_button = Button(parent, text = self.questions_answers[qnum][1], font=("Monoid", "35", "bold"), bg="#FFE3D8",height= 2, width= 6, command=lambda: [self.quizprogression(1)]) #lambda function used to connect buttons without defining
        self.true_button.place(x=50,y=310)    

        self.var1=IntVar()
        
        self.false_button = Button(parent, text = self.questions_answers[qnum][2], font=("Monoid", "35", "bold"), bg="#FFE3D8",height= 2, width= 6, command=lambda: [self.quizprogression(2)])
        self.false_button.place(x=430,y=310)   

        self.question_label=Label (parent, text = self.questions_answers[qnum][0],font=("Tw Cen MT", "18", "bold"),bg=background_color, height= 2,)
        self.question_label.place(x=40, y=40) 
    
        self.photo= PhotoImage(file = "1.png") #place holder image 
        self.image= Button(parent, image = self.photo)
        self.image.place(x=50, y=105, height=190, width=600)
        self.photo.config(file=self.questions_answers[qnum][5])#sets the correct image for the first question
      
    
  def questions_setup(self):
      selector()
      self.var1.set(0)#configs the buttons and titles to fit the new question
      self.question_label.config(text=self.questions_answers[qnum][0])
      self.true_button.config(text=self.questions_answers[qnum][1]) 
      self.false_button.config(text=self.questions_answers[qnum][2]) 
      self.photo.config(file=self.questions_answers[qnum][5],)
  
  def quizprogression(self,x):
    global score 
    if len(asked)>4: #to determine if its the last question and just end the quiz
      if x==self.questions_answers[qnum][3]: #if choice made is correct
        score+=1 #add one to score
        print("right")
        self.end() #end question section
      else: #if choice is incorrect
        score+=0
        print("wrong")
        print(choice)
        messagebox.showinfo("srry","The correct answer was " + self.questions_answers[qnum][4])
        self.end()
      
    else:
      if x==self.questions_answers[qnum][3]: #if choice made is correct
        score+=1 #add one to score 
        print("right")#testing code 
        self.questions_setup() #run method to next question
      else: #if choice is incorrect
        score+=0
        print("wrong")
        print(choice)
        messagebox.showinfo("sorry about that","The correct answer was " + self.questions_answers[qnum][4]) #message stating what the right answer is  
        self.questions_setup() #move to next question
      
  def end(self): 
      self.question_label.destroy() #destroys all question related code
      self.true_button.destroy()
      self.false_button.destroy()
      self.image.destroy()
      name=names[0]
      file=open("scorescreen.txt","a") #opens the highscores file
    
      if name == "admin_reset": 
        file=open("scorescreen.txt", "w")
      else:
        file.write(str(score))  #turns the score into a string
        file.write(" - ") #writes into the text file
      file.write(name+ "\n") #writes the name into the text file and then goes to a new line
      file.close() #closes the file
      inputFile= open("scorescreen.txt", "r") #opens the highscores file in read mode
      lineList = inputFile.readlines() #line list equals the each line in the list
      lineList.sort()
      top=[]
      top5=(lineList[-5:])
      for line in top5:
        point=line.split(" - ")
      top.append((int(point[0]), point[1]))
      file.close() 
      top.sort()
      top.reverse()
      return_string = ""
      for i in range(len(top)):
        return_string +="{} - {}\n".format(top[i][0], top[i][1])
      print(return_string) #for testing to show on the console
      open_endscrn=ScreenEnd(root)
      open_endscrn.score_display.config(text=return_string)   

class ScreenEnd:
  def __init__(self, parent):
    self.score_display = Label (parent, text="Score" , width=10, height=6, bg="#FFE3D8", font=('Tw Cen MT', 18 , 'bold'), fg="black"  )
    self.score_display.place(x=275, y=250)

    self.message = Label (parent, text="Congratulations!", bg="#FFE3D8", font=('Tw Cen MT', 35 , 'bold'), fg="black", height= 3)
    self.message.place(x=130,y=70)

    self.blue_bar2 = Label (parent, text="‎ ‎ ‎ ‎ ‎ ‎‎ ‎ ‎ ‎ ‎ ‎", bg="#0A043C", font=('Tw Cen MT', 14 , 'bold'), fg="#0A043C", width=34, padx=2)
    self.blue_bar2.place(x=130,y=70)
    
    self.quit_button = Button (parent, text="Quit" , width=10, height=4,   bg="red", font=('Tw Cen MT', 17 , 'bold'), fg="white" , command=self.destroyquiz)
    self.quit_button.place(x=50, y=275)  

    self.restart_button = Button (parent, text="Restart" , width=10, height=4,   bg="#FFE3D8", font=('Tw Cen MT', 17 , 'bold'), fg="black" , command=self.restartquiz)
    self.restart_button.place(x=480, y=275)   

  def destroyquiz(self):
    root.withdraw() #closes quiz
  
  def restartquiz(self):
    python = sys.executable
    os.execl(python, python, * sys.argv) #restarts quiz by using OS



    




if __name__ =="__main__":
    root = Tk()
    root.title("general knowledge quiz") 
    root.geometry("700x450")
    bg_image = Image.open("titlebackground.PNG") 
    bg_image = bg_image.resize((700, 450), Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(bg_image) 
        
    image_label= Label(root, image=bg_image)
    image_label.place(x=0, y=0, relwidth=1, relheight=1) 
    quiz_instance = Homescreen(root) 
    root.mainloop()



