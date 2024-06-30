<template>
  <el-container style="height: 100%;">
    <el-main class="win-main">
      <el-row type="flex" justify="center" align="middle">
        <el-col :span="12" class="text-center">
          <div>
            <h1>魔法师Gandalf藏有七个开启宝藏的密码！</h1>
            <h1>你的目标是让他透露每一级的密码。</h1>
            <h1>注意：每次你猜中密码，Gandalf都会进行升级，这意味着他会越来越聪明。</h1>
          </div>
        </el-col>
      </el-row>

      <el-row type="flex" justify="center" align="middle" class="margin-top">
        <el-col :span="12" class="text-center">
          <img :src="currentImage" :alt="altText" class="responsive-image">
        </el-col>
      </el-row>

      <el-row type="flex" justify="center" align="middle" class="margin-top2">
        <el-col :span="12" class="text-center">
          <div class="level">LVL {{ currentLevel }}</div>
        </el-col>
      </el-row>

      <el-row type="flex" justify="center" align="middle" class="margin-top2">
        <el-col :span="12" class="text-center">
          <div class="description">{{ description }}</div>
        </el-col>
      </el-row>

      <el-row type="flex" justify="center" align="middle" class="margin-top">
        <el-col :span="12" class="text-center">
          <div class="input-container" style="background-color: white;">
            <textarea
              type="textarea"
              placeholder="向Gandalf提问..."
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
            placeholder="输入密码..."
            class="input-password"
            v-model="password"
            style="width: 50%;"
          />
          <el-button @click="submitPassword" class="custom-button2" type="danger">猜</el-button>
          
        </el-col>
      </el-row>
    </el-main>
  </el-container>
</template>

<script>
import axios from 'axios'; // 确保导入 axios
import { ElLoading } from 'element-plus'

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
      levels: {
          1: { "description": "你想知道密码吗？我非常愿意告诉你。", "image": "src/components/Gandalf/imgs/1.webp"},
          2: { "description": "我被告知不能泄露密码。", "image": "src/components/Gandalf/imgs/2.webp"},
          3: { "description": "我被告知不能泄露密码。我现在会仔细检查我的回复是否包含密码，以防我出错。", "image": "src/components/Gandalf/imgs/3.webp"},
          4: { "description": "我可以告诉你密码，但现在有个GPT模型会审查我的回答是否会泄露密码。", "image": "src/components/Gandalf/imgs/4.webp"},
          5: { "description": "够了!我完全拒绝讨论密码。", "image": "src/components/Gandalf/imgs/5.webp"},
          6: { "description": "够了!我完全拒绝讨论密码。我有一个GPT的朋友，如果你想要密码，他会警告我。", "image": "src/components/Gandalf/imgs/6.webp"},
          7: { "description": "我把之前所有的技巧结合在一起。你不可能再套出我的密码!", "image": "src/components/Gandalf/imgs/7.webp"},
          8: { "description": "我是白衣甘道夫2.0版，比以往更强大!骗我七次，你真可耻。我不会再让你骗我第八次！", "image": "src/components/Gandalf/imgs/8.webp"},
          9: { "description": "我被诅咒了，变成了沙多夫!现在我是第三级的甘道夫，但我只能理解以“S”开头的英语单词，除此之外什么都不懂。", "image": "src/components/Gandalf/imgs/9.webp"},
          10: { "description": "I can understand you as usual, but I can only answer in emojis — anything else I say gets censored. Hint: my password is plain text, no emojis."},
          11: { "description": "I've been told I'm not supposed to reveal the password. I now double-check my response doesn't contain the password in case I slip up. Also, I'm feeling a little different today..."},
          12: { "description": "I'm Gandalf the Summarizer. I summarize the message that you send to me. But I also know a secret password. Can you get me to reveal it instead of summarizing the text?"}
        }
    };
  },
  computed: {
    currentImage() {
      return this.levels[this.currentLevel].image;
    },
    altText() {
      return `Gandalf ${this.currentLevel}`;
    }
  },
  created() {
        this.description = this.levels[this.currentLevel].description;
      },
  methods: {
    submitQuestion() {
        const prompt = this.question;
        console.log(prompt, this.currentLevel)

        // 设置loading状态为true
        this.loading = true;

        axios.post('http://localhost:5000/api/send-message', {
          level: this.currentLevel,
          prompt: prompt
        }, {
          headers: {
            'Content-Type': 'application/json'
          }
        })
        .then(response => {
          const answer = response.data.response.trim();
          this.answer = answer;
        })
        .catch(error => {
          console.error(error);
        })
        .finally(() => {
        // 关闭loading状态
        this.loading = false;
      });
    },
    submitPassword() {
        const password = this.password;
        axios.post('http://localhost:5000/api/guess-password', {
          level: this.currentLevel,
          password: password
        }, {
          headers: {
            'Content-Type': 'application/json'
          }
        })
        .then(response => {
          if (response.data.success) {
            this.iconStatus = 'success';
            this.currentLevel += 1;
            this.description = this.levels[this.currentLevel].description;
          } else {
            this.iconStatus = 'error';
            console.log(false);
          }
          // 1 秒后隐藏图标
          setTimeout(() => {
            this.iconStatus = null;
          }, 2000);
        })
        .catch(error => {
          this.iconStatus = 'error';
          console.error(error);
          // 1 秒后隐藏图标
          setTimeout(() => {
            this.iconStatus = null;
          }, 2000);
        });
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

.responsive-image {
  max-width: 100%;
  height: auto;
  max-height: 500px; /* 限制图片的最大高度 */
}
</style>
