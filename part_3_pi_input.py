import numpy as np
import time
import statistics
import math
import itertools

def nSphereVolume_Monte_carloVolume(dim, N):
           start_time = time.time()
           count_in_sphere = 0

           for i in range(N):

                      point = np.random.uniform(-1.0, 1.0, dim)

                      dist = np.linalg.norm(point)

                      if isWithinSphere(dist):

                                 count_in_sphere = count_in_sphere + 1

           volume = (count_in_sphere/N)*(2**dim)
           print("--- %s seconds for Montecarlo ---" % (time.time() - start_time))
           return volume





def nSphereVolume_cubebased(dim, K):
           start_time=time.time()
           n_list = []

           n = 1

           while n <= int(K/2):

                      n_list.append(n)

                      n = n + 1



           dist_list = [2/K] * dim

           total = 0

           middle_bound = 0

           lower_bound = 0
           i=0           
           while( i< math.pow(2,dim)):
               i=i+1
               for j in itertools.product(n_list, repeat=dim):

                    total = total + 1
 
                    inner_list = [x-1 for x in j]

                    if np.linalg.norm([j*dist_list for j,dist_list in zip(j,dist_list)]) < 1:

                                 lower_bound = lower_bound + 1



                    else:

                                 if np.linalg.norm([inner_list*dist_list for inner_list,dist_list in zip(inner_list,dist_list)]) < 1:

                                            middle_bound = middle_bound + 1





           print(lower_bound)

           print(middle_bound)

           print(total)



           upper_bound_volume = (lower_bound + middle_bound)*(2**dim)/total

           lower_bound_volume = lower_bound*(2**dim)/total
           
           print("--- %s seconds for Cubebased ---" % (time.time() - start_time))
    
           return (lower_bound_volume, upper_bound_volume)


def isWithinSphere( d):
    if d <= 1:
       return True
    return False

def isAnyElementZero(list_of_volumes):
    if(list_of_volumes[0]==0 or list_of_volumes[1]==0):
        return True
    return False

#N = [1000,10000,100000,1000000]
n = int(input("Enter N: "))
for dimensions in range(1,9):
    print ("For Dimension"+str(dimensions))
    
    print("Taking N Value: " + str(n))
    print("calculating Montecarlo Pi")
    monte_carlo_volume=nSphereVolume_Monte_carloVolume(dimensions,n)
    mc_pi = math.pow(monte_carlo_volume*math.gamma(dimensions/2 + 1),2/dimensions)
    print("Pi using montecarlo: "+str(mc_pi))
    k=math.pow(n,1/dimensions)
    k=math.ceil(k)
    print("calculating Cube Based Pi")
    print("k"+str(k))
    cube_based_vol=nSphereVolume_cubebased(dimensions,k)
    cb_vol = statistics.mean(cube_based_vol)
    cb_pi = math.pow(cb_vol*math.gamma(dimensions/2 + 1),2/dimensions)
    print("Pi using cube based: "+str(cb_pi))
    print()
    if(monte_carlo_volume==0 or isAnyElementZero(cube_based_vol)):
        break
