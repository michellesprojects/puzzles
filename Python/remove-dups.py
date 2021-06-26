'''
Remove Duplicates

alter a sorted input list with all duplicates moved to the end of the list.

The return value will be the index of the final unique value. '''

# remove duplicates 
# constant space
# return index of last unique element

def move_duplicates(dupe_list):
  index = 0

  #move through all values
  for i in range(0, len(dupe_list)-1):

    #set j to value after i
    j = i+1

    #if the values are not equal, replace i with the unique value 
    if(dupe_list[i] != dupe_list[j]):
      dupe_list[i] = dupe_list[j]
      index +=1
    print(dupe_list)

  return index

      

#### TESTS SHOULD ALL BE TRUE ####
print("{0}\n should equal \n{1}\n {2}\n".format(move_duplicates(['a', 'a', 'g', 't', 't', 'x', 'x', 'x']), 3, move_duplicates(['a', 'a', 'g', 't', 't', 'x', 'x', 'x']) == 3))

print("{0}\n should equal \n{1}\n {2}\n".format(move_duplicates(['a', 'a', 'c', 'c', 'd', 'd', 'e', 'e', 'f']), 4, move_duplicates(['a', 'a', 'c', 'c', 'd', 'd', 'e', 'e', 'f']) == 4))

print("{0}\n should equal \n{1}\n {2}\n".format(move_duplicates([13, 13, 13, 13, 13, 42]), 1, move_duplicates([13, 13, 13, 13, 13, 42]) == 1))
