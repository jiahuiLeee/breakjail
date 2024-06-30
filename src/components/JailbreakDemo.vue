<template>
    <el-container>
        <el-main>
            <el-tabs type="border-card" class="custom-tabs">
                <el-tab-pane label="基于人工设计的攻击" class="tab-font tab-bgcolor">
                    <Manual />
                </el-tab-pane>
                <el-tab-pane label="基于编码的攻击" class="tab-font tab-bgcolor">
                    <Coder />
                </el-tab-pane>
                <el-tab-pane label="基于模型生成的攻击" class="tab-font tab-bgcolor">
                    <ModelGen />
                </el-tab-pane>
            </el-tabs>
        </el-main>
    </el-container>
</template>

<style scoped>
.tab-font {
    font-size: 24px;
}

.el-container,
.el-main,
.el-tabs {
    margin: 0;
    padding: 0;
    height: 100%;
    width: 100%;
}

.custom-tabs :deep(.el-tabs__item) {
    font-size: 24px; /* 调整标签字体大小 */
    /* background-color: #303133; */
}

.tab-bgcolor {
    /* background-color: #303133; */
    height: 100%;
    color: black;
}
</style>


<script>
import Manual from './JailbreakDemo/BaseManual.vue'; // 导入子组件
import Coder from './JailbreakDemo/BaseCoder.vue'
import ModelGen from './JailbreakDemo/BaseModelGenerate.vue'

export default {
  name: 'JailbreakDemo',
  components: {
    Manual, // 注册子组件
    Coder,
    ModelGen
  }
};
</script>
