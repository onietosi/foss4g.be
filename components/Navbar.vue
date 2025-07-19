<template>
    <nav class="fixed inset-x-0 top-0 bg-stone-light/90 backdrop-blur-md z-20">
        <div class="max-w-7xl mx-auto px-4 py-3 flex items-center justify-between">
            <!-- Logo / Brand -->
            <NuxtLinkLocale to="/" class="text-teal-dark font-bold text-lg">
                FOSS4G BELGIUM 2025
            </NuxtLinkLocale>

            <!-- Desktop Links -->
            <ul class="hidden md:flex space-x-6">
                <li><NuxtLinkLocale to="/about" class="hover:text-teal-dark">{{ $t('nav.about') }}</NuxtLinkLocale></li>
                <!--<li><NuxtLinkLocale to="/schedule" class="hover:text-teal-dark">{{ $t('nav.schedule') }}</NuxtLinkLocale></li>-->
                <li><NuxtLinkLocale to="/our-sponsors" class="hover:text-teal-dark">{{ $t('nav.ourSponsors') }}</NuxtLinkLocale></li>
                <li><NuxtLinkLocale to="/become-sponsor" class="hover:text-teal-dark">{{ $t('nav.becomeSponsor') }}</NuxtLinkLocale></li>
                <li><NuxtLinkLocale to="/volunteer" class="hover:text-teal-dark">{{ $t('nav.volunteer') }}</NuxtLinkLocale></li>
            </ul>

            <!-- Mobile Toggle Button (now z-30) -->
            <button
                @click="isOpen = !isOpen"
                aria-label="Toggle menu"
                class="md:hidden relative z-30 w-8 h-8"
            >
                <!-- CLOSED: three‐line burger -->
                <span
                    v-if="!isOpen"
                    class="absolute inset-0 flex flex-col items-center justify-center space-y-1.5"
                >
                  <span class="block w-6 h-0.5 bg-teal-dark"></span>
                  <span class="block w-6 h-0.5 bg-teal-dark"></span>
                  <span class="block w-6 h-0.5 bg-teal-dark"></span>
                </span>

                <!-- OPEN: two crossed lines -->
                <span v-else class="absolute inset-0">
                  <span
                      class="absolute inset-0 m-auto block w-6 h-0.5 bg-teal-dark transform rotate-45 origin-center"
                  ></span>
                  <span
                      class="absolute inset-0 m-auto block w-6 h-0.5 bg-teal-dark transform -rotate-45 origin-center"
                  ></span>
                </span>
            </button>
        </div>

        <!-- Fullscreen Mobile Menu Overlay -->
        <transition name="fade">
            <div
                v-if="isOpen"
                @click.self="close()"
                class="absolute inset-0 h-screen bg-stone-light/95 backdrop-blur-md flex flex-col items-center justify-center space-y-6 z-20"
            >
                <router-link @click="close()" to="/" class="text-teal-dark text-xl">{{ $t('nav.home') }}</router-link>
                <router-link @click="close()" to="/schedule" class="text-teal-dark text-xl">{{ $t('nav.schedule') }}</router-link>
                <router-link @click="close()" to="/sponsors" class="text-teal-dark text-xl">{{ $t('nav.sponsors') }}</router-link>
                <router-link @click="close()" to="/volunteer" class="text-teal-dark text-xl">{{ $t('nav.volunteers') }}</router-link>
            </div>
        </transition>
    </nav>
</template>

<script setup lang="ts">
import { ref } from 'vue'
const isOpen = ref(false)
function close() {
    isOpen.value = false
}
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