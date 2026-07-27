<template>
  <h2>Courses</h2>

  <label for="search">Search Course</label>

  <input
    id="search"
    type="text"
    placeholder="Search Course"
    v-model="searchTerm"
  />

  <p role="status" aria-live="polite">
    {{ filteredCourses.length }} courses found
  </p>

  <div
    v-for="course in filteredCourses"
    :key="course.id"
    class="course-card"
    tabindex="0"
    @keydown.enter="store.fetchAndEnroll(course)"
  >
    <CourseCard
      :name="course.name"
      :code="course.code"
      :credits="course.credits"
      :grade="course.grade"
    />

    <button @click="store.fetchAndEnroll(course)">
  Enroll
</button>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import CourseCard from '../components/CourseCard.vue'
import { useEnrollmentStore } from '../stores/enrollment'
import { getAllCourses } from '../api/courseApi'

const store = useEnrollmentStore()
import { storeToRefs } from 'pinia'

const { enrolledCourses } = storeToRefs(store)

const searchTerm = ref('')
const courses = ref([])

onMounted(async () => {
  try {
    const data = await getAllCourses()

    courses.value = data.slice(0, 5).map(post => ({
      id: post.id,
      name: post.title,
      code: `CRS${post.id}`,
      credits: 3,
      grade: 'A'
    }))
  } catch (error) {
    console.error(error.message)
  }
})

const filteredCourses = computed(() =>
  courses.value.filter(course =>
    course.name.toLowerCase().includes(searchTerm.value.toLowerCase())
  )
)
</script>