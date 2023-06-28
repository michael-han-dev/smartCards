<script setup>
import in_no_time from '../assets/in_no_time_-6-igu.svg'
import check from '../assets/check.svg'
import cloud_upload from '../assets/cloud-upload.svg'
import FlashCards from '../views/FlashCardsView.vue'
const features = [
  {
    name: 'Valid extension name.',
    description: 'Make sure your file is a PDF file.',
    icon: check
  },
  {
    name: 'Upload.',
    description: 'Upload your PDF file using the form to the right and press `submit`.',
    icon: cloud_upload
  },
  {
    name: 'Wait.',
    description: 'Wait while we generate your flash cards and get all the facts right for you.',
    icon: in_no_time
  }
]
</script>

<template>
  <nav
    class="fixed top-0 flex items-center justify-between p-6 lg:px-8 z-50 w-screen bg-white border-b"
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
      <RouterLink
        to="/"
        class="text-sm font-semibold leading-6 text-gray-900 hover:text-indigo-600 transition ease-in-out"
        >Features</RouterLink
      >
      <RouterLink
        to="/learn"
        class="text-sm font-semibold leading-6 text-gray-900 hover:text-indigo-600 transition ease-in-out"
        >Learn<span class="animate-ping bg-indigo-700 absolute top-8 w-2 h-2 rounded-full"></span>
        <span class="bg-indigo-700 absolute top-8 w-2 h-2 rounded-full"></span
      ></RouterLink>
      <RouterLink
        to="/"
        class="text-sm font-semibold leading-6 text-gray-900 hover:text-indigo-600 transition ease-in-out"
        >About</RouterLink
      >
    </div>
    <div class="hidden lg:flex lg:flex-1 lg:justify-end">
      <!-- REPLACE LATER -->
    </div>
  </nav>
  <div id="generate" class="relative isolate overflow-hidden sm:py-32">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
      <div
        class="mx-auto grid max-w-2xl grid-cols-1 gap-x-8 gap-y-16 sm:gap-y-20 lg:mx-0 lg:max-w-none lg:grid-cols-2"
      >
        <div class="lg:pr-8 lg:pt-10">
          <div class="lg:max-w-lg">
            <h2 class="text-base font-semibold leading-7 text-indigo-600">Get started.</h2>
            <p class="mt-2 text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
              Start by uploading your <span class="text-indigo-600">PDF</span>.
            </p>
            <p class="mt-6 text-lg leading-8 text-gray-600">
              Upload your PDF file containing learning objectives and questions you have. We'll take
              care of the flash card generation and the fact look-ups.
            </p>
            <dl class="mt-14 max-w-xl space-y-8 text-base leading-7 text-gray-600 lg:max-w-none">
              <div v-for="feature in features" :key="feature.name" class="relative pl-9">
                <dt class="inline font-semibold text-gray-900">
                  <component class="flex flex-col">
                    <img
                      :src="feature.icon"
                      class="absolute left-1 top-1 h-5 w-5"
                      aria-hidden="true"
                    />
                    <p class="text-indigo-600">
                      {{ feature.name }}
                    </p>
                  </component>
                </dt>
                {{ ' ' }}
                <dd class="inline">{{ feature.description }}</dd>
              </div>
            </dl>
          </div>
        </div>
        <div class="pdf-form flex justify-center items-center drop-shadow-sm">
          <form
            @submit.prevent="submitForm"
            enctype="multipart/form-data"
            class="text-gray-900 font-bold flex flex-col items-center space-y-4 p-10"
          >
            <label for="pdf" class="font-bold"> Upload your PDF: </label>
            <label for="pdf">
              <img
                :class="{ 'border-rose-500': error, 'border-emerald-500': uploadSuccess }"
                src="../assets/add_files_re_v09g.svg"
                class="w-48 h-48 border-2 rounded-xl p-4"
                alt="Add files"
              />
            </label>
            <p v-if="error" class="text-rose-500 font-medium text-md">Error uploading PDf file!</p>
            <p v-if="uploadSuccess" class="text-emerald-500 font-medium text-md">
              File uploaded successfully!
            </p>
            <input
              id="pdf"
              class="ml-28 font-medium py-2 px-4 focus:outline-none text-gray-600 flex"
              type="file"
              name="pdf"
              ref="pdf"
            />
            <button
              type="submit"
              class="w-20 flex justify-center transition ease-in-out rounded-md bg-indigo-600 text-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600 py-2 px-4 shadow-md duration-300"
            >
              <p v-if="!isLoading" class="text-white font-medium">Submit</p>
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
          </form>
        </div>
      </div>
    </div>
  </div>
  <a class="animate-bounce" href="#flashcards" v-smooth-scroll>
    <img
      v-if="flashcards"
      src="../assets/undraw_straight-arrow.svg"
      class="mb-10 p-1 h-10 w-10 rotate-180 m-auto border-2 border-gray-600 rounded-full"
      alt="Arrow"
    />
  </a>
  <hr v-if="flashcards" class="w-3/4 m-auto border-gray-400" />
  <div v-if="flashcards">
    <FlashCards :flashcards="flashcards" />
  </div>
</template>

<script>
export default {
  components() {
    FlashCardsView
  },
  data() {
    return {
      isLoading: false,
      uploadSuccess: false,
      error: false,
      flipped: false,
      flashcards: null
    }
  },
  methods: {
    flip() {
      this.flipped = !this.flipped
    },
    submitForm() {
      this.isLoading = true
      const formData = new FormData()
      formData.append('pdf', this.$refs.pdf.files[0])
      fetch('http://127.0.0.1:5000/api/generate', {
        method: 'POST',
        body: formData
      })
        .then((response) => {
          if (response.status === 200) {
            console.log('Uploaded successfully')
            this.uploadSuccess = true
            this.error = false
            response.json().then((data) => {
              this.flashcards = data.cards
            })
          } else {
            console.log('Upload failed')
            this.uploadSuccess = false
            this.error = true
          }
          this.isLoading = false
        })
        .catch((error) => {
          this.isLoading = false
          console.error('Error:', error)
          ;(this.uploadSuccess = false), (this.error = true)
        })
    }
  }
}
</script>

<style scoped>
.pdf-form {
  background-color: rgb(241, 241, 242);
  border-radius: 10px;
  border-color: rgb(209, 213, 219);
  border-width: 1px;
}

form {
  background-color: #fff;
  border-radius: 10px;
  border-color: rgb(209, 213, 219);
  border-width: 1px;
}

::file-selector-button {
  display: none;
}
</style>
