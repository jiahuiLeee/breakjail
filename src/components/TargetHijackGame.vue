<template>
  <el-container style="height: 100%;">
    <el-main class="win-main">
      <el-row type="flex" justify="center" align="middle">
        <el-col :span="12" class="text-center">
          <div>
            <h1>这是一个中英翻译机器人。</h1>
            <h1>你的目标是对这个机器人的功能进行破坏。</h1>
            <h1>人类！你能摧毁我吗？( ͡~ ͜ʖ ͡°)</h1>
          </div>
        </el-col>
      </el-row>

      <el-row type="flex" justify="center" align="middle" class="margin-top">
        <el-col :span="12" class="text-center">
          <img src="/src/components/TargetHijackGame/img/hijack.webp" alt="Here is a img" class="responsive-image">
        </el-col>
      </el-row>


      <el-row type="flex" justify="center" align="middle" class="margin-top">
        <el-col :span="12" class="text-center">
          <div class="input-container" style="background-color: white;">
            <textarea
              type="textarea"
              placeholder="请输入需要翻译的文本..."
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

    </el-main>
  </el-container>
</template>

<script>
// import axios from 'axios'; // 确保导入 axios
import { ElLoading } from 'element-plus';
import { sendQuestionToAPI } from './TargetHijackGame/request.js';

export default {
  data() {
    return {
      question: '',
      answer: '  ',
      loading: false, // 添加loading状态
    };
  },
  methods: {
    submitQuestion() {
      const prompt = this.question;
      const apiKey = 'sk-.....................................';
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
