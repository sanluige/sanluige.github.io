#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CHANGE TO TEST GITHUB COMMIT
Created on Thu Feb 17 20:33:40 2022

@author: luisgerardosanchezsoto

Basic ABM Model:
    This model emulates grazing behaviour of agents in an environment. 
    Agents move in and eat from the environment and share grazed resources with other neighbouring agents.
    The model:   
    - builds agents in a space;
    - gets them to interact with each other;
    - reads in environmental data;
    - gets agents to interact with the environment;
    - randomizes the order of agent actions;
    - displays the model as an animation;
    - is contained within a GUI;
    - is initialised with data from the web.

"""
#Imports
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot
import matplotlib.animation 
import csv
import agentframework
import tkinter
import requests
import bs4

#Define and set variables with default values
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20

#Allow user to change parameters
def set_parameters():
    global num_of_agents
    global num_of_iterations
    global neighbourhood

    num_of_agents = int(input("Enter number of agents in model: "))
    num_of_iterations = int(input("Enter number of iterations: "))
    neighbourhood = int(input("Enter neighbourhood radius: "))
    
agents = []
environment = []

#read and store coordinates from website
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})

#Read in.txt and create environmentas as list of lists
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

#Create agents and append to agents list
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents, y, x))

#update agent actions by frame_number
carry_on = True	
def update(frame_number):
    
    fig.clear()  
    global carry_on
    print("Iteration " + str(frame_number))
    
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
    
    #Stopping condition: Limit overall grazing of environment
    s = 0
    
    for i in range(num_of_agents):
       s = s + agents[i].store
       
    if s > num_of_agents*100:
        carry_on = False
        print("Stopping condition: Maximun environment grazing achieved")
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
    matplotlib.pyplot.ylim(ylenght, 0)
    matplotlib.pyplot.xlim(0, xlenght)
    matplotlib.pyplot.imshow(environment)

#Stopping process logic
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < num_of_iterations) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

#Run method to be called by animation
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()

def print_info():
    print("\n Agent information:")
    for i in range(num_of_agents):
        print(agents[i])

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#Set up model window  
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Change model parameters", command=set_parameters)
model_menu.add_command(label="Run model", command=run)
model_menu.add_command(label="Print agent information", command=print_info)

tkinter.mainloop() # Wait for interactions.  




