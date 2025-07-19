<template>
    <div class="flex-1 px-4 py-6 space-y-8 lg:px-8 lg:py-12">
        <!-- Volunteer Call Grid -->
        <section class="grid grid-cols-1 sm:grid-cols-2 gap-6 max-w-3xl mx-auto">
            <!-- Volunteer Card spanning two cols -->
            <div class="bg-off-white px-6 py-6 rounded-xl shadow overflow-hidden sm:col-span-2">
                <h2 class="text-lg font-bold mb-4">À la recherche de bénévoles</h2>
                <p class="text-sm text-neutral-dark mb-4">
                    Nous recherchons des bénévoles pour nous aider à organiser le FOSS4G Belgique. Si vous êtes intéressé,
                    merci de nous contacter pour rejoindre l'équipe et contribuer au succès de l'événement.
                </p>
                <div class="text-center">
                    <NuxtLinkLocale
                        to="/contact"
                        class="inline-block border-2 border-primary text-primary font-semibold px-4 py-2 rounded-lg hover:bg-primary hover:text-white transition text-sm"
                    >
                        Nous contacter
                    </NuxtLinkLocale>
                </div>
            </div>
        </section>
    </div>
</template>

<style>
.fade-enter-active, .fade-leave-active {
    transition: opacity 0.2s;
}
.fade-enter-from, .fade-leave-to {
    opacity: 0;
}
</style>