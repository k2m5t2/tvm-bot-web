<script setup lang="ts">
import { ref } from 'vue' // don't think this should be required b/c of Nuxt's auto-import, yet VSCode linter will still complain.
import { cos_sim, env, pipeline } from '@xenova/transformers'
import { Voy } from 'voy-search'

env.allowLocalModels = false // 되나 모르겠네?

const query = ref('')
const contents = ref([''])

// const extractor = ref()
const extractor = shallowRef()
const index = shallowRef()
const embeddings = ref()

const results = ref('')

async function load() {
  // load embedding model
  extractor.value = await pipeline('feature-extraction', 'Supabase/gte-small')

  // test data
  contents.value = [
    'That is a very happy Person',
    'That is a Happy Dog',
    'Today is a sunny day',
    'Today was depressing',
    'Do you respect me, as a person?',
    'I don\'t even know.',
  ]

  // create embeddings
  embeddings.value = (await extractor.value(contents.value, { pooling: 'cls' })).tolist()
}

// data format: { id: string, title: string, url: string, embeddings: number[] }

async function load2() {
  // Index embeddings with Voy
  const data = embeddings.value.map((x, i) => ({
    id: String(i),
    title: contents.value[i],
    url: `/path/${i}`,
    embeddings: x,
  }))
  const resource = { embeddings: data }

  index.value = new Voy(resource)
}

async function main() {
  // NOTE 1. pooling: 'cls' option is required for whole-sentence embedding generation (not token-wise)
  //      2. tolist() is used to convert tensor to JS array
  //      3. wrapping query.value as a length-1 [] isn't strictly necessary

  // Convert query into embedding vector
  const query_embeddings = (await extractor.value([query.value], { pooling: 'cls' })).tolist()[0]

  // Compute similarity scores

  // METHOD 1. cosine similarity using transformer.js
  // const similarities = embeddings.value.map(x => cos_sim(source_embeddings, x))
  // results.value = similarities

  // METHOD 2. k-d tree using Voy (Rust+WASM)
  // const result = index.search(q.result, 1);
  const top_results = index.value.search(query_embeddings, 2) // similarity search
  results.value = top_results
}

function fetchData() {
  // fetch data from sources
  
}

async function processDataAndUpdateIndex(data) {
  // chunk data, convert to embeddings, update index

}

function saveIndexToStorage() {
  // use localStorage to save serialized Voy results
}

function log() {
  // console.log(embeddings.value)
  // console.log(query.value)
}

await load()
await load2()

// Display search result
// result.neighbors.forEach((result) =>
//   console.log(`✨ voy similarity search result: "${result.title}"`)
// );
</script>

<template>
  <div>
    <input v-model="query">
    <br>
    <button @click="load()">
      Load
    </button>
    <br>
    <button @click="main()">
      Main
    </button>
    <br>
    <button @click="log()">
      Log
    </button>
    <br>
    <button @click="load2()">
      Load2
    </button>
    <!-- <button @click="asdf">
      asdf
    </button> -->
    <br>
    <p>{{ results }}</p>
    <br>
  </div>
</template>

<style scoped>

</style>
