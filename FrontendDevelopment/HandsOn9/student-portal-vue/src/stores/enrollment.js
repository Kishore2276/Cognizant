import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useEnrollmentStore = defineStore('enrollment', () => {

  const enrolledCourses = ref([])

  const totalCredits = computed(() =>
    enrolledCourses.value.reduce((sum, course) => sum + course.credits, 0)
  )

  function enroll(course) {
    enrolledCourses.value.push(course)
  }

  function unenroll(course) {
    enrolledCourses.value =
      enrolledCourses.value.filter(c => c.id !== course.id)
  }

  return {
    enrolledCourses,
    totalCredits,
    enroll,
    unenroll
  }

})