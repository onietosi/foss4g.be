<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import { NuxtLink } from '#components'

// Countdown state for 25 September 2025
const timeLeft = ref({ days: 0, hours: 0, minutes: 0, seconds: 0 })
const targetDate = new Date('2025-09-25T00:00:00')

function updateCountdown() {
    const now = Date.now()
    const diff = targetDate.getTime() - now
    if (diff <= 0) {
        timeLeft.value = { days: 0, hours: 0, minutes: 0, seconds: 0 }
        return
    }
    const secs = Math.floor((diff / 1000) % 60)
    const mins = Math.floor((diff / (1000 * 60)) % 60)
    const hrs  = Math.floor((diff / (1000 * 60 * 60)) % 24)
    const days = Math.floor(diff / (1000 * 60 * 60 * 24))
    timeLeft.value = { days, hours: hrs, minutes: mins, seconds: secs }
}

let timer: ReturnType<typeof setInterval>
onMounted(() => {
    updateCountdown()
    timer = setInterval(updateCountdown, 1000)
})
onUnmounted(() => clearInterval(timer))
</script>

<template>
    <div class="min-h-screen flex flex-col font-sans text-primary-dark">
        <main class="flex-1 px-4 py-6 space-y-8 lg:px-8 lg:py-12">

            <!-- HERO -->
            <section
                class="bg-off-white py-6 rounded-xl shadow max-w-3xl mx-auto flex items-center justify-center"
            >
                <img
                    src="/images/foss4g.svg"
                    alt="FOSS4G Logo"
                    class="w-full max-w-xs sm:max-w-sm md:max-w-md lg:max-w-lg xl:max-w-xl h-60 object-contain"
                />
            </section>

            <!-- ABOUT -->
            <section
                id="about"
                class="bg-off-white px-6 py-6 rounded-xl shadow max-w-3xl mx-auto flex flex-col items-center"
            >
                <h2 class="text-lg font-bold mb-3">{{ $t('about.title') }}</h2>
                <p class="text-sm text-neutral-dark text-center mb-4">
                    {{ $t('about.teaser') }}
                </p>

                <ul class="w-full grid grid-cols-1 sm:grid-cols-2 gap-4 mb-6">
                    <li class="flex flex-col items-center space-y-2">
                        <MdiIcon icon="mdiBullhorn" size="2.5em" />
                        <span class="text-sm font-medium text-primary-dark">{{ $t('about.features.keynotes') }}</span>
                    </li>
                    <li class="flex flex-col items-center space-y-2">
                        <MdiIcon icon="mdiWrench" size="2.5em" />
                        <span class="text-sm font-medium text-primary-dark">{{ $t('about.features.workshops') }}</span>
                    </li>
                    <li class="flex flex-col items-center space-y-2">
                        <MdiIcon icon="mdiAccountMultiple" size="2.5em" />
                        <span class="text-sm font-medium text-primary-dark">{{ $t('about.features.networking') }}</span>
                    </li>
                    <li class="flex flex-col items-center space-y-2">
                        <MdiIcon icon="mdiCheck" size="2.5em" />
                        <span class="text-sm font-medium text-primary-dark">{{ $t('about.features.openSource') }}</span>
                    </li>
                </ul>

                <NuxtLink
                    to="/about"
                    class="flex justify-center border-2 border-primary text-primary font-semibold px-4 py-2 rounded-lg hover:bg-primary hover:text-white transition text-sm"
                >
                    {{ $t('about.learnMore') }}
                </NuxtLink>
            </section>

            <!-- CARDS GRID -->
            <section class="grid grid-cols-1 sm:grid-cols-2 gap-6 max-w-3xl mx-auto">
                <!-- Call for Topics -->
                <div class="bg-off-white rounded-xl shadow overflow-hidden flex flex-col sm:flex-row">
                    <div class="w-full sm:w-2/5 h-40 sm:h-auto">
                        <img
                            src="/images/megaphone.png"
                            alt="Megaphone"
                            class="w-full h-full object-contain p-4"
                        />
                    </div>
                    <div class="p-5 flex flex-col justify-center flex-1">
                        <h2 class="text-lg font-bold mb-2">{{ $t('cards.callForTopics.title') }}</h2>
                        <p class="text-sm text-neutral mb-4">
                            {{ $t('cards.callForTopics.description') }}
                        </p>
                        <NuxtLink
                            to="/submit"
                            class="flex justify-center border-2 border-primary hover:border-secondary text-primary font-semibold px-4 py-2 rounded-lg hover:bg-secondary hover:text-white transition text-sm"
                        >
                            {{ $t('cards.callForTopics.button') }}
                        </NuxtLink>
                    </div>
                </div>

                <!-- Schedule preview -->
                <div id="schedule" class="bg-primary rounded-xl shadow p-5 flex flex-col">
                    <h2 class="text-lg font-bold text-white mb-3">{{ $t('cards.schedulePreview.title') }}</h2>
                    <ul class="space-y-2 text-white flex-1 text-sm">
                        <li><span class="font-medium">{{ $t('cards.schedulePreview.day1Label') }}</span> {{ $t('cards.schedulePreview.day1Items') }}</li>
                        <li><span class="font-medium">{{ $t('cards.schedulePreview.day2Label') }}</span> {{ $t('cards.schedulePreview.day2Items') }}</li>
                    </ul>
                    <NuxtLink
                        to="/schedule"
                        class="mt-4 inline-block bg-accent-dark hover:bg-gold text-off-white hover:text-black font-semibold px-4 py-2 rounded-lg transition text-sm self-start"
                    >
                        {{ $t('cards.schedulePreview.button') }}
                    </NuxtLink>
                </div>

                <!-- Call for Sponsors -->
                <div class="bg-off-white px-2 rounded-xl shadow overflow-hidden flex flex-col sm:flex-row">
                    <div class="p-5 flex flex-col justify-center flex-1">
                        <h2 class="text-lg font-bold mb-2">{{ $t('cards.callForSponsors.title') }}</h2>
                        <p class="text-sm text-neutral mb-4">{{ $t('cards.callForSponsors.description') }}</p>
                        <NuxtLink
                            to="/sponsors"
                            class="flex justify-center border-2 border-neutral text-neutral font-semibold px-4 py-2 rounded-lg hover:bg-secondary hover:text-off-white hover:border-secondary transition text-sm"
                        >
                            {{ $t('cards.callForSponsors.button') }}
                        </NuxtLink>
                    </div>
                    <div class="w-full sm:w-2/5 h-40 sm:h-auto">
                        <img
                            src="/images/saving-pig.png"
                            alt="Piggy bank"
                            class="w-full h-full object-contain p-4"
                        />
                    </div>
                </div>

                <!-- Volunteers -->
                <div class="bg-off-white px-2 rounded-xl shadow overflow-hidden flex flex-col sm:flex-row">
                    <div class="w-full sm:w-1/3 h-40 sm:h-auto">
                        <img
                            src="/images/volunteer-image.png"
                            alt="Handshake icon"
                            class="w-full h-full object-contain"
                        />
                    </div>
                    <!-- Text panel -->
                    <div class="p-5 flex flex-col justify-center flex-1">
                        <h2 class="text-lg font-bold mb-2">
                            {{ $t('cards.volunteers.title') }}
                        </h2>
                        <p class="text-neutral text-sm mb-4">
                            {{ $t('cards.volunteers.description') }}
                        </p>
                        <NuxtLink
                            to="/volunteer"
                            class="flex justify-center border-2 border-primary hover:border-secondary text-primary font-semibold px-4 py-2 rounded-lg hover:bg-secondary hover:text-white transition text-sm"
                        >
                            <span>{{ $t('cards.volunteers.button') }}</span>
                        </NuxtLink>
                    </div>


                </div>
            </section>

            <!-- Countdown -->
            <section
                id="countdown"
                class="max-w-3xl mx-auto bg-gradient-to-r from-primary-dark to-accent text-white rounded-2xl shadow-lg p-8 grid grid-cols-2 sm:grid-cols-4 gap-4 text-center"
            >
                <div>
                    <p class="text-4xl sm:text-5xl font-extrabold">{{ timeLeft.days }}</p>
                    <span class="text-xs uppercase opacity-80">{{ $t('countdown.days') }}</span>
                </div>
                <div>
                    <p class="text-4xl sm:text-5xl font-extrabold">{{ timeLeft.hours }}</p>
                    <span class="text-xs uppercase opacity-80">{{ $t('countdown.hours') }}</span>
                </div>
                <div>
                    <p class="text-4xl sm:text-5xl font-extrabold">{{ timeLeft.minutes }}</p>
                    <span class="text-xs uppercase opacity-80">{{ $t('countdown.minutes') }}</span>
                </div>
                <div>
                    <p class="text-4xl sm:text-5xl font-extrabold">{{ timeLeft.seconds }}</p>
                    <span class="text-xs uppercase opacity-80">{{ $t('countdown.seconds') }}</span>
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