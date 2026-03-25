const API = {
    async getMetrics() {
        try {
            const response = await fetch(`${CONFIG.API_BASE}/metrics`);
            if (!response.ok) throw new Error('Error fetching metrics');
            return await response.json();
        } catch (error) {
            console.error('Error en getMetrics:', error);
            return { metrics: [] };
        }
    },

    async getMetricData(metricKey) {
        try {
            const response = await fetch(`${CONFIG.API_BASE}/data/${metricKey}`);
            if (!response.ok) throw new Error('Error fetching metric data');
            return await response.json();
        } catch (error) {
            console.error('Error en getMetricData:', error);
            return null;
        }
    },

    async getAllData() {
        try {
            const response = await fetch(`${CONFIG.API_BASE}/all-data`);
            if (!response.ok) throw new Error('Error fetching all data');
            return await response.json();
        } catch (error) {
            console.error('Error en getAllData:', error);
            return {};
        }
    }
};
