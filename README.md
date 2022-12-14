# Assignment-2 Planning for drunks Agent Based Modelling

The aim of this assignment is to show the paths of drunks attempting to get home from the pub which will allow for town planning. The project aim is achieved by using agent based modelling. In the town there was 25 drunks that were modelled from the pub to their homes, there house numbers were labelled as 10-250 for each respective drunk from 1-25. The drunks move in random steps and once they reach their respective homes they stop. The script produces a density map of all the drunks paths from the pub to their homes.

The town.pln file was downloaded and ran into the script as environment. The environment was printed as a test to ensure it has been ran in properly and plotted. This displayed a town plan; where the empty space in the town, has the value in the environment as 0, therefore coded in purple; where each of the 25 houses of the drunks were displayed as 20x20 squares had the value of 10-250, which corresponded to the drunk from 1-25 respectively, these values filled the houses with varying colours. The pub had values in the environment of 1, which gave rise to the first challenge of the assignment. As the value in the environment where the pub was located was 1 the plot fills the pub in with a colours extremely close to that of the empty space. Therefore, to find the coordinates of the pub it was useful to create a loop over the environment to find the index where the entry value was equal to 1 using the numpy.argwhere function. This gave the pub corner coordinates as, (139,129),(139,148), (158,129), (158,148). Once the town plan and pub location had been created an established the code from assingment one could be adapted to initiate agents which model the drunks. Rather than allowing the code to intiate agents with random coordinates between 0 and 99 on both the x and y axis, the intial coordinates of all the drunks were restricted to between the outer coordinates of the pub. 

Moving the drunks used the same code as assignment 1, however, in the assignment 1 code the agents, once at one edge of the map, were able to leave and enter at the other side which gave the impression that the map was a torus. In town planning this would not be an effective was to model the boundary solutions as drunks would not be able to jump to the other side, therefore the boundary condtions were changed to that of solid wall boundaries. This could model a fence or wall around the town and the drunks do not move off the map but stays on the boundary until it moves in another direction. Another problem that was faced was how slow the drunks moved around the town therefore the code was adjusted to move the drunks in steps of 10. 

In assignment 1 code the agents would move around continuously until the stopping condition of 10 frames was met at which point the variable carry_on became false and the whole model stops. However, in this assignment the individual agents, 'drunks' need to stop once they reach their respective homes. This was challenging as initially a function was created in the agent framework which made the agents coordinates the same over every iteration once they were in their house. However, this did not work as this needed to be inside the move function as the move function was still changing the coordinates while the new function made them the same. In order to achieve this a if condition was placed inside the move function which when the entry value of the index of the environment where the agent was matched the number of the agent times 10 then the coordinates of the agent remained constant over each iteration. If it did not match then the agent coordinates were randomly moved. When this was run it was noticed that there was a single agent not moving from the initial coordinates this was because python indexes beginning at 0 so the initial agent was 0 and the final agent was 24 which meant that the agents had to match the (the number of the agent +1) times 10 to be at the correct house. 

The stopping function function needed to be adapted in order to stop the model from running once all the agents were home rather than just for a set number of frames. The gen_function produced frames up to the value of 10 in assignment 1 and changing the variable carry_on to false once which stopped the whole model. The adaptation of the code was made to combat this issue but not having a value of the variable a that it was stopped at and just allowing the model to iterate over the frames while carry_on was true. In the class an if condition was added to the if condition where the agents stopped once they were home, this new if function said if the number of agent that was home was the final agent then carry_on variable became false which stopped the model from running. This was quite easy to over come as it was quite a logical step once the previous if statement was in the correct place. Within the gen_function the step of storing the coordinates of each agent now takes place in order to see its path.

A problem that arose while watching the model is that the drunks kept tracing over others houses or back over the pub which would not be able to occur. Therefore the agent framework was adapted and another if statement was added into the mode function. Whereby if the entry value of the environment where the drunk was being moved to did not equal 0 and did not equal their house number then the drunk would stay at that point until it moved to another point. This meant that the drunks were only able to move to a new space if it was empty of their own home. This was challenging as it was difficult to try and find the correct conditions to stop the drunks from moving over others houses. 

Overall, this assignment has been interesting and allowed for the connection to be made between agent based modelling and research that it may be used for. Initially it took a while to get into the assignment as it was challenging trying to understand how the first assignment 1 code could be used to complete this assignment. However, once the connection had been made the coding adaptations became easier and more enjoyable. There was challenges that were overcome throughout which allowed for the assignment to be completed. Using the feedback from assingment 1 the comments within the code where able to be increased and highlighting which parts were tests and not needed to be run for the assignment has been implemented. Given more time a way to help the drunks get to their houses would be to maybe have a function that does move the drunks randomly but also converges them to their house using numerical methods. This would be a good way to model drunks as they may walk kind of randomly but it would be more towards the direction of their house than randomly. 
