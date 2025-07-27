<script setup lang="ts">
import { NuxtLink } from '#components'

// array of i18n keys:
const tiers = [
    {
        key: 'Gold',
        titleKey: 'sponsors.tiers.gold.title',
        priceKey: 'sponsors.tiers.gold.price',
        banner: 'bg-gold',
        advantages: [
            'sponsors.tiers.gold.features.0',
            'sponsors.tiers.gold.features.1',
            'sponsors.tiers.gold.features.2',
        ],
        ctaKey: 'sponsors.tiers.gold.cta',
    },
    {
        key: 'Silver',
        titleKey: 'sponsors.tiers.silver.title',
        priceKey: 'sponsors.tiers.silver.price',
        banner: 'bg-silver',
        advantages: [
            'sponsors.tiers.silver.features.0',
            'sponsors.tiers.silver.features.1',
        ],
        ctaKey: 'sponsors.tiers.silver.cta',
    },
    {
        key: 'Bronze',
        titleKey: 'sponsors.tiers.bronze.title',
        priceKey: 'sponsors.tiers.bronze.price',
        banner: 'bg-bronze',
        advantages: [
            'sponsors.tiers.bronze.features.0',
            'sponsors.tiers.bronze.features.1',
        ],
        ctaKey: 'sponsors.tiers.bronze.cta',
    },
]

const sponsors_gold = [
]

const sponsors_silver = [
    {
        id: 1,
        name: 'Champs libres',
        link: 'https://www.champs-libres.coop',
        logo: '/images/sponsors/champslibres-logo.svg',
        bgClass: 'bg-white',
    },
    {
        id: 2,
        name: 'Geo Solutions',
        link: 'https://geosolutions.be/',
        logo: '/images/sponsors/geosolutions-logo.jpg',
        bgClass: 'bg-white',
    },
]

const sponsors_bronze = [
    {
        id: 3,
        name: 'Atelier Cartographique',
        link: 'https://atelier-cartographique.be/',
        logo: '/images/sponsors/ateliercartographique-logo.svg',
        bgClass: 'bg-white',
    },
    {
        id: 4,
        name: 'Spacebel',
        link: 'https://www.spacebel.com/',
        logo: '/images/sponsors/spacebel-logo.svg',
        bgClass: 'bg-white',
    },
]
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