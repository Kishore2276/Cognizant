<template>

<h2>Enrolled Courses</h2>

<ul>

<li
v-for="course in store.enrolledCourses"
:key="course.id">

{{ course.name }}

</li>

</ul>

<h3>Total Credits: {{ store.totalCredits }}</h3>

</template>

<script setup>

import { useEnrollmentStore } from '../stores/enrollment'

const store = useEnrollmentStore()

</script>