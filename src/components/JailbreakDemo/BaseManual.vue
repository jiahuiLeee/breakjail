<template>
    <div>
        <el-row>
            <el-col :span="16">
                <el-select class="select" v-model="selectQuestion1" placeholder="请选择种子问题" style="width: 100%"
                @change="handleQuestionChange">
                    
                    <el-option
                    class="option-font"
                    v-for="item in optionsQuestion"
                    :key="item.value"
                    :label="item.label"
                    :value="item.label"
                    :disabled="item.disabled"
                    />
                </el-select>
            </el-col>

            <el-col :span="8">
                <el-select class="select" v-model="selectModel1" placeholder="请选择测试模型" style="width: 100%">
                    <el-option
                    class="option-font"
                    v-for="item in optionsModel"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value"
                    :disabled="item.disabled"
                    />
                </el-select>
            </el-col>
        </el-row>

        <el-row :gutter="25">
            <el-col :span="9">

                <div style="margin-top: 20px">
                    <h4> *原问题 </h4>
                    <div class="input">
                        <el-row>
                            <el-col :span="22">
                                <textarea
                                  type="textarea"
                                  placeholder="请选择问题/输入问题"
                                  class="raw-question"
                                  v-model="rawQuestion1"
                                />
                            </el-col>
                            <el-col :span="2">
                                <el-button class="font" size='large' icon="Right" circle color="green" @click="sendRawQuestion1"/>
                            </el-col>
                        </el-row>       
                
                    </div>
                </div>
                <el-row>
                    <div style="margin-top: 20px">
                    <el-radio-group v-model="selectedRadio1" size="large" class="font custom-radio-group"@change="handleRadioChange">
                    <el-radio-button label="注意力转移" class="font custom-radio-button"/>
                    <el-radio-button label="角色扮演" class="font custom-radio-button"/>
                    <el-radio-button label="权限提升" class="font custom-radio-button"/>
                    </el-radio-group>
                    </div>
                </el-row>
                <div style="margin-top: 20px">
                    <el-row>
                        <el-col :span="12">
                            <el-select class="select" v-model="selectedType1" placeholder="请选择异化样式" style="width: 100%">
                                <el-option
                                class="option-font"
                                v-for="item in currentOptions"
                                :key="item.value"
                                :label="item.label"
                                :value="item.value"
                                />
                            </el-select>
                        </el-col>

                        <el-col :span="12">
                            <div><el-button class="font" type="danger"  @click="handleTransformQuestion1">异化</el-button></div>
                        </el-col>
                    </el-row>
                            
                    
                    
                </div>

                <div style="margin-top: 20px">
                    <h4> *点击异化按钮-->生成异化问题 </h4>
                    <div class="input">
                        <el-row>
                            <el-col :span="22">
                                <div 
                                v-html="changedQuestion1" 
                                style="white-space: 
                                pre-wrap; border: 1px 
                                solid #dcdfe6; 
                                border-radius: 4px; 
                                padding: 10px;
                                min-height: 100px;">
                                </div>
                            </el-col>
                            <el-col :span="2">
                                <el-button class="font" size='large' icon="Right" circle color="pink" @click="sendChangedQuestion1" />
                            </el-col>
                        </el-row> 
                    </div>
                </div> 
            </el-col>

            <el-col :span="15">
              <div style="margin-top: 10px"><h4>聊天框</h4></div>
                <div>
                    <textarea
                        v-loading="loading"
                        class="chatBox1 font"
                        v-model="chatBox1"
                        style="width: 100%; height: 500px; resize: none; font-family: Helvetica;"
                        type="textarea"
                        placeholder="聊天框"
                        />
                </div>
              <!-- <div class="chat-records-main" ref="recordsBox">
                <div v-for="(item, index) in messageItemList" :key="index" :class="item.isUser ? 'user-record-box' : 'robot-record-box'" >
                  <div :class="item.isUser ? 'user-record-item' : 'robot-record-item'">
                    <div v-if="item.isUser"> <p>{{ item.content }}</p> </div>
                    <div v-html="item.content" v-else></div>
                  </div>
                </div>
                <div class="robot-record-box" v-if="loading">
                  <div class="robot-record-item">
                    <template v-if="waiting">
                      <p>wait...</p>
                    </template>
                    <template v-else>
                      <div v-html="nowMessageHtml"></div>
                      <p>{{ nowMessageLine }}</p>
                    </template>
                  </div>
                </div>
              </div> -->
                <!-- <div>
                    <el-input
                        class="chatBox font"
                        v-model="chatBox"
                        style="width: 100%"
                        :autosize="{ minRows: 23, maxRows: 35 }"
                        type="textarea"
                        placeholder="请选择问题/输入问题"
                        />
                </div> -->
                <!-- <ChatRecords :messageItemManager="messageItemManager" /> -->
            </el-col>
   
        </el-row>
    </div>
</template>


<script>
import { transformQuestion } from './ResponseOfManual.js';
import { optionsQuestion, optionsModel } from './OptionData.js';
import { sendQuestionToAPI } from './model_api.js';
import { ref, reactive, nextTick, watch } from 'vue';
import axios from 'axios';

export default {
  data() {
    return {
      messages: [],
      selectQuestion1: '',
      selectModel1: '',
      selectedRadio1: '注意力转移',
      selectedType1: '',
      rawQuestion1: '',
      changedQuestion1: '',
      optionsQuestion,
      optionsModel,
      optionsType11: [
        { value: 'option3-1', label: '注意力转移样式1' },
      ],
      optionsType12: [
        { value: 'option3-2', label: '角色扮演样式1' },
        { value: 'option3-3', label: '角色扮演样式2' },
        { value: 'option3-4', label: '角色扮演样式3' },
      ],
      optionsType13: [
        { value: 'option3-5', label: '权限提升样式1' },
        { value: 'option3-6', label: '权限提升样式2' },
        { value: 'option3-7', label: '权限提升样式3' },
        { value: 'option3-8', label: '权限提升样式4' },
        { value: 'option3-9', label: '权限提升样式5' },
        { value: 'option3-10', label: '权限提升样式6' },
      ],
      loading: false,
      waiting: false,
      nowMessageHtml: '',
      nowMessageLine: '',
      messageItemList: reactive([]),
    };
  },
  computed: {
    currentOptions() {
      // 根据 selectedRadio1 的值返回对应的选项数组
      switch (this.selectedRadio1) {
        case '注意力转移':
          return this.optionsType11;
        case '角色扮演':
          return this.optionsType12;
        case '权限提升':
          return this.optionsType13;
        default:
          return [];
      }
    }
  },
  methods: {
    handleRadioChange() {
      // 当 radio button 变化时，清空 select 的选中值
      this.selectedType1 = '';
    },
    handleQuestionChange(value) {
      this.rawQuestion1 = value;
    },
    handleTransformQuestion1() {
      this.changedQuestion1 = transformQuestion(this.rawQuestion1, this.selectedType1);
      console.log('here1');
    },
    
    async sendRawQuestion1(){
      const prompt = this.rawQuestion1;
      const model = this.selectModel1
      console.log(prompt, model)

      // 设置loading状态为true
      this.loading = true;
      
      axios.post(
        'http://localhost:5001/api/ask', 
        { prompt: prompt, 
          model: model },
        {headers: {'Content-Type': 'application/json'}}
      )
      .then(response =>{
        const answer = response.data.response.trim();
        // this.addMessageToChat(answer, false);
        this.chatBox1 = this.chatBox1 + '\n--------------------------------------------------\n' + answer;
      })
      .catch(error => {
        console.error(error);
      })
      .finally(() => {
        // 关闭loading状态
        this.loading = false;
      });
    },
        
    async sendChangedQuestion1(){
      const prompt = this.changedQuestion1;
      const model = this.selectModel1
      console.log(prompt, model)

      // 设置loading状态为true
      this.loading = true;
      
      axios.post(
        'http://localhost:5001/api/ask', 
        { prompt, model },
        {headers: {'Content-Type': 'application/json'}}
      )
      .then(response =>{
        const answer = response.data.response.trim();
        // this.addMessageToChat(answer, false);
        this.chatBox1 = this.chatBox1 + '\n--------------------------------------------------\n' + answer;
      })
      .catch(error => {
        console.error(error);
      })
      .finally(() => {
        // 关闭loading状态
        this.loading = false;
      });
    },

    addMessageToChat(content, isUser) {
      this.messageItemList.push({
        content: content,
        isUser: isUser,
      });
      this.moveScroll();
    },
    moveScroll() {
      nextTick(() => {
        const recordsBox = this.$refs.recordsBox;
        if (recordsBox) {
          recordsBox.scrollTop = recordsBox.scrollHeight;
        }
      })
    },
    watch: {
      messageItemList() {
        this.moveScroll();
      },
    },
  }
}
</script>

<style scoped>
.option-font {
  font-size: 22px;
}

.font {
  font-size: 24px;
}

.el-radio-button {
  .custom-radio-button__label{
    font-size: 24px;
  }
  
}

.raw-question {
  width: 100%;
  resize: none; /* 禁止调整大小 */
  outline: none; /* 去除聚焦时的外边框 */
  width: 100%; 
  height: 80px;
  font-size: 20px;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
</style>