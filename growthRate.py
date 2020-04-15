import matplotlib.pyplot as plt
import numpy as np

def showGraph():
	x0 = 1.565
	b = 1.1194
	x = np.arange(1,100,0.01)
	y = [x0 * b**i for i in x]
	plt.plot(x,y,"b--2") 
	plt.grid(which="major")
	plt.ylabel("Number of cases")
	plt.xlabel("Time (days)")
	plt.title("Predicted Growth Rate of CoVID-19 Virus in the USA")
	plt.show()

if __name__ == "__main__":
	showGraph()