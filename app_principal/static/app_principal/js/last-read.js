document.addEventListener("DOMContentLoaded", () => {
  // Gráfico de sensores
  const options = {
    series: [{
      name: "Percentual (%)",
      data: [mq2Data[0] || 0, mq3Data[0] || 0, mq5Data[0] || 0, mq135Data[0] || 0]
    }],
    chart: {
      type: "bar",
      height: 350,
      foreColor: "#f8f9fa",
      toolbar: { show: false },
    },
    plotOptions: {
      bar: {
        horizontal: true,
        borderRadius: 4,
        distributed: true
      }
    },
    dataLabels: {
      enabled: true,
      formatter: val => val + "%"
    },
    xaxis: {
      categories: ["MQ2", "MQ3", "MQ5", "MQ135"],
      min: 0,
      max: 100
    },
    colors: ['#0dcaf0', '#6f42c1', '#d63384', '#fd7e14'],
  };

  const chart = new ApexCharts(document.querySelector("#sensorChart"), options);
  chart.render();
});
