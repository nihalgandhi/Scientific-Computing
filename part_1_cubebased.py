import numpy as np

import itertools
import time
def check_cube_inside(dist):
  if dist < 1:
    return True
  return False 

def nSphereVolume(dim, K):
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

           for j in itertools.product(n_list, repeat=dim):

                      total = total + 1

                      inner_list = [x-1 for x in j]

                      dist_out=np.linalg.norm([j*dist_list for j,dist_list in zip(j,list(dist_list))])

                      
                      if check_cube_inside(dist_out):

                                 lower_bound = lower_bound + 1
                                 

 

                      else:

                                 if np.linalg.norm([inner_list*dist_list for inner_list,dist_list in zip(inner_list,dist_list)]) < 1:

                                            middle_bound = middle_bound + 1

                     

 
           print("Lower bound cubes:")
           print(lower_bound)
           print("Middle bound cubes:")
           print(middle_bound)
           print("Total Number of cubes:")
           print(total)

 

           upper_bound_volume = (lower_bound + middle_bound)*(2**dim)/total

           lower_bound_volume = lower_bound*(2**dim)/total
           
           return (lower_bound_volume, upper_bound_volume)

 

def calculateIdealK():
    start_time=time.time()
    dimensions=int(input("Enter dimensions D"))
    k=1000 ##Starting from k=1000
    while( k< 100000):
     
    
        list_of_volumes=nSphereVolume(dimensions,k)
        print("Lower and Upperbound volumes")
        print(list_of_volumes)
        diff_volumes=list_of_volumes[1]-list_of_volumes[0]
        print("Difference between upper and lower bound"+str(diff_volumes))
        ##Precision check
        if((list_of_volumes[1]-list_of_volumes[0])/np.mean(list_of_volumes) <=.0001):
             print(k)
             print("--- %s seconds for Cubebased ---" % (time.time() - start_time))
             break
        else:
            k=k+1000
 

          
calculateIdealK()

