<template>
    <div class="flex-1 px-4 py-6 space-y-8 lg:px-8 lg:py-12">
        <!-- Parent grid for cards -->
        <section class="grid grid-cols-1 sm:grid-cols-2 gap-6 max-w-3xl mx-auto">
            <!-- Title Card -->
            <div class="bg-off-white px-6 py-6 rounded-xl shadow overflow-hidden">
                <h2 class="text-lg font-bold mb-2">{{ $t('present.callToPresentations.title') }}</h2>
                <p class="text-sm text-neutral-dark">
                    {{ $t('present.callToPresentations.limitDateText') }}
                    <span class="font-semibold text-main-color-3">
                        {{ $t('present.callToPresentations.limitDate') }}
                    </span>
                </p>
                <p class="mt-2 text-sm text-neutral-dark">{{ $t('present.callToPresentations.pleaseSubmit') }}</p>
            </div>

            <!-- Overview Card -->
            <div class="bg-off-white px-6 py-6 rounded-xl shadow overflow-hidden">
                <h2 class="text-lg font-bold mb-2">{{ $t('present.overview.title') }}</h2>
                <p class="text-sm text-neutral-dark">{{ $t('present.overview.content1') }}</p>
                <p class="mt-2 text-sm text-neutral-dark">{{ $t('present.overview.content2') }}</p>
            </div>

            <!-- Considerations Card -->
            <div class="bg-off-white px-6 py-6 rounded-xl shadow overflow-hidden sm:col-span-2">
                <h2 class="text-lg font-bold mb-2">{{ $t('present.considerations.title') }}</h2>
                <ul class="list-disc list-inside space-y-1 ml-4 text-sm text-neutral-dark">
                    <li>{{ $t('present.considerations.duration') }}</li>
                    <li>{{ $t('present.considerations.explain') }}</li>
                    <li>{{ $t('present.considerations.message') }}</li>
                    <li>{{ $t('present.considerations.passion') }}</li>
                </ul>
            </div>

            <!-- Topics Card spanning both columns on small screens -->
            <div class="bg-off-white px-6 py-6 rounded-xl shadow overflow-hidden sm:col-span-2">
                <h2 class="text-lg font-bold mb-2">{{ $t('present.topics.title') }}</h2>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
                    <div v-for="(topic, i) in topics" :key="i" class="text-sm text-neutral-dark">
                        • {{ topic }}
                    </div>
                </div>
            </div>

            <!-- Format & Submission Card -->
            <div class="bg-off-white px-6 py-6 rounded-xl shadow overflow-hidden">
                <h2 class="text-lg font-bold mb-2">{{ $t('present.submission.title') }}</h2>
                <p class="text-sm text-neutral-dark mb-4">{{ $t('present.submission.presentations') }}</p>
                <p class="text-sm text-neutral-dark mb-4">{{ $t('present.submission.proposals') }}</p>
                <a
                    target="_blank" rel="noopener noreferrer"
                    href="https://docs.google.com/forms/d/e/1FAIpQLSdsFUSFvC8j9vrIIGVjlYshRHLIgRMtKdjiF2V2DagdtWxDmQ/viewform"
                    class="bg-main-color-1 inline-block border-2 text-white font-semibold px-4 py-2 rounded-lg hover:bg-green-800 hover:text-white transition text-sm"
                >
                    {{ $t('present.submission.submit') }}
                </a>
            </div>

            <!-- Deadline & Criteria Card -->
            <div class="bg-off-white px-6 py-6 rounded-xl shadow overflow-hidden">
                <h2 class="text-lg font-bold mb-2">{{ $t('present.criterias.title') }}</h2>
                <p class="text-sm text-neutral-dark mb-2"><span class="font-semibold">{{ $t('present.criterias.deadlineSubTitle') }}</span> {{ $t('present.criterias.deadlineContent') }}</p>
                <p class="text-sm text-neutral-dark"><span class="font-semibold">{{ $t('present.criterias.criteriasSubTitle') }}</span> {{ $t('present.criterias.criteriasContent') }}</p>
            </div>

            <!-- Contact Card -->
            <div class="bg-off-white px-6 py-6 rounded-xl shadow overflow-hidden">
                <h2 class="text-lg font-bold mb-2">{{ $t('present.questions.title') }}</h2>
                <p class="text-sm text-neutral-dark">{{ $t('present.questions.contactUsAt') }} <a href="mailto:presentation@foss4g.be" class="text-primary-dark underline">presentation@foss4g.be</a>.</p>
            </div>
        </section>
    </div>
</template>

<script setup lang="ts">
import { NuxtLinkLocale } from '#components'

const topics = [
    'Quoi de neuf dans le monde OSGeo?',
    'SIG open source: QGIS, PostGIS, GDAL, Proj…',
    'Stockage, traitement et diffusion de données spatiales web',
    'Solutions SIG réussies avec FOSS4G',
    'Architecture de solution open source',
    'Gestion de solutions géospatiales',
    'OpenStreetMap & données ouvertes',
    'Usage par gouvernements, entreprises, chercheurs',
    'Migration de commercial vers open source',
    'Chaîne FOSS4G: QGIS → PostGIS → GeoServer',
    'Intégration QGIS & bases volumineuses',
    'Extensions QGIS & dev Python',
    'Analyse spatiale à grande échelle',
    'Solutions open source pour institutions belges',
    'Autres sujets SIG & FOSS4G',
]
</script>

<style>
/* Fade transition not used here but kept for consistency */
.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.2s;
}
.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}
</style>
