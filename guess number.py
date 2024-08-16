import tkinter as tk 
import random

computer_number = random.randint(1,100)
print(computer_number)

root = tk.Tk()
root.title("Guess number")
root.geometry("300x300")

guess_number = None # Переменная для чисел, которые мы будем вводить 


def check_number():
    global computer_number
    global guess_number
    global entry
    guess_number = entry.get() 
    try: 
        guess_number = int(guess_number)
        if guess_number < computer_number:
            help.set(f"Computer number is bigger than {guess_number}.")
        elif guess_number > computer_number:
            help.set(f"Computer number is less than {guess_number}.")
        else:
            button.pack_forget()
            entry.pack_forget()
            label_help.config(font=("Arial",30))
            help.set(f"You win!")


    except ValueError:
        help.set(f"{guess_number} is not a number >:(.")
    entry.delete(0,tk.END)



help = tk.StringVar() 
label_help = tk.Label(root, textvariable= help)
label_help.pack()
entry = tk.Entry()
entry.pack()
button = tk.Button(root,text="Guess", command=check_number) # Кнопка ввода номера
button.pack()

root.mainloop()