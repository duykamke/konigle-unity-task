<script setup lang="ts">
defineProps({
    title: {
        type: String,
        required: true,
    },
    value: {
        type: Number,
        required: true,
    },
})
</script>

<template>
    <div class="bg-neutral-600 flex flex-col p-4">
        <span class="text-lg">{{title}}</span>
        <span class="text-3xl mt-6">{{value}}</span>
    </div>
</template>