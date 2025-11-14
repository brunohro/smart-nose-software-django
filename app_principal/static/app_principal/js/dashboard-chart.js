document.addEventListener("DOMContentLoaded", function () {
    const options = {
        series: [
            { name: 'MQ-2', data: mq2Data },
            { name: 'MQ-3', data: mq3Data },
            { name: 'MQ-5', data: mq5Data },
            { name: 'MQ-135', data: mq135Data },
        ],
        chart: {
            height: 380,
            type: "line",
            zoom: { enabled: false },
            toolbar: { show: false },
            foreColor: '#adb5bd'
        },
        colors: ['#7c4dff', '#448aff', '#69f0ae', '#f50057'],
        dataLabels: { enabled: false },
        stroke: {
            curve: 'smooth',
            width: 3
        },
        grid: {
            borderColor: '#495057',
            strokeDashArray: 4,
            row: {
                colors: ['transparent', 'transparent'],
                opacity: 0.5
            },
        },
        xaxis: {
            categories: timestamps,
            title: { text: 'Hora do Dia' },
        },
        yaxis: {
            title: { text: 'Percentual (%)' },
            min: 0,
            max: 100
        },
        legend: {
            position: 'top',
            horizontalAlign: 'right',
            markers: { strokeWidth: 0 },
        },
        tooltip: {
            theme: 'dark',
            x: { show: true },
        }
    };

    const chart = new ApexCharts(document.querySelector("#lineChart"), options);
    chart.render();
});
