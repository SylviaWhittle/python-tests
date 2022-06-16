import tkinter as tk

window = tk.Tk()

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

# btn_decrease = tk.Button(master=window, text="-")
# btn_decrease.grid(row=0, column=0, sticky="nsew")

lbl_value = tk.Label(master=window, text="0")
lbl_value.grid(row=0, column=1)

# btn_increase = tk.Button(master=window, text="+")
# btn_increase.grid(row=0, column=2, sticky="nsew")

# def decrease():
#     value = int(lbl_value["text"])
#     lbl_value["text"] = f"{value - 1}"

# Function to increase the value 
# def increase():
#     value = int(lbl_value["text"])
#     lbl_value["text"] = f"{value + 1}"

# Button to decrease the value. Calls the decrease function
# btn_decrease = tk.Button(master=window, text="-", command=decrease)
# Sets grid layout
# btn_decrease.grid(row=0, column=0, sticky="nsew")

# Label to store the value
lbl_value = tk.Label(master=window, text="0")
# lbl_value.grid(row=0, column=1)

# Button to increase the value 
# btn_increase = tk.Button(master=window, text="+", command=increase)
# btn_increase.grid(row=0, column=2, sticky="nsew")



window.mainloop()