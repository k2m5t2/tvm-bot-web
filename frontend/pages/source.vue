<script setup lang="ts">
import {plugins, clone, commit, push} from 'isomorphic-git'
// import http from 'https://unpkg.com/isomorphic-git@beta/http/web/index.js'
import FS from '@isomorphic-git/lightning-fs';

const fs = new FS("testfs")
const pfs = fs.promises;
// const git = window.isomorphicGit;

async function cloneRepo() {
  await clone({
    fs: pfs,
    dir: '/repo',
    url: 'https://github.com/user/repository.git',
    corsProxy: 'https://cors.isomorphic-git.org'
  });
  console.log('Repository cloned!');
}

cloneRepo().catch(console.error);


</script>
