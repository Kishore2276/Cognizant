// -----------------------------------------
// Local Course Data
// -----------------------------------------

const courses = [
    {
        id:1,
        name:"HTML",
        duration:"4 Weeks"
    },
    {
        id:2,
        name:"CSS",
        duration:"5 Weeks"
    },
    {
        id:3,
        name:"JavaScript",
        duration:"6 Weeks"
    },
    {
        id:4,
        name:"React",
        duration:"8 Weeks"
    }
];


// =========================================
// STEP 45
// Promise Chaining
// =========================================

function fetchUser(id){

    return fetch(`https://jsonplaceholder.typicode.com/users/${id}`)
    .then(response => response.json())
    .then(user=>{
        console.log("Promise:",user.name);
        return user;
    });

}

fetchUser(1);


// =========================================
// STEP 46
// async/await + try catch
// =========================================

async function fetchUserAsync(id){

    try{

        const response = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`);

        const user = await response.json();

        console.log("Async/Await:",user.name);

    }
    catch(error){

        console.log(error);

    }

}

fetchUserAsync(2);


// =========================================
// STEP 47
// Simulate 1 second delay
// =========================================

function fetchAllCourses(){

    return new Promise(resolve=>{

        setTimeout(()=>{

            resolve(courses);

        },1000);

    });

}



// =========================================
// STEP 48
// Loading Message
// =========================================

async function displayCourses(){

    const loading=document.getElementById("loading");
    const courseContainer=document.getElementById("courses");

    loading.innerText="Loading courses...";

    const data=await fetchAllCourses();

    loading.innerText="";

    data.forEach(course=>{

        courseContainer.innerHTML+=`

        <div class="card">

            <h3>${course.name}</h3>

            <p>Duration : ${course.duration}</p>

        </div>

        `;

    });

}

displayCourses();



// =========================================
// STEP 49
// Promise.all()
// =========================================

Promise.all([
    fetch("https://jsonplaceholder.typicode.com/users/1").then(res=>res.json()),
    fetch("https://jsonplaceholder.typicode.com/users/2").then(res=>res.json())
])
.then(users=>{

    console.log("Promise.all():");

    users.forEach(user=>{

        console.log(user.name);

    });

});