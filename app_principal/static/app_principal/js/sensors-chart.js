import ApexCharts from "apexcharts";

// Definindo as opções dos gráficos

var optionsMQ2 = {
    series: [{ data: [50, 60, 70] }],
    chart: {
        type: "bar",
        height: 350,
        toolbar: {
            show: true,
            tools: { download: false },
        },
    },
    plotOptions: {
        bar: {
            borderRadius: 4,
            borderRadiusApplication: "end",
            horizontal: true,
        },
    },
    title: {
        text: "PERCENTUAL DE SENSIBILIDADE AOS GASES - MQ2",
        align: "center",
        floating: true,
        style: { color: "#fafafa", fontSize: "12px" },
    },
    tooltip: {
        theme: "dark",
        x: { show: false },
        y: {
            title: {
                formatter: function () {
                    return "";
                },
            },
        },
    },
    xaxis: {
        categories: ["Fumaça", "GLP", "Hidrogênio"],
        labels: {
            style: { fontSize: "12px", colors: "#ffffff" },
        },
    },
    yaxis: {
        labels: {
            style: { fontSize: "12px", colors: "#ffffff" },
        },
    },
    colors: ["#00E396", "#FEB019", "#FF4560"],
    dataLabels: {
        enabled: true,
        style: { colors: ["#fff"], fontSize: "12px" },
        formatter: function (val) {
            return val + "%";
        },
    },
    grid: { borderColor: "#272f38" },
};

var optionsMQ3 = {
    series: [
        {
            data: [90, 56, 34, 44, 20],
        },
    ],
    chart: {
        type: "bar",
        height: 350,
        width: "100%",
        toolbar: {
            show: true,
            tools: {
                download: false, // Desativa o botão de download
            },
        },
    },
    plotOptions: {
        bar: {
            borderRadius: 4,
            borderRadiusApplication: "end",
            horizontal: true,
        },
    },
    title: {
        text: "PERCENTUAL DE SENSIBILIDADE AOS GASES",
        align: "center",
        floating: true,
        style: {
            color: "#fafafa",
            fontSize: "12px",
        },
    },
    tooltip: {
        theme: "dark",
        x: {
            show: false,
        },
        y: {
            title: {
                formatter: function () {
                    return "";
                },
            },
        },
    },
    xaxis: {
        categories: ["GLP", "Álcool", "Benzina", "Metano", "Hexano"],
        labels: {
            style: {
                fontSize: "12px",
                colors: "#ffffff", // Cor dos rótulos do eixo X
            },
        },
    },
    yaxis: {
        labels: {
            style: {
                fontSize: "12px",
                colors: "#ffffff", // Cor dos rótulos do eixo Y
            },
        },
    },
    colors: ["#33b2df", "#546E7A", "#d4526e", "#13d8aa"], // Cores individuais para o gráfico MQ3
    dataLabels: {
        enabled: true,
        style: {
            colors: ["#fff"],
            fontSize: "12px",
        },
        formatter: function (val) {
            return val + "%"; // Adiciona o símbolo de porcentagem
        },
    },
    grid: {
        borderColor: "#272f38",
    },
};

var optionsMQ5 = {
    series: [
        {
            data: [78, 88, 65, 73],
        },
    ],
    chart: {
        type: "bar",
        height: 350,
        toolbar: {
            show: true,
            tools: {
                download: false, // Desativa o botão de download
            },
        },
    },
    plotOptions: {
        bar: {
            borderRadius: 4,
            borderRadiusApplication: "end",
            horizontal: true,
        },
    },
    title: {
        text: "PERCENTUAL DE SENSIBILIDADE AOS GASES",
        align: "center",
        floating: true,
        style: {
            color: "#fafafa",
            fontSize: "12px",
        },
    },
    tooltip: {
        theme: "dark",
        x: {
            show: false,
        },
        y: {
            title: {
                formatter: function () {
                    return "";
                },
            },
        },
    },
    xaxis: {
        categories: ["C02", "H", "HCL4", "H2O"],
        labels: {
            style: {
                fontSize: "12px",
                colors: "#ffffff", // Cor dos rótulos do eixo X
            },
        },
        style: {
            borderColor: "#272f38",
        },
    },
    yaxis: {
        labels: {
            style: {
                fontSize: "12px",
                colors: "#ffffff", // Cor dos rótulos do eixo Y
            },
        },
    },
    colors: ["#ff4560", "#775dd0", "#00e396", "#feb019"], // Cores individuais para o gráfico MQ5
    dataLabels: {
        enabled: true,
        style: {
            colors: ["#fff"],
            fontSize: "12px",
        },
        formatter: function (val) {
            return val + "%"; // Adiciona o símbolo de porcentagem
        },
    },
    grid: {
        borderColor: "#272f38",
    },
};

var optionsMQ8 = {
    series: [{ data: [80, 55, 42] }],
    chart: {
        type: "bar",
        height: 350,
        toolbar: {
            show: true,
            tools: { download: false },
        },
    },
    plotOptions: {
        bar: {
            borderRadius: 4,
            borderRadiusApplication: "end",
            horizontal: true,
        },
    },
    title: {
        text: "PERCENTUAL DE SENSIBILIDADE AOS GASES - MQ8",
        align: "center",
        floating: true,
        style: { color: "#fafafa", fontSize: "12px" },
    },
    tooltip: {
        theme: "dark",
        x: { show: false },
        y: {
            title: {
                formatter: function () {
                    return "";
                },
            },
        },
    },
    xaxis: {
        categories: ["Hidrogênio", "Metano", "Gás Natural"],
        labels: {
            style: { fontSize: "12px", colors: "#ffffff" },
        },
    },
    yaxis: {
        labels: {
            style: { fontSize: "12px", colors: "#ffffff" },
        },
    },
    colors: ["#775DD0", "#FF4560", "#3F51B5"],
    dataLabels: {
        enabled: true,
        style: { colors: ["#fff"], fontSize: "12px" },
        formatter: function (val) {
            return val + "%";
        },
    },
    grid: { borderColor: "#272f38" },
};

var optionsMQ135 = {
    series: [{ data: [40, 67, 53, 28] }],
    chart: {
        type: "bar",
        height: 350,
        toolbar: {
            show: true,
            tools: { download: false },
        },
    },
    plotOptions: {
        bar: {
            borderRadius: 4,
            borderRadiusApplication: "end",
            horizontal: true,
        },
    },
    title: {
        text: "PERCENTUAL DE SENSIBILIDADE AOS GASES - MQ135",
        align: "center",
        floating: true,
        style: { color: "#fafafa", fontSize: "12px" },
    },
    tooltip: {
        theme: "dark",
        x: { show: false },
        y: {
            title: {
                formatter: function () {
                    return "";
                },
            },
        },
    },
    xaxis: {
        categories: ["Amônia", "CO2", "Benzeno", "Álcool"],
        labels: {
            style: { fontSize: "12px", colors: "#ffffff" },
        },
    },
    yaxis: {
        labels: {
            style: { fontSize: "12px", colors: "#ffffff" },
        },
    },
    colors: ["#F86624", "#2E93fA", "#FF9F43", "#00E396"],
    dataLabels: {
        enabled: true,
        style: { colors: ["#fff"], fontSize: "12px" },
        formatter: function (val) {
            return val + "%";
        },
    },
    grid: { borderColor: "#272f38" },
};

// Função para ajustar as opções dos gráficos conforme a largura da tela
/* function adjustChartOptions() {
  if (window.innerWidth <= 900) {
    optionsMQ3.title.style.fontSize = "5px";
    optionsMQ3.xaxis.labels.style.fontSize = "8px";
    optionsMQ3.yaxis.labels.style.fontSize = "8px";
    optionsMQ3.dataLabels.style.fontSize = "8px";

    optionsMQ5.title.style.fontSize = ".2rem";
    optionsMQ5.xaxis.labels.style.fontSize = "8px";
    optionsMQ5.yaxis.labels.style.fontSize = "8px";
    optionsMQ5.dataLabels.style.fontSize = "8px";
  } else {
    optionsMQ3.title.style.fontSize = "12px";
    optionsMQ3.xaxis.labels.style.fontSize = "12px";
    optionsMQ3.yaxis.labels.style.fontSize = "12px";
    optionsMQ3.dataLabels.style.fontSize = "12px";

    optionsMQ5.title.style.fontSize = "12px";
    optionsMQ5.xaxis.labels.style.fontSize = "12px";
    optionsMQ5.yaxis.labels.style.fontSize = "12px";
    optionsMQ5.dataLabels.style.fontSize = "12px";
  }

  // Redesenhar os gráficos com as novas opções
  chartMQ3.updateOptions(optionsMQ3);
  chartMQ5.updateOptions(optionsMQ5);
}
 */

// Criar os gráficos
var chartMQ3 = new ApexCharts(document.querySelector("#chart-mq3"), optionsMQ3);
var chartMQ5 = new ApexCharts(document.querySelector("#chart-mq5"), optionsMQ5);
var chartMQ2 = new ApexCharts(document.querySelector("#chart-mq2"), optionsMQ2);
var chartMQ8 = new ApexCharts(document.querySelector("#chart-mq8"), optionsMQ8);
var chartMQ135 = new ApexCharts(
    document.querySelector("#chart-mq135"),
    optionsMQ135
);

[chartMQ3, chartMQ5, chartMQ2, chartMQ8, chartMQ135].forEach((c) => c.render());

// [chartMQ3, chartMQ5].forEach((c) => c.render());

// Ajustar as opções dos gráficos na carga da página e ao redimensionar a janela
/* window.addEventListener("load", adjustChartOptions);
window.addEventListener("resize", adjustChartOptions);
 */
