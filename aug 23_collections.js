const tasks = 
["laundry", 
"shovel driveway", 
"grocery shopping", 
"check email", 
"daydream",
"phone parents", 
"fill prescription", 
"exercise", 
"take out recycling", 
"check the weather"];

let sundayList = function() {
    console.log("Sunday To Do List:");
    for(let i = 0; i < tasks.length; i++) {
    console.log(`${i+1}: ${tasks[i]}`);
    }; 
}; 
