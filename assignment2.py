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
    
    #make sum from original data 
    species_sum = np.sum(data[:, 1:], axis=1)
    
    #create ne_data as a copy
    new_data = data.copy()
    
    #modify carrot population below 40000 to 0
    new_data[new_data[:, 3] < 40000, 3] = 0
    
    #append original sum column
    new_data = np.column_stack((data, species_sum))
    
    #return results
    return data, hare, min_year_hare, lynx_avg, new_data
