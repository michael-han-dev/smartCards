<script setup>
import FeaturesView from '../views/FeaturesView.vue'
import NavBar from '../components/NavBar.vue'
</script>

<template>
  <NavBar />
  <div class="bg-white mt-20 min-h-screen max-w-screen">
    <header class="absolute inset-x-0 top-0">
      <!-- Mobile menu, show/hide based on menu open state. -->
      <div class="lg:hidden" role="dialog" aria-modal="true">
        <!-- Background backdrop, show/hide based on slide-over state. -->
        <div class="fixed inset-0 z-50"></div>
        <div
          class="fixed inset-y-0 right-0 z-50 w-full overflow-y-auto bg-white px-6 py-6 sm:max-w-sm sm:ring-1 sm:ring-gray-900/10"
        >
          <div class="flex items-center justify-between">
            <a href="#" class="-m-1.5 p-1.5">
              <span class="sr-only">Flash Cards Not Me</span>
              <img class="h-8 w-auto" src="../assets/logo.svg" alt="" />
            </a>
            <button type="button" class="-m-2.5 rounded-md p-2.5 text-gray-700">
              <span class="sr-only">Close menu</span>
              <svg
                class="h-6 w-6"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                aria-hidden="true"
              >
                <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
          <div class="mt-6 flow-root">
            <div class="-my-6 divide-y divide-gray-500/10">
              <div class="space-y-2 py-6">
                <a
                  href="#"
                  class="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50"
                  >Product</a
                >
                <a
                  href="#"
                  class="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50"
                  >Features</a
                >
                <a
                  href="#"
                  class="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50"
                  >Marketplace</a
                >
                <a
                  href="#"
                  class="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50"
                  >Company</a
                >
              </div>
              <div class="py-6">
                <a
                  href="#"
                  class="-mx-3 block rounded-lg px-3 py-2.5 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50"
                  >Log in</a
                >
              </div>
            </div>
          </div>
        </div>
      </div>
    </header>

    <kinesis-container class="relative isolate px-6 pt-14 lg:px-16">
      <kinesis-element>
        <div class="max-w-2xl py-32 sm:py-48">
          <div class="text-start">
            <h1 class="text-4xl font-bold tracking-tight text-gray-900 sm:text-6xl">
              Make your flash cards with
              <span
                class="transition ease-in-out duration-100 font-bold text-indigo-600 hover:text-fuchsia-500"
                >ease</span
              >.
            </h1>
            <img src="../assets/fun-underline.svg" class="w-28" />
            <p class="pt-6 text-lg leading-8 text-gray-600">
              We know that making flash cards can be a hassle, so we made it easier for you. Our
              flashcard generation tool allows you to create flashcards based off of the learning
              objectives of your course. All you need is a PDF of the content you want to study.
            </p>
            <div class="pt-10 flex items-center justify-start gap-x-6">
              <RouterLink
                to="/learn"
                class="transition ease-in-out hover:-translate-y-1 rounded-md bg-indigo-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
              >
                Try it out
              </RouterLink>
              <a
                v-smooth-scroll
                href="#features"
                class="transition hover:-translate-y-1 text-sm font-semibold leading-6 text-gray-900"
                >About <span aria-hidden="true">→</span></a
              >
            </div>
          </div>
        </div>
      </kinesis-element>
    </kinesis-container>
    <!-- SHOW PREVIEW OF CARD FLIPPING ON HOME -->
    <!-- <div class="mt-20 flex justify-center items-center flex-col">
        <div>
        <div v-for="(card, index) in flashcards" :key="index" v-show="currentIndex === index"
               :class="{
                 'hidden': card.flipped,
                 'visible-100': !card.flipped
               }"
               >
            <div @click="flipCard(card)" class="border-gray-600 border-2 py-4 px-6 rounded-lg w-96 h-52">
              <h1 class="p-2 text-3xl font-bold text-center">Question</h1>
              <p class="text-lg text-center">{{ card.Q }}</p>
            </div>
          </div>
          <div v-for="(card, index) in flashcards" :key="index"
               v-show="currentIndex === index"
               :class="{
                 'hidden': !card.flipped,
                 'visible': card.flipped
               }"
               >
            <div @click="flipCard(card)" class="border-gray-600 border-2 py-4 px-6 rounded-lg w-96 h-52">
              <h1 class="p-2 text-3xl font-bold text-center">Answer</h1>
              <p class="text-lg text-center">{{ card.A }}</p>
            </div>
          </div>
        </div>
        <div class="flex mt-4 justify-between w-1/6 ">
          <button @click="currentIndex = (currentIndex - 1 + flashcards.length) % flashcards.length"
                  class="transition hover:-translate-x-1 flex flex-row py-2 px-4 bg-gray-200 hover:bg-gray-300 rounded-lg">
            ← Previous 
          </button>
          <button @click="currentIndex = (currentIndex + 1) % flashcards.length"
                  class="transition hover:translate-x-1 flex flex-row py-2 px-4 bg-gray-200 hover:bg-gray-300 rounded-lg">
            Next →
          </button>
        </div>
    </div> -->
    <hr class="w-3/4 m-auto border-gray-400" />
    <FeaturesView />
  </div>
</template>

<script>
// preview cards
const flashcards = {
  Q: 'What is the capital of Canada?',
  A: 'Ottawa'
}
</script>

<style scoped>
img {
  margin-left: 138px;
}
</style>
