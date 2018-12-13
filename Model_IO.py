#import modules
import random
#importing operator to use for working out max x agent value:
#import operator
#import matplotlib pyplot to plot agent locations:
import matplotlib.pyplot
#import agents
import agentframework
import csv
import time
start=time.process_time()

#pythagoras code as a function:
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a._x - agents_row_b._x)**2) + ((agents_row_a._y - agents_row_b._y)**2))**0.5


#create environment list to put rowlist in:
environment = []


#Reading in the csv DEM data from text file:
f = open('in.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:
    rowlist = []         #create a list for each row
    for value in row:
        rowlist.append(value)  #appends each row of values into a list for each row
        #print(value)      #prints the data as raw values
    #append the rowlist to the environment list:    
    environment.append(rowlist)
f.close()


#using matplotlib to show the data has been read in correctly:
#matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show()


random_seed = 50    
#controlling how many agents there are:
num_of_agents = 10
#specify the number of times the agents are to be moved:
num_of_iterations = 100
#create list "agents":
agents = []

#make agents a random integer between inc 0 and 99 and add them to the list of agents
#takes agents created in "agentframework" module
#puts y and x coordinates in list "agents"
for i in range(num_of_agents):
    agents.append(agentframework.Agent(random_seed, environment))
print("agents created in framework and stored in agents list; number of agents created is determined by value assigned to num_of_agents:")
#print(agents)


#move the agents num_of_iterations times. "% 100" in "agentframework" creates torus environment, creating boundary to prevent agents leaving the space
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
print("randomly moved the agents num_of_iterations times:")   
#print(agents)

'''
#calculate euclidean distance between [0][0],[0][1] and [1][0],[1][1]
print("euclidean distance between first and second agents:")
answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
print(answer)    


#prints the agent pair with the highest x-coord
print("maximum x-value:")
print(max(agents, key=operator.itemgetter(1)))
'''

#plot agent locations after movements
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y)
#matplotlib.pyplot.scatter(agents[1][1],agents[1][0], color='red')
matplotlib.pyplot.show()

#result of pythagoras function:
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
print("distance between agents_row_a, agents_row_b:")
print(distance)


end=time.process_time()
print("processing time="+str(end-start))
