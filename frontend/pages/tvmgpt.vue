<script setup lang="ts">

const online = useOnline()
</script>

<template>
  <div>
    <br/>
    <br/>
    <br/>
    <br/>
    <br/>
    <br/>
    <h1 class="text-7xl font-semibold"><span class="text-green-700">TVM</span>GPT</h1>
    <br/>
    <SearchBar></SearchBar>
    <button class="px-6 py-3 rounded-full shadow-md">Send</button>
    <!-- <button>Continue Saved Chats</button> -->
    <SavedChatsButton></SavedChatsButton>
    <div class="fixed bottom-4 left-4 text-left">
      <CornerButton
        :handleClick="handleRightClick"
        location="left"
        buttonText="About"
        :index="0"
      />
      <br/>
      <CornerButton
        :handleClick="handleRightClick"
        location="left"
        buttonText="GitHub"
        :index="1"
      />
      <br/>
      <CornerButton
        :handleClick="handleRightClick"
        location="left"
        buttonText="Contact"
        :index="2"
      />
    </div>
    <div class="fixed bottom-4 right-4 text-right">
      <CornerButton
        :handleClick="handleRightClick"
        location="right"
        buttonText="Settings"
        :index="0"
      />
      <br/>
      <CornerButton
        :handleClick="handleRightClick"
        location="right"
        buttonText="Explore !?"
        index="1"
      />
      <br/>
      <CornerButton
        :handleClick="handleRightClick"
        location="right"
        buttonText="Feedback"
        :index="2"
      />
    </div>

  </div>
</template>
