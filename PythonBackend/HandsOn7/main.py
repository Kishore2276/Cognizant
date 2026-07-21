from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from schemas import (
    CourseCreate,
    CourseUpdate,
    CourseResponse,
    StudentCreate,
    StudentUpdate,
    StudentResponse,
    EnrollmentCreate,
    EnrollmentResponse
)
from typing import Optional

app = FastAPI(
    title="Course Management API",
    version="1.0"
)

courses = {
    1: {
        "id": 1,
        "name": "Python",
        "code": "CS101",
        "credits": 4,
        "department_id": 1
    }
}

@app.get("/")
async def root():
    return {"message": "API running"}

@app.post(
    "/api/courses/",
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_course(
    course: CourseCreate,
    db: AsyncSession = Depends(get_db)
):
    new_id = len(courses) + 1

    new_course = {
        "id": new_id,
        **course.model_dump()
    }

    courses[new_id] = new_course

    return new_course

@app.get(
    "/api/courses/{course_id}",
    response_model=CourseResponse
)
async def get_course(course_id: int):

    if course_id not in courses:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return courses[course_id]

@app.get("/api/courses/")
async def get_courses(
    skip: int = 0,
    limit: int = 10,
    department_id: Optional[int] = None,
    db: AsyncSession = Depends(get_db)
):
    return {
    "skip": skip,
    "limit": limit,
    "department_id": department_id,
    "message": "Pagination works"
}

@app.put(
    "/api/courses/{course_id}",
    response_model=CourseResponse
)
async def update_course(
    course_id: int,
    course: CourseUpdate
):

    if course_id not in courses:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    old = courses[course_id]

    update = course.model_dump(exclude_unset=True)

    old.update(update)

    courses[course_id] = old

    return old


@app.delete(
    "/api/courses/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_course(course_id: int):

    if course_id not in courses:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    del courses[course_id]


@app.get("/api/courses/{course_id}/students")
async def get_course_students(course_id: int):

    if course_id not in courses:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return {
        "course_id": course_id,
        "students": [
            {
                "id": 1,
                "name": "John"
            },
            {
                "id": 2,
                "name": "Alice"
            }
        ]
    }