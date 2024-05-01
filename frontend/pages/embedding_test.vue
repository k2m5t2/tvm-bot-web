<script setup lang="ts">
import { cos_sim, env, pipeline } from '@xenova/transformers';

let results = ref("")
let extractor = ref("")

env.allowLocalModels=false;

const extractorFunction = () => {
  // pipeline('feature-extraction', 'mixedbread-ai/mxbai-embed-large-v1') // NOTE ERROR (Unexpected token '<'). Idk why
  pipeline('feature-extraction', 'Supabase/gte-small')
    .then((result) => {
      extractor.value = result;
    })
    .catch((error) => {
      console.error('Error occurred while creating the pipeline:', error);
      // Handle the error or provide a fallback value if needed
      extractor.value = null;
    });
};

async function test() {
  const output = await extractor.value('This is a simple test.');
  results.value = output;
}
</script>

<template>
  <div>
    <button @click="extractorFunction">start extractor</button>
    <button @click="test">Test</button>
    <p>{{ results }}</p>
  </div>
</template>