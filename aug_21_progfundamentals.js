// Given an array of strings and an integer k, 
// your task is to return the longest string consisting of k consecutive strings from the array concatenated together.

// loop through my list
    // length i, length i + 1, length i + 2 (will give group of and the length of their group)
// find the length of characters per strings in group of 3 

function longestConsecutive(array, k) {
    let combos = [] 
    for (i = 0; i < array.length; i++) {
        let count = array.slice(i, i+k); 
        combos.push(count.join('')); 
        // let count = array[i].length + array[i+1].length 
        
    }
    // console.log(combos); 
    let sorted = combos.sort( function(a, b) {
      return  a.length - b.length 
    })
    console.log(sorted.pop());
}; 



longestConsecutive(['hi', 'marbles', 'mittens', 'bye', 'lorem', 'ipsum', 'to', 'a', 'hippocampus'], 3); // -> 'marblesmittensbye'

// longestConsecutive(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2); // --> "abigailtheta"

//  next steps : firgure out how to refactor code with any built in JS functions 

// OTHER WAYS TO SOLVE: 

/*
function longestConsecutive(array, k) {
    let newStr = ""; 
    for (i = 0; i < array.length; i++) {
        let tempStr = array.slice(i, i+k).join("");
            if(newStr.length < tempStr.length)
                newStr = tempStr; 
             };   
    return newStr;  
}; 

*/

// using forEach() 
/*
refactor the for loop: 

getLongestString(array, k){
    let longestStr = ""; 
    arr.forEach( (str, index, array) 
        => { let currentStr =  arr.slice(i, i+k).join("");   //- replaces comma with nothing to concatenate the string - 
            
            if (currentStr.length > longestStr.length) {
                longestStr = currentStr
            }     
            return longestStr 
    })


    )
}
*/