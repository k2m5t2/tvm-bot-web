<script setup lang="ts">
import { useChatStore } from '~/composables/chat'

const chatStore = useChatStore()
const newMessage = ref('')

function sendMessage() {
  if (newMessage.value.trim()) {
    chatStore.addMessage(newMessage.value.trim(), 'user')
    newMessage.value = ''
  }
}
</script>

<template>
  <div class="chat-container flex justify-center">
    <div class="chat-messages w-1/2">
      <ChatBubble v-for="message in chatStore.messages" :key="message.id" :message="message" />
    </div>
    <div class="chat-input-container fixed bottom-20 left-0 right-0 flex justify-center">
      <div class="chat-input w-1/2 p-4 rounded-lg shadow-[inset_0_0px_10px_rgba(0,0,0,0.10)] bg-white">
      <input v-model="newMessage" @keyup.enter="sendMessage" placeholder="Type a message..." class="w-3/4"></input>
      <button @click="sendMessage">Send</button>
    </div>
    </div>
  </div>
</template>

<style scoped>
/* .chat-container {
  display: flex;
  flex-direction: column;
  height: 50vh;
  padding: 20px;
} */

</style>