import { courses } from "./data.js";

const courseGrid = document.querySelector(".course-grid");
const totalCredits = document.querySelector("#total-credits");
const searchBox = document.querySelector("#search-courses");
const sortBtn = document.querySelector("#sort-btn");
const selectedCourse = document.querySelector("#selected-course");

let displayedCourses = [...courses];

// Render Function
function renderCourses(courseList){

    courseGrid.innerHTML = "";

    courseList.forEach(course=>{

        const article=document.createElement("article");

        article.className="course-card";

        article.dataset.id=course.id;

        article.innerHTML=`
            <h3>${course.name}</h3>
            <p><strong>Code:</strong> ${course.code}</p>
            <p><strong>Credits:</strong> ${course.credits}</p>
        `;

        courseGrid.appendChild(article);

    });

    const total=courseList.reduce(
        (sum,course)=>sum+course.credits,
        0
    );

    totalCredits.textContent=`Total Credits : ${total}`;
}

// Initial Render
renderCourses(displayedCourses);

// Search
searchBox.addEventListener("input",()=>{

    const keyword=searchBox.value.toLowerCase();

    displayedCourses=courses.filter(course=>
        course.name.toLowerCase().includes(keyword)
    );

    renderCourses(displayedCourses);

});

// Sort
sortBtn.addEventListener("click",()=>{

    displayedCourses.sort(
        (a,b)=>b.credits-a.credits
    );

    renderCourses(displayedCourses);

});

// Event Delegation
courseGrid.addEventListener("click",(event)=>{

    const card=event.target.closest(".course-card");

    if(!card) return;

    const id=parseInt(card.dataset.id);

    const course=displayedCourses.find(c=>c.id===id);

    selectedCourse.textContent=
        `Selected Course: ${course.name} | Grade: ${course.grade}`;

});