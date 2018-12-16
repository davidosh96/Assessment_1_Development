#import the modules to be used in the program:

import random                 #import random is used to generate random integers/values to specify locations for the agents
import matplotlib.pyplot      #import pyplot from the matplotlib library, used to plot graphs/agent locations
import matplotlib.animation   #imported in order to plot the agents and environment as an animation
import agentframework         #import agents module from the file "agentframework.py"
import csv                    #imported in order to read in the csv file
import time                   #in order to time how long it takes for the code to be processed/read

start=time.process_time()     #starts the timer


environment = []              #creates environment list to put rowlist in



#Reading in the csv DEM raster data from text file and appending it to the environment list:

f = open('in.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:
    rowlist = []                   #create a list for each row
    for value in row:
        rowlist.append(value)      #appends each row of values into a list for each row
        #print(value)              #prints the data as raw values in the console
    environment.append(rowlist)    #appends the rowlist to the environment list:    
f.close()



#using matplotlib to show the data has been read in correctly:
#matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show()


    
neighbourhood = 50
num_of_agents = 50      #controls how many agents there are
num_of_iterations = 50  #specifies the number of times the agents are to be moved. This is different from the number of frames in the animated plot.
agents = []             #creates list "agents" to append the agents to



#specifies the size of the figure and axes:
fig = matplotlib.pyplot.figure(figsize=(12, 12))
ax = fig.add_axes([0, 0, 1, 1])



#takes agents created in "agentframework" module
#puts them in list "agents":
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, neighbourhood, agents))


#animating the movement of agents:

carry_on = True	    #carry_on is a Boolean value, i.e it is either True or False
            
def update(frame_number):
    fig.clear()
    global carry_on    

#call eat for each agent:   
    #for j in range(num_of_iterations):
        #random.shuffle(agents)
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        #agents[i].share_with_neighbours(neighbourhood)
    
    matplotlib.pyplot.xlim(0, 300)          #specifying the x and y limits for the graph
    matplotlib.pyplot.ylim(300, 0)
    matplotlib.pyplot.imshow(environment)   #plots the environment (from the csv file) on the graph.
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y, color='white')    #plots the list of agent locations on the graph in white
        matplotlib.pyplot.scatter(agents[25]._x,agents[25]._y, color='black')  #displays one agent from the list as a black sheep
    #print(agents[i]._x, agents[i]._y)                                         #prints values of the agents to the console.
    

    
#setting the stopping conditions for the animation: 
#This stopping condition will stop the animation if any agent
#is generated a random.random value of less than 0.01 in the agent framework.
#random.random generates values between 0 and 1:    
    if random.random() < 0.01:
        carry_on = False
        print("Stopping condition met: the sheep weren't very hungry.")

        
#If the random.random stopping condition is not met, the animation will continue
#until the specified number of frames is reached, at which point carry_on will become False.
#The number of frames for the animation depends on the maximum value specified for
# "a" in "gen_function" below, in this case 50. "a" gains a value of +1 for every frame displayed,
#until it reaches 50. This number can be changed if necessary.
def gen_function(b = [0]):
    a = 0
    global carry_on 
    while (a < 50) & (carry_on) :
        yield a			
        a = a + 1
        
        #Printing to the console when the animation begins:
        if a == 1:
            print("The sheep start eating...")
            
        #Printing to the console if full model animation is completed:
        #This value must match the value for "a" in "gen_function" above.
        if a == 50:
            print("The sheep are full.")
            print ("Animation complete.")
            
#calling and displaying the animation:
#if repeat=True, the animation will continue regardless of the frame number, unless the alternate stopping condition is met.
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
matplotlib.pyplot.show()


#stops the timer after all the code has been read, prints time to the console:
end=time.process_time()
print("processing time = "+str(end-start))