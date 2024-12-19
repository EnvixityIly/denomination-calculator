import tkinter as tk
import re

def check_password_strength():
    password = password_entry.get()
    length_min = len(password)>=8
    digit_min = bool(re.search(r"\d",password))
    uppercase_min = bool(re.search(r"[A-Z]}",password))
    lowercase_min = bool(re.search(r"[a-z]",password))
    symbol_min = bool(re.search(r"[@#$%&[();:.,/\~_^|+=!?<>*]]",password))
    min_met = sum([length_min,digit_min,uppercase_min,lowercase_min,symbol_min])
    if min_met <= 2:
        strength = "weak"
    elif min_met == 3 or min_met == 4:
        strength = "Medium"
    elif min_met == 5:
        strength = "Strong"
    
    result_label.config(text=f"Paaword Strenght: {strength}")

root = tk.Tk()
root.title("Password strength checker")
root.geometry("300x300")

password_label = tk.Label(root,text = "Enter Password")
password_label.pack(pady=10)

password_entry = tk.Entry(root)
password_entry.pack(pady= 5)

check_button = tk.Button(root, text = "Check strength", command = check_password_strength)
check_button.pack(pady=10)

result_label = tk.Label(root,text = "")
result_label.pack(pady=10)

root.mainloop()