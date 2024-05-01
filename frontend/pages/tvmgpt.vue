<script setup lang="ts">
const online = useOnline()

function handleRightClick() {
  // do nothing

};
</script>

<template>
  <div>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <h1 class="text-7xl font-semibold">
      <span class="text-green-700">TVM</span>GPT
    </h1>
    <br>
    <SearchBar />
    <button class="rounded-full px-6 py-3 shadow-md">
      Send
    </button>
    <!-- <button>Continue Saved Chats</button> -->
    <SavedChatsButton />
    <div class="fixed bottom-4 left-4 text-left">
      <a href="/about">
        <CornerButton
          :handleClick="handleRightClick"
          location="left"
          buttonText="About"
          :index="0"
        />
      </a>
      <br>
      <a href="https://github.com/k2m5t2/tvm-bot-web" target="_blank">
        <CornerButton
          :handle-click="handleRightClick"
          location="left"
          button-text="GitHub"
          :index="1"
        />
      </a>
      <br>
      <a href="mailto:contact@yunhocho.com" target="_blank">
        <CornerButton
          :handleClick="handleRightClick"
          location="left"
          buttonText="Contact"
          :index="2"
        />
      </a>
    </div>
    <div class="fixed bottom-4 right-4 text-right">
      <a href="/settings">
        <CornerButton
          :handleClick="handleRightClick"
          location="right"
          buttonText="Settings"
          :index="0"
        />
      </a>
      <br>
      <CornerButton
        :handleClick="handleRightClick"
        location="right"
        buttonText="Explore !?"
        :index="1"
      />
      <br>
      <a href="/feedback">
        <CornerButton
          :handleClick="handleRightClick"
          location="right"
          buttonText="Feedback"
          :index="2"
        />
      </a>
    </div>
  </div>
</template>
