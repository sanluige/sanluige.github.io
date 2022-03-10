#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 12:19:58 2022

@author: luisgerardosanchezsoto
"""
import random

#definition of superclass "Agent"
class Agent():
    def __init__(self, environment, agents, x = None, y = None):
        if (x == None):
            self._x = random.randint(0, len(environment[0]))
        else:
            self._x = x
        if (y == None):
            self._y = random.randint(0, len(environment))
        else:
            self._y = y
        self.environment = environment
        self.agents = agents
        self.store = 0
        self.energy = 0

    #protect x
    def getx(self):
        return self._x
    def setx(self, value):
        return self._x + value
    def delx(self):
        del self._x
    x = property(getx, setx, delx, "I'm the 'x' property.")

    #protect y
    def gety(self):
        return self._y
    def sety(self, value):
        return self._y + value
    def dely(self):
        del self._y
    y = property(gety, sety, dely, "I'm the 'y' property.")
    
    
    def __str__(self):
        """
        Overwrites Agent print() function to show values in x, y and store variables

        Returns
        -------
        TYPE
            Displays values in x, y and store variables.

        """
        return "x = " + str(self._x) + ", y = " + str(self._y) + ", store = " + str(self.store)
    
    def move(self):
        """
        Moves Agent by altering x and y using move_coordinate

        Returns
        -------
        None.

        """
        self._x = self.move_coordinate(self._x)
        self._y = self.move_coordinate(self._y)
    
    def distance_between(self, otheragent):
        return (((self._x - otheragent.x)**2) + ((self._y - otheragent.y)**2))**0.5
    
#definition of subclass "Grazer"
#Inherits from Agent
class Grazer(Agent):
    def eat(self): # can you make it eat what is left?
        """
        Evaluates value of coordinate point in environment and substracts 10 if available, or substracts to reach zero if value in environment is less than 10
        If store surpasses value of 100, store is dumped on environment

        Returns
        -------
        None.

        """
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10
        else:
            self.environment[self._y][self._x] = 0
            self.store += self.environment[self._y][self._x]
        if self.store > 150:
            self.environment[self._y][self._x] += self.store / 2
            self.store = self.store / 2
 
    def move_coordinate(self, xory):
        """
        Randomly increases or decreases parameter xory by 1 in a torus plane of dimensions defined by lenght of agent.environment

        Parameters
        ----------
        xor : number
            Parameter indicating an x or y value of a coordinate.

        Returns
        -------
        xor : number
            Parameter after processing.

        """
        if random.random() < 0.5:
            xory = (xory + 1) % len(self.environment)
        else:
            xory = (xory - 1) % len(self.environment)
        return xory

    def share_with_neighbours(self, neighbourhood):
        """
        Method to share store with neighbouring agents. Evaluates distance between self and otheragent and shares store equally between them if within neighbourhood.

        Parameters
        ----------
        neighbourhood : Integer
            Parameter indicating radius of neighbourhood

        Returns
        -------
        None.

        """
        for otheragent in self.agents:
            if otheragent is not self:
                distance = self.distance_between(otheragent)
                if distance <= neighbourhood:
                    average = (self.store + otheragent.store)/2
                    self.store = average
                    otheragent.store = average
                    print("sharing " + str(distance) + " " + str(average))

#definition of subclass "Predator"
#Inherits from "Agent"
class Predator(Agent): 
    
    def __str__(self):
        """
        Overwrites Predator print() function to show values in x, y and store variables

        Returns
        -------
        TYPE
            Displays values in x, y and store variables.

        """
        return "x = " + str(self._x) + ", y = " + str(self._y) + ", store = " + str(self.store) + ", energy level = " + str(self.energy)
    
    def eat(self, neighbourhood):
        """
        Method by which Predator attempts to eat agents within neighbourhood. 
        Evaluates distance between self and agent and attempts to eat with a 20% probability of success.
        Limited to eat one grazer per iteration.

        Parameters
        ----------
        neighbourhood : Integer
            Parameter indicating radius of neighbourhood

        Returns
        -------
        None.

        """
        
        ate_once = False
        
        for agent in self.agents:
            distance = self.distance_between(agent)
            if distance <= neighbourhood and  ate_once == False:
                if random.randint(0, 1) < 0.2:
                    self.store += 1
                    self.energy += 10 
                    print("Grazer " + str(agent) + " at distance " + str(distance) + " units of distance from predator has been eaten")
                    self.agents.remove(agent)
                    ate_once = True

    def move_coordinate(self, xory):
        """
        Randomly increases or decreases parameter xory by 1 in a torus plane of dimensions defined by lenght of agent.environment. 
        Disproportionate movement forward (decreasing x or y 90% of the time) emulates predator circuit in the plane.

        Parameters
        ----------
        xor : number
            Parameter indicating an x or y value of a coordinate.

        Returns
        -------
        xor : number
            Parameter after processing.

        """
        if random.random() < 0.1:
            xory = (xory + 1) % len(self.environment)
        else:
            xory = (xory - 3) % len(self.environment)
        return xory
