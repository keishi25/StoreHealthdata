
var ctx = document.getElementById("myChart").getContext('2d');
// グラフの高さサイズ
ctx.canvas.height = 320;
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
            data: [{
                x: 10,
                y: 10
            },
            {
                x: 11,
                y: 11
            },
            {
                x: 21,
                y: 21
            },
            {
                x: 31,
                y: 41
            },
            {
                x: 21,
                y: 34
            },
            {
                x: 14,
                y: 14
            }]
        }]
    },
    options: {
        //横はレスポンシブル
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            xAxes: [{
                type: 'linear',
                position: 'bottom'
            }]
        }
    }
});
