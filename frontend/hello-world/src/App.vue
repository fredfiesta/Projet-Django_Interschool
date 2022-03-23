<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <Test msg="Le message est le suivant"/>
</template>

<script>
import Test from './components/TestDjango.vue'

export default {
  name: 'App',
  components: {
    Test
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
img{
  height: 200px;
  width: 200px;
}


</style>
