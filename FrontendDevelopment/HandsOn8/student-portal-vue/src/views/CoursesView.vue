import { useEnrollmentStore } from '../stores/enrollment'

const store = useEnrollmentStore()

<template>

<h2>Courses</h2>

<input
placeholder="Search Course"
v-model="searchTerm">

<div
  v-for="course in filteredCourses"
  :key="course.id"
>

  <CourseCard
    :name="course.name"
    :code="course.code"
    :credits="course.credits"
    :grade="course.grade"
  />

  <button @click="store.enroll(course)">
    Enroll
  </button>

</div>

</template>

<script setup>

import { ref, computed, onMounted } from 'vue'
import CourseCard from '../components/CourseCard.vue'

const searchTerm = ref('')

const courses = ref([])

onMounted(() => {

courses.value = [

{ id:1,name:'Vue Basics',code:'VUE101',credits:3,grade:'A' },

{ id:2,name:'Java',code:'JAVA201',credits:4,grade:'A+' },

{ id:3,name:'Python',code:'PY301',credits:3,grade:'A' },

{ id:4,name:'Database',code:'DB401',credits:4,grade:'B+' },

{ id:5,name:'Angular',code:'ANG501',credits:3,grade:'A' }

]

})

const filteredCourses = computed(() =>
courses.value.filter(course =>
course.name.toLowerCase().includes(searchTerm.value.toLowerCase())
)
)

</script>