<script setup>
import NavBar from '@/components/NavBar.vue'
import DashboardPanel from '../components/DashboardPanel.vue'
</script>
<template>
  <NavBar />
  <DashboardPanel :heading="'Insights'" />
</template>
