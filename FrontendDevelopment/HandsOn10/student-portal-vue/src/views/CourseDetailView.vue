<template>

<h2>Course Detail</h2>

<p>Course ID : {{ route.params.id }}</p>

<button @click="enroll">
Enroll
</button>

</template>

<script setup>

import { useRoute,useRouter } from 'vue-router'

const route=useRoute()

const router=useRouter()

function enroll(){

router.push('/profile')

}

</script>