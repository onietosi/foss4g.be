<template>
    <div class="flex-1 px-4 py-6 space-y-8 lg:px-8 lg:py-12">
        <!-- Parent grid for cards -->
        <section class="grid grid-cols-1 sm:grid-cols-2 gap-6 max-w-3xl mx-auto">
            <!-- Title Card -->
            <div class="bg-off-white px-6 py-6 rounded-xl shadow overflow-hidden">
                <h2 class="text-lg font-bold mb-2">Appel à présentations</h2>
                <p class="text-sm text-neutral-dark">Date limite de soumission: <span class="font-semibold text-danger">8 août 2025</span></p>
                <p class="mt-2 text-sm text-neutral-dark">Soyez partenaire du succès de l'édition 2025. Soumettez votre proposition!</p>
            </div>

            <!-- Overview Card -->
            <div class="bg-off-white px-6 py-6 rounded-xl shadow overflow-hidden">
                <h2 class="text-lg font-bold mb-2">À propos</h2>
                <p class="text-sm text-neutral-dark">Nous couvrons une grande variété de publics et de sujets liés à la géomatique: techno, geek, cas d’usage publics, privés ou professionnels.</p>
                <p class="text-sm text-neutral-dark">Notre objectif? Une conférence riche en diversité, tant sur les sujets que sur les intervenants.</p>
            </div>

            <!-- Considerations Card -->
            <div class="bg-off-white px-6 py-6 rounded-xl shadow overflow-hidden sm:col-span-2">
                <h2 class="text-lg font-bold mb-2">Quelques considérations</h2>
                <ul class="list-disc list-inside space-y-1 ml-4 text-sm text-neutral-dark">
                    <li>Durée : 25 min (20 min de présentation + 5 min de Q&A).</li>
                    <li>Expliquez clairement ce que vous souhaitez partager.</li>
                    <li>Concentrez-vous sur le message et la technologie principale.</li>
                    <li>Rendez votre talk passionnant, puis échanger autour d’un verre pour prolonger la discussion.</li>
                </ul>
            </div>

            <!-- Topics Card spanning both columns on small screens -->
            <div class="bg-off-white px-6 py-6 rounded-xl shadow overflow-hidden sm:col-span-2">
                <h2 class="text-lg font-bold mb-2">Idées de présentations</h2>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
                    <div v-for="(topic, i) in topics" :key="i" class="text-sm text-neutral-dark">
                        • {{ topic }}
                    </div>
                </div>
            </div>

            <!-- Format & Submission Card -->
            <div class="bg-off-white px-6 py-6 rounded-xl shadow overflow-hidden">
                <h2 class="text-lg font-bold mb-2">Format & soumission</h2>
                <p class="text-sm text-neutral-dark mb-4">Présentations en anglais, néerlandais ou français (20 min + 5 min Q&A). </p>
                <p class="text-sm text-neutral-dark mb-4">Propositions en FR/NL/EN.</p>
                <a
                    target="_blank" rel="noopener noreferrer"
                    href="https://docs.google.com/forms/d/e/1FAIpQLSdsFUSFvC8j9vrIIGVjlYshRHLIgRMtKdjiF2V2DagdtWxDmQ/viewform"
                    class="bg-green-600 inline-block border-2 text-white font-semibold px-4 py-2 rounded-lg hover:bg-green-800 hover:text-white transition text-sm"
                >
                    Soumettre ma présentation
                </a>
            </div>

            <!-- Deadline & Criteria Card -->
            <div class="bg-off-white px-6 py-6 rounded-xl shadow overflow-hidden">
                <h2 class="text-lg font-bold mb-2">Date limite & critères</h2>
                <p class="text-sm text-neutral-dark mb-2"><span class="font-semibold">Date limite :</span> 8 août 2025 – soumettez dès que possible.</p>
                <p class="text-sm text-neutral-dark"><span class="font-semibold">Critères :</span> Qualité, pertinence pour le public et intégration dans le programme.</p>
            </div>

            <!-- Contact Card -->
            <div class="bg-off-white px-6 py-6 rounded-xl shadow overflow-hidden">
                <h2 class="text-lg font-bold mb-2">Des questions?</h2>
                <p class="text-sm text-neutral-dark">Contactez-nous à <a href="mailto:presentation@foss4g.be" class="text-primary-dark underline">presentation@foss4g.be</a>.</p>
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
