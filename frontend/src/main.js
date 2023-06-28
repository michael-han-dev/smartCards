import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import VueSmoothScroll from 'vue3-smooth-scroll'
import VueKinesis from 'vue-kinesis'

// firebase stuff
// Import the functions you need from the SDKs you need
import { initializeApp } from 'firebase/app'
import { getAnalytics } from 'firebase/analytics'
import { getAuth, onAuthStateChanged, signInWithRedirect } from 'firebase/auth'

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: 'AIzaSyDGlfH6JlEouNLtqjk-FdfHyd5f_lfDMOA',
  authDomain: 'smartcards-9e663.firebaseapp.com',
  projectId: 'smartcards-9e663',
  storageBucket: 'smartcards-9e663.appspot.com',
  messagingSenderId: '580017813259',
  appId: '1:580017813259:web:8e0cc5df8e75600327140e',
  measurementId: 'G-K5D3DRW817'
}

// Initialize Firebase
const firebaseApp = initializeApp(firebaseConfig)
const auth = getAuth(firebaseApp)
const analytics = getAnalytics(firebaseApp)

import './assets/base.css'

const app = createApp(App)

app.use(router)
app.use(VueSmoothScroll)
app.use(VueKinesis)
app.mount('#app')

export { auth, onAuthStateChanged, signInWithRedirect }
