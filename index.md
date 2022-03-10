---
title: Assignment 1: Agent Based Model
---

# **Assignment 1:** Basic Agent Based Model

**Module:** GEOG5990M Programming for Geographical Information Analysis: Core Skills

**Student ID:** 201534083


## Model summary

The model presented here is the result of the practical work of the module, with additional enhancements.

This model emulates basic behaviour of grazers and predators in an environment. Grazers move in and eat from the environment and share grazed resources with other neighbouring grazers. Predators move in a circuit and hunt nearby grazers with probability to fail.

In general, the model:
- builds agents and initializes them in a space;
- gets them to interact with each other by assesing distances between each other and sharing grazed resources;
- reads in environmental data;
- gets agents to interact with the environment;
- randomizes the order of agent actions;
- displays the model as an animation;
- is contained within a GUI;
- is initialised with data from the web.

## Program components

The program requires to scripts to run:
- [agenbasedmodel.py](https://sanluige.github.io/agentbasedmodel.py), which is the main script from which the program is executed, and;
- [agentframework.py](https://sanluige.github.io/agentframework.py), which is the definition of the Agent class and subclasses Grazer and Predator.

## Navigating the model menu


The menu allows the user to:

**Run model**: Run the model with default parameters.

**Change model parameters**: Allows the user to change the following parameters on the console:

- Number of grazers
- Number of predators
- Number of iterations of the model
- Grazers sharing neighbourhood radio
- Predator hunting neighbourhood radio

**Print agent information**: Prints the information of agents - grazers and predators - in the console.

**Print environment file**: Updates the environment state in an exixting CSV file. User should download it to their working directory (or change the directory in the code" for this to work. Alternatively, the user can create a blank CSV file called "environmentout.csv" in point the code to it locally.

**Quit model**: Quits the execution of the model and closes model window.

![This is an image](https://sanluige.github.io/Model_menu.png)

## Additional notes

- The code was developed to run on MacOS, so users running the program in other operating systems should alter the code (particularly matplotlib commands) to run correctly in their computer.
