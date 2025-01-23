from tkinter import *

window = Tk()

window.title("Miles to Kilometers Converter")
window.minsize(width=400,height=200)
window.config(padx=100,pady=50)

def value_in_miles():
    miles = entry.get()
    return miles

def miles_to_km(miles):
    km = float(miles) * 1.60934
    return round(km,2)

def button_click_action():
    label3.config(text=f"{miles_to_km(value_in_miles())}")

label1 = Label(text="is equal to",font=("Arial",16))
label1.grid(column=0,row=1)
label1.config(pady=5,padx=5)

label2 = Label(text="miles",font=("Arial",16))
label2.grid(column=2,row=0)
label2.config(pady=5,padx=5)

entry = Entry(width=4,font=("Arial",16))
entry.grid(column=1,row=0)

label3 = Label(text="0",font=("Arial",16))
label3.grid(column=1,row=1)
label3.config(pady=5,padx=5)

label4 = Label(text="km",font=("Arial",16))
label4.grid(column=2,row=1)
label4.config(pady=5,padx=5)

button = Button(text="Convert",font=("Arial",16),command=button_click_action)
button.grid(column=1,row=3)

window.mainloop()