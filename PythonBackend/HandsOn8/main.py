from fastapi import FastAPI, Depends, HTTPException, status, Response
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

# API Versioning
# URL Versioning (used here): /api/v1/courses
# Alternative:
# Header Versioning:
# Accept: application/vnd.api+json;version=1

@app.get("/")
async def root():
    return {"message": "API running"}

@app.post(
    "/api/v1/courses/",
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_course(
    response: Response,
    course: CourseCreate,
    db: AsyncSession = Depends(get_db)
):
    new_id = len(courses) + 1

    new_course = {
        "id": new_id,
        **course.model_dump()
    }

    courses[new_id] = new_course

    response.headers["Location"] = f"/api/v1/courses/{new_id}"

    return new_course

@app.get(
    "/api/v1/courses/{course_id}",
    response_model=CourseResponse
)
async def get_course(course_id: int):

    if course_id not in courses:
        raise HTTPException(
    status_code=404,
    detail={
        "error": {
            "code": "NOT_FOUND",
            "message": f"Course with id {course_id} does not exist",
            "field": None
        }
    }
)

    return courses[course_id]

@app.get("/api/v1/courses/")
async def get_courses(
    page: int = 1,
    page_size: int = 2,
    search: Optional[str] = None
):

    course_list = list(courses.values())

    if search:
        search = search.lower()

        course_list = [
            c for c in course_list
            if search in c["name"].lower()
            or search in c["code"].lower()
        ]

    total = len(course_list)

    start = (page - 1) * page_size
    end = start + page_size

    results = course_list[start:end]

    next_page = (
        f"/api/v1/courses/?page={page+1}&page_size={page_size}"
        if end < total
        else None
    )

    previous_page = (
        f"/api/v1/courses/?page={page-1}&page_size={page_size}"
        if page > 1
        else None
    )

    return {
        "count": total,
        "next": next_page,
        "previous": previous_page,
        "results": results
    }

@app.put(
    "/api/v1/courses/{course_id}",
    response_model=CourseResponse
)
async def update_course(
    course_id: int,
    course: CourseCreate
):

    if course_id not in courses:
        raise HTTPException(
    status_code=404,
    detail={
        "error": {
            "code": "NOT_FOUND",
            "message": f"Course with id {course_id} does not exist",
            "field": None
        }
    }
)

    updated_course = {
        "id": course_id,
        **course.model_dump()
    }

    courses[course_id] = updated_course

    return updated_course


@app.delete(
    "/api/v1/courses/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_course(course_id: int):

    if course_id not in courses:
        raise HTTPException(
    status_code=404,
    detail={
        "error": {
            "code": "NOT_FOUND",
            "message": f"Course with id {course_id} does not exist",
            "field": None
        }
    }
)

    del courses[course_id]


@app.get("/api/v1/courses/{course_id}/students")
async def get_course_students(course_id: int):

    if course_id not in courses:
        raise HTTPException(
    status_code=404,
    detail={
        "error": {
            "code": "NOT_FOUND",
            "message": f"Course with id {course_id} does not exist",
            "field": None
        }
    }
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

@app.patch(
    "/api/v1/courses/{course_id}",
    response_model=CourseResponse
)
async def patch_course(
    course_id: int,
    course: CourseUpdate
):

    if course_id not in courses:
        raise HTTPException(
    status_code=404,
    detail={
        "error": {
            "code": "NOT_FOUND",
            "message": f"Course with id {course_id} does not exist",
            "field": None
        }
    }
)

    update_data = course.model_dump(exclude_unset=True)

    courses[course_id].update(update_data)

    return courses[course_id]