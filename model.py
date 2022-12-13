import random
import operator
import agentframework
import matplotlib.animation
import csv
import matplotlib.pyplot
import matplotlib
matplotlib.use('TkAgg')
import tkinter
import time
import numpy as np
#Assignment 2 

#Read in the environment data from the town plan file
f = open('town.plan', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
environment = []
#reading in the data and loading each of the lines as a row of the environment dataset
for row in reader:
    rowlist=[]				# A list of rows
    for value in row:				# A list of value
        rowlist.append(value)
    environment.append(rowlist)		
f.close()

#testing to ensure the environment has been read in properly, viewing the rows using rowlist and then the full data set as environment
#print(rowlist)
#print(environment)
#print(f)

#testing the plot of the environment to see the lay out of the data and ensure it shows the town plan with the houses and pub as required
#NO NEED TO PRINT: as the plan of the environment is on the animation this is just a test
#matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show()

#NO NEED TO PRINT: finding the pub index as the fill colour value 1 of the pub is so similar to 0 so it was difficult to see in the map
#import numpy as np
#array = np.array(environment)
#index = np.argwhere(array == 1)
#print(index)
#138-158 128-148 these are the x and y coordinates of the pub

#initialising the variables, for the assignment the drunks are modelled by agents and there are 25 drunks with house numbers from 10-25 so the number 
#of agents needs needed is 25           
num_of_agents = 25
num_of_iterations = 100
agents = []#creates an empty list to store the initiated agents in

#sets the plot size of the animation
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


ax.set_autoscale_on(False)
carry_on = True	
# Intiates the agents.
for i in range(num_of_agents):
    x = random.randint(139,158) #sets the agents with random coordinates randomly between the coordinates of the corners of the pubs
    y = random.randint(129,148)
    agents.append(agentframework.Agent(x,y,environment,agents)) #uses the agent framework, agent class to initiate all 25 agents in the pub


# Moves the agents.
def update(frame_number):
    #This function creates each frame of the animation, updating the animation each frame while moving each of the agents.
    fig.clear()
    global carry_on
    matplotlib.pyplot.xlim(0, 300)
    matplotlib.pyplot.ylim(0, 300)
    matplotlib.pyplot.imshow(environment)#plots the environment in the background
    for i in range(num_of_agents):
        x_ = None
        y_ = None
        agents[i].move(environment,i,carry_on,x_,y_)
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y,color='blue')#plots each of the agents paths frame by frame to show the path of each drunks until they get home
        
        
def gen_function(b = [0]):
    #This function sets the number of frames using a variable carry_on which when true iterates adding a frame to the animation, when carry_on becomes false in the agent frame work
    #once all the drunks are at their respective homes it stops the iteration. This function also stores the coordinates of each frame of each of the agents in the array matrix.
 #   global carry_on #Not actually needed as we're not assigning, but clearer
     matrix = np.array([x,y])
     a=0
     while carry_on==True :
        yield a			# Returns control and waits next call.
        a = a + 1
        for i in range(num_of_agents):
            matrix = np.vstack((matrix,[agents[i].y,agents[i].x]))
            #print(matrix) NO NEED TO BE PRINTED this was used as a test in order to ensure all the coordinates are stored in the array matrix.
        
                 
#Creates the animation plotting the environment and the agents updating the coordinates of the agents where they move to at each frame 
def run():
    animation = matplotlib.animation.FuncAnimation(fig,update,frames=gen_function, repeat=False)
    canvas.draw()
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run Model", command=run)
tkinter.mainloop()#sets the GUI waiting for events

