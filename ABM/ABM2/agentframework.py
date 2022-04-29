#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 8 12:19:58 2022

@author: luisgerardosanchezsoto

This script defines the Agent class and subclasses Grazer and Predator used in 
the Agent Based Model (pfdmodel.py) and their functionality. Shared 
functionality of subclasses is defined in Agent Class.

"""
import random

# definition of superclass "Agent"
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

    # protect x
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
        return self._x
    def delx(self):
        del self._x
    x = property(getx, setx, delx, "I'm the 'x' property.")

    # protect y
    def gety(self):
        return self._y
    def sety(self, value):
        self._y = value
        return self._y
    def dely(self):
        del self._y
    y = property(gety, sety, dely, "I'm the 'y' property.")
    
    
    def __str__(self):
        """
        Overwrites Agent print() function to show values in x, y and store variables

        Returns
        -------
        STRING
            Displays values in x, y and store variables.
        
        DOCTESTS
        -------
        
        The following set of instructions tests that __str__ returns the expected string through print().        
        
        >>> a = Agent("Env", "Agents", 10, 20)
        >>> print(a)
        x = 10, y = 20, store = 0
        >>> a.store = 5
        >>> print(a)
        x = 10, y = 20, store = 5

        """
        return "x = " + str(self._x) + ", y = " + str(self._y) + ", store = " + str(self.store)
    
    def move(self):
        """
        Moves Agent by altering x and y using move_coordinate

        Returns
        -------
        None.
        
        DOCTESTS
        -------
        
        The following set of instructions tests the functionality of move() for Grazer and Predator subclasses. It tests that x and y values change after move() and that they remain of type integer.
        
        >>> import random
        >>> Env = [[100.0, 100.0, 100.0, 100.0, 100.0, 100.0], [100.0, 100.0, 100.0, 100.0, 100.0, 100.0], [100.0, 100.0, 100.0, 100.0, 100.0, 100.0], [100.0, 100.0, 100.0, 100.0, 100.0, 100.0], [100.0, 100.0, 100.0, 100.0, 100.0, 100.0], [100.0, 100.0, 100.0, 100.0, 100.0, 100.0]]
        >>> a = Grazer(Env, "Agents", 0, 4)
        >>> x = a.getx()
        >>> x
        0
        >>> y = a.gety()
        >>> y
        4
        >>> a.move()
        >>> type(a.getx())
        <class 'int'>
        >>> a.getx() != x
        True
        >>> type(a.gety())
        <class 'int'>
        >>> a.gety() != y
        True
        
        
        >>> b = Predator(Env, "Agents", 2, 2)
        >>> x = b.getx()
        >>> x
        2
        >>> y = b.gety()
        >>> y
        2
        >>> b.move()
        >>> type(b.getx())
        <class 'int'>
        >>> b.getx() != x
        True
        >>> type(b.gety())
        <class 'int'>
        >>> b.gety() != y
        True

        """
        self._x = self.move_coordinate(self._x)
        self._y = self.move_coordinate(self._y)
    
    def distance_between(self, otheragent):
        """
        Calculate euclidean distance between to agents in space, using their position in coordinates

        Parameters
        ----------
        otheragent : Agent
            Object of type Agent.

        Returns
        -------
        DOUBLE
            Number indicating distance between agent positions.
            
        DOCTESTS
        -------
        
        The following set of instructions tests that distance_between(otheragent) correctly calculates the distance between two agents.
        
        >>> a = Agent("Env", "Agents", 10, 20)
        >>> b = Agent("Env", "Agents", 10, 20)
        >>> a.distance_between(b)
        0.0
        >>> b._x = 30
        >>> a.distance_between(b)
        20.0
        >>> b = Agent("Env", "Agents", 50, 30)
        >>> a.distance_between(b)
        41.23105625617661
        
        """
        return (((self._x - otheragent.x)**2) + ((self._y - otheragent.y)**2))**0.5
    
# definition of subclass "Grazer". Inherits from Agent.
class Grazer(Agent):
    def eat(self): # can you make it eat what is left?
        """
        Evaluates value of coordinate point in environment and substracts 10 if available, or substracts to reach zero if value in environment is less than 10
        If store surpasses value of 150, half of store is dumped on position in environment.

        Returns
        -------
        None.
        
        DOCTESTS
        -------
        
        The following set of instructions tests that eat() works correctly by:
            - creating a Grazer agent
            - evaluating its initial store
            - checking that eat() increases Grazer's store variable
            - the amount eaten by Grazer is substracted from Environment (Env)
            - they sick up half of their store if they pass a store value of 150
        
        >>> import random
        >>> Env = [[100.0, 100.0, 100.0, 100.0, 100.0, 100.0], [100.0, 100.0, 100.0, 100.0, 100.0, 100.0], [100.0, 100.0, 100.0, 100.0, 100.0, 100.0], [100.0, 100.0, 100.0, 100.0, 100.0, 100.0], [100.0, 100.0, 100.0, 100.0, 100.0, 100.0], [100.0, 100.0, 100.0, 100.0, 100.0, 100.0]]
        >>> Agents = []
        >>> a = Grazer(Env, Agents, 0, 4)
        >>> Agents.append(a)
        >>> a.store
        0
        >>> a.eat()
        >>> float(a.store)
        10.0
        >>> Env[a.gety()][a.getx()]
        90.0
        >>> a.eat(); a.eat(); a.eat(); a.eat(); a.eat(); a.eat(); a.eat();
        >>> float(a.store)
        80.0
        >>> a.move()
        >>> a.eat(); a.eat(); a.eat(); a.eat(); a.eat(); a.eat(); a.eat(); a.eat()
        >>> float(a.store) 
        80.0
        
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
        
        DOCTESTS
        -------
        
        The following set of instructions tests that move_coordinate() works correctly by:
            - creating an grazer
            - moving the x value of the agent
            - checking that new value increased or decreased by 1
        
        >>> import random
        >>> Env = [[100.0, 100.0, 100.0, 100.0, 100.0, 100.0], [100.0, 100.0, 100.0, 100.0, 100.0, 100.0], [100.0, 100.0, 100.0, 100.0, 100.0, 100.0], [100.0, 100.0, 100.0, 100.0, 100.0, 100.0], [100.0, 100.0, 100.0, 100.0, 100.0, 100.0], [100.0, 100.0, 100.0, 100.0, 100.0, 100.0]]
        >>> Agents = []
        >>> a = Grazer(Env, Agents, 0, 0)
        >>> Agents.append(a)
        >>> a.getx()
        0
        >>> n = a.move_coordinate(a._x)
        >>> (n == 1 or n == 5)
        True
        
        
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
        
        DOCTESTS
        -------
        
        The following set of instructions tests that share_with_neighbour(neighbourhood) works correctly by:
            - creating two grazers
            - checking that share_with_neighbour(neighbourhood) does nothing if no other agent within neighbourhood argument
            - making grazer eat and move so that other agent is within neighbourhood
            - check that agents share their stores to each keep the same amount.
        
        >>> import random
        >>> Env = [[100.0, 100.0, 100.0, 100.0, 100.0, 100.0], [100.0, 100.0, 100.0, 100.0, 100.0, 100.0], [100.0, 100.0, 100.0, 100.0, 100.0, 100.0], [100.0, 100.0, 100.0, 100.0, 100.0, 100.0], [100.0, 100.0, 100.0, 100.0, 100.0, 100.0], [100.0, 100.0, 100.0, 100.0, 100.0, 100.0]]
        >>> Agents = []
        >>> a = Grazer(Env, Agents, 0, 0)
        >>> b = Grazer(Env, Agents, 5, 5)
        >>> Agents.append(a)
        >>> Agents.append(b)
        >>> a.share_with_neighbours(1)
        >>> a.store
        0
        >>> b.store
        0
        >>> a.eat()
        >>> a.share_with_neighbours(1)
        >>> a.store
        10
        >>> b.store
        0
        >>> a.setx(4);a.sety(5)
        4
        5
        >>> a.share_with_neighbours(1)
        sharing 1.0 5.0
        >>> a.store
        5.0
        >>> b.store
        5.0

        """
        for otheragent in self.agents:
            if otheragent is not self:
                distance = self.distance_between(otheragent)
                if distance <= neighbourhood:
                    average = (self.store + otheragent.store)/2
                    self.store = average
                    otheragent.store = average
                    print("sharing " + str(distance) + " " + str(average))

# definition of subclass "Predator". Inherits from "Agent".
class Predator(Agent): 
    
    def __str__(self):
        """
        Overwrites Predator print() function to show values in x, y and store variables

        Returns
        -------
        TYPE
            Displays values in x, y, store, and energy level variables.
        
        DOCTESTS
        -------
        
        The following set of instructions tests that __str__ returns the expected string through print().        
        
        >>> a = Agent("Env", "Agents", 10, 20)
        >>> print(a)
        x = 10, y = 20, store = 0
        >>> a.store = 5
        >>> print(a)
        x = 10, y = 20, store = 5

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
        
        DOCTESTS
        -------
        
        The following set of instructions tests that eat() works correctly by:
            - creating 2 agents nd 1 predator
            - place predator within eating neighbourhood
            - validating that eat() results in an increase in energy and store if eat is succefuls or no change if unsuccesful
            - validating that grazer is removed from list if eat() is succesful

        >>> import random
        >>> Env = [[100.0, 100.0, 100.0, 100.0, 100.0, 100.0], [100.0, 100.0, 100.0, 100.0, 100.0, 100.0], [100.0, 100.0, 100.0, 100.0, 100.0, 100.0], [100.0, 100.0, 100.0, 100.0, 100.0, 100.0], [100.0, 100.0, 100.0, 100.0, 100.0, 100.0], [100.0, 100.0, 100.0, 100.0, 100.0, 100.0]]
        >>> Agents = []
        >>> a = Grazer(Env, Agents, 0, 0)
        >>> b = Grazer(Env, Agents, 5, 5)
        >>> Agents.append(a)
        >>> Agents.append(b)
        >>> p = Predator(Env, Agents, 0, 0)
        >>> p.eat(0) # doctest:+SKIP
        ...
        >>> if p.store == 1:
        ...     p.energy == 10 and len(Agents) == 1
        ... else:
        ...     p.energy == 0 and len(Agents) == 2
        True
        
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
        Randomly increases xory by 1 or decreases parameter xory by 3 in a torus plane of dimensions defined by lenght of agent.environment. 
        Disproportionate movement forward (decreasing x or y 90% of the time) emulates predator circuit in the plane.

        Parameters
        ----------
        xor : number
            Parameter indicating an x or y value of a coordinate.

        Returns
        -------
        xor : number
            Parameter after processing.
        
        DOCTESTS
        -------
        
        The following set of instructions tests that move_coordinate() works correctly by:
            - creating an predator
            - moving the x value of the agent
            - checking that new value increased by 1 or decreased by 3
        
        >>> import random
        >>> Env = [[100.0, 100.0, 100.0, 100.0, 100.0, 100.0], [100.0, 100.0, 100.0, 100.0, 100.0, 100.0], [100.0, 100.0, 100.0, 100.0, 100.0, 100.0], [100.0, 100.0, 100.0, 100.0, 100.0, 100.0], [100.0, 100.0, 100.0, 100.0, 100.0, 100.0], [100.0, 100.0, 100.0, 100.0, 100.0, 100.0]]
        >>> Agents = []
        >>> a = Predator(Env, Agents, 0, 0)
        >>> Agents.append(a)
        >>> a.getx()
        0
        >>> n = a.move_coordinate(a._x)
        >>> (n == 1 or n == 3)
        True

        """
        if random.random() < 0.1:
            xory = (xory + 1) % len(self.environment)
        else:
            xory = (xory - 3) % len(self.environment)
        return xory
