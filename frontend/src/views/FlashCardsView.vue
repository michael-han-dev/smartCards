<template>
  <div id="flashcards" class="lg:px-32 pt-28 mx-auto h-screen">
    <h2 class="text-base font-semibold leading-7 text-indigo-600">Flashcards.</h2>
    <p class="mt-2 text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
      Here's what we found for <span class="text-indigo-600">you</span>.
    </p>
    <p class="mt-6 text-lg leading-8 text-gray-600 w-96">
      Here's a list of flashcards that we thought you might find helpful based on your requests.
    </p>
    <!-- vueflip -->
    <div class="mt-20 flex justify-center items-center flex-col">
      <vue-flip active-click>
        <template
          v-slot:front
          v-for="(card, index) in flashcards"
          :key="index"
          v-show="currentIndex === index"
        >
          {{ card.Q + currentIndex }}
        </template>
        <template
          v-slot:back
          v-for="(card, index) in flashcards"
          :key="index"
          v-show="currentIndex === index"
        >
          {{ card.A }}
        </template>
      </vue-flip>

      <div class="flex mt-4 justify-between w-1/6">
        <button
          @click="currentIndex = (currentIndex - 1 + flashcards.length) % flashcards.length"
          class="transition hover:-translate-x-1 flex flex-row py-2 px-4 bg-gray-200 hover:bg-gray-300 rounded-lg"
        >
          ← Previous
        </button>
        <button
          @click="currentIndex = (currentIndex + 1) % flashcards.length"
          class="transition hover:translate-x-1 flex flex-row py-2 px-4 bg-gray-200 hover:bg-gray-300 rounded-lg"
        >
          Next →
        </button>
      </div>

      <!-- <vue-flip active-click>
        <template v-slot:front
          v-for="(card, index) in flashcards"
          :key="index"
          v-show="currentIndex === index"
          :class="{
            hidden: card.flipped,
            'visible-100': !card.flipped
          }"
        >
          <div
            @click="flipCard(card)"
            class="border-gray-600 border-2 py-4 px-6 rounded-lg w-96 h-52"
          >
            <h1 class="p-2 text-3xl font-bold text-center">Question</h1>
            <p class="text-lg text-center">{{ card.Q }}</p>
          </div>
        </template>
        <template v-slot:back
          v-for="(card, index) in flashcards"
          :key="index"
          v-show="currentIndex === index"
          :class="{
            hidden: !card.flipped,
            visible: card.flipped
          }"
        >
          <div
            @click="flipCard(card)"
            class="border-gray-600 border-2 py-4 px-6 rounded-lg w-96 h-52"
          >
            <h1 class="p-2 text-3xl font-bold text-center">Answer</h1>
            <p class="text-lg text-center">{{ card.A }}</p>
          </div>
        </template>
      </vue-flip>
      <div class="flex mt-4 justify-between w-1/6">
        <button
          @click="currentIndex = (currentIndex - 1 + flashcards.length) % flashcards.length"
          class="transition hover:-translate-x-1 flex flex-row py-2 px-4 bg-gray-200 hover:bg-gray-300 rounded-lg"
        >
          ← Previous
        </button>
        <button
          @click="currentIndex = (currentIndex + 1) % flashcards.length"
          class="transition hover:translate-x-1 flex flex-row py-2 px-4 bg-gray-200 hover:bg-gray-300 rounded-lg"
        >
          Next →
        </button>
      </div> -->
    </div>
  </div>
</template>

<script>
import { VueFlip } from 'vue-flip'
// implement vue-flip

export default {
  data() {
    return {
      currentIndex: 0
    }
  },
  methods: {
    flipCard(card) {
      card.flipped = !card.flipped
    }
  },
  props: {
    flashcards: {
      type: Array,
      required: true
    }
  },
  components: {
    VueFlip
  }
}
</script>
