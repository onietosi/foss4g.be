<script setup lang="ts">
import { ref, computed } from 'vue'
import type { Ref } from 'vue'
import EventCard from '@/components/EventCard.vue'
import { useSwipe } from '@/composables/useSwipe'

// —————————————————————————————————————————————————————————————
// Types & Data
// —————————————————————————————————————————————————————————————
type Talk = {
    id: number,
    time: string
    room?: 'Fiji' | 'Zanzibar'
    title?: string
    speaker?: string
    abstract?: string
    break?: 'coffee' | 'lunch'
}

const days = [
    {
        label: 'Day 1',
        date:  '25 Sep 2025',
        sessions: <Talk[]>[
            {
                id: 1,
                time:'09:00',
                room:'Fiji',
                title:'Opening Keynote',
                speaker:'Alice Johnson',
                abstract:'Kick-off and roadmap for FOSS4G Belgium.'
            },
            {
                id: 2,
                time:'09:00',
                room:'Zanzibar',
                title:'Mapping APIs Overview',
                speaker:'Sam Williams',
                abstract:'REST, GraphQL & OGC in 15 minutes.'
            },
            {
                id: 3,
                time:'10:00',
                break:'coffee'
            },
            {
                id: 4,
                time:'10:30',
                room:'Fiji',
                title:'Geo-Arrow 101',
                speaker:'Dan Williams',
                abstract:'Accelerating geodata with Apache Arrow.'
            },
            {
                id: 5,
                time:'10:30',
                room:'Zanzibar',
                title:'Spatial Data Management',
                speaker:'Sally Brown',
                abstract:'Best practices for petabyte-scale PostGIS.'
            },
            {
                id: 6,
                time:'12:00',
                break:'lunch'
            },
            {
                id: 7,
                time:'14:00',
                room:'Fiji',
                title:'Geospatial Visualization',
                speaker:'John Smith',
                abstract:'D3, deck.gl & WebGPU demos.'
            },
            {
                id: 8,
                time:'14:00',
                room:'Zanzibar',
                title:'Building Web Maps',
                speaker:'Mark Davis',
                abstract:'From raster to vector tiles in 2025.'
            },
        ]
    },
    { label:'Day 2', date:'26 Sep 2025', sessions: <Talk[]>[] },
    { label:'Day 3', date:'27 Sep 2025', sessions: <Talk[]>[] }
]

const activeDay = ref(0)
const direction = ref<'left'|'right'>('left')

// Group sessions by time, including breaks
const groupedSessions = computed(() => {
    const map: Record<string, any> = {}
    for (const talk of days[activeDay.value].sessions) {
        if (talk.break) {
            map[`break-${talk.time}-${talk.id}`] = { ...talk }
            continue
        }
        if (!map[talk.time]) map[talk.time] = { time: talk.time }
        if (talk.room) map[talk.time]![talk.room] = talk
    }
    return Object.values(map)
})

// Icon helper
const breakIcon = (b?: Talk['break']) =>
    b === 'coffee' ? 'mdiCoffee' : 'mdiSilverwareForkKnife'

// —————————————————————————————————————————————————————————————
// Day switching with swipe
// —————————————————————————————————————————————————————————————
const container = ref<HTMLElement|null>(null)

function goTo(dayIndex: number, dir: 'left'|'right') {
    if (dayIndex < 0 || dayIndex >= days.length) return
    direction.value = dir
    activeDay.value = dayIndex
}

useSwipe(
    container as Ref<HTMLElement>,
    // swipe → go previous
    () => goTo(activeDay.value - 1, 'right'),
    // swipe ← go next
    () => goTo(activeDay.value + 1, 'left'),
)
</script>

<template>
    <div class="min-h-screen flex flex-col" ref="container">
        <!-- HEADER -->
        <header class="py-16 text-center text-off-white">
            <h1 class="text-4xl sm:text-5xl font-extrabold">Schedule</h1>
            <div class="mx-auto mt-6 w-44 h-2 bg-warning rounded-b-2xl"></div>
            <nav class="mt-10 flex justify-center gap-4 flex-wrap">
                <button
                    v-for="(d,i) in days"
                    :key="d.label"
                    @click="goTo(i, i>activeDay? 'left':'right')"
                    class="px-6 py-2 rounded-full font-semibold transition"
                    :class=" i === activeDay
                        ? 'bg-warning text-primary-dark'
                        : 'bg-primary-dark/50 hover:bg-primary-dark/70 text-off-white' "
                >
                    {{ d.label }}
                </button>
            </nav>
        </header>

        <!-- AGENDA -->
        <section class="max-w-5xl w-full mx-auto px-4 space-y-6">
            <p class="text-center text-white font-semibold mb-4">{{ days[activeDay].date }}</p>
            <!-- Room labels -->
            <div class="hidden md:grid grid-cols-2 gap-6 text-center font-semibold text-white uppercase mb-2">
              <div>Fiji</div>
              <div>Zanzibar</div>
            </div>
            <transition
                :name="`swipe-${direction}`"
                mode="out-in"
            >
                <div :key="activeDay" class="space-y-4">
                    <div
                        v-for="(row, idx) in groupedSessions"
                        :key="idx"
                        class="space-y-2"
                    >
                        <!-- BREAK -->
                        <div
                            v-if="row.break"
                            class="flex items-center gap-3 bg-warning/80 text-primary-dark rounded-xl py-3 px-4 font-semibold shadow-sm"
                        >
                            <MdiIcon :icon="breakIcon(row.break)" size="1.25em" />
                            <span class="flex-1 capitalize">
                                {{ row.break === 'coffee' ? 'Coffee Break' : 'Lunch' }}
                            </span>
                        </div>

                        <!-- TALKS -->
                        <div v-else class="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <EventCard
                                v-if="row.Fiji"
                                :key="row.Fiji.id"
                                :time="row.Fiji.time"
                                :title="row.Fiji.title!"
                                :speaker="row.Fiji.speaker!"
                                :details="row.Fiji.abstract"
                            />
                            <div v-else class="hidden md:block"></div>
                            <EventCard
                                v-if="row.Zanzibar"
                                :key="row.Zanzibar.id"
                                :time="row.Zanzibar.time"
                                :title="row.Zanzibar.title!"
                                :speaker="row.Zanzibar.speaker!"
                                :details="row.Zanzibar.abstract"
                            />
                        </div>
                    </div>
                </div>
            </transition>
        </section>
    </div>
</template>

<style lang="css">
/* swipe-left: new day slides in from right, old slides out left */
.swipe-left-enter-active,
.swipe-left-leave-active {
    transition: transform 0.3s ease;
}
.swipe-left-enter-from {
    transform: translateX(100%);
}
.swipe-left-leave-to {
    transform: translateX(-100%);
}

/* swipe-right: new day slides in from left, old slides out right */
.swipe-right-enter-active,
.swipe-right-leave-active {
    transition: transform 0.3s ease;
}
.swipe-right-enter-from {
    transform: translateX(-100%);
}
.swipe-right-leave-to {
    transform: translateX(100%);
}
</style>