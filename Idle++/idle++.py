import threading
import time
import os
import tkinter as tk

# Colours 
global col_bg 
col_bg = '#222e2c'
col_text = '#dddddd'

# def clear_console():
#     os.system('clear -x')

# class Clicker():

#     def __init__(self):
#         print('initialising clicker')

#     def click(self):
#         global gp
#         gp += 1

# def get_input():
#     inp = input('>_ ')
#     return inp

# def parse_input(inp):
#     if inp == '':
#         clicker.click()

# def adding_loop():
#     global gp
#     global gplabel

#     # Game loop

#     while True:
#         gp += 1

#         gplabel['text'] = f'gp: {gp}'

#         time.sleep(1)


# def handle_keypress(event):
#     print(event.char)


# if __name__ == '__main__':
#     global gp
#     global clicker
#     global gplabel

#     gp = 0

    

#     # clicker = Clicker()

#     # game_loop_thread = threading.Thread(target=game_loop, args=())
#     # game_loop_thread.start()

#     window = tk.Tk()
#     window.geometry('400x400')
#     window.configure(bg=col_bg)
#     window.title('idle++')
#     window.resizable(width=False, height=False)
#     window.rowconfigure(0, minsize=50, weight=1)
#     window.columnconfigure([0, 1, 2], minsize=50, weight=1)

#     canvas = tk.Canvas(window, width=400, height=400)
#     canvas.create_rectangle(10, 10, 20, 20, '#00ffff')

#     gplabel = tk.Label(
#         master=window,
#         fg=col_text,
#         bg=col_bg,
#         text=f'gp: {gp}'
#     )
#     gplabel.grid(row=0, column=1)

#     adding = threading.Thread(target=adding_loop, args=())
#     adding.start()

#     window.mainloop()



