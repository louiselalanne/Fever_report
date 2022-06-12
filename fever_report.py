from msilib.schema import RadioButton
from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Fever Report")
root.geometry("600x600")

q1_radioValue = StringVar(value="0")
q1 = Label(root, text="Do you have headache and sore throat?")
q1.pack()
q1_radio1 = Radiobutton(root, text="yes", variable=q1_radioValue, value="yes")
q1_radio1.pack()
q1_radio2 = Radiobutton(root, text="no", variable=q1_radioValue, value="no")
q1_radio2.pack()

q2_radioValue = StringVar(value="0")
q2 = Label(root, text="Is your body temperature hight?")
q2.pack()
q2_radio1 = Radiobutton(root, text="yes", variable=q2_radioValue, value="yes")
q2_radio1.pack()
q2_radio2 = Radiobutton(root, text="no", variable=q2_radioValue, value="no")
q2_radio2.pack()

q3_radioValue = StringVar(value="0")
q3 = Label(root, text="Are there any symptoms of eye redness?")
q3.pack()
q3_radio1 = Radiobutton(root, text="yes", variable=q3_radioValue, value="yes")
q3_radio1.pack()
q3_radio2 = Radiobutton(root, text="no", variable=q3_radioValue, value="no")
q3_radio2.pack()

def fever_score():
    score=0
    if q1_radioValue.get() == "yes":
        score = score + 20
    if q2_radioValue.get() == "yes":
        score = score + 20
    if q3_radioValue.get() == "yes":
        score = score + 20

    if score <= 20:
        messagebox.showinfo("Report", "You don't need to visit a doctor.")
    elif score > 20 and score <= 40:
        messagebox.showinfo("Report", "You might perhaps have to visit a doctor.")
    else:
        messagebox.showwarning("Report", "I strongly advise you to visit a doctor")

btn = Button(root, text="Click Me", command=fever_score)
btn.pack()

root.mainloop()