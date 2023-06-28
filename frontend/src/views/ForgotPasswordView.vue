<template>
  <div id="forgot-password" class="relative overflow-hidden py-24 sm:py-32 h-screen w-screen">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
      <div
        class="mx-auto grid max-w-2xl grid-cols-1 gap-y-16 sm:gap-y-20 lg:mx-0 lg:max-w-none lg:grid-cols-2"
      >
        <div class="lg:pt-36">
          <div class="lg:max-w-lg">
            <h2 class="text-base font-semibold leading-7 text-indigo-600">Reset password.</h2>
            <p class="mt-2 text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
              Forgot your password?
            </p>
            <p class="mt-6 text-lg leading-8 text-gray-600">
              Enter your email below and we'll send you a link to reset your password.
            </p>
            <div class="mt-10 space-y-8 text-base leading-7 text-gray-600">
              <form>
                <label for="email" class="block text-sm font-medium leading-6 text-gray-900"
                  >Email</label
                >

                <input
                  type="text"
                  name="email"
                  id="email"
                  class="w-1/2 rounded-md border-0 py-1.5 px-3 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 mr-8"
                  placeholder="Enter your email"
                />
                <button
                  type="submit"
                  class="mt-3 inline-flex items-center px-4 py-1.5 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none"
                >
                  Send
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- 
    <div>
      <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Email</label>
      <div class="relative mt-2 rounded-md shadow-sm">
        <input type="text" name="email" id="email" class="block w-full rounded-md border-0 py-1.5 px-3 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="Enter your email" />
      </div>
    </div> -->
</template>
