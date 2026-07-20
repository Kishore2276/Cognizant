from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from schemas import CourseCreate
from typing import Optional

app = FastAPI(
    title="Course Management API",
    version="1.0"
)

@app.get("/")
async def root():
    return {"message": "API running"}

@app.post("/api/courses/")
async def create_course(
    course: CourseCreate,
    db: AsyncSession = Depends(get_db)
):
    return {
        "message": "Async Course Created",
        "course": course
    }

@app.get("/api/courses/{course_id}")
async def get_course(course_id: int):
    return {
        "course_id": course_id,
        "message": "Course Found"
    }

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