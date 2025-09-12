<script setup lang="ts">
import { useI18n } from 'vue-i18n'

// i18n
const { t } = useI18n()
</script>
<template>
    <div class="flex-1 px-4 py-6 space-y-8 lg:px-8 lg:py-12">
        <!-- Grid of cards -->
        <section class="grid grid-cols-1 sm:grid-cols-2 gap-6 max-w-3xl mx-auto">
            <!-- Call for maps -->
            <div class="bg-off-white px-6 py-6 rounded-xl shadow overflow-hidden sm:col-span-2 space-y-5">
                <h2 class="text-lg font-bold mb-2">{{ $t('maps.title') }}</h2>
                <p class="text-sm text-neutral-dark" v-html="$t('maps.parag_1_1')"></p>
                <p class="text-sm text-neutral-dark" v-html="$t('maps.parag_1_2')"></p>
                <p class="text-sm text-neutral-dark" v-html="$t('maps.parag_1_3')"></p>
                <p class="text-sm text-neutral-dark" v-html="$t('maps.parag_1_4')"></p>
                <p class="text-sm text-neutral-dark" v-html="$t('maps.parag_1_5')"></p>
                <p class="text-sm text-neutral-dark" v-html="$t('maps.parag_1_6')"></p>
                <h3 class="text-md font-semibold mt-4">{{ $t('maps.subtitle_2') }}</h3>
                <p class="text-sm text-neutral-dark" v-html="$t('maps.parag_2_1')"></p>
                <h3 class="text-md font-semibold mt-4">{{ $t('maps.subtitle_3') }}</h3>
                <p class="text-sm text-neutral-dark" v-html="$t('maps.parag_3_1')"></p>
                <p class="text-sm text-neutral-dark" v-html="$t('maps.parag_3_2')"></p>
                <p class="text-sm text-neutral-dark" v-html="$t('maps.parag_3_3')"></p>
                <h3 class="text-md font-semibold mt-4">{{ $t('maps.subtitle_4') }}</h3>
                <p class="text-sm text-neutral-dark" v-html="$t('maps.parag_4_1')"></p>
            </div>
        </section>
    </div>
</template>
