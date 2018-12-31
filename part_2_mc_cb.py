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

for dimensions in range(1,100):
    print ("For Dimension"+str(dimensions))
    N=1000000
    print("Taking N Value 1000000")
    print("calculating Montecarlo volume")
    monte_carlo_volume=nSphereVolume_Monte_carloVolume(dimensions,N)
    print("Volume using montecarlo"+str(monte_carlo_volume))
    k=math.pow(N,1/dimensions)
    k=math.ceil(k)
    print("k cubes"+str(k))
    cube_based_vol=nSphereVolume_cubebased(dimensions,k)
    print("volume using cube based"+str(cube_based_vol))
    
    if(monte_carlo_volume==0 or isAnyElementZero(cube_based_vol)):
        break


