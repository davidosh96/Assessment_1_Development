#import modules
import random
#importing operator to use for working out max x agent value
import operator
#import matplotlib pyplot to plot agent locations
import matplotlib.pyplot
import time
start=time.process_time()

#controlling how many agents there are:
num_of_agents = 10
#specify the number of times the agents are to be moved
num_of_iterations = 100
#create list "agents"
agents = []

#make agents a random integer between inc 0 and 99 and add them to the list of agents
#puts y and x coordinates as the first list (number [0]) in list "agents"
#[0][0]= ycoord and [0][1]=xcoord
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])
print("list of agents created and then stored in agents list [0]; number of agents created is determinted by value assigned to num_of_agents:")
print(agents)


# randomly move the agents num_of_iterations times. "% 100" creates torus environment, creating boundary to prevent agents leaving the space
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0]  + 1) % 100
        else:
           agents[i][0] = (agents[i][0] - 1) % 100
        if random.random() <0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1]-1) % 100
print("randomly moved the agents num_of_iterations times:")   
print(agents)

'''
#calculate euclidean distance between [0][0],[0][1] and [1][0],[1][1]
print("euclidean distance between first and second agents:")
answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
print(answer)    
'''

#prints the agent pair with the highest x-coord
print("maximum x-value:")
print(max(agents, key=operator.itemgetter(1)))


#plot agent locations after movements
for i in range(num_of_agents):
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
#matplotlib.pyplot.scatter(agents[1][1],agents[1][0], color='red')
matplotlib.pyplot.show()

end=time.process_time()
print("processing time="+str(end-start))