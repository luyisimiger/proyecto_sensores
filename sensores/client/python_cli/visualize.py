
def matplotlib_demo():
    # Import the necessary packages and modules
    import matplotlib.pyplot as plt
    import numpy as np

    # Prepare the data
    x = np.linspace(0, 10, 100)

    # Plot the data
    plt.plot(x, x, label='linear')

    # Add a legend
    plt.legend()

    # Show the plot
    plt.show()

def matplotlib_demo2():
    import numpy as np
    import matplotlib.pyplot as plt

    plt.axis([0, 10, 0, 1])

    for i in range(10):
        y = np.random.random()
        plt.scatter(i, y)
        plt.pause(0.1)

    plt.show()

def matplotlib_demo3():
    import pylab
    import time
    import random
    import matplotlib.pyplot as plt

    dat=[0,1]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    Ln, = ax.plot(dat)
    ax.set_xlim([0,20])
    plt.ion()
    plt.show()    
    for i in range (180):
        dat.append(random.uniform(0,1))
        Ln.set_ydata(dat)
        Ln.set_xdata(range(len(dat)))
        plt.pause(0.3)

        print('done with loop')


def pandas_demo():
    import pandas as pd
    iris = pd.read_csv('iris.data', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
    print(iris.head())

if __name__ == "__main__":

    # matplotlib_demo()
    # matplotlib_demo2()
    matplotlib_demo3()
    # pandas_demo()
