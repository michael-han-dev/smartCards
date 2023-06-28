<template>
  <div class="mt-20 min-h-screen flex flex-row">
    <div class="flex justify-start mr-10">
      <div class="bg-indigo-700 px-10 pt-20 font-semibold">
        <RouterLink
          to="/dashboard/insights"
          class="transition ease-in-out text-slate-300 hover:text-slate-200"
        >
          Insights
        </RouterLink>
      </div>
    </div>
    <div class="m-10 text-4xl font-bold tracking-tight text-gray-900">
      {{ heading }}
    </div>
  </div>
</template>

<script>
export default {
  props: ['heading']
}
</script>
