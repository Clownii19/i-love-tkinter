from tkinter import *
from PIL import Image, ImageTk
import random 
from tkinter import messagebox
names = []
global questions_answers
asked = []
score=0

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
        background_color="white"
        
        self.question_label=questions(self.quiz_frame, text = questions_answers[1][0], font=("Tw Cen MT", "18", "bold"),bg=background_color)
        self.question_label.place() 
  

        questions_answers = {
        1:  ["The thumb has the fastest growing nail.", 
               'True', 'False', 2], 
      
        2: ["There are 193 countries recognised by the UN", 'True', 
               'False', 1], 
      
        3: ["Jeff Bezos is the richest person in the world.", 'true', 'false', 2],
      
        4: ["The number 1 a prime number", 'True', 'False', 2],
      
        5: ["The Film 'Titanic' has won the most Oscars", 'True', 'False', 1],
      
      }

        
        self.True_button = Button(parent, text="true", font=("Monoid", "35", "bold"), bg="#FFE3D8",height= 2, width= 6,)
        self.True_button.place(x=50,y=310)    
        
        self.False_button = Button(parent, text="False", font=("Monoid", "35", "bold"), bg="#FFE3D8",height= 2, width= 6,)
        self.False_button.place(x=430,y=310)   








  




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