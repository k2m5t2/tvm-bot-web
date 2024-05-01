<script setup lang="ts">
// slowly integrating parts of original code (part by part)

// new
import * as webllm from '@mlc-ai/web-llm'
import type { AppConfig } from '@mlc-ai/web-llm'
import appConfig from '~/config/app-config'
import { useChatStore } from '~/composables/chat'

// old 
// import { ChatInterface, ChatModule, ChatRestModule, ChatWorkerClient, AppConfig } from "@mlc-ai/web-llm";
// import { useChatStore } from '~/composables/chat'
// import appConfig from "~/config/app-config";

// const chat = ref<ChatInterface | null>(null)
// const localChat = ref<ChatInterface | null>(null)
// const selectedModel = ref('')
// const chatLoaded = ref(false)
const requestInProgress = ref(false)
// const chatRequestChain = ref<Promise<void>>(Promise.resolve())
// const config: AppConfig = appConfig;


const chatStore = useChatStore()
const newMessage = ref('')

const config: AppConfig = appConfig // does this work just fine!?

// const chat = ref() // ERROR
const chat = shallowRef() // solves it // https://stackoverflow.com/a/75150991
// const chat = ref(new webllm.ChatModule())

// =========
// old
// =========

// onMounted(async () => {
//   const useWebWorker = appConfig.use_web_worker;

//   if (useWebWorker) {
//     chat.value = new ChatWorkerClient(new Worker(
//       new URL('./worker.ts', import.meta.url),
//       { type: 'module' }
//     ));
//     localChat.value = new ChatRestModule();
//   } else {
//     chat.value = new ChatModule();
//     localChat.value = new ChatRestModule();
//   }

//   await initChat();
// })

// async function initChat() {
//   if (chatLoaded.value) return;
//   requestInProgress.value = true;
//   appendMessage("init", "");
//   const initProgressCallback = (report) => {
//     updateLastMessage("init", report.text);
//   }
//   chat.value?.setInitProgressCallback(initProgressCallback);

//   try {
//     if (selectedModel.value != "Local Server") {
//       await chat.value?.reload(selectedModel.value, undefined, config);
//     }
//   } catch (err) {
//     appendMessage("error", "Init error, " + err.toString());
//     console.log(err.stack);
//     await unloadChat();
//     requestInProgress.value = false;
//     return;
//   }
//   requestInProgress.value = false;
//   chatLoaded.value = true;
// }

// async function unloadChat() {
//   await chat.value?.unload();
//   chatLoaded.value = false;
// }

function appendMessage(kind: string, text: string) {
  if (kind === "init") {
    text = "[System Initialize] " + text;
  }
  chatStore.addMessage(text, kind);
}

function updateLastMessage(kind, text) {
  // if (kind == "init") {
  //   text = "[System Initialize] " + text;
  // }
  chatStore.updateLastMessage(text, kind);
}

async function sendMessage() {
  if (newMessage.value.trim()) {
    chatStore.addMessage(newMessage.value.trim(), 'user')
    // newMessage.value = ''; // clear the input field
    await asyncGenerate(newMessage.value.trim());
  }
}

async function asyncGenerate(prompt: string) {
  // await initChat();
  requestInProgress.value = true;

  // appendMessage("user", prompt);

  // appendMessage("assistant", "");
  const callbackUpdateResponse = (step, msg) => {
    updateLastMessage("assistant", msg);
  };
  
  // try {
    // const output = await chat.value?.generate(prompt, callbackUpdateResponse);
    chatStore.addMessage('', "bot")
    await chat.value?.generate(prompt, callbackUpdateResponse);
    // updateLastMessage("assistant", output);
  // } catch (err) {
  //   appendMessage("error", "ERROR: " + err.toString());
  //   console.log(err.stack);
  //   await unloadChat();
  // }
  requestInProgress.value = false;
}

// =========
// new
// =========

// We use label to intentionally keep it simple
function setLabel(id: string, text: string) {
  const label = document.getElementById(id)
  if (label == null)
    throw new Error(`Cannot find label ${id}`)

  label.textContent = text
}

async function main() {
  chat.value = new webllm.ChatModule()
  // console.log(config)

  // create a ChatModule,
  // This callback allows us to report initialization progress
  chat.value.setInitProgressCallback((report: webllm.InitProgressReport) => {
    setLabel('init-label', report.text)
  })
  // You can also try out "RedPajama-INCITE-Chat-3B-v1-q4f32_1"
  // await chat.reload('Llama-2-7b-chat-hf-q4f32_1')
  await chat.value.reload('NeuralHermes-2.5-Mistral-7B-q4f16_1', undefined, config)

  const generateProgressCallback = (_step: number, message: string) => {
    setLabel('generate-label', message)
  }

  // const prompt0 = 'What is the capital of Canada?'
  // setLabel('prompt-label', prompt0)
  // const reply0 = await chat.value.generate(prompt0, generateProgressCallback)
  // console.log(reply0)

  // const prompt1 = 'Can you write a poem about it?'
  // setLabel('prompt-label', prompt1)
  // const reply1 = await chat.value.generate(prompt1, generateProgressCallback)
  // console.log(reply1)

  // console.log(await chat.runtimeStatsText())
}

main()
</script>

<template>
  <div>
    <div>
      <h2 class="text-3xl font-semibold">
        <span class="text-green-700">TVM</span>GPT
      </h2>
      <p id="init-label" class="text-xs" />
    </div>
    <div class="chat-container flex justify-center">
      <div id="prompt-label" />
      <div id="generate-label" />
      <div class="chat-messages w-1/2">
        <ChatBubble v-for="message in chatStore.messages" :key="message.id" :message="message" />
      </div>
      <div class="chat-input-container fixed bottom-20 left-0 right-0 flex justify-center">
        <div class="chat-input w-1/2 rounded-lg bg-white p-4 shadow-[inset_0_0px_10px_rgba(0,0,0,0.10)]">
          <input v-model="newMessage" placeholder="Type a message..." class="w-3/4" @keyup.enter="sendMessage"></input>
          <button @click="sendMessage">
            Send
          </button>
        </div>
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
