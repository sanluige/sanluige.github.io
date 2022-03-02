#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 11:45:36 2022

@author: luisgerardosanchezsoto
"""
import random

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
            self.environment[self._y][self._x] += self.store
            self.store = 0
 
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
                    
   
    def distance_between(self, otheragent):
        return (((self._x - otheragent.x)**2) + ((self._y - otheragent.y)**2))**0.5
