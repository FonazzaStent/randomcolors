"""Random Colors 1.0.0 - Generate random colors.
Copyright (C) 2024  Fonazza-Stent

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>."""

import tkinter as tk
from tkinter import *
from tkinter.filedialog import asksaveasfilename
from tkinter import colorchooser
import csv
from math import sqrt
import random
from random import randint

#create main window
def create_main_window():
    global top
    global root
    img=b'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'

    root= tk.Tk()
    top= root
    top.geometry("320x300")
    top.title("Random Colors")
    top.resizable(0,0)
    favicon=tk.PhotoImage(data=img) 
    root.wm_iconphoto(True, favicon)

#ColorDisplayFrame
def color_display_frame():
    global ColorDisplayFrame
    global ColorMatchFrame
    global ColorMatchLabel
    ColorDisplayFrame= Frame(top)
    ColorDisplayFrame.place(x=20, y=20, height=220, width=280)
    ColorDisplayFrame.configure(relief='groove')
    ColorDisplayFrame.configure(borderwidth="2")
    ColorDisplayFrame.configure(relief="groove")
    ColorDisplayFrame.bind("<Button-1>",generate_color_frame)
    
    ColorMatchLabel=Text(top)
    ColorMatchLabel.place(x=20,y=250,height=25,width=280)
    ColorMatchLabel.configure(state="disabled")

#choose color
def generate_color():
    global color
    global R
    global G
    global B
    global RGBcolor

    Rm=randint(1,255)
    Gm=randint(1,255)
    Bm=randint(1,255)
    hexmatch=rgb_to_hex(Rm,Gm,Bm)
    ColorDisplayFrame.configure(bg=hexmatch)
    colorlabel="R "+str(Rm)+" G "+str(Gm)+" B "+str(Bm)+" - Hex: "+hexmatch
    ColorMatchLabel.configure(state='normal')
    ColorMatchLabel.delete(1.0,END)
    ColorMatchLabel.insert(INSERT,colorlabel)
    ColorMatchLabel.configure(state="disabled")

def generate_color_frame(event):
    generate_color()

def closest_color(rgb):
    r, g, b = rgb
    color_diffs = []
    for color in RGBlist:
        cr, cg, cb = color
        cr=int(cr)
        cg=int(cg)
        cb=int(cb)
        color_diff = sqrt((r - cr)**2 + (g - cg)**2 + (b - cb)**2)
        color_diffs.append((color_diff, color))
    return min(color_diffs)[1]

def rgb_to_hex(r,g,b):
    #return '#%02x%02x%02x' % rgb
    return "#{:02x}{:02x}{:02x}".format(r,g,b)

#convert Hex to RGB
def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

#CopyContextMenu
def create_context_menu():
    global menu
    menu = tk.Menu(root, tearoff = 0)
    menu.add_command(label="Copy", command=copy_text)
    root.bind("<Button-3>", context_menu)

def context_menu(event): 
    try: 
        menu.tk_popup(event.x_root, event.y_root)
    finally: 
        menu.grab_release()
        
def copy_text():
        ColorMatchLabel.event_generate(("<<Copy>>"))

#main
def main():
    create_main_window()
    color_display_frame()
    create_context_menu()

main()
root.mainloop()
