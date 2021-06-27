'''
Capturing Rain Water:

A histogram is a chart which consists of a series of bars. A Python list can represent a histogram by containing integers, each of which represents the height of a single bar.
For our problem, imagine that rainwater has fallen over the histogram and collected between the bars.
We need to write a function which calculates the total water captured from an input of a list of integers.

'''

####### TEST INPUTS HERE

small = [1,0,1]
medium = [4,2,1,3,0,1,2]
edge_case = [0,2,0]

####### NAIVE SOLUTION HERE

def rain_water(histogram):

    total_water = 0 

    #loop through all values except left-most and right-most
    for i in range(1, len(histogram)-1):

      #left_max value relative to i
      left_max = histogram[0]

      #right_max relative to i
      right_max = histogram[len(histogram)-1]

      #search all values left of i for the max
      for left in range(0, i):
        
        #update left_max variable
        if(histogram[left] > left_max):
          left_max = histogram[left]

      #search all values right of i for max
      for right in range(i+1, len(histogram)-1):
        
        #update right_max value
        if(histogram[right] > right_max):
          right_max = histogram[right]

      #fill mark is the second largest or the two max's. This is the limit to how high the water can fill, subtract it from value at i to get fill amount
      fill_mark = min(right_max,left_max) - histogram[i]

      #make sure fill mark is not negative
      if(fill_mark > 0):
        total_water += fill_mark

    return total_water



####### OPTIMIZED SOLUTION HERE
def optmized_rain_water(histogram):

    #return value
    total_water = 0 

    
    left_maxes = []
    right_maxes = []
    
    left_max = histogram[0]

    #loop through all values and get the max left value relative to i, append it to left_maxes
    for i in range(0, len(histogram)):

      if(histogram[i] > left_max):
        left_max = histogram[i]

      left_maxes.append(left_max)
  
    right_max = histogram[-1]

    #loop through all values and get the max right value relative to i, append it to right_maxes
    for i in range(len(histogram)-1,-1 ,-1):
      if(histogram[i] > right_max):
        right_max = histogram[i]
      right_maxes.append(right_max)

    #reverse right_maxes so indices align with left_maxes
    right_maxes.reverse()
  
    #loop through values, find 2nd largest of two maxes and add the remainer of it - value at i to total_water
    for i in range(1, len(histogram)-1):
      val = min(right_maxes[i],left_maxes[i]);
      total_water += val - histogram[i]

    return total_water

####### BENCHMARKING HERE
print(optmized_rain_water(small))
print(optmized_rain_water(medium))
print(optmized_rain_water(edge_case))
