from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("BMI Calculator")
root.geometry("1000x1000")
root.resizable(0,0)

def calculate_bmi():
    w=weight.get()
    h=height.get()
    bmi=(w/((h*h)/10000))
   
    bmi_index(bmi)
def bmi_index(bmi):
    if bmi<18.5:
         messagebox.showinfo("output","bmi is:%.2f -is underweight -take vitamin D eficiency food"%bmi)
    elif (bmi>18.5) and (bmi<24.9):
         messagebox.showinfo("output","bmi is:%.2f -is normal "%bmi)
    elif (bmi>25) and (bmi<29.9):
         messagebox.showinfo("output","bmi is:%.2f -is overweight -avoid salty,fat or junk food"%bmi)
    elif (bmi>30) and (bmi<35):
         messagebox.showinfo("output","bmi is:%.2f -is obese - choose healthier dfood such as fruits ,vegetables"%bmi)
    else:
        messagebox.showinfo("output","bmi is:%.2f- is morbid obesity -take healthy food,avoid junk food"%bmi)
        
var=IntVar()
age=IntVar()
weight=IntVar()
height=IntVar()
l=Label(root,text="Body Mass Index Calculator \n (International System)",font="arial 20",bg="pink",fg="black").place(x=150,y=50)

l1=Label(root,text="Age(10-100)   :",font="arial 15",).place(x=50,y=150)
l1_entry=Entry(root,font="arial 15",width=15,bd=5,textvariable=age).place(x=250,y=150)

l2=Label(root,text="Weight(kgs)    :",font="arial 15",).place(x=50,y=250)
l2_entry=Entry(root,font="arial 15",width=15,bd=5,textvariable=weight).place(x=250,y=250)

l3=Label(root,text="Height(cm)     :",font="arial 15").place(x=50,y=350)
l3_entry=Entry(root,font="arial 15",width=15,bd=5,textvariable=height).place(x=250,y=350)

b=Button(root,text="compute",font="arial 15",bg="green",fg="white",command=calculate_bmi).place(x=250,y=500)

root.mainloop()
