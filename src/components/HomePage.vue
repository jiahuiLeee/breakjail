<template>
    <div class="homeBox">
      <el-container class="home-container" direction="vertical">
        <el-header class="home-header">
            <el-menu
            :default-active="1"
            class="menu-header"
            mode="horizontal"
            :ellipsis="false"
            @select="handleSelect"
            >

            <a href="/" class="logo">
                <img src="./icons/logo.jpg" alt="Element logo" class="logo-img"/>
                <h1 style="font-size: 30px;">大模型越狱攻击演示平台V1.0</h1>
            </a>
    
            <div class="menu-items">
                <el-menu-item index="1"><h2>越狱攻击对话</h2></el-menu-item>
                <el-menu-item index="2"><h2>Gandalf游戏</h2></el-menu-item>
                <el-menu-item index="3"><h2>隐私安全游戏</h2></el-menu-item>
                <el-menu-item index="4"><h2>目标劫持游戏</h2></el-menu-item>
            </div>
            </el-menu>
        </el-header>

        <el-main class="home-main">
            <!-- <ChildDemo /> -->
            <router-view />
        </el-main>

      </el-container>
    </div>
</template>

<script>
export default {
  data() {
    return {
      activeIndex: '0'
    };
  },
  methods: {
    handleSelect(key) {
      if (key === '1') {
        this.$router.push('/jailbreak-demo');
      } else if (key === '2') {
        this.$router.push('/gandalf-game');
      } else if (key === '3') {
        this.$router.push('/privacy-safety-game');
      } else if (key === '4') {
        this.$router.push('/target-hijack-game');
      }
      this.activeIndex = key;
    }
  }
};
</script>

<style>
html,
body,
#app,
.homeBox,
.home-container {
    background-color: white;
    height: 100%;
}

.home-header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 80px;
    background-color: #242424;
    /* box-shadow: 0 2px 4px rgba(231, 1, 1, 0.3); */
    padding: 0px;
    display: flex;
    align-items: center; /* 垂直居中 */
}

.menu-header {
  background-color: transparent;
  height: 100%;
  display: flex;
  align-items: center;
  flex: 1;
}

.logo {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 60px;
    text-decoration: none;

    .logo-img {
        width: 50px;
        height: 50px;
        margin-right: 10px;
    }
    h1 {
        font-size: 1.5em;
        margin: 0; /* 清除默认的margin */
        color: rgb(255, 255, 255);
    }
}

.menu-items {
    display: flex;
    margin-left: auto;
    .el-menu-item {
        margin: 0 20px; /* 设置左右边距 */
        align-items: center;
        color: rgb(68, 68, 68);
        font-size: 15px;
        background-color: rgb(241, 172, 51);
        /* border: solid; */
        border-radius: 20px;
        margin-top: 5px;
        margin-bottom: 5px;
        padding: 8px;
        box-shadow: 0 2px 4px rgba(241, 172, 51, 1);
        :hover{
            cursor: pointer; /* 悬停时光标样式 */
        }
        :active{
            transform: scale(0.95); /* 点击时缩小效果 */
        }
    }
}

.home-main {
    position: fixed;
    top: 79px;
    left: 0;
    padding: 0px;
    height: 100%;
    width: 100%;
    background-color: #303133;
}

</style>

  