import random #random module

class Agent(): #crearing a class agent that defines a function to initiate the agents 
    def __init__(self,x,y,environment,agents):
        if x == None:
            self.x = random.randint(139,158) #initiating the agent x coordinate randomly in the pub, which lies between the coordinate 139 and 158
        else:
            self.x = x
        if y == None:
            self.y = random.randint(129,148) #initiating the agent y coordinate randomly in the pub, which lies between the coordinate 129 and 148
        else:
            self.y = y
        self.environment = environment
        self.store=0
        self.agents = agents
    def move(self,environment,i,carry_on,x_,y_):
        if self.environment[self.y][self.x] == (i+1)*10: #if the agent i from 0 to 24 is at the point in the environment where it matches its home 10-250 respectively
            self.y = self.y #it stops and the coordinates remain the same
            self.x = self.x
            if i == 24: #once the final agent 'drunk' No24 is home the variable carry_on becomes false which stops the animation running
                carry_on=False
            else:
                carry_on = True
        else:#the initial model moved the agents by 1 space however, this was taking a very long time so the drunks now move 10 spaces 
            #if the agent is not at its own home then the coordinates are moved randomly
            if random.random() < 0.5: #if a random number between 0-1 is less than 0.5 the y coordinate of the agent becomes +10, the drunk moves up 10
                self.y_ = (self.y + 10)
                if self.y_  < 0:
                    self.y_ = 0
                if self.y_ > 299:
                    self.y_ = 299
            else: #if a random number between 0-1 is more than 0.5 the y coordinate of the agent becomes -10, the drunk moves down 10
                self.y_ = (self.y - 10)
                if self.y_  < 0:
                    self.y_ = 0
                if self.y_  > 299:
                    self.y_ = 299
            if random.random() < 0.5: #if a random number between 0-1 is less than 0.5 the x coordinate of the agent becomes +10, the drunk moves right 10
                self.x_ = (self.x + 10)
                if self.x_  < 0:
                    self.x_ = 0
                if self.x_  > 299:
                    self.x_ = 299
            else: #if a random number between 0-1 is more than 0.5 the x coordinate of the agent becomes +10, the drunk left 10
                self.x_ = (self.x - 10)
                if self.x_  < 0:
                    self.x_ = 0
                if self.x_  > 299:
                    self.x_ = 299
            if self.environment[self.y_][self.x_] != 0 and self.environment[self.y_][self.x_] != (i+1)*10: #this stops the agents from going over a house that is not their own or the pub
                self.y = self.y #the drunk once has left the pub the drunk will not go back over the pub and will not pass over anothers house.  
                self.x = self.x #if the new moved coordinates are back on the pub or on another persons house then the coordinates are not moved and another iteration is conducted
            else:
                self.y = self.y_ #if the moved coordinates are not on a pub or on another persons house then the new moved coordinates become the new coordinates
                self.x = self.x_ 
                    
                
                