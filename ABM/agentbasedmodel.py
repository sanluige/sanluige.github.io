#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 20:33:40 2022

@author: luisgerardosanchezsoto

Basic ABM Model:
    This model emulates basic behaviour of grazers and predators in an 
    environment. Grazers move in and eat from the environment and share grazed 
    resources with other neighbouring grazers. Predators move in a circuit and 
    hunt nearby grazers with probability to fail.
    The model:   
    - builds agents (grazers and predtors) in a space;
    - gets them to interact with each other;
    - reads in environmental data;
    - gets agents to interact with the environment;
    - randomizes the order of agent actions;
    - displays the model as an animation;
    - is contained within a GUI;
    - is initialised with data from the web.

"""
# imports
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot
import matplotlib.animation 
import csv
import agentframework
import tkinter
import requests
import bs4
import sys

"""
·····································································
······················ MODEL METHODS/FUNCTIONS ······················
·····································································
"""

# update agent actions by frame_number
def update(frame_number):
    
    fig.clear()
    global carry_on
    global num_of_grazers
    global num_of_predators
    print("Iteration " + str(frame_number))
    
    for i in range(num_of_predators):
        if predators[i].energy > 0:
            predators[i].energy -= 1
    
    for i in range(num_of_grazers):
        grazers[i].move()
        grazers[i].eat()
        grazers[i].share_with_neighbours(neighbourhood)
    
    for i in range(num_of_predators):
        predators[i].move()
        if predators[i].energy < 2:
            predators[i].eat(pred_neighbourhood)
    
    num_of_grazers = len(grazers)
    
    # stopping condition: Limit overall grazing of environment
    s = 0
    
    for i in range(num_of_grazers):
       s = s + grazers[i].store
       
    if s - 1 > num_of_grazers*200:
        carry_on = False
        print("Stopping condition: Maximun environment grazing achieved")
    
    for i in range(num_of_grazers):
        matplotlib.pyplot.scatter(grazers[i].x,grazers[i].y, c = "#eeeeee")
    for i in range(num_of_predators):
        matplotlib.pyplot.scatter(predators[i].x,predators[i].y, c = "#000000")
    matplotlib.pyplot.ylim(ylenght, 0)
    matplotlib.pyplot.xlim(0, xlenght)
    matplotlib.pyplot.imshow(environment)

# stopping process logic
def gen_function(b = [0]):
    a = 0
    global carry_on # not actually needed as we're not assigning, but clearer
    while (a < num_of_iterations) & (carry_on) :
        yield a	# returns control and waits next call.
        a = a + 1

# run method to be called by animation
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()

# print agent information in console
def print_info():
    print("\n Grazer information:")
    for i in range(num_of_grazers):
        print(grazers[i])
    print("\n Predator information:")
    for i in range(num_of_predators):
        print(predators[i])

# write environment in existing csv file        
def file_env():
    f2 = open('environmentout.csv', 'w', newline='')
    writer = csv.writer(f2)
    for rowlist in environment:
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

# script for user to set parameters at the start of execution, 
# limiting user inputs to Integers
print("\n Please enter the following parameters: \n")
while True:
    try:
        num_of_grazers = int(input("Enter number of grazers in model: "))
    except ValueError:
        print("Cannot parse this input. Please enter a integer.")
        # incorrect input. Return to the start of the loop
        continue
    else:
        # input was successfully parsed. Exit while loop.
        break

while True:
    try:
        num_of_predators = int(input("Enter number of predators in model: "))
    except ValueError:
        print("Cannot parse this input. Please enter an integer.")
        # incorrect input. Return to the start of the loop
        continue
    else:
        # input was successfully parsed. Exit while loop.
        break

while True:
    try:
        num_of_iterations = int(input("Enter number of iterations: "))
    except ValueError:
        print("Cannot parse this input. Please enter an integer.")
        #Incorrect input. Return to the start of the loop
        continue
    else:
        #input was successfully parsed. Exit while loop.
        break

while True:
    try:
        neighbourhood = int(input("Enter grazer neighbourhood radius: "))
    except ValueError:
        print("Cannot parse this input. Please enter an integer.")
        # incorrect input. Return to the start of the loop
        continue
    else:
        # input was successfully parsed. Exit while loop.
        break

while True:
    try:
        pred_neighbourhood = int(input("Enter predator neighbourhood radius: "))
    except ValueError:
        print("Cannot parse this input. Please enter an integer.")
        # incorrect input. Return to the start of the loop
        continue
    else:
        # input was successfully parsed. Exit while loop.
        break
print("\n Parameters have been updated")

# define and set variables with default values (NOW DEFINED BY USER)
#num_of_grazers = 10
#num_of_predators = 3
#num_of_iterations = 150
#neighbourhood = 5
#pred_neighbourhood = 10
        
grazers = [] # list of grazers
predators = [] # list of predators
environment = [] # list to store environment as map (list of lists)

carry_on = True # used for update(frame_number) method

# read and store coordinates from website
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})

# read in.txt and create environmentas as list of lists
f = open('in.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader: 
    rowlist = []
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
f.close()
ylenght = len(environment)
xlenght = len(environment[0])

# create grazers and append to agents list
for i in range(num_of_grazers):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    grazers.append(agentframework.Grazer(environment, grazers, y, x))

# create predators and append to agents list
for i in range(num_of_predators):
    predators.append(agentframework.Predator(environment, grazers))

# create figure for plot in simulation
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# set up model window  
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# set up window menu
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)
model_menu.add_command(label="Print agent information", command=print_info)
model_menu.add_command(label="Print environment file", command=file_env)
model_menu.add_command(label="Quit model", command=quit_model)

tkinter.mainloop() # wait for interactions.  




