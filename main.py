from tkinter import *

#window
window = Tk()
window.minsize(400,400)
window.title("BMI-CALCULATOR")

#label
label1 = Label(text="Please enter your weight",font=("arial",20,"normal"),bg="lightblue")
label1.pack(padx=20,pady=20)

#entry
entry1 = Entry(width=10)
entry1.pack(padx=20,pady=10)

#label
label2 = Label(text="Please enter your height",font=("arial",20,"normal"),bg="lightblue")
label2.pack(padx=20,pady=10)

#entry
entry2 = Entry(width=10)
entry2.pack(padx=20,pady=10)

#label
label3 = Label(text=":)",font=("arial",20,"normal"),bg="pink")
label3.pack(padx=20,pady=10)

def check_button():
    while True:
        try:
            w = int(entry1.get())
            h = int(entry2.get())
            bmi = w/((0.01*h)**2)
            if bmi < 18.5:
                label3.config(text=f"Your BMI : {bmi} Underweight !!",bg="light blue")
            elif bmi >= 18.5 and bmi < 24.9 :
                label3.config(text=f"Your BMI : {bmi} Normal",bg="green")
            elif bmi >= 24.9 and bmi < 29.9:
                label3.config(text=f"Your BMI : {bmi} Overweight",bg="yellow")
            elif bmi >= 29.9 and bmi < 35:
                label3.config(text=f"Your BMI : {bmi} Obese",bg="orange")
            else:
                label3.config(text=f"Your BMI : {bmi} Extremly Obese", bg="red")
            break
        except:
            label3.config(text="Please check the values")
            break


#button
button = Button(text="Calculate",bg="light green",command=check_button)
button.pack(padx=20,pady=10)
window.mainloop()