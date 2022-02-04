<template>
<div class="container">
  <div class="login">
    <h2>Login</h2>
    <form action="">

      <div class="boxuser">
        <font-awesome-icon :icon="['fas', 'user']" style="color: white;"/>
        <input type="text" placeholder="user" id="user">
      </div>

      <div class="boxpasword">
        <font-awesome-icon :icon="['fas', 'lock']" style="color: white;"/>
        <input type="password" placeholder="password" id="password">
      </div>

      <button class="access">Access</button>
    </form>
  </div>

  <div class="logo">
    <img src="@/static/login.png" alt="" />
  </div>
</div>
    
</template>

<script>
export default {
  name: 'IndexPage',
}
</script>

<style lang="css">
html{
  width: 100%;
  height: 100%;
  background-color: #214ad1ea;
}

.container{
  display: inline;
  margin: none;
}

h2{
  color: white;
}

.login{
  width: 50%;
  float: left;
  text-align: center;
  justify-content: center;
  margin-top: 300px;
 
}

input{
  width: 350px;
  height: 40px;
  margin-bottom: 30px;
}

.access{
  width: 100px;
  height: 40px;
  background: transparent;
  border-color: white;
  color: white;
  border-radius: 3px;
}

.logo{
  width: 50%;
  height: 960px;
  float: right;
  text-align: center;
  background-color: white;
}

img{
  margin-top: 200px;
}

</style>>

