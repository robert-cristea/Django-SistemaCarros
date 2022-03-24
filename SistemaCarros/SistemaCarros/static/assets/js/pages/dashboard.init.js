var options1 = {
    series: [{ data: [25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54] }],
    fill: { colors: ["#5b73e8"] },
    chart: { type: "bar", width: 70, height: 40, sparkline: { enabled: !0 } },
    plotOptions: { bar: { columnWidth: "50%" } },
    labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    xaxis: { crosshairs: { width: 1 } },
    tooltip: {
        fixed: { enabled: !1 },
        x: { show: !1 },
        y: {
            title: {
                formatter: function (e) {
                    return "";
                },
            },
        },
        marker: { show: !1 },
    },
},
chart1 = new ApexCharts(document.querySelector("#total-revenue-chart"), options1);
chart1.render();
var options = {
    fill: { colors: ["#34c38f"] },
    series: [70],
    chart: { type: "radialBar", width: 45, height: 45, sparkline: { enabled: !0 } },
    dataLabels: { enabled: !1 },
    plotOptions: { radialBar: { hollow: { margin: 0, size: "60%" }, track: { margin: 0 }, dataLabels: { show: !1 } } },
},
chart = new ApexCharts(document.querySelector("#orders-chart"), options);
chart.render();
options = {
fill: { colors: ["#5b73e8"] },
series: [55],
chart: { type: "radialBar", width: 45, height: 45, sparkline: { enabled: !0 } },
dataLabels: { enabled: !1 },
plotOptions: { radialBar: { hollow: { margin: 0, size: "60%" }, track: { margin: 0 }, dataLabels: { show: !1 } } },
};
(chart = new ApexCharts(document.querySelector("#customers-chart"), options)).render();
var options2 = {
    series: [{ data: [25, 66, 41, 89, 63, 25, 44, 12, 36, 9, 54] }],
    fill: { colors: ["#f1b44c"] },
    chart: { type: "bar", width: 70, height: 40, sparkline: { enabled: !0 } },
    plotOptions: { bar: { columnWidth: "50%" } },
    labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    xaxis: { crosshairs: { width: 1 } },
    tooltip: {
        fixed: { enabled: !1 },
        x: { show: !1 },
        y: {
            title: {
                formatter: function (e) {
                    return "";
                },
            },
        },
        marker: { show: !1 },
    },
},
chart2 = new ApexCharts(document.querySelector("#growth-chart"), options2);
chart2.render();
options = {
chart: { height: 339, type: "line", stacked: !1, toolbar: { show: !1 } },
stroke: { width: [0, 2, 4], curve: "smooth" },
plotOptions: { bar: { columnWidth: "30%" } },
colors: ["#5b73e8"],
series: [
    
    { name: "Sales", type: "area", data: [44, 55, 41, 67, 22, 43, 21, 41, 56, 27, 43] },
    { name: "", type: "line", data: [30, 25, 36, 30, 45, 35, 64, 52, 59, 36, 39] },
],
fill: { opacity: [0.85, 1], gradient: { inverseColors: !1, shade: "light", type: "vertical", opacityFrom: 0.85, opacityTo: 0.55, stops: [0, 100, 100, 100] } },
labels: ["01/01/2003", "02/01/2003", "03/01/2003", "04/01/2003", "05/01/2003", "06/01/2003", "07/01/2003", "08/01/2003", "09/01/2003", "10/01/2003", "11/01/2003"],
markers: { size: 0 },
xaxis: { type: "datetime" },
yaxis: { title: { text: "Sales number" } },
tooltip: {
    shared: !0,
    intersect: !1,
    y: {
        formatter: function (e) {
            return void 0 !== e ? e.toFixed(0) + " points" : e;
        },
    },
},
grid: { borderColor: "#f1f1f1" },
};
(chart = new ApexCharts(document.querySelector("#sales-analytics-chart"), options)).render();


var options = {
    series: [{
      name: "Sales",
      data: [10, 41, 35, 51, 49, 62, 69, 91, 148]
  }],
    chart: {
    height: 350,
    type: 'line',
    zoom: {
      enabled: false
    }
  },
  dataLabels: {
    enabled: false
  },
  stroke: {
    curve: 'straight'
  },
  title: {
    text: '',
    align: 'left'
  },
  grid: {
    row: {
      colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
      opacity: 0.5
    },
  },
  xaxis: {
    categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep'],
  }
  };

  var chart = new ApexCharts(document.querySelector("#chart"), options);
  chart.render();