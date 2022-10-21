<script setup lang="ts">
import Card from './Card.vue'
import { DateTime } from 'luxon'
import { useFetch } from '@vueuse/core'
import { User, UserCount } from '../models/user';

const UNITY_API = import.meta.env.UNITY_API || 'http://localhost:8000/api'

const currentMonth = DateTime.now().toLocaleString(DateTime.DATE_FULL);

const { data: totalCount } = useFetch(
    `${UNITY_API}/users/count/`
).json<UserCount>()

const { data: monthlyCount } = useFetch(
    `${UNITY_API}/users/count/?from_date=${DateTime.now().minus({ 'months': 1 }).toISODate()}`
).json<UserCount>()

const { data: unsubscribedCount } = useFetch(
    `${UNITY_API}/users/count/?subscription_status=0`
).json<UserCount>()

const { data: users } = useFetch(`${UNITY_API}/users/`, {
    afterFetch(ctx) {
        ctx.data.results = ctx.data.results.map((user: {
            email: string;
            created_at: string;
            updated_at: string;
            subscription_status: string;
        }) => ({
            email: user.email,
            createdAt: user.created_at,
            updatedAt: user.updated_at,
            subscriptionStatus: user.subscription_status
        }))
        return ctx
    }
}).json<{
    metadata: Record<string, any>
    results: User[]
}>()

</script>

<template>
    <div class="text-neutral-100">
        <div class="py-4">
            <h4>{{currentMonth}}</h4>
        </div>
        <div class="py-4 flex flex-row justify-between items-center">
            <Card :title="'Email list'" :value="totalCount?.count ?? 0" class="w-3/12" />
            <Card :title="'New this month'" :value="monthlyCount?.count ?? 0" class="w-3/12" />
            <Card :title="'Unsubscribed'" :value="unsubscribedCount?.count ?? 0" class="w-3/12" />
        </div>
        <div class="py-4 w-full">
            <table class="border table-auto w-full">
                <thead class="border text-left">
                    <tr>
                        <th class="p-2">Email ID</th>
                        <th class="p-2">Timestamp</th>
                        <th class="p-2">Status</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="user in users?.results ?? []" :key="user.email">
                        <td class="border px-2 py-4">{{user.email}}</td>
                        <td class="border px-2 py-4">{{DateTime.fromISO(user.createdAt).toRelative()}}</td>
                        <td class="border px-2 py-4">{{user.subscriptionStatus}}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>