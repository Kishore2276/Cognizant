import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { CourseCardComponent } from '../course-card/course-card';
import { CourseService } from '../services/course';

@Component({
  selector: 'app-course-list',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    CourseCardComponent
  ],
  templateUrl: './course-list.html',
  styleUrl: './course-list.css'
})
export class CourseListComponent implements OnInit {

  searchTerm = '';

  courses: any[] = [];

  loading = true;

  constructor(private courseService: CourseService) {}

  ngOnInit(): void {

  this.loading = false;

  this.courses = [
    {
      name: 'Angular Test',
      code: 'TEST101',
      credits: 3,
      grade: 'A'
    }
  ];

}

  get filteredCourses() {
    return this.courses.filter(course =>
      course.name.toLowerCase().includes(this.searchTerm.toLowerCase())
    );
  }

}