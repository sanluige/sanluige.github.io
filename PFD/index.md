
# **Assignment 2:** Planning for Drunks Model

**Module:** GEOG5990M Programming for Geographical Information Analysis: Core Skills

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

The length of time for the program to run will vary slightly depending on the initial randomised positions of the agents, but is mostly dependent on the number of iterations defined by the user (default number of iterations is 150). The model run will stop when:
- Simulation completes the number of iterations,
- All sheep are hunted,
- Maximum grazing is achieved.

The program requires to scripts to run:
- [pfdmodel.py](https://sanluige.github.io/PFD/pfdmodel.py), which is the main script from which the program is executed, and;
- [drunksframework.py](https://sanluige.github.io/PFD/drunksframework.py), which is the definition of the Drunk class and its functionality.

Additionally, it requires two files:
- [town.txt](https://sanluige.github.io/PFD/town.txt), which contains the environment information.
- [step_dmap.csv](https://sanluige.github.io/PFD/step_dmap.csv), which is the file used to write the step density map data out of the model when requested by the user.

Please download the files into the same local directory to run.

## Navigating the model menu

The menu allows the user to:

**Print drunk information**: Prints the information of drunks (position, housenumber, status and drunk level) in the console.

**Run simulation**: Runs the program and displays the town map with the 25 routes on the GUI window and figure window (for closer inspection).

**Draw step density map and export CSV file**: creates density map, displays map on the GUI and figure window, and overwrites file step_dmap.csv with the data from that simulation.

**Quit model**: Quits the execution of the model and closes model window.

![This is an image](https://sanluige.github.io/PFD/PFDMenu.png)

## Code testing

The testing of the functionality of relevant methods and functions has been done using Doctests. 
The tests validate that each method/function performs as expected, changes and updates variables as expected and returns the appropriate values and types of values.
Please run the doctests on the script agentframework.py for testing:
- Navigate to the directory where the script is located;
- run the command "python -m doctest -v drunksframework.py" to initiate Doctests.

## License

This projects is licensed under the GNU GENERAL PUBLIC LICENSE v3.0 or any later versions (LICENSE). Full details of the license can be found at [LICENSE](https://www.gnu.org/licenses/lgpl-3.0.md)

## Additional notes

- The code was developed to run on MacOS, so users running the program in other operating systems should alter the code (particularly matplotlib commands) to run correctly in their computer.
