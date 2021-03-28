/*Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.*/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

 //Brute force solution, use two for-loops to iterate the array 
var twoSum = function(nums, target) {
    for(var i=0; i<nums.length; i++){
        for(var j=i+1; j<nums.length; j++){
            if(nums[i]+nums[j] == target)
            return [i,j];
        }
    }
    return null;
};

//Hashmap solution 
var twoSum = function(nums, target) {
    
    var i, comp;
    var map = new Map();
    
    for(i=0; i<nums.length; i++){
        comp = target - nums[i];
        if(map.has(comp)){ //check to see if the map contains the compliment, if it does return the two indices
            return [map.get(comp), i];
        }

        map.set(nums[i],i); //add the value the map
    }
    
    return null;
};

