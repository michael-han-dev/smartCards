<script setup>
import { RouterLink, RouterView } from 'vue-router'
import NavBar from '../src/components/NavBar.vue'
import FooterView from '../src/components/Footer.vue'
</script>

<template>
  <main>
    <RouterView />
    <FooterView />
  </main>
</template>

<style scoped>
body {
  font-family: 'Roboto', sans-serif;
}

h1 {
  color: #111827;
}

p {
  color: #9199b4;
}
</style>
