<template>
  <div
    @click.prevent="reset"
    class="flex min-h-screen flex-1 flex-col justify-center px-6 py-12 lg:px-8"
  >
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <img class="mx-auto h-10 w-auto" src="../assets/logo.svg" alt="SmartCard" />
      <h2 class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">
        Register your account
      </h2>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6" action="#" method="POST">
        <div>
          <label for="email" class="block text-sm font-medium leading-6 text-gray-900"
            >Email address</label
          >
          <div class="mt-2">
            <input
              :class="{ 'ring-rose-500 ring-1': emailInUse || emailInvalid }"
              v-model="email"
              id="email"
              name="email"
              type="email"
              autocomplete="email"
              placeholder="Enter your email"
              required="true"
              class="px-2 w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            />
          </div>
        </div>

        <div>
          <div class="flex items-center justify-between">
            <label for="password" class="block text-sm font-medium leading-6 text-gray-900"
              >Password</label
            >
          </div>
          <div class="mt-2">
            <input
              :class="{ 'ring-rose-500 ring-1': error || weakPassword }"
              v-model="password"
              id="password"
              name="password"
              type="password"
              placeholder="Enter your password"
              autocomplete="current-password"
              required="true"
              class="px-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            />
          </div>
        </div>

        <div>
          <div class="flex items-center justify-between">
            <label for="retype-password" class="block text-sm font-medium leading-6 text-gray-900"
              >Retype Password</label
            >
          </div>
          <div class="mt-2">
            <input
              :class="{ 'ring-rose-500 ring-1': error || weakPassword }"
              v-model="retypePassword"
              id="retype-password"
              name="retypePassword"
              type="password"
              placeholder="Retype your password"
              required="true"
              class="px-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            />
          </div>
        </div>

        <div>
          <button
            @click.prevent="submitForm"
            type="submit"
            class="hover:-translate-y-1 transition ease-in-out flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
          >
            <p v-if="!isLoading">Register</p>
            <svg
              v-if="isLoading"
              class="animate-spin h-5 w-5 text-white"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
            >
              <circle
                class="opacity-25"
                cx="12"
                cy="12"
                r="10"
                stroke="currentColor"
                stroke-width="4"
              ></circle>
              <path
                class="opacity-75"
                fill="currentColor"
                d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
              ></path>
            </svg>
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { getAuth, createUserWithEmailAndPassword } from 'firebase/auth'
import { useRouter } from 'vue-router'
const router = useRouter()

const auth = getAuth()
export default {
  data() {
    return {
      email: '',
      password: '',
      retypePassword: '',
      error: false,
      isLoading: false,
      emailInUse: false,
      emailInvalid: false,
      weakPassword: false
    }
  },
  methods: {
    reset() {
      ;(this.emailInUse = false), (this.emailInvalid = false), (this.weakPassword = false)
    },
    submitForm() {
      // add email validation
      this.isLoading = true
      if (this.password !== this.retypePassword) {
        this.isLoading = false
        this.error = true
        alert('Passwords do not match')
        return
      }
      this.error = false
      createUserWithEmailAndPassword(auth, this.email, this.password)
        .then((userCredential) => {
          this.isLoading = false
          // Signed in
          const user = userCredential.user
          // ...
        })
        .catch((error) => {
          this.isLoading = false
          const errorCode = error.code
          const errorMessage = error.message
          if (this.email === '' || this.password === '' || this.retypePassword === '') {
            this.emailInUse = false
            this.emailInvalid = true
            this.weakPassword = true
            return
          } else if (errorCode == 'auth/email-already-in-use') {
            this.emailInUse = true
          } else if (errorCode == 'auth/invalid-email') {
            this.emailInvalid = true
          } else if (errorCode == 'auth/weak-password') {
            this.weakPassword = true
          }
        })
    }
  }
}
</script>
