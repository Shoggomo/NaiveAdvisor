function pie_chart(input) {
    console.log(input);
    var ultimateColors = [['rgb(146, 123, 21)', 'rgb(177, 180, 34)', 'rgb(206, 206, 40)', 'rgb(175, 51, 21)', 'rgb(35, 36, 21)']];

    var data = [{
        values: Object.values(input),
        labels: Object.keys(input),
        type: 'pie',
        marker: {
            colors: ['#f46d43', '#fdae61', '#fee090', '#e0f3f8', '#abd9e9', '#74add1']
        }
    }];

    var layout = {
    title: 'Gewichtung',
    paper_bgcolor: '#ccdffa',
    font:
        {
            color:'#555555'
        }

}

    Plotly.newPlot('chartDiv', data, layout);
}