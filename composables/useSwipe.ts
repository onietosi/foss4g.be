// composables/useSwipe.ts
import { onMounted, onUnmounted } from 'vue'
import type { Ref } from 'vue'

export function useSwipe(
    el: Ref<HTMLElement | null>,
    onLeft: () => void,
    onRight: () => void
) {
    let x0: number | null = null

    function handleTouchStart(e: TouchEvent) {
        x0 = e.changedTouches[0].clientX
    }
    function handleTouchEnd(e: TouchEvent) {
        if (x0 === null) return
        const dx = e.changedTouches[0].clientX - x0
        if (dx > 50) onRight()
        else if (dx < -50) onLeft()
        x0 = null
    }

    onMounted(() => {
        const el0 = el.value
        if (!el0) return
        el0.addEventListener('touchstart', handleTouchStart)
        el0.addEventListener('touchend', handleTouchEnd)
    })
    onUnmounted(() => {
        const el0 = el.value
        if (!el0) return
        el0.removeEventListener('touchstart', handleTouchStart)
        el0.removeEventListener('touchend', handleTouchEnd)
    })
}