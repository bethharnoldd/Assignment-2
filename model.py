import random
import operator
import matplotlib.pyplot
#import agentframework
import matplotlib.animation
import tkinter
import csv
import matplotlib.pyplot
import matplotlib
matplotlib.use('TkAgg')
import requests
import bs4


#Assignment 2 

#Run in the data
environment = []
town = open('town.plan', newline='') 
reader = csv.reader(town, quoting=csv.QUOTE_NONNUMERIC)
#reading in the data
for row in reader:
    rowlist=[]				# A list of rows
    for value in row:				# A list of value
        rowlist.append(value)
    environment.append(rowlist)				# Floats
town.close() 	# Don't close until you are done with the reader;
		# the data is read on request.
#initialising the variables            
num_of_agents = 25
num_of_iterations = 100
neighbourhood = 20
agents = []

#sets the plot size
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


ax.set_autoscale_on(False)
carry_on = True	
# Make the agents.
for i in range(num_of_agents):
    y = 0
    x = 0
    agents.append(agentframework.Agent(x,y,environment,agents))

def update(frame_number):
    fig.clear()
    global carry_on
    random.shuffle(agents)
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        
        agents[i].move()
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y,color='blue')
    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
#Plot the environment
#Plot the environment in a plot and colour points different depending on' 
#whether it is a house, pub or empty space, label points with house numbers'
#agents
#randomly generate 25 agents and label them 10 to 250 with the same initial coordiates of the pub between 
#the dimensions of the environment' 
#moving the agents
#move the agent 1 space up or down left or right'
#condition if the coordinate has been repeated redo the step
#removing
#if the labels match the coordinate label it is removed onto the next agent this is a condition loop'
