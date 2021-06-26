'''
List Rotation: Slice

We would like to “rotate” a list, or **move elements forward** in a list by a number of spaces, `k`.
'''







#This solution continiously removes the last element of the list and inserts it at the front, repeated num_rotations (adjusted) times
def rotate(my_list, num_rotations):
	#Get the net number of rotations, in num is greater than size of list to prevent repeating operations
	num_rotations %= len(my_list)

  for i in range(0,num_rotations):

    #remove last eleemnt
    #push it to front
    my_list.insert(0,my_list.pop())
    #print(my_list)
  
  return my_list

# This next solution does not use any Python insert() which is an O(n) operation
# Instead it uses a swap function 3 times
# rotate list
# Constant space requirement
# return input list "rotated"

'''
Below is an example of this function on rotate(['a', 'b', 'c', 'd', 'e', 'f'], 2)
# <> marks selected elements
 
# 2 rotations
['a', 'b', 'c', 'd', 'e', 'f'] 
 
# reverse first 2
[<'b', 'a',> 'c', 'd' ,'e', 'f'] 
 
# reverse all but first 2
['b', 'a', <'f', 'e', 'd', 'c'>] 
 
# reverse all
[<'c', 'd', 'e', 'f', 'a', 'b'>] 
 
# all done!
['c', 'd', 'e', 'f', 'a', 'b']
'''

def rev(lst, low, high):
  while low < high:
    lst[low], lst[high] = lst[high], lst[low]
    high -= 1
    low += 1
  return lst
 
def rotate2(my_list, num_rotations):
	
  num_rotations %= len(my_list) #net number of rotations

  my_list = rev(my_list,0,num_rotations-1) #rotate [0,num-1]
  
  my_list = rev(my_list, num_rotations, len(my_list)-1) #rotate [num, end]
  
  return rev(my_list, 0, len(my_list)-1) #rotate all 
