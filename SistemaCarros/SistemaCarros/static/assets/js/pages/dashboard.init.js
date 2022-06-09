
dashboard_chart_options.chart =  {
    height: 350,
    type: 'line',
    zoom: {
      enabled: false
    }
  };
dashboard_chart_options.dataLabels =  {
    enabled: false
  };
dashboard_chart_options.stroke={
    curve: 'straight'
  };
dashboard_chart_options.title = {
    text: '',
    align: 'left'
  };
dashboard_chart_options.grid = {
  row: {
      colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
      opacity: 0.5
    },
};
var chart = new ApexCharts(document.querySelector("#chart"), dashboard_chart_options);
chart.render();