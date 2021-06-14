# IMPLE REGISTRATION FORM

#importing library
from tkinter import*
from tkinter import ttk

window=Tk()

#declaring window title
window.title("Registration Screen")
#declaring window size
window.geometry('600x600')
#declaring window colour
window.configure(background="yellow");               
#feilds declare
Firstname=Label(window,text="First Name").grid(row=0,column=0)         
Lastname=Label(window,text="Lat Name").grid(row=1,column=0)               
Email=Label(window,text="Email Id").grid(row=2,column=0)               
Mobile=Label(window,text="Contact Number").grid(row=3,column=0)                                 
Age=Label(window,text="Age").grid(row=4,column=0)         
Linkedin=Label(window,text="Linkedin Id").grid(row=5,column=0)                      
EmployeeID=Label(window,text="Employee Id").grid(row=6,column=0)               
Address=Label(window,text="Address").grid(row=7,column=0)  

Qualification=Label(window,text="Qualification").grid(row=8,column=0) 
list1=['Degree','PUC','SSLC'];   
c=StringVar()
droplist=OptionMenu(window, c,*list1) 
c.set('Select your qualification')
droplist.grid(row=8,column=1) 

Gender=Label(window,text="Gender").grid(row=9,column=0)
var=IntVar()
Radiobutton(window,text="Male",padx=20,variable=var,value=1).grid(row=9,column=1)
Radiobutton(window,text="Female",padx=20,variable=var,value=2).grid(row=9,column=2)

Firstname1=Entry(window).grid(row=0,column=1)         
Lastname1=Entry(window).grid(row=1,column=1)               
Email1=Entry(window).grid(row=2,column=1)               
Mobile1=Entry(window).grid(row=3,column=1)                                    
Age=Entry(window).grid(row=4,column=1)         
Linkedin=Entry(window).grid(row=5,column=1)                            
EmployeeID=Entry(window).grid(row=6,column=1)               
Address=Entry(window).grid(row=7,column=1)  

var1=IntVar()
Checkbutton(window,text="I accept all the terms and condition",variable=var1).grid(row=10,column=0) 
        
#function declaration
def clicked():
    res="Welcome to" + txt.get()
    lbl.configure(text=res)
btn=ttk.Button(window,text="Submit").grid(row=11,column=1)
window.mainloop()


         