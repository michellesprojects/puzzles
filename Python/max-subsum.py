'''
Max list sub-sum
Given a list of integers, return the maximum sum possible from a contiguous sub-list.
'''

# max sub sum
# no time/space requirements
# return maximum contiguous sum in list

def maximum_sub_sum(my_list):
  max = my_list[0]
  sum = my_list[0]
  
  for i in range(1,len(my_list)):
    
    #if the cur sum < max sum, restart the sum at the value of the current index
    if(sum < max):
      sum = my_list[i]
    else: #if cur sum >= max, add next index to the sum
      sum+=my_list[i]
    
    if(sum > max): #now that the sum has been changed in both conditional above, update the max value if sum is larger than it
      max = sum
    
  return max 




