import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

star = pd.read_csv('https://github.com/YBIFoundation/Dataset/raw/main/Stars.csv')
temp = star["Temperature (K)"]
#brightness = star["Luminosity (L/Lo)"]
#radius = star["Radius (R/Ro)"]
absmag = star["Absolute magnitude (Mv)"]
graph = pd.concat([absmag, temp], axis=1)

def main():
    graph.to_csv('Star_Data.txt', sep='\t', index=False)
    plt.plot('Absolute magnitude (Mv)', 'Temperature (K)', data=graph, linestyle='none', marker='o')
    plt.xlabel('Absolute Magnitude (Mv)')
    plt.ylabel('Temperature (K)')
    plt.title('Temperature(K) of a Star Compared to Absolute Magnitude(Mv)')
    plt.savefig('Star_Scatter_Plot.pdf')
    plt.show()
    #print(graph.head())
    
    
if __name__ == "__main__":
    main()
    #end script
    exit