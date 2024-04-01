<!-- class="fixed bottom-4 px-6 py-3 rounded-full shadow-md bg-white-500 text-gray-700" -->
<template>
  <button
    class="px-3 py-2 m-1 rounded-2xl shadow-md bg-white-500 text-gray-700"
    :class="[buttonPositionClass, buttonVerticalPositionClass]"
    @click="handleClick"
  >
    {{ buttonText }}
  </button>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
  handleClick: {
    type: Function,
    required: true,
  },
  location: {
    type: String,
    required: true,
    validator: (value) => ['left', 'right'].includes(value),
  },
  buttonText: {
    type: String,
    required: true,
  },
  index: {
    type: Number,
    required: true,
  },
});

const buttonPositionClass = computed(() => {
  return props.location === 'left' ? 'left-4' : 'right-4';
});

const buttonVerticalPositionClass = computed(() => {
  return `mb-[${4 + props.index * 12}rem]`;
});
</script>