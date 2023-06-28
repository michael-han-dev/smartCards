<script setup></script>

<template>
  <!-- add props so the navbar routes change according to page -->
  <nav
    class="fixed top-0 flex items-center justify-between p-6 lg:px-8 z-50 w-screen bg-white border-b drop-shadow-sm"
    aria-label="Global"
  >
    <div class="flex lg:flex-1">
      <RouterLink to="/" class="-m-1.5 p-1.5">
        <span class="sr-only">Flash Cards Not Me!</span>
        <img class="h-8 w-auto" src="../assets/logo.svg" alt="" />
      </RouterLink>
    </div>
    <div class="flex lg:hidden">
      <button
        type="button"
        class="-m-2.5 inline-flex items-center justify-center rounded-md p-2.5 text-gray-700"
      >
        <span class="sr-only">Open main menu</span>
        <svg
          class="h-6 w-6"
          fill="none"
          viewBox="0 0 24 24"
          stroke-width="1.5"
          stroke="currentColor"
          aria-hidden="true"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5"
          />
        </svg>
      </button>
    </div>
    <div class="hidden lg:flex lg:gap-x-12">
      <a
        href="#features"
        v-smooth-scroll
        class="text-sm font-semibold leading-6 text-gray-900 hover:text-indigo-600 transition ease-in-out"
        >Features</a
      >
      <RouterLink
        to="/learn"
        class="text-sm font-semibold leading-6 text-gray-900 hover:text-indigo-600 transition ease-in-out"
        >Learn<span class="animate-ping bg-indigo-700 absolute top-8 w-2 h-2 rounded-full"></span>
        <span class="bg-indigo-700 absolute top-8 w-2 h-2 rounded-full"></span
      ></RouterLink>
      <RouterLink
        to="/dashboard"
        class="text-sm font-semibold leading-6 text-gray-900 hover:text-indigo-600 transition ease-in-out"
      >
        Dashboard
      </RouterLink>
      <RouterLink
        to="/about"
        class="text-sm font-semibold leading-6 text-gray-900 hover:text-indigo-600 transition ease-in-out"
        >About</RouterLink
      >
    </div>
    <div class="hidden lg:flex lg:flex-1 lg:justify-end">
      <RouterLink
        v-if="!authenticated"
        to="/login"
        class="pr-10 text-md font-semibold leading-6 text-gray-900 hover:text-indigo-600 transition ease-in-out"
      >
        Login
      </RouterLink>
      <RouterLink
        v-if="!authenticated"
        to="/register"
        class="text-md font-semibold leading-6 text-gray-900 hover:text-indigo-600 transition ease-in-out"
      >
        Register
      </RouterLink>
      <RouterLink
        v-if="authenticated"
        @click="signOut()"
        to="/"
        class="text-md font-semibold leading-6 text-gray-900 hover:text-indigo-600 transition ease-in-out"
      >
        Sign out
      </RouterLink>
    </div>
  </nav>
</template>

<script>
import { auth, onAuthStateChanged } from '../main.js'
export default {
  data() {
    return {
      authenticated: false
    }
  },
  created() {
    onAuthStateChanged(auth, (user) => {
      if (user) {
        console.log('logged in')
        this.authenticated = true
      } else {
        console.log('not logged in')
        this.authenticated = false
      }
    })
  },
  methods: {
    signOut() {
      auth
        .signOut()
        .then(() => {
          // Redirect the user to the login page or do any other post-signout action
          console.log('signed out')
          this.authenticated = false
        })
        .catch((error) => {
          console.error(error)
        })
    }
  }
}
</script>
