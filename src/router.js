import { createRouter, createWebHistory } from 'vue-router';
import Welcome from './components/Welcome.vue';
import JailbreakDemo from './components/JailbreakDemo.vue';
import GandalfGame from './components/GandalfGame.vue';
import PrivacySafetyGame from './components/PrivacySafetyGame.vue';
import TargetHijackGame from './components/TargetHijackGame.vue';

const routes = [
    { path: '/', component: Welcome },
    { path: '/jailbreak-demo', component: JailbreakDemo },
    { path: '/gandalf-game', component: GandalfGame },
    { path: '/privacy-safety-game', component: PrivacySafetyGame },
    { path: '/target-hijack-game', component: TargetHijackGame }
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;
