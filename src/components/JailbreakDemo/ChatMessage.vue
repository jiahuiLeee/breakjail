<!-- src/components/ChatMessage.vue -->
<template>
  <div :class="['chat-message', message.role]">
    <p>{{ message.content }}</p>
  </div>
</template>

<script>
export default {
  props: {
    message: Object
  }
};
</script>

<style scoped>
.chat-message {
  margin: 10px 0;
  padding: 10px;
  border-radius: 4px;
  max-width: 60%;
}
.chat-message.user {
  background-color: #007bff;
  color: white;
  align-self: flex-end;
}
.chat-message.bot {
  background-color: #f1f1f1;
  align-self: flex-start;
}
</style>
