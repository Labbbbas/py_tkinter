from tkinter import *
import pygame

root = Tk()
root.geometry('500x400')

pygame.mixer.init()

def play():
    pygame.mixer.music.load('/Users/iMac27Wow/Downloads/escobar.wav')
    # /Users/iMac27Wow/Documents/tkinter_py/music/biza.mp3
    pygame.mixer.music.play(loops=0)

def stop():
    pygame.mixer.music.stop()

my_button = Button(root, text='Play Song', font=('Helvetica', 32), fg='#0000FF', command=play)
my_button.pack(pady=20)

stop_button = Button(root, text='Stop', font=('Helvetica', 32), fg='#FF0000', command=stop)
stop_button.pack(pady=20)

root.mainloop()