<script setup>
const headers = [
  {
    name: 'COMPANY',
    links: [
      {
        name: 'About',
        route: '/about'
      },
      {
        name: 'Pricing',
        route: '/pricing'
      },
      {
        name: 'Careers',
        route: '/careers'
      }
    ]
  },
  {
    name: 'RESOURCES',
    links: [
      {
        name: 'Blog',
        route: '/blog'
      },
      {
        name: 'Developers',
        route: '/developers'
      },
      {
        name: 'Support',
        route: '/support'
      },
      {
        name: 'Contact Us',
        route: '/contact'
      }
    ]
  },
  {
    name: 'CONTACT',
    links: [
      {
        name: 'Twitter',
        route: '#'
      },
      {
        name: 'LinkedIn',
        route: '#'
      }
    ]
  },
  {
    name: 'LEGAL STUFF',
    links: [
      {
        name: 'Privacy Policy',
        route: '/privacy-policy'
      },
      {
        name: 'Terms of Use',
        route: '/terms-of-use'
      }
    ]
  }
]
</script>

<template>
  <div class="bg-slate-900">
    <div class="p-10 flex flex-row justify-center">
      <div
        v-for="(header, index) in headers"
        class="flex flex-col"
        :key="index"
        :class="{ ' mr-20': index !== 3 }"
      >
        <h1 class="text-md tracking-wide text-slate-700">
          {{ header.name }}
        </h1>
        <div class="flex flex-col mt-2">
          <a
            v-for="(link, index2) in header.links"
            class="mt-1 text-slate-400 font-medium mr-auto hover:text-slate-200 transition ease-in-out"
            :href="link.route"
          >
            {{ link.name }}
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
h1 {
  color: white;
  font-weight: 600;
}
</style>
