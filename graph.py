import matplotlib.pyplot as plt
import numpy as np


def generate_graph(resultsArray):
    yValues = np.array(resultsArray)
    valuesLength = len(yValues)
    xValues = np.array(range(0, len(yValues)))

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot the data
    ax.plot(xValues, yValues)

    # Set labels and title

    ax.set_ylabel("current rating")
    ax.set_xlabel("time (seconds)")

    """
    every5minsticks = np.array(range(0, valuesLength, 300))
    every5minslabels = np.array([x*5 for x in range(0,len(every5minsticks))])
    
    every10secsticks = np.array(range(0,valuesLength, 10)
    every10secslabels = np.array([x*10 for x in range(0, len(every10secslabels))])
    
    if(len(yValues)>=every5minsticks):
        ax.set_xlabel("time (mins)")
        ax.set_xticks(ticks=every5minsticks, labels=every5minslabels)

    else:
        ax.set_xlabel("time (seconds)")
        ax.set_xticks(ticks=every10secsticks, labels=every5minslabels)
    """

    ax.set_yticks(ticks= np.array(range(0,101,10)),labels = np.array(range(0,101, 10)))
    #ax.set_xticks(ticks=np.array([x*300 for x in (range(0, 3,600, 300))]), labels=np.array(range(0, 60, 5)))


    # Save the figure to a file
    plt.savefig('./templates/graph.png')
    plt.close()

