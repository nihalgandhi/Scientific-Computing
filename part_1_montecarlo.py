






import numpy as np
import time
import statistics

 

def nSphereVolume(dim, N):
           
           count_in_sphere = 0

           for i in range(N):

                      point = np.random.uniform(-1.0, 1.0, dim)

                      dist = np.linalg.norm(point)

                      if isWithinSphere(dist):

                                 count_in_sphere = count_in_sphere + 1

           volume = (count_in_sphere/N)*(2**dim)
           ##print("--- %s seconds for Montecarlo ---" % (time.time() - start_time))
           return volume

def isWithinSphere( d):
    if d <= 1:
       return True
    return False

def runs(d, iterations):
           start_time = time.time()
           list = []

           runs = 0

           while runs < 100000:

                      value = nSphereVolume(d, iterations)

                      runs = runs + 1

                      list.append(value)

                      if runs <= 1:

                                 continue

                      mean = statistics.mean(list)

                      final_value = 4*statistics.stdev(list)/((runs**0.5)*statistics.mean(list))
                      print("Run number:")
                      print(runs)
                      
                      print("Calculated volume in this run:")

                      print(final_value)

                      if final_value < 0.0001:

                                 break

          
           print("--- %s seconds for Montecarlo Runs given these dimesnions---" % (time.time() - start_time))
           print(list)
           return statistics.mean(list)

 

 

dimension = int(input("Enter your dimension D ")) 
no_of_points = int(input("Enter the number of Random points N")) 
print("Final Calculated volume:")
print(runs(dimension,no_of_points))
