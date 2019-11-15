!(function(r, t) {
  
  "object" == typeof exports && "undefined" != typeof module
    ? (module.exports = t())
    : "function" == typeof define && define.amd
    ? define(t)
    : (r.util = t());

})(this, function() {
  "use strict";
  return {

    /* adopted from http://randomcolour.com */
    randomColor: function() {
      var bg_colour = Math.floor(Math.random() * 16777215).toString(16);
      bg_colour = "#" + ("000000" + bg_colour).slice(-6);
      return bg_colour;
    },

    promedio: function(vector) {

      let value = vector.reduce( (acumulador, valor) => acumulador + valor, 0 );
      value = value / vector.length;

      return value;
    },

    desviacion_estandar: function(vector) {
      let media = this.promedio(vector);
      let diferencia_cuadrados = vector.reduce( (a, v) => a + Math.pow( (v - media) , 2 ) );
      
      let value = Math.sqrt( diferencia_cuadrados / vector.length );
      return value;
    }

  }
  
});
