!(function(u, r, fn) {
  "object" == typeof exports && "undefined" != typeof module
    ? (module.exports = fn())
    : "function" == typeof define && define.amd
    ? define(t)
    : (r.realtime = fn);
})(util, this, function(sensores) {
  "use strict";

  const process_meditions = meditions => {
    let data = [];

    meditions.forEach( (medition) => {
      data.push({
        t: new Date(medition.fechahora),
        //t: medition.fechahora,
        y: medition.value
      });
    });

    return data;
  }

  const process_sensor = sensor => {
      
    const color = util.randomColor();
    const meditions = process_meditions(sensor.meditions)

    let dataset = {
      label: sensor.name,
      data: meditions,
      backgroundColor: color,
      borderColor: color,
      fill: false,
      cubicInterpolationMode: 'monotone',
    };

    return dataset;
  }

  return {

    datasets: () => {
      let datasets = [];

      sensores.forEach( (sensor, index) => {
        //if (index % 2 != 0) return;
        let dataset = process_sensor(sensor);
        datasets.push(dataset);
      })

      return datasets;
    }
  };

});
