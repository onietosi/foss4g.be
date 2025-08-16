<script setup lang="ts">
import sponsorsData from '~/assets/sponsors-data.json'
import type { Sponsor } from '~/types/sponsors'

// Use centralized sponsor data
const sponsors_gold: Sponsor[] = sponsorsData.gold
const sponsors_silver: Sponsor[] = sponsorsData.silver
const sponsors_bronze: Sponsor[] = sponsorsData.bronze
</script>

<template>
    <div class="min-h-screen font-sans text-primary-dark flex flex-col">
        <main class="flex-1 px-4 py-6 lg:px-8 lg:py-12 space-y-12">
            <!-- Sponsors Footer -->
            <section class="max-w-5xl mx-auto px-4 py-8 bg-off-white rounded-lg shadow">
                <h3 class="text-center text-xl font-semibold text-primary mb-2">
                    {{ $t('sponsors.footer.thankYou') }}
                </h3>
                <p class="text-center text-sm text-neutral-dark mb-6">
                    {{ $t('sponsors.footer.subtext') }}
                </p>

                <!-- h4 class="mb-2 mt-2 font-semibold">{{ $t('sponsors.gold') }}</h4 -->

                <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-6">
                    <a
                        v-for="s in sponsors_gold"
                        :key="s.id"
                        :href="s.link"
                        target="_blank"
                        rel="noopener"
                        :class="[
                          'group rounded-lg border border-neutral-light p-6 flex flex-col items-center text-center transition-shadow filter sm:grayscale sm:opacity-60 sm:hover:filter-none sm:hover:opacity-100 sm:hover:shadow-lg',
                          s.bgClass
                        ]"
                    >
                        <img
                            :src="s.logo"
                            :alt="`${s.name} logo`"
                            class="pointer-events-none h-16 w-auto mb-4 object-contain transition-transform group-hover:scale-105"
                        />
                    </a>
                </div>

                <h4 class="mb-2 mt-2 font-semibold">{{ $t('sponsors.silver') }}</h4>


                <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-6">
                    <a
                        v-for="s in sponsors_silver"
                        :key="s.id"
                        :href="s.link"
                        target="_blank"
                        rel="noopener"
                        :class="[
                          'group rounded-lg border border-neutral-light p-6 flex flex-col items-center text-center transition-shadow filter sm:grayscale sm:opacity-60 sm:hover:filter-none sm:hover:opacity-100 sm:hover:shadow-lg',
                          s.bgClass
                        ]"
                    >
                        <img
                            :src="s.logo"
                            :alt="`${s.name} logo`"
                            class="pointer-events-none h-16 w-auto mb-4 object-contain transition-transform group-hover:scale-105"
                        />
                    </a>
                </div>

                <h4 class="mb-2 mt-2 font-semibold">{{ $t('sponsors.bronze') }}</h4>

                <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-6">
                    <a
                        v-for="s in sponsors_bronze"
                        :key="s.id"
                        :href="s.link"
                        target="_blank"
                        rel="noopener"
                        :class="[
                          'group rounded-lg border border-neutral-light p-6 flex flex-col items-center text-center transition-shadow filter sm:grayscale sm:opacity-60 sm:hover:filter-none sm:hover:opacity-100 sm:hover:shadow-lg',
                          s.bgClass
                        ]"
                    >
                        <img
                            :src="s.logo"
                            :alt="`${s.name} logo`"
                            class="pointer-events-none h-16 w-auto mb-4 object-contain transition-transform group-hover:scale-105"
                        />
                    </a>
                </div>


            </section>
        </main>
    </div>
</template>

<style>
.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.2s;
}
.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}
</style>
