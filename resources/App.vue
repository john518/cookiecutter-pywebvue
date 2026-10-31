<template>
  <!-- Splash screen hidden via CSS when ready -->
  <div v-show="!isReady" class="splash-screen">
    <div class="spinner-container">
      <p>Starting {{ projectName }}...</p>
    </div>
  </div>

  <!-- Child component is rendered immediately in the background, keeping childRef valid -->
  <HelloWorld ref="childRef" v-show="isReady" />
</template>

<script setup>
import { ref, onMounted } from 'vue'
import HelloWorld from './components/HelloWorld.vue'

const projectName = ref("@PROJECT_NAME@")
const isReady = ref(false)
const childRef = ref(null)

onMounted(async () => {
  // Wait for Python-Javascript bridge to be initialized and ready
  const startTime = Date.now()
  const timeoutMs = 3000

  while (Date.now() - startTime < timeoutMs) {
    if (window.pywebview && window.pywebview.api && typeof window.pywebview.api.ping === 'function') {
      try {
        const response = await window.pywebview.api.ping()
        if (response && response.status === 'ok') {
          // await new Promise(resolve => setTimeout(resolve, 1000))  // for debug only

          isReady.value = true  // display the child component

          // Call onBackendReady method on child component
          if (childRef.value) {
            childRef.value.onBackendReady()
          }
          else {
            console.error("childRef component is not mounted => cannot proceed")
          }
          return
        }
      } catch (e) {
        // IPC pipe not fully warm yet, retry on next loop
      }
    }
    await new Promise(resolve => setTimeout(resolve, 50))
  }

  console.error("Failed to connect to Python backend within timeout.")
})
</script>

<style scoped>
.splash-screen {
  width: 100vw;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f8fafc;
  color: #475569;
  font-family: inherit;
  font-size: 1.1rem;
}
</style>
