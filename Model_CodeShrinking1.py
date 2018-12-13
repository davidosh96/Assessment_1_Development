#import modules
import random
#importing operator to use for working out max x agent value
import operator
#import matplotlib pyplot to plot agent locations
import matplotlib.pyplot
#create list "agents"
agents = []

#make agents a random integer between inc 0 and 99 and add them to the list of agents
#puts y and x coordinates as the first list (number [0]) in list "agents"
#[0][0]= ycoord and [0][1]=xcoord
agents.append([random.randint(0,99),random.randint(0,99)])
print("coords created and then stored in agents list [0]:")
print(agents)


#randomly move first set of agents 1 step
if random.random() < 0.5:
    agents[0][0] = agents[0][0]  + 1
else:
   agents[0][0] = agents[0][0] - 1
if random.random() <0.5:
    agents[0][1] = agents[0][1] + 1
else:
    agents[0][1] = agents[0][1]-1
print("moved them 1 step:")   
print(agents)


#move agents a second step
if random.random() < 0.5:
    agents[0][0] = agents[0][0] + 1
else:
    agents[0][0] = agents[0][0] - 1
if random.random() <0.5:
    agents[0][1] = agents[0][1] + 1
else:
    agents[0][1] = agents[0][1] - 1
print("moved them a second step")    
print(agents)    


#make second set of agents, and add them to "agents" list in list position [1]
agents.append([random.randint(0,99),random.randint(0,99)])
print("first set of agents after 2 steps, second agents are created and put in agents list, position [1]:")
print(agents)


#randomly move second set of agents 1 step
if random.random() < 0.5:
    agents[1][0] = agents[1][0]  + 1
else:
   agents[1][0] = agents[1][0] - 1
if random.random() <0.5:
    agents[1][1] = agents[1][1] + 1
else:
    agents[1][1] = agents[1][1]-1
print("second agents are moved one step:")
print(agents)


#move agents a second step
if random.random() < 0.5:
    agents[1][0] = agents[1][0] + 1
else:
    agents[1][0] = agents[1][0] - 1
if random.random() <0.5:
    agents[1][1] = agents[1][1] + 1
else:
    agents[1][1] = agents[1][1] - 1
print("second agents are moved a second step:")    
print(agents) 


#calculate euclidean distance between [0][0],[0][1] and [1][0],[1][1]
print("euclidean distance between first and second agents")
answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
print(answer)    


#prints the agent pair with the highest x-coord
print("maximum x-value:")
print(max(agents, key=operator.itemgetter(1)))


#plot agent locations after movements
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0], color='red')
matplotlib.pyplot.show()