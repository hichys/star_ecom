<template>
  <div class="m-3">
    <Header/>
    <router-view />
  </div>
  <Footer></Footer>
</template>

<script setup>
  import Header from './pages/Header.vue'
import Footer from './pages/Footer.vue';
</script>