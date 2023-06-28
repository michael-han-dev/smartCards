<template>
  <div
    @click.prevent="reset"
    class="flex min-h-screen flex-1 flex-col justify-center px-6 py-12 lg:px-8"
  >
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <img class="mx-auto h-10 w-auto" src="../assets/logo.svg" alt="SmartCard" />
      <h2 class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">
        Sign in to your account
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
              :class="{ 'ring-rose-500 ring-1': loginFailed }"
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
            <div class="text-sm">
              <RouterLink
                to="/forgot-password"
                class="font-semibold text-indigo-600 hover:text-indigo-500"
                >Forgot password?</RouterLink
              >
            </div>
          </div>
          <div class="mt-2">
            <input
              :class="{ 'ring-rose-500 ring-1': loginFailed }"
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
          <button
            @click.prevent="submitForm"
            type="submit"
            class="hover:-translate-y-1 transition ease-in-out flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
          >
            <p v-if="!isLoading">Sign in</p>
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
        <div class="flex flex-row justify-center items-center">
          <hr class="w-full flex border-gray-400" />
          <p class="text-gray-600 font-semibold text-sm px-4">OR</p>
          <hr class="w-full flex border-gray-400" />
        </div>
        <div class="flex justify-center">
          <button
            @click.prevent="googleLogin()"
            class="hover:bg-white transition ease-in-out bg-gray-100 ring-gray-400 ring-2 rounded-xl p-2"
          >
            <img src="../assets/google.png" alt="Google" class="h-5 w-5" />
          </button>
        </div>
      </form>

      <p class="mt-10 text-center text-sm text-gray-500">
        Don't have an account?
        {{ ' ' }}
        <RouterLink
          to="/register"
          class="font-semibold leading-6 text-indigo-600 hover:text-indigo-500"
          >Register</RouterLink
        >
      </p>
    </div>
  </div>
</template>

<script>
import {
  getAuth,
  signInWithEmailAndPassword,
  signInWithRedirect,
  GoogleAuthProvider
} from 'firebase/auth'
import { useRouter } from 'vue-router'
const provider = new GoogleAuthProvider()
const auth = getAuth()
const router = useRouter()

export default {
  data() {
    return {
      email: '',
      password: '',
      loginFailed: false,
      isLoading: false
    }
  },
  methods: {
    reset() {
      this.loginFailed = false
    },
    submitForm() {
      this.loginFailed = false
      this.isLoading = true
      signInWithEmailAndPassword(auth, this.email, this.password)
        .then((userCredential) => {
          this.isLoading = false
          // Signed in
          const user = userCredential.user
          this.loginFailed = false
          this.$router.push('/')
        })
        .catch((error) => {
          this.isLoading = false
          const errorCode = error.code
          const errorMessage = error.message
          this.loginFailed = true
        })
    },
    googleLogin() {
      signInWithRedirect(auth, provider)
      // getRedirectResult(auth)
      // .then((result) => {
      //   // This gives you a Google Access Token. You can use it to access Google APIs.
      //   const credential = GoogleAuthProvider.credentialFromResult(result);
      //   const token = credential.accessToken;

      //   // The signed-in user info.
      //   const user = result.user;
      //   // IdP data available using getAdditionalUserInfo(result)
      //   // ...
      // }).catch((error) => {
      //   // Handle Errors here.
      //   const errorCode = error.code;
      //   const errorMessage = error.message;
      //   // The email of the user's account used.
      //   const email = error.customData.email;
      //   // The AuthCredential type that was used.
      //   const credential = GoogleAuthProvider.credentialFromError(error);
      //   // ...
      // });
    }
  }
}
</script>
