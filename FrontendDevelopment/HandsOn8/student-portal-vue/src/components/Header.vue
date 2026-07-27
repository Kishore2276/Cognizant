<template>

<nav>

<RouterLink to="/">Home</RouterLink>

|

<RouterLink to="/courses">Courses</RouterLink>

|

<RouterLink to="/profile">Profile</RouterLink>

|

<b>Enrolled:</b> {{ store.enrolledCourses.length }}

</nav>

<hr>

</template>

<script setup>

import { RouterLink } from 'vue-router'
import { useEnrollmentStore } from '../stores/enrollment'

Enrolled: {{ store.enrolledCourses.length }}

const store = useEnrollmentStore()

</script>