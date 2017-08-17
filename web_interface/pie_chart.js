function pie_chart(input) {
    console.log(input);
    var data = [{
        values: Object.values(input),
        labels: Object.keys(input),
        type: 'pie'
    }];
    Plotly.newPlot('myDiv', data);
}