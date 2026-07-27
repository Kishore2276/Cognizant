import { defineStore } from 'pinia'
import { enrollStudent } from '../api/courseApi'

export const useEnrollmentStore = defineStore('enrollment', {
  state: () => ({
    enrolledCourses: []
  }),

  actions: {
    enroll(course) {
      this.enrolledCourses.push(course)
    },

    async fetchAndEnroll(course) {
      try {
        await enrollStudent(1, course.id)
        this.enrolledCourses.push(course)
      } catch (error) {
        console.error(error.message)
      }
    },

    $reset() {
      this.enrolledCourses = []
    }
  }
})