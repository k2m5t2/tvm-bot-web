<script setup lang="ts">
// import { Message } from '~/composables/chat'

const props = defineProps<{
  message: Message
}>()

const isUser = computed(() => props.message.sender === 'user')
</script>

<template>
  <div class="chat-bubble" :class="{ 'chat-bubble-user': isUser }">
    <div class="chat-bubble-text">{{ message.text }}</div>
    <!-- <div class="chat-bubble-timestamp">{{ message.timestamp.toLocaleTimeString() }}</div> -->
  </div>
</template>

<style scoped>
.chat-bubble {
  max-width: 70%;
  padding: 10px;
  border-radius: 20px;
  margin-bottom: 10px;
  font-size: 14px;
  line-height: 1.4;
  position: relative;
  clear: both;
  word-wrap: break-word;
  animation: fadeIn 0.3s ease;
}

.chat-bubble-user {
  background-color: #333;
  color: white;
  float: right;
}

.chat-bubble:not(.chat-bubble-user) {
  background-color: #e5e5ea;
  color: black;
  float: left;
}

.chat-bubble-timestamp {
  font-size: 12px;
  color: #8e8e93;
  margin-top: 5px;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
