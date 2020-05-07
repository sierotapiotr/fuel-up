<template>
   <div>
      <Navbar />
      <img alt="Vue logo" src="./assets/logo.png">
      <HelloWorld msg="Welcome to Your Vue.js App"/>
   </div>
</template>

<script>
import Navbar from "./components/Navbar";
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'Fuel-up',
  components: {
    Navbar,
    HelloWorld
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
