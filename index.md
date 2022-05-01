
---
title: Assignment 2: Planning for Drunks
---

# **Assignment 2:** Planning for Drunks Model

**Module:** GEOG5990M Programming for Geographical Information Analysis: Core Skills

**Luis Gerardo Sanchez Soto**

**Student ID:** 201534083


## Model summary

The model presented here is the work for Assignment 2 of the Module. The problem selected is "Planning for Drunks".

The program models the behaviour of 25 drunks heading home from the pub after drinking, with varied levels of drunkness.
- The program reads an external file to create the town of map, including the pub and 25 houses
- The drunks are created and assigned a house number and a drunk level between 1 and 4 (1: least drunk, 4: very drunk)
- One by one, the drunks head home, with the randomness of their steps dependent to their drunk level
- At each step, the drunk evaluates their position to determine their status (At bar, Walking, or At home) and stops when reaching home
- All drunks start their journey home from a point within the pub and end their journey when reaching their respective house.
- Their drunk level impacts their sense of direction. That is: Drunks with lower drunk levels will show less randomness in the direction of their steps, and higher levels will increase the possibility of stepping away from the direction of their house.

The program uses a TKinter GUI to display the results of the simulation:
- a town map with the routes taken by all drunks
- a step density map
- overwrites a text file with the step density information

## Program components
Running the model:
Execute the pfdmodel.py script to run the model. A GUI window will appear with several options in the Model menu (described delow). An additional matplotlib figure window will appear for closer inspection of the outputs of the model.

Running the model run the main mechanincs of the program and display a visual representation of the town and show the routes that each drunk took to reach their house. Once ran, the user can use the model menu to create a step density map (a map marking the number of steps at each coordinate position in the map) from the simulation, display it on the model window and export it as a CSV file.

The program requires to scripts to run:
- [pfdmodel.py](https://sanluige.github.io/pfdmodel.py), which is the main script from which the program is executed, and;
- [drunksframework.py](https://sanluige.github.io/drunksframework.py), which is the definition of the Drunk class and its functionality.

Additionally, it requires two files:
- [town.txt](https://sanluige.github.io/town.txt), which contains the environment information.
- [step_dmap.csv](https://sanluige.github.io/step_dmap.csv), which is the file used to write the step density map data out of the model when requested by the user.

Please download the files into the same local directory to run.

**Please also refer the [README](https://sanluige.github.io/README) and [LICENSE](https://sanluige.github.io/LICENCE) files, which include the information in this page.**

## Navigating the model menu

The menu allows the user to:

**Print drunk information**: Prints the information of drunks (position, housenumber, status and drunk level) in the console.

**Run simulation**: Runs the program and displays the town map with the 25 routes on the GUI window and figure window (for closer inspection). This also creates the density map without displaying it on program window.

**Draw step density map and export CSV file**: displays density map on the GUI and figure window, and overwrites file step_dmap.csv with the data from that simulation.

**Quit model**: Quits the execution of the model and closes model window.

![This is an image](https://sanluige.github.io/PFDMenu.png)

## Code testing

The testing of the functionality of relevant methods and functions in drunksframework.py has been done using Doctests. The tests validate that each method/function performs as expected, changes and updates variables as expected and returns the appropriate values and types of values.
Please run the doctests on the script drunksframework.py for testing:
- Navigate to the directory where the script is located;
- run the command "python -m doctest -v drunksframework.py" to initiate Doctests.

Some code used for testing and previous steps was commented out as additional proof of testing in pfdmodel.py.

## Experience with the assignment

I had a great time developing the code for this assignment, building on the foundations laid by the practical work during the module and assignment 1. Below are some important notes on my experience:

- Initially I intended to do an animation of the process of drunks finding their way home, but encountered problems implementing it and also reconsidered the relevance of animating the process, given that there's no interaction between drunks and therefore the animation would be a little boring. The coded for that is commented out at the bottom section of the script pfdmodel.py (section with title "Unsuccesful implementations").

- My initial approach was to allow drunks to move in a completely random manner, but I quickly realised that this often resulted in excessive run times and the program crashing as drunks would move around the map virtually indefinitely, with no sense of where their house was. I ended up defining four levels of "drunkness" (1 through 4) that defined the randomness of their movement. Essentially, drunks moved towards their house location depending on if a random number was above or below a limit defined by the drunkness level:

```
    
def move_ycoordinate(self, y):
    dl = self.drunklevel/10
    if y > 0 and y < len(self.town):
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

```

After testing, 1 to 4 allow for diversity in randomness of movement, but not too much that would allow the drunk to wander off the general direction to their house.

- Additionally, I initially developed a slightly inefficient way of drawing the density map. As drunks move, their steps are saved as coordinate pairs in a list. When drawing the map, a 300x300 list of lists if filled with zeros and then for each point in the map, the drunks' step lists are searched to find that point and add 1 to that point for each appearance. This worked well enough, although it can take about 10-15 seconds to process. The implemented improvement to this inefficiency issue was to embed the density map drawing process in the simulation of the drunk's journey itself. That doesn't require searching the drunks' step list 90,000 times (map size 300x300), given that now, at every step taken by every drunk, the density map is updated. The initial (inefficient attempt) is commented out under the method draw_density().

## License

This projects is licensed under the GNU GENERAL PUBLIC LICENSE v3.0 or any later versions (LICENSE). Full details of the license can be found at [LICENSE](https://sanluige.github.io/LICENCE)

## Additional notes

- The code was developed to run on MacOS operating system, so users running the program in other operating systems should alter the code (particularly matplotlib commands) to run correctly in their computer.
