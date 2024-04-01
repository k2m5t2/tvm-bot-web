import { defineStore } from 'pinia'

export interface Message {
  id: number
  text: string
  sender: 'user' | 'bot'
  timestamp: Date
}

export const useChatStore = defineStore('chat', () => {
  const messages = ref<Message[]>([])

  function addMessage(text: string, sender: 'user' | 'bot') {
    const newMessage: Message = {
      id: Date.now(),
      text,
      sender,
      timestamp: new Date(),
    }
    messages.value.push(newMessage)
  }

  return {
    messages,
    addMessage,
  }
})
