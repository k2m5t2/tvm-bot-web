<!-- <script setup>
import { ref } from 'vue';

const text = ref('');
</script>

<template>
  <div class="relative">
    <textarea
      class="w-1/2 h-24 p-4 rounded-lg shadow-[inset_0_0px_10px_rgba(0,0,0,0.10)] bg-white"
      placeholder="Ask me anything..."
      v-model="text"
    ></textarea>
  </div>
</template>

<style scoped>
textarea { resize: none; }
</style> -->

<template>
  <div class="relative">
    <textarea
      class="w-1/2 h-24 p-4 rounded-2xl shadow-[inset_0_0px_10px_rgba(0,0,0,0.10)] bg-white"
      v-model="textInput"
      @input="handleInput"
    @keydown.up="navigateSuggestions('up')"
      @keydown.down="navigateSuggestions('down')"
      @keydown.enter="selectSuggestion"
    ></textarea>
    <ul v-if="suggestions.length > 0" class="suggestions mx-auto w-1/2 p-4 rounded-lg shadow-lg bg-white border-none">
      <li
        v-for="(suggestion, index) in suggestions"
        :key="index"
        :class="{ 'is-active': index === activeSuggestionIndex }"
        @click="selectSuggestion(suggestion)"
      >
        {{ suggestion }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const textInput = ref('')
const suggestions = ref([])
const activeSuggestionIndex = ref(-1)

// Replace this with your autocomplete logic
const getSuggestions = (input) => {
  // Return an array of suggestions based on the input
  return ['Suggestion 1', 'Suggestion 2', 'Suggestion 3']
}

const handleInput = () => {
  suggestions.value = getSuggestions(textInput.value)
  activeSuggestionIndex.value = -1
}

const navigateSuggestions = (direction) => {
  if (suggestions.value.length === 0) return

  if (direction === 'up') {
    activeSuggestionIndex.value =
      activeSuggestionIndex.value > 0
        ? activeSuggestionIndex.value - 1
        : suggestions.value.length - 1
  } else {
    activeSuggestionIndex.value =
      activeSuggestionIndex.value < suggestions.value.length - 1
        ? activeSuggestionIndex.value + 1
        : 0
  }
}

const selectSuggestion = (suggestion) => {
  if (suggestion) {
    textInput.value = suggestion
    suggestions.value = []
  } else if (activeSuggestionIndex.value !== -1) {
    textInput.value = suggestions.value[activeSuggestionIndex.value]
    suggestions.value = []
  }
}
</script>

<style>
.suggestions {
  list-style-type: none;
}

.suggestions li {
  cursor: pointer;
  padding: 0.5rem;
}

.suggestions li.is-active {
  background-color: #f0f0f0;
}

textarea { resize: none; }
</style>