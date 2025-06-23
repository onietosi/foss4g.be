<template>
    <article
        class="group relative flex flex-col sm:flex-row gap-4
           bg-off-white/90 backdrop-blur rounded-xl shadow px-5 py-4
           transition hover:shadow-lg"
    >
        <!-- time badge -->
        <div
            class="flex-none w-20 sm:w-24 h-12 sm:h-14 grid place-content-center
             rounded-lg bg-warning text-primary-dark font-extrabold
             text-base sm:text-lg tracking-wide"
        >
            {{ time }}
        </div>

        <!-- talk info -->
        <div class="flex-1">
            <h3 class="text-primary-dark font-semibold text-lg sm:text-xl leading-tight">
                {{ title }}
            </h3>
            <p class="mt-1 flex items-center gap-1 text-neutral text-sm sm:text-base">
                <MdiIcon icon="mdiMapMarker" size="1em" class="text-primary" />
                {{ speaker }}
            </p>

            <!-- expandable abstract -->
            <Transition name="fade">
                <p
                    v-if="open"
                    class="mt-3 text-neutral-dark text-sm leading-relaxed
                 border-l-4 border-warning pl-3"
                >
                    {{ details }}
                </p>
            </Transition>
        </div>

        <!-- toggle button -->
        <button
            @click="open = !open"
            class="absolute right-3 top-3 sm:static sm:self-center w-8 h-8
             rounded-full bg-warning/90 hover:bg-warning grid place-content-center
             text-primary-dark shadow-md transition"
            :aria-label="open ? 'collapse' : 'expand'"
        >
            <MdiIcon :icon="open ? 'mdiMinus' : 'mdiPlus'" size="1.1em" />
        </button>
    </article>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { MdiIcon } from '#components' // ← Nuxt auto-imports this alias

defineProps<{
    key: number
    time: string
    title: string
    speaker: string
    details?: string
}>()

const open = ref(false)
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.2s ease;
}
.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}
</style>