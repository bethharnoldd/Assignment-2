import random #random module

class Agent(): #crearing a class agent that defines a function to initiate the agents 
    def __init__(self,x,y,environment,agents):
        if x == None:
            self.x = 0
        else:
            self.x = 0
        if y == None:
            self.y = 0
        else:
            self.y = 0
        self.environment = environment
        self.store=0
        self.agents = agents
    def move(self):
        for agent in self.agents
            if random.random() < 0.5:
                self.y = (self.y + 1) % 100
            else:
                self.y = (self.y - 1) % 100

            if random.random() < 0.5:
                self.x = (self.x + 1) % 100
            else:
                self.x = (self.x - 1) % 100
    def home(self, environment): # can you make it eat what is left?
        for agent in self.agents:
            if self.environment[self.y][self.x]\10==agent
                del agents[agent]
                
            
import random #random module

class Agent(): #crearing a class agent that defines a function to initiate the agents 
    def __init__(self,x,y,environment,agents):
        if x == None:
            self.x = random.randint(0,99)
        else:
            self.x = x
        if y == None:
            self.y = random.randint(0,99)
        else:
            self.y = y
        self.environment = environment
        self.store=0
        self.agents = agents
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100