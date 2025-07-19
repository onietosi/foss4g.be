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

const sponsors = [
    {
        id: 1,
        name: 'Geopostcodes',
        link: 'https://geopostcodes.com',
        logo: '/images/sponsors/geopostcodes-logo.svg',
        bgClass: 'bg-deepMapBlue',
    },
    {
        id: 2,
        name: 'GIM',
        link: 'https://gim.be',
        logo: '/images/sponsors/gim-logo.svg',
        bgClass: 'bg-white',
    },
    {
        id: 3,
        name: 'Champs libres',
        link: 'https://www.champs-libres.coop',
        logo: '/images/sponsors/champs-libres-logo.png',
        bgClass: 'bg-white',
    },
    {
        id: 4,
        name: 'OpenStreetMap Belgium',
        link: 'https://openstreetmap.be',
        logo: '/images/sponsors/osm-be-logo.svg',
        bgClass: 'bg-white',
    }
]
</script>

<template>
    <div class="min-h-screen font-sans text-primary-dark flex flex-col">
        <main class="flex-1 px-4 py-6 lg:px-8 lg:py-12 space-y-12">

            <!-- Hero -->
            <section
                class="relative bg-[url('/images/card-bg-1.png')] bg-cover bg-center py-12 rounded-xl shadow max-w-5xl mx-auto text-center"
            >
                <div class="inline-block bg-off-white bg-opacity-90 px-8 py-6 rounded-lg">
                    <h1 class="text-3xl sm:text-4xl font-extrabold mb-4">
                        {{ $t('sponsors.hero.title') }}
                    </h1>
                    <p class="text-base text-neutral-dark max-w-xl mx-auto">
                        {{ $t('sponsors.hero.description') }}
                    </p>
                </div>
            </section>

            <!-- Tier cards -->
            <section class="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-5xl mx-auto">
                <div
                    v-for="tier in tiers"
                    :key="tier.key"
                    class="bg-off-white rounded-xl overflow-hidden shadow-md flex flex-col"
                >
                    <!-- colored banner -->
                    <div :class="[tier.banner, 'h-12']"></div>

                    <div class="p-6 flex flex-col flex-1 justify-between">
                        <div>
                            <h2 class="text-xl font-bold mb-1">
                                {{ $t(tier.titleKey) }}
                            </h2>
                            <p class="text-2xl font-extrabold text-primary mb-4">
                                {{ $t(tier.priceKey) }}
                            </p>
                            <ul class="list-disc list-inside text-sm space-y-1">
                                <li v-for="adv in tier.advantages" :key="adv">
                                    {{ $t(adv) }}
                                </li>
                            </ul>
                        </div>
                        <NuxtLinkLocale
                            :to="`/contact?sponsor=${tier.key.toLowerCase()}`"
                            class="mt-6 block text-center bg-primary hover:bg-primary-dark text-off-white font-semibold py-2 rounded-lg transition"
                        >
                            {{ $t(tier.ctaKey) }}
                        </NuxtLinkLocale>
                    </div>
                </div>
            </section>

            <!-- Support banner -->
            <section
                class="relative bg-off-white
               sm:bg-[url('/images/piggy-bank-bg13.png')] sm:bg-cover sm:bg-left
               rounded-xl shadow-md max-w-5xl mx-auto overflow-hidden
               sm:aspect-[3/1]"
            >
                <div class="flex flex-col-reverse sm:flex-row h-full justify-end">
                    <div class="w-full sm:w-1/2 p-6 flex flex-col justify-center text-primary-dark">
                        <h2 class="text-lg sm:text-2xl font-bold mb-2">
                            {{ $t('sponsors.support.title') }}
                        </h2>
                        <p class="text-sm mb-4">
                            {{ $t('sponsors.support.description') }}
                        </p>
                        <!--
                        <NuxtLinkLocale
                            to="/contact?sponsor=gold"
                            class="inline-block bg-accent hover:bg-accent-dark text-off-white font-semibold px-6 py-2 rounded-lg transition w-full sm:w-auto text-center"
                        >
                            {{ $t('sponsors.support.cta') }}
                        </NuxtLinkLocale>
                        -->
                    </div>

                    <!-- Piggy-bank image below on mobile -->
                    <div class="w-full sm:hidden px-6 pt-6 flex items-center justify-center">
                        <img
                            src="/images/piggy-bank-1.png"
                            alt="Piggy bank"
                            class="w-32 h-32 object-contain mx-auto"
                        />
                    </div>
                </div>
            </section>

            <!-- Sponsors Footer -->
            <section class="max-w-5xl mx-auto px-4 py-8 bg-off-white rounded-lg shadow">
                <h3 class="text-center text-xl font-semibold text-primary mb-2">
                    {{ $t('sponsors.footer.thankYou') }}
                </h3>
                <p class="text-center text-sm text-neutral-dark mb-6">
                    {{ $t('sponsors.footer.subtext') }}
                </p>

                <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-6">
                    <a
                        v-for="s in sponsors"
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