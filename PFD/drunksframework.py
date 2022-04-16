#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 09:27:36 2022

@author: luisgerardosanchezsoto

This script defines the Drunk class used in the Planning 
for Drunks model (pfdmodel.py) and its functionality.

"""

# imports
import random

# definition of class "Drunk"
class Drunk():
    def __init__(self, town, bara, adbk, x = None, y = None):
        p = random.choice(bara)
        
        # test random.choice(bara)
        if (p[0] == None):
            print("p[0] == None")
        if (p[1] == None):
            print("p[1] == None")
        
        if (x == None):
            self._x = p[0]
        else:
            self._x = x
        if (y == None):
            self._y = p[1]
        else:
            self._y = y
        self.town = town
        self.baraddress = bara
        self.addressbook = adbk
        self.steps = [] # list of coordinate pairs [[x1,y1],[x2,y2],...]
        self.status = 0 # 0: at bar, 1: walking, 2: at home
        self.housenumber = random.choice(list(adbk))
        self.haddress = adbk[self.housenumber]
        self.drunklevel = random.randint(1,4)
        
    # protect x and y
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
        return self._x
    def delx(self):
        del self._x
    x = property(getx, setx, delx, "'x' property.")

    def gety(self):
        return self._y
    def sety(self, value):
        self._y = value
        return self._y
    def dely(self):
        del self._y
    y = property(gety, sety, dely, "'y' property.")
    
    # 
    def __str__(self):
        """
        Overwrites print() function to show variables of drunk agent

        Returns
        -------
        None.
            print(drunk object) displays values in x, y, Housenumber, Status and Drunk level variables.
        
        DOCTESTS
        -------
        
        The following set of instructions tests that __str__ returns the expected string through print().
        
        >>> import random
        >>> import drunksframework
        >>> # create town - dummy for testing
        >>> town = [[10.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0],]
        >>> ylenght = len(town)
        >>> xlenght = len(town[0])
        >>> # create addressbook as a dictionary - keys are house numbers, list of (x,y) pairs - dummy for testing
        >>> addressbook = {}
        >>> for i in range(1):
        ...     a = []
        ...     for x in range(xlenght):
        ...         for y in range(ylenght):
        ...             if town[x][y] == (i+1)*10:
        ...                 a.append([x, y])
        ...     addressbook.setdefault((i+1)*10, []).append(a)
        >>> # create bar address - list of bar x,y pairs
        >>> baraddress = []
        >>> for x in range(xlenght):
        ...     for y in range(ylenght):
        ...         if town[y][x] == 1:
        ...             baraddress.append([y, x])
        >>> adrunk = drunksframework.Drunk(town, baraddress, addressbook)
        >>> adrunk.drunklevel = 4
        >>> print(adrunk)
        x = 1, y = 4, Housenumber = 10, Status = 0, Drunk level = 4
        
        """
        return "x = " + str(self._x) + ", y = " + str(self._y) + ", Housenumber = " + str(self.housenumber) + ", Status = " + str(self.status) + ", Drunk level = " + str(self.drunklevel)
    
    def move_xcoordinate(self, x):
        """
        Randomly increases or decreases parameter x by 1 in plane of dimensions defined by dimensions of town

        Parameters
        ----------
        x : number
            Parameter indicating x value of a coordinate.

        Returns
        -------
        x : number
            Parameter after processing.
            
        DOCTESTS
        -------
        
        The following set of instructions tests the functionality of move_xcoordinate.
        By creating a dummy object of the Drunk class, it tests that move_xcoordinate:
            - changes x value of Drunk object
            - returns an integer
            - changes x value by +1 or -1 
        
        >>> import random
        >>> import drunksframework
        >>> # create town - dummy for testing
        >>> town = [[10.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0],]
        >>> ylenght = len(town)
        >>> xlenght = len(town[0])
        >>> # create addressbook as a dictionary - keys are house numbers, list of (x,y) pairs - dummy for testing
        >>> addressbook = {}
        >>> for i in range(1):
        ...     a = []
        ...     for x in range(xlenght):
        ...         for y in range(ylenght):
        ...             if town[x][y] == (i+1)*10:
        ...                 a.append([x, y])
        ...     addressbook.setdefault((i+1)*10, []).append(a)
        >>> # create bar address - list of bar x,y pairs
        >>> baraddress = []
        >>> for x in range(xlenght):
        ...     for y in range(ylenght):
        ...         if town[y][x] == 1:
        ...             baraddress.append([y, x])
        >>> adrunk = drunksframework.Drunk(town, baraddress, addressbook)
        >>> n = adrunk.move_xcoordinate(adrunk.getx())
        >>> n != adrunk.getx()
        True
        >>> type(n)
        <class 'int'>
        >>> n == adrunk.getx() + 1 or n == adrunk.getx() - 1
        True
        
        """
        dl = self.drunklevel/10
        if x > 0 and x < len(self.town[0]):
            #if x == self.haddress[0][0][0]:
            #    pass
            #else:
            if x < self.haddress[0][0][0]:
                if random.random() > dl:
                    x = (x + 1)
                else:
                    x = (x - 1)
            else:
                if random.random() > dl:
                    x = (x - 1)
                else:
                    x = (x + 1)
        else:
            if x >= len(self.town[0]):
                x = (x - 1)
            else:
                x = (x + 1)
        return x

    def move_ycoordinate(self, y):
        """
        Randomly increases or decreases parameter y by 1 in plane of dimensions defined by dimensions of town

        Parameters
        ----------
        y : number
            Parameter indicating an y value of a coordinate.

        Returns
        -------
        y : number
            Parameter after processing.
        
        DOCTESTS
        -------
        
        The following set of instructions tests the functionality of move_ycoordinate.
        By creating a dummy object of the Drunk class, it tests that move_ycoordinate:
            - changes y value of Drunk object
            - returns an integer
            - changes y value by +1 or -1            
        
        >>> import random
        >>> import drunksframework
        >>> # create town - dummy for testing
        >>> town = [[10.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0],]
        >>> ylenght = len(town)
        >>> xlenght = len(town[0])
        >>> # create addressbook as a dictionary - keys are house numbers, list of (x,y) pairs - dummy for testing
        >>> addressbook = {}
        >>> for i in range(1):
        ...     a = []
        ...     for x in range(xlenght):
        ...         for y in range(ylenght):
        ...             if town[x][y] == (i+1)*10:
        ...                 a.append([x, y])
        ...     addressbook.setdefault((i+1)*10, []).append(a)
        >>> # create bar address - list of bar x,y pairs
        >>> baraddress = []
        >>> for x in range(xlenght):
        ...     for y in range(ylenght):
        ...         if town[y][x] == 1:
        ...             baraddress.append([y, x])
        >>> adrunk = drunksframework.Drunk(town, baraddress, addressbook)
        >>> n = adrunk.move_ycoordinate(adrunk.gety())
        >>> n != adrunk.gety()
        True
        >>> type(n)
        <class 'int'>
        >>> n == adrunk.gety() + 1 or n == adrunk.gety() - 1
        True
        
        """
        dl = self.drunklevel/10
        if y > 0 and y < len(self.town):
            #if y == self.haddress[0][0][1]:
            #    pass
            #else:
            if y < self.haddress[0][0][1]:
                if random.random() > dl:
                    y = (y + 1)
                else:
                    y = (y - 1)
            else:
                if random.random() > dl:
                    y = (y - 1)
                else:
                    y = (y + 1)
        else:
            if y >= len(self.town):
                y = (y - 1)
            else:
                y = (y + 1)
        return y

    def move(self):
        """
        Moves Agent by altering x and y using move_xcoordinate and move_ycoordinate

        Returns
        -------
        None.
        
        DOCTESTS
        -------
        
        The following set of instructions tests the functionality of move.
        By creating a dummy object of the Drunk class, it tests that move:
            - changes x and y values of Drunk object.
        
        >>> import random
        >>> import drunksframework
        >>> # create town - dummy for testing
        >>> town = [[10.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0],]
        >>> ylenght = len(town)
        >>> xlenght = len(town[0])
        >>> # create addressbook as a dictionary - keys are house numbers, list of (x,y) pairs - dummy for testing
        >>> addressbook = {}
        >>> for i in range(1):
        ...     a = []
        ...     for x in range(xlenght):
        ...         for y in range(ylenght):
        ...             if town[x][y] == (i+1)*10:
        ...                 a.append([x, y])
        ...     addressbook.setdefault((i+1)*10, []).append(a)
        >>> # create bar address - list of bar x,y pairs
        >>> baraddress = []
        >>> for x in range(xlenght):
        ...     for y in range(ylenght):
        ...         if town[y][x] == 1:
        ...             baraddress.append([y, x])
        >>> adrunk = drunksframework.Drunk(town, baraddress, addressbook)
        >>> x = adrunk.getx()
        >>> y = adrunk.gety()
        >>> l = len(adrunk.steps)
        >>> adrunk.move()
        >>> adrunk.getx() != x
        True
        >>> adrunk.gety() != y
        True
        >>> len(adrunk.steps) == l + 1
        True
        

        """
        self._x = self.move_xcoordinate(self._x)
        self._y = self.move_ycoordinate(self._y)
        self.steps.append([self._x, self._y])
    
    def evalposition(self):
        """
        Updates status variable of Drunk by evaluating the coordinate position of Drunk to address if Drunk is "At bar" (0), "Walking" (1) or "At home" (2).

        Returns
        -------
        status : number
            Variable of Drunk indicating status.
        
        DOCTESTS
        -------
        
        The following set of instructions tests the functionality of evalposition.
        By creating a dummy object of the Drunk class:
            - evaluates if Drunk position is in bar and tests that evalposition returns 0 if so
            - sets Drunk's position in town to house address and tests that evalposition returns 2
            - sets Drunk's position somewhere else in town and tests that evalposition returns 1
        
        >>> import random
        >>> import drunksframework
        >>> # create town - dummy for testing
        >>> town = [[10.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0],]
        >>> ylenght = len(town)
        >>> xlenght = len(town[0])
        >>> # create addressbook as a dictionary - keys are house numbers, list of (x,y) pairs - dummy for testing
        >>> addressbook = {}
        >>> for i in range(1):
        ...     a = []
        ...     for x in range(xlenght):
        ...         for y in range(ylenght):
        ...             if town[x][y] == (i+1)*10:
        ...                 a.append([x, y])
        ...     addressbook.setdefault((i+1)*10, []).append(a)
        >>> # create bar address - list of bar x,y pairs
        >>> baraddress = []
        >>> for x in range(xlenght):
        ...     for y in range(ylenght):
        ...         if town[y][x] == 1:
        ...             baraddress.append([y, x])
        >>> adrunk = drunksframework.Drunk(town, baraddress, addressbook)
        >>> [adrunk.getx(), adrunk.gety()] in baraddress
        True
        >>> adrunk.evalposition()
        0
        >>> adrunk.setx(0)
        0
        >>> adrunk.sety(0)
        0
        >>> [adrunk.getx(), adrunk.gety()] in adrunk.haddress[0]
        True
        >>> adrunk.evalposition()
        2
        >>> adrunk.setx(1)
        1
        >>> adrunk.sety(1)
        1
        >>> [adrunk.getx(), adrunk.gety()] not in adrunk.haddress[0] or [adrunk.getx(), adrunk.gety()] not in adrunk.baraddress
        True
        >>> adrunk.evalposition()
        1
        
        """
        a = [self._x, self._y]
        if a in self.baraddress:
            self.status = 0 #"At bar"
        else:
            if a in self.haddress[0]:
                self.status = 2 #"At home"
            else:
                self.status = 1 #"Walking"
        return self.status