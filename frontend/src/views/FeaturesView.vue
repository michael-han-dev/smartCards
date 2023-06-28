<template>
  <div
    id="features"
    class="relative overflow-hidden isolate py-24 sm:py-32 max-w-screen min-h-screen"
  >
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
      <div
        class="mx-auto grid max-w-2xl grid-cols-1 gap-x-8 gap-y-16 sm:gap-y-20 lg:mx-0 lg:max-w-none lg:grid-cols-2"
      >
        <div class="lg:pr-8 lg:pt-4">
          <div class="lg:max-w-lg">
            <h2 class="text-base font-semibold leading-7 text-indigo-600">
              Make flash cards faster.
            </h2>
            <p class="mt-2 text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
              Spend more time <span class="text-indigo-600">reviewing </span>than making.
            </p>
            <p class="mt-6 text-lg leading-8 text-gray-600">
              With our flash card generation tool, we can help you save time and effort.
            </p>
            <dl class="mt-10 max-w-xl space-y-8 text-base leading-7 text-gray-600 lg:max-w-none">
              <div v-for="feature in features" :key="feature.name" class="relative pl-9">
                <dt class="inline font-semibold text-gray-900">
                  <component class="flex flex-col">
                    <img :src="feature.icon" class="absolute -left-2 h-8 w-8" aria-hidden="true" />
                    <p class="text-indigo-600">
                      {{ feature.name }}
                    </p>
                  </component>
                </dt>
                <dd class="inline">{{ feature.description }}</dd>
              </div>
            </dl>
          </div>
        </div>
        <img
          src="../assets/demo.png"
          alt="Product screenshot"
          class="lg:mt-10 w-1/2 rounded-xl shadow-xl ring-1 ring-gray-400/10 sm:w-[57rem] md:-ml-4 lg:-ml-0"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import time_management from '../assets/time_management.svg'
import online_information_re_erks from '../assets/online_information_re_erks.svg'

const features = [
  {
    name: 'Save time.',
    description:
      'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Maiores impedit perferendis suscipit eaque, iste dolor cupiditate blanditiis ratione.',
    icon: time_management
  },
  {
    name: 'Save effort.',
    description: 'random'
    //   icon: LockClosedIcon,
  },
  {
    name: 'Get accurate information.',
    description:
      'We use the latest tech to ensure that the info on the flash cards generated are up-to-date.',
    icon: online_information_re_erks
  }
]
</script>

<script></script>
