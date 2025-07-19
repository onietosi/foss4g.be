<template>
    <div class="flex-1 px-4 py-6 space-y-8 lg:px-8 lg:py-12">
        <!-- Grid of cards -->
        <section class="grid grid-cols-1 sm:grid-cols-2 gap-6 max-w-3xl mx-auto">
            <!-- Who We Are -->
            <div class="bg-off-white px-6 py-6 rounded-xl shadow overflow-hidden sm:col-span-2">
                <h2 class="text-lg font-bold mb-2">Qui sommes-nous ?</h2>
                <p class="text-sm text-neutral-dark">
                    Nous sommes le chapitre belge de la Open Source Geospatial Foundation (OSGeo).
                </p>
            </div>

            <!-- Event Info -->
            <div class="bg-off-white px-6 py-6 rounded-xl shadow overflow-hidden sm:col-span-2">
                <h3 class="text-lg font-bold mb-2">Événement FOSS4G Belgium 2025</h3>
                <p class="text-sm text-neutral-dark">
                    Rejoignez-nous le <span class="font-semibold">25 septembre 2025</span> à Bruxelles pour une conférence d’une journée
                    avec discours, ateliers pratiques et réseautage autour des outils géospatiaux open-source.
                </p>
            </div>
            <!-- Conference Details Card -->
            <div class="bg-off-white px-6 py-6 rounded-xl shadow overflow-hidden sm:col-span-2">
                <h3 class="text-lg font-bold mb-2">La conférence FOSS4G</h3>
                <ul class="list-disc list-inside space-y-1 ml-4 text-sm text-neutral-dark">
                    <li><span class="font-semibold">Discours &amp; Présentations</span> : sessions animées par des experts du domaine.</li>
                    <li><span class="font-semibold">Réseautage Communautaire</span> : rencontres et échanges avec la communauté SIG open-source.</li>
                    <li><span class="font-semibold">Outils OSGeo</span> : démonstrations et ateliers pratiques sur QGIS, PostGIS, GDAL, et plus.</li>
                </ul>
            </div>

            <!-- Mission Card -->
            <div class="bg-off-white px-6 py-6 rounded-xl shadow overflow-hidden">
                <h3 class="text-lg font-bold mb-2">Notre mission</h3>
                <p class="text-sm text-neutral-dark">
                    OSGeo est une organisation à but non lucratif dont la mission est de soutenir le développement de logiciels
                    géospatiaux open source et de promouvoir leur utilisation. La fondation fournit un soutien financier,
                    organisationnel et juridique à la communauté géospatiale open source au sens large.
                </p>
            </div>

            <!-- Support & Advocacy Card -->
            <div class="bg-off-white px-6 py-6 rounded-xl shadow overflow-hidden">
                <h3 class="text-lg font-bold mb-2">Support</h3>
                <p class="text-sm text-neutral-dark">
                    Elle sert d'entité juridique indépendante où les membres peuvent contribuer par du code, des financements et
                    d'autres ressources, assurant la préservation des contributions pour le bénéfice public. OSGeo agit aussi en
                    tant qu'organisation de sensibilisation et de plaidoyer, offrant forum et infrastructure partagée pour
                    renforcer la collaboration entre projets.
                </p>
            </div>

            <!-- Open Source Projects Card -->
            <div class="bg-off-white px-6 py-6 rounded-xl shadow overflow-hidden sm:col-span-2">
                <h3 class="text-lg font-bold mb-2">Projets open source</h3>
                <p class="text-sm text-neutral-dark">
                    Les projets de la fondation sont tous librement disponibles et utilisables sous une licence open source
                    certifiée par l'OSI.
                </p>
            </div>
        </section>
    </div>
</template>

<script setup lang="ts">
import { NuxtLinkLocale } from '#components'
</script>

<style>
/* Transition classes */
.fade-enter-active, .fade-leave-active {
    transition: opacity 0.2s;
}
.fade-enter-from, .fade-leave-to {
    opacity: 0;
}
</style>
