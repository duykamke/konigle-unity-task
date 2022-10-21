<script setup lang="ts">
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://vuejs.org/api/sfc-script-setup.html#script-setup
import Header from './components/Header.vue';
import Dashboard from './components/Dashboard.vue';
</script>

<template>
  <div>
    <Header />
    <div class="px-32 py-10">
      <Dashboard />
    </div>
  </div>
</template>

<style>
@import url(//fonts.googleapis.com/css?family=Roboto:400,400italic,500,500italic,700,700italic,900,900italic,300italic,300,100italic,100);

body {
  @apply h-full w-full subpixel-antialiased bg-neutral-700;
}
</style>
