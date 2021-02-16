

var ctx = document.getElementById("myChart").getContext('2d');
// グラフの高さサイズ
ctx.canvas.height = 320;
var scatter_data = scatter_data["scatter_data"];

var input_data = [];
for (let step = 0; step < scatter_data.length; step++) {
  date = new Date(scatter_data[step]["day"]);
  //alert(typeof date);
  //alert(date);
  input_data.push({x:date, y:scatter_data[step]["weight"]});
}

//date = new Date(scatter_data[0]["x"]);


// グラフの設定
var scatterChart = new Chart(ctx, {
    type: 'scatter',
    data: {
        datasets: [{
            label: '散布図データセット',
            // マーカー 背景色
            backgroundColor: 'rgba(0, 159, 255, 0.45)',
            // マーカー 枠線の色
            borderColor: 'rgba(0, 159, 255, 0.5)',
            // マーカー 大きさ
            pointRadius: 5,
            data: input_data
        }]
    },
    options: {
        //横はレスポンシブル
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            xAxes: [{
                type: 'time',
                time: {
                    displayFormats: {
                        quarter: 'MMM YYYY'
                    }
                }
            }]
        }
    }
});
