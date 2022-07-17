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
        self.continue_button = Button(parent, text="Start", font=("Monoid", "35", "bold"), bg="#FFE3D8",height= 2, width= 6, command=self.name_collection)
        self.continue_button.place(x=240,y=310)       
       


    def name_collection(self):
    
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
        


        self.questions_answers = {
        1:  ["‎ ‎ ‎ ‎ ‎ ‎ The thumb has the fastest growing nail.‎ ‎ ‎ ‎ ‎ ‎ ", 
               'True', 'False', 2, "False", "thumb.PNG"], 
      
        2: ["There are 193 countries recognised by the UN", 'True', 
               'False', 1, "True", "UN.png"], 
      
        3: ["Jeff Bezos is the richest person in the world.‎ ‎ ‎ ‎ ‎ ‎", 'True', 'False', 2, "False", "jeffbezos.png"],
      
        4: ["‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ The number 1 is a prime number‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ", 'True', 'False', 2, "False", "1.png"],
      
        5: ["‎ ‎ ‎ ‎ ‎ ‎ The Film 'Titanic' has won the most Oscars‎ ‎ ‎ ‎ ‎ ‎ ", 'True', 'False', 1, "True", "titanic.PNG"],
      
      }

        
        self.True_button = Button(parent, text = self.questions_answers[qnum][1], font=("Monoid", "35", "bold"), bg="#FFE3D8",height= 2, width= 6, command=lambda: [self.quizprogression(1)])
        self.True_button.place(x=50,y=310)    

        self.var1=IntVar()
        
        self.False_button = Button(parent, text = self.questions_answers[qnum][2], font=("Monoid", "35", "bold"), bg="#FFE3D8",height= 2, width= 6, command=lambda: [self.quizprogression(2)])
        self.False_button.place(x=430,y=310)   

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
      self.True_button.config(text=self.questions_answers[qnum][1]) 
      self.False_button.config(text=self.questions_answers[qnum][2]) 
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
        score+=1
        print("right")#add one to score
        self.questions_setup() #run method to next question
      else: #if choice is incorrect
        score+=0
        print("wrong")
        print(choice)
        messagebox.showinfo("sorry about that","The correct answer was " + self.questions_answers[qnum][4])
        self.questions_setup() #move to next question
      
  def end(self): 
      self.question_label.destroy()
      self.True_button.destroy()
      self.False_button.destroy()
      self.image.destroy()






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