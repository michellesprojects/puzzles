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
 
 
 # find rotation point 
# O(logN) time requirement
# return index of "rotation point" element

#using Binary Search to find the smallest element in the list
def rotation_point_Binary_Search(rotated_list):
  #inital low and high 
  low = 0
  high = len(rotated_list) - 1

  while(low <= high):

    mid = (low + high) // 2

    #using modulo to adjust indices for out-of-bounds
    mid_prev = (mid-1) % len(rotated_list)
    mid_next = (mid+1) % len(rotated_list)

    #if value at mid < both mid_prev and mid_next, it's the target
    if(rotated_list[mid] < rotated_list[mid_prev] and rotated_list[mid] < rotated_list[mid_next]):
      return mid
    
    #if left side of list is smaller, go left 
    if(rotated_list[mid] < rotated_list[high]):
      high = mid - 1 
    else: #if right side is smaller, go right
      low = mid + 1
