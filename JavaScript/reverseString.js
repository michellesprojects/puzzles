
/*Write a function that reverses a string. The input string is given as an array of characters s.
*/


/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */

//This solutions defines and returns a newString variable containing the reversed string
var reverseString = function(s) {
    let newString = "";
     for (let i = s.length - 1; i >= 0; i--) { 
         newString += s[i];
     }
     return newString; // "olleh"
 };

 //This solution uses a JS built-in method
var reverseString = function(s){
    return s.reverse();
}

//This solution reverses the string in place
var reverseString = function(s) {
    let i = 0, j = s.length-1
      while(i <= j){
          let temp = s[i]
          s[i++] = s[j]
          s[j--] = temp
      }
  }
  
 