<template>
  <div>
      <h1>Ceci est un test</h1>
      <h2>{{msg}}</h2>
  </div>
</template>

<script>
export default {
  name: 'TestDjango',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    h1 {
        margin: 40px 0 0;
    }
</style>
