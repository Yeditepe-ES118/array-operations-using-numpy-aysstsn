import numpy as np

def stat(): 
    #load the data
    
    data = np.loadtxt("populations.txt")
    
    #extract hare population
    
    hare = data[:, 1]
    
    #year of minimum hare population
    
    min_index = np.argmin(hare)
    min_year_hare = data[min_index, 0]
    
    #lynx population average
    
    lynx = data[:, 2]
    lynx_avg = np.mean(lynx)
    
    #make new_data by adding sum of species
    
    species_sum = np.sum(data[:, 1:], axis=1)
    new_data = np.column_stack((data, species_sum))
    
    #modify carrot population below 4000 to 0
    
    new_data[new_data[:, 3] < 4000, 3] = 0
    
    
    #return results
    
    return data, hare, min_year_hare, lynx_avg, new_data
