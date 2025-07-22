<template>
    <div class="flex-1 px-4 py-6 space-y-8 lg:px-8 lg:py-12">
        <!-- Grid of contact cards -->
        <section class="grid grid-cols-1 sm:grid-cols-2 gap-6 max-w-3xl mx-auto">
            <!-- Main Contact Card spanning two cols -->
            <div class="bg-off-white px-6 py-6 rounded-xl shadow overflow-hidden sm:col-span-2 text-center">
                <h2 class="text-lg font-bold mb-4">{{ $t('contact.contactUs') }}</h2>
                <p class="text-sm text-neutral-dark mb-4">
                    {{ $t('contact.askByEmailTo') }}
                    <a href="mailto:info@foss4g.be" class="text-primary-dark underline">info@foss4g.be</a>.
                </p>
                <div class="text-center">
                    <a
                        href="mailto:info@foss4g.be"
                        class="inline-block border-2 border-primary text-primary font-semibold px-4 py-2 rounded-lg hover:bg-primary hover:text-white transition text-sm"
                    >
                        {{ $t('contact.sendAnEmail') }}
                    </a>
                </div>
            </div>

            <!-- Social Links Card spanning two cols -->
            <div class="bg-off-white px-6 py-6 rounded-xl shadow overflow-hidden sm:col-span-2">
                <h3 class="text-lg font-bold mb-2">{{ $t('contact.followUs') }}</h3>
                <ul class="list-inside list-disc space-y-2 ml-4 text-sm text-neutral-dark">
                    <li>
                        LinkedIn:
                        <a
                            href="https://www.linkedin.com/company/osgeo-be"
                            target="_blank"
                            class="text-primary-dark underline"
                        >
                            FOSS4G Belgium
                        </a>
                    </li>
                    <li>
                        Facebook:
                        <a
                            href="https://www.facebook.com/100068093147129"
                            target="_blank"
                            class="text-primary-dark underline"
                        >
                            Facebook FOSS4G Belgium
                        </a>
                    </li>
                    <li>
                        Mastodon:
                        <a
                            href="https://fosstodon.org/@osgeobe"
                            target="_blank"
                            class="text-primary-dark underline"
                        >
                            @osgeobe@fosstodon.org
                        </a>
                    </li>
                </ul>
            </div>
        </section>
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
