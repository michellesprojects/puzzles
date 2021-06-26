'''
Rotation point: Linear Search

given a sorted list rotated k times, return the index where the “unrotated” list would begin.

rotated_list = ['c', 'd', 'e', 'f', 'a']
rotation_point(rotated_list)
# index 4
# a sorted list would start with 'a'
 
another_rotated_list = [13, 8, 9, 10, 11] 
rotation_point(rotated_list)
# index 1
# a sorted list would start with 8
'''

def rotation_point(rotated_list):
  smallest = rotated_list[0]
  index = 0
  for i in range(1,len(rotated_list)):

    if(rotated_list[i] < smallest):
      
      smallest = rotated_list[i]
      index = i
      return index #We can return immediately after finding a value smaller than arr[0], because the input was a sorted rotated list  

  return 0
