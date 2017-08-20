function pie_chart(input) {
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
        },
    height: 400,
    width: 500

}

    Plotly.newPlot('chartDiv', data, layout);
}