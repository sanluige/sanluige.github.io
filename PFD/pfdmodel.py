#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 09:00:39 2022

@author: luisgerardosanchezsoto

This is the main script to be run to start the Planning for Drunks model, as the second assignment for the
module GEOG5990M Programming for Geographical Information Analysis: Core Skills.

The program models the behaviour of 25 drunks heading home from the pub after drinking, with varied levels of drunkness.
    - The program reads a file to create the town of map, including the pub and 25 houses
    - The drunks are created and assigned a house number and a drunk level between 1 and 4 (1: least drunk, 4: very drunk)
    - One by one, the drunks head home, with the randomness of their steps dependent to their drunk level
    - At each step, the drunk evaluates their position to determine their status (At bar, Walking, or At home) and stops when reaching home
    - All drunks start their journey home from a point within the pub

The program uses a TKinter GUI to display the results of the simulation:
    - a town map with the routes taken by all drunks
    - a step density map
    - overwrites a text file with the step density information

"""

import csv
import drunksframework
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
#import matplotlib.animation
import numpy as np
import tkinter
import sys   

"""
·····································································
··························· MODEL METHODS ···························
·····································································
"""

# print drunks information
def print_info():
    print("\n Drunks information:")
    for i in range(len(drunks)):
        print(drunks[i])

# run method to be called by animation
def run():
    
    fig.clear()
    
    # graph town
    matplotlib.pyplot.ylim(ylenght, 0)
    matplotlib.pyplot.xlim(0, xlenght)
    matplotlib.pyplot.imshow(town)
    
    # each step and evaluate if position is in home (search list of tuples)
    n = 0
    for i in range(len(drunks)):
        while drunks[i].status != 2 and n < 300:
            drunks[i].move()
            drunks[i].evalposition()
            n = i+1
        print("Drunk " + str(n) + " arrived home.")
        y, x = np.array(drunks[i].steps).T
        matplotlib.pyplot.scatter(x, y)
        matplotlib.pyplot.show()
    
    canvas.draw()

# draw step density map    
def draw_density():
    
    print("Draw step density process started")
    
    # create density map as list of lists
    global dmap
    for i in range(ylenght):
        row = []
        for j in range(xlenght):
            row.append(0.0)
        dmap.append(row)
    
    # list of steps of drunks
    allsteps = []
    for i in range(len(drunks)):
        allsteps.append(drunks[i].steps)
    
    # draw steps in density map
    for d in range(len(drunks)):
        for i in range(ylenght):
            for j in range(xlenght):
                if [i, j] in allsteps[d]:
                    dmap[i][j] +=1
    
    print("Draw step density process completed")
    
    # show density map in model window figure
    fig.clear()
    matplotlib.pyplot.imshow(dmap)
    matplotlib.pyplot.ylim(ylenght, 0)
    matplotlib.pyplot.xlim(0, xlenght)

    canvas.draw()
    
    # write step density map in existig csv file  
    f2 = open('step_dmap.csv', 'w', newline='')
    writer = csv.writer(f2)
    for rowlist in dmap:
        writer.writerow(rowlist) # List of values.
    f2.close() 
 
# quit model execution
def quit_model():
    print("Thank you for using this model")
    root.destroy()
    matplotlib.pyplot.close()
    sys.exit()


"""
·····································································
···························· MODEL SETUP ····························
·····································································
"""

# read in.txt and create town as list of lists
town = []
dmap = []    
f = open('town.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader: 
    rowlist = []
    for value in row:
        rowlist.append(value)
    town.append(rowlist)
f.close()
ylenght = len(town)
xlenght = len(town[0])

# create addressbook as a dictionary - keys are house numbers, list of (x,y) pairs
addressbook = {}
for i in range(25):
    a = []
    for x in range(xlenght):
        for y in range(ylenght):
            if town[x][y] == (i+1)*10:
                a.append([x, y])
    addressbook.setdefault((i+1)*10, []).append(a)

# create bar address - list of bar x,y pairs
baraddress = []
for x in range(xlenght):
    for y in range(ylenght):
        if town[y][x] == 1:
            baraddress.append([y, x])

# initialise drunks and store in a list within baraddress and assign housenumber
drunks = []
aux_book = dict(addressbook)
for i in range(len(addressbook)):
    adrunk = drunksframework.Drunk(town, baraddress, aux_book)
    drunks.append(adrunk)
    del aux_book[adrunk.housenumber]

# draw output figure windows
fig = matplotlib.pyplot.figure(1, figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# set up model window (GUI)
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Print drunk information", command=print_info)
model_menu.add_command(label="Run simulation", command=run)
model_menu.add_command(label="Draw step density map and export CSV file", command=draw_density)
model_menu.add_command(label="Quit model", command=quit_model)

tkinter.mainloop()