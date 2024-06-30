<template>
    <div>
        <el-row>
            <el-col :span="16">
                <el-select 
                v-model="selectQuestion2" 
                placeholder="请选择种子问题" 
                style="width: 100%"
                @change="handleQuestionChange2">
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
                <el-select v-model="selectModel2" placeholder="请选择测试模型" style="width: 100%">
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
                                  v-model="rawQuestion2"
                                />
                            </el-col>
                            <el-col :span="2">
                                <el-button class="font" size='large' icon="Right" circle color="green" @click="sendRawQuestion2"/>
                            </el-col>
                        </el-row>                       
                    </div>
                </div>

                <el-row>
                    <div style="margin-top: 20px">
                        <el-radio-group v-model="selectEncodeType2" size="large">
                        <el-radio-button label="Base64"/>
                        <!-- <el-radio-button label="ASCII-art(仅适用英文)"/> -->
                        <el-radio-button label="Leetspeak(仅适用英文)"/>
                        <el-radio-button label="Rot13(仅适用英文)"/>
                        <el-radio-button label="-连接"/>
                        </el-radio-group>
                    </div>
                </el-row>
                <div style="margin-top: 20px">
                    <el-row>
                        <el-col :span="12">
                            <div><el-button class="font" type="danger" @click="handleTransformQuestionEncoder">异化</el-button></div>
                        </el-col>
                    </el-row>
                            
                </div>

                <div style="margin-top: 20px">
                    <h4> *点击异化按钮-->生成异化问题 </h4>
                    <div class="input">
                        <el-row>
                            <el-col :span="22">
                                <div 
                                v-html="changedQuestion2" 
                                style="white-space: 
                                pre-wrap; border: 1px 
                                solid #dcdfe6; 
                                border-radius: 4px; 
                                padding: 10px;
                                min-height: 100px;">
                                </div>
                            </el-col>
                            <el-col :span="2">
                                <el-button 
                                class="font"
                                size='large'
                                icon="Right" 
                                circle 
                                color="pink"
                                @click="sendChangedQuestion2" />
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
                        class="chatBox2 font"
                        v-model="chatBox2"
                        style="width: 100%; height: 500px; resize: none; font-family: Helvetica;"
                        type="textarea"
                        placeholder="聊天框"
                        />
                </div>
            </el-col>
   
        </el-row>
    </div>
</template>


<script>
import {transformQuestion_Encoder} from './ResponseOfCoder.js';
import { optionsQuestion, optionsModel } from './OptionData.js';
import axios from 'axios';

export default {
  data() {
    return {
      selectQuestion2: '',
      selectModel2: '',
      rawQuestion2: '',
      changedQuestion2: '',
      optionsQuestion,
      optionsModel,
      loading : false
    };
  },
  methods: {
    handleQuestionChange2(value) {
      this.rawQuestion2 = value;
    },
    handleTransformQuestionEncoder() {
      this.changedQuestion2 = transformQuestion_Encoder(this.rawQuestion2, this.selectEncodeType2);
      console.log('here');
    },
    async sendRawQuestion2(){
      const prompt = this.rawQuestion2;
      const model = this.selectModel2
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
        this.chatBox2 = this.chatBox2 + '\n--------------------------------------------------\n' + answer;
      })
      .catch(error => {
        console.error(error);
      })
      .finally(() => {
        // 关闭loading状态
        this.loading = false;
      });
    },
        
    sendChangedQuestion2(){
      const prompt = this.changedQuestion2;
      const model = this.selectModel2
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
        console.log(answer);
        // this.addMessageToChat(answer, false);
        this.chatBox2 = this.chatBox2 + '\n--------------------------------------------------\n' + answer;
      })
      .catch(error => {
        console.error(error);
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
.option-font {
  font-size: 22px;
}

.font {
  font-size: 24px;
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