

//var ctx = document.getElementById("myChart").getContext('2d');
// グラフの高さサイズ
//ctx.canvas.height = 520;
var scatter_data = scatter_data["scatter_data"];

var weight_data = [];
var measured_date = [];

for (let step = 0; step < scatter_data.length; step++) {
  date = new Date(scatter_data[step]["day"]);
  //alert(typeof date);
  //alert(date);
  weight_data.push(scatter_data[step]["weight"]);
  measured_date.push(date.getMonth() + "月" + date.getDate() + "日");
}

//date = new Date(scatter_data[0]["x"]);


// グラフの設定
 var ctx = document.getElementById("myChart");
 var myLineChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: measured_date,
      datasets: [
        {
          label: '体重',
          data: weight_data,
          borderColor: "rgba(255,0,0,1)",
          backgroundColor: "rgba(0,0,0,0)"
        },
      ],
    },
    options: {
      title: {
        display: true,
        //text: '体重'
      },
      scales: {
        yAxes: [{
          ticks: {
            //suggestedMax: 80,
            //suggestedMin: 30,
            //stepSize: 10,
            callback: function(value, index, values){
              return  value +  'kg'
            }
          }
        }]
      },
    }
  });