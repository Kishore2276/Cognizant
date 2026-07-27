<template>
  <nav aria-label="Main navigation">
    <RouterLink to="/" custom v-slot="{ href, navigate, isActive }">
      <a
        :href="href"
        @click="navigate"
        :aria-current="isActive ? 'page' : null"
      >
        Home
      </a>
    </RouterLink>

    |

    <RouterLink to="/courses" custom v-slot="{ href, navigate, isActive }">
      <a
        :href="href"
        @click="navigate"
        :aria-current="isActive ? 'page' : null"
      >
        Courses
      </a>
    </RouterLink>

    |

    <RouterLink to="/profile" custom v-slot="{ href, navigate, isActive }">
      <a
        :href="href"
        @click="navigate"
        :aria-current="isActive ? 'page' : null"
      >
        Profile
      </a>
    </RouterLink>
  </nav>

  <hr>

  <main>
    <RouterView />
  </main>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>