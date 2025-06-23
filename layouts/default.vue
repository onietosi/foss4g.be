<template>
    <div>
        <Html :dir="head.htmlAttrs?.dir ?? 'ltr'" :lang="head.htmlAttrs?.lang ?? 'en'">

        <Head>
            <Title>{{ title }}</Title>
            <template v-for="link in head.link" :key="link.hid">
                <Link :id="link.hid" :href="link.href" :hreflang="link.hreflang" :rel="link.rel"/>
            </template>
            <template v-for="meta in head.meta" :key="meta.hid">
                <Meta :id="meta.hid" :content="meta.content" :property="meta.property"/>
            </template>
        </Head>

        <Body>
            <!-- Wrapper div for sticky footer -->
            <div class="min-h-screen bg-primary-dark font-sans bg-repeat text-primary-dark"
                :class="bgImageClass"
            >
                <main>
                    <!-- Spacer for mobile navbar -->
                    <slot/>
                </main>

                <footer class="p-4 text-xs text-white bg-transparent">
                    <div class="flex flex-wrap items-center justify-end space-x-1">
                        <!-- Credits / copyright etc-->
                    </div>
                </footer>
            </div>
        </Body>

        </Html>
    </div>
</template>

<script lang="ts" setup>
import {useRoute} from 'vue-router'
import {computed, ref, onUnmounted, } from 'vue'
import {useI18n} from 'vue-i18n'
import {useLocaleHead} from '#i18n'
import {eventBus} from "~/eventBus";

const route = useRoute()
const {t} = useI18n()
const head = useLocaleHead()
const currentRoute = useRoute();

const bgImageClass = computed(() => {
    // if the route’s name or path contains "schedule", use background-schedule.png
    // otherwise fall back to background-topology.png
    return currentRoute.name?.toString().toLowerCase().includes('schedule') ||
    route.path.toLowerCase().includes('schedule')
        ? "bg-[url('/images/background-schedule.png')]"
        : "bg-[url('/images/background-topology.png')]"
})

const showNotification = ref(false)
const notification = ref({
    message: '',
    persistent: false,
    duration: 5000,
    variant: 'neutral'
})

const notifyHandler = (payload: any) => {
    notification.value = {
        message: payload.message,
        persistent: payload.persistent ?? false,
        duration: payload.duration ?? 5000,
        variant: payload.variant ?? 'neutral'
    }
    showNotification.value = true

    if (!notification.value.persistent) {
        setTimeout(() => {
            showNotification.value = false
        }, notification.value.duration)
    }
}

eventBus.on('notify', notifyHandler)

onUnmounted(() => {
    eventBus.off('notify', notifyHandler)
})

const title = computed(() => t(typeof route.meta.title === 'string' ? route.meta.title : 'head.title'))
// check if has argument "product"
</script>
