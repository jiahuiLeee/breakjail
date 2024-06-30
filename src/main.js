import './assets/main.css'
// 引入 Element UI 组件库
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

import { createApp } from 'vue'
import HomePage from './components/HomePage.vue'
import router from './router'; // 引入路由配置文件
import * as ElementPlusIconsVue from '@element-plus/icons-vue'


// createApp(HomePage).mount('#app')
const app = createApp(HomePage)

for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
  }

app.use(ElementPlus)
app.use(router)
app.mount('#app')
