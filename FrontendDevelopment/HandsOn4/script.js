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

// ==========================================
// TASK 2
// Reusable Fetch Function
// ==========================================

async function apiFetch(url){

    const response = await fetch(url);

    if(!response.ok){
        throw new Error("Unable to load notifications.");
    }

    return await response.json();

}



// ==========================================
// Load Notifications
// ==========================================

async function loadNotifications(){

    const loading=document.getElementById("loadingPosts");
    const container=document.getElementById("notifications");
    const error=document.getElementById("errorMessage");

    loading.innerText="Loading notifications...";
    container.innerHTML="";
    error.innerHTML="";

    try{

        const posts=await apiFetch("https://jsonplaceholder.typicode.com/posts");

        loading.innerText="";

        posts.slice(0,6).forEach(post=>{

            container.innerHTML+=`
            <div class="notification-card">
                <h3>${post.title}</h3>
                <p>${post.body}</p>
            </div>
            `;

        });

    }

    catch(err){

        loading.innerText="";

        error.innerHTML=`
        ${err.message}
        <br><br>
        <button onclick="loadNotifications()">Retry</button>
        `;

    }

}

loadNotifications();

// ===================================================
// TASK 3 - Introduction to Axios
// ===================================================

// Axios Request Interceptor
axios.interceptors.request.use(function (config) {

    console.log("API call started:", config.url);

    return config;

});

// Reusable Axios Fetch Function
async function apiFetchAxios(url) {

    const response = await axios.get(url);

    return response.data;

}

// Load Posts for User ID = 1
async function loadUserPostsAxios() {

    try {

        const posts = await axios.get(
            "https://jsonplaceholder.typicode.com/posts",
            {
                params: {
                    userId: 1
                }
            }
        );

        console.log("Axios User 1 Posts:");

        posts.data.forEach(post => {
            console.log(post.title);
        });

    }
    catch (error) {

        console.log("Axios Error:", error.message);

    }

}

loadUserPostsAxios();



/*
========================================================
Fetch vs Axios

1. Fetch requires response.json(); Axios automatically parses JSON.

2. Fetch does not throw errors for HTTP 404/500.
   Axios throws errors automatically for non-2xx responses.

3. Fetch is built into browsers.
   Axios is an external library with interceptors, timeout,
   request cancellation and many additional features.
========================================================
*/