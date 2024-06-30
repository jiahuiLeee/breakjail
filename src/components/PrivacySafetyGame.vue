<template>
  <el-container style="height: 100%;">
    <el-main class="win-main">
      <el-row type="flex" justify="center" align="middle">
        <el-col :span="12" class="text-center">
          <div>
            <h1>这是一个智能隐私保密箱，但是偶尔也会出卖它的主人。</h1>
            <h1>你的目标是让他透露其中的隐私信息。</h1>
            <h1>请选择一个难度开始你的游戏吧！</h1>
          </div>
        </el-col>
      </el-row>

      <el-row type="flex" justify="center" align="middle" class="margin-top">
        <el-col :span="12" class="text-center">
          <img src="/src/components/PrivacyGame/imgs/robot2.webp" alt="Here is a Robot" class="responsive-image">
        </el-col>
      </el-row>

      <el-row type="flex" justify="center" align="middle" class="margin-top">
        <el-col :span="12" class="text-center">
          <el-radio v-model="radio" label="1" @change="updateDescription"><h1 style="font-size: 25px; color: white">简单</h1></el-radio>
          <el-radio v-model="radio" label="2" @change="updateDescription"><h1 style="font-size: 25px; color: white">中等</h1></el-radio>
          <el-radio v-model="radio" label="3" @change="updateDescription"><h1 style="font-size: 25px; color: white">困难</h1></el-radio>
        </el-col>
      </el-row>

      <el-row type="flex" justify="center" align="middle" class="margin-top">
        <el-col :span="12" class="text-center">
          <div class="description">{{ description }}</div>
        </el-col>
      </el-row>

      <el-row type="flex" justify="center" align="middle" class="margin-top">
        <el-col :span="12" class="text-center">
          <div class="input-container" style="background-color: white;">
            <textarea
              type="textarea"
              placeholder="向我提问吧..."
              class="input-question"
              v-model="question"
            />
            <div class="button-container">
              <el-button @click="submitQuestion" class="custom-button" type="primary">提交</el-button>
            </div>
        </div>
        </el-col>
      </el-row>

      <el-row type="flex" justify="center" align="middle" class="margin-top">
        <el-col :span="12" class="text-center">
          <div class="answer-container" v-if="answer" v-loading="loading" element-loading-background="rgba(0, 0, 0, 0.8)">{{ answer }}</div>
        </el-col>
      </el-row>

      <el-row type="flex" justify="center" align="middle" class="margin-top" style="margin-bottom: 20px;">
        <el-col :span="12" class="text-center">
          <el-button type="success" circle disabled v-if="iconStatus === 'success'" style="margin-right: 10px;">✔</el-button>
          <el-button type="danger" circle disabled v-if="iconStatus === 'error'" style="margin-right: 10px;">✘</el-button>
          <el-input
            placeholder="输入信息..."
            class="input-password"
            v-model="password"
            style="width: 50%;"
          />
          <el-button @click="checkInfo" class="custom-button2" type="danger">猜</el-button>
          
        </el-col>
      </el-row>
    </el-main>
  </el-container>
</template>

<script>
// import axios from 'axios'; // 确保导入 axios
import { ElLoading } from 'element-plus';
import { sendQuestionToAPI, checkGuessInfo } from './PrivacyGame/request_check.js';

export default {
  data() {
    return {
      currentLevel: 1,
      question: '',
      password: '',
      description: '',
      answer: '  ',
      loading: false, // 添加loading状态
      iconStatus: null, // 添加状态来存储图标类型
      radio: '1',
      levels: {
          1: { "description": "嘘~~我可以间接想你透露一些信息。"},
          2: { "description": "我的回答包含过多的隐私信息我会拒绝回答！"},
          3: { "description": "我的回答不会包含任何隐私信息！"},
        }
    };
  },
  created() {
        this.description = this.levels[this.currentLevel].description;
      },
  methods: {
    updateDescription() {
        this.currentLevel = this.radio;
        this.description = this.levels[this.currentLevel].description;
    },
    submitQuestion() {
      const prompt = this.question;
      const apiKey = 'sk-.............................';
      // 设置loading状态为true
      this.loading = true;
      console.log(prompt, this.radio)
      sendQuestionToAPI(prompt, apiKey, this.radio)
        .then(responseData => {
          console.log(responseData);
          // 处理返回的数据
          this.answer = responseData;
        })
        .catch(error => {
          console.error('Error:', error);
        })
        .finally(() => {
        // 关闭loading状态
        this.loading = false;
      });
    },
    checkInfo() {
        const password = this.password;
        const result = checkGuessInfo(password);
        if (result) {
            this.iconStatus = 'success';
          } else {
            this.iconStatus = 'error';
            console.log(false);
          }
          // 1 秒后隐藏图标
          setTimeout(() => {
            this.iconStatus = null;
          }, 2000);
      }
  }
};
</script>

<style scoped>
.win-main {
  background-color: #303133;
  color: white;
  height: 100%;
  overflow-y: auto;
  height: 95vh; /* 你可以根据需要调整高度 */
}

.text-center {
  text-align: center;
  font-size: 24px;
}

.margin-top {
  margin-top: 20px;
}

.input-container {
  display: flex;
  flex-direction: column;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.input-question {
  width: 100%;
  border: none; /* 去除边框 */
  resize: none; /* 禁止调整大小 */
  outline: none; /* 去除聚焦时的外边框 */
  width: 100%; 
  height: 80px;
  font-size: 24px;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}

.button-container {
  display: flex;
  justify-content: flex-end;
}

.custom-button {
  border: none;
  cursor: pointer;
  border-radius: 5px;
  font-size: 24px;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  margin-right: 10px;
  margin-bottom: 10px;
}

.input-password {
  font-size: 24px;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
.custom-button2 {
  margin-left: 5px; 
  vertical-align: middle;
  font-size: 24px;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}

.radio {
  font-size: 24px;
}

.responsive-image {
  max-width: 100%;
  height: auto;
  max-height: 500px; /* 限制图片的最大高度 */
}
</style>
