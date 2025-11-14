function createChart(selector, seriesData, title) {

    let chartColor = "#ffffff"; // cor padrão
  if (title.toLowerCase().includes("temperatura")) chartColor = "#e74c3c"; // vermelho
  if (title.toLowerCase().includes("umidade")) chartColor = "#3498db"; // azul

  var options = {
    series: [{ data: seriesData }],
    chart: {
      type: "area", // pode mudar para "bar", "line" ou "area"
      height: 350,
      toolbar: { show: true, tools: { download: false } }
    },
    title: {
      text: title,
      align: "center",
      style: { color: "#fafafa", fontSize: "14px" }
    },
    xaxis: {
      categories: timestamps,
      labels: { style: { fontSize: "12px", colors: "#ffffff" } }
    },
    yaxis: {
      labels: { style: { fontSize: "12px", colors: "#ffffff" } }
    },
    colors: [chartColor],
    dataLabels: {
      enabled: true,
      formatter: val => val.toFixed(1), 
      style: { colors: ["#0c0c0c"], fontSize: "12px" }
    },
    grid: { borderColor: "#272f38" }
  };

  var chart = new ApexCharts(document.querySelector(selector), options);
  chart.render();
}

// Criando gráficos com os dados do Django
createChart("#chart-temperatura", temperaturaData, "Temperatura");
createChart("#chart-umidade", umidadeData, "Umidade");
