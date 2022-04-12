$(function(){
	$('.datepicker').pickadate({
			monthsFull: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
			monthsShort: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'],
			weekdaysFull: ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'],
			weekdaysShort: ['Dom', 'Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb'],
		    selectMonths: true,
		    selectYears: 100, // Puedes cambiarlo para mostrar más o menos años
		    today: 'Hoy',
		    clear: 'Limpiar',
		    close: 'Ok',
		    labelMonthNext: 'Siguiente mes',
			labelMonthPrev: 'Mes anterior',
			labelMonthSelect: 'Selecciona un mes',
			labelYearSelect: 'Selecciona un año',
		  });
});

//Time Picker:
$('.timepicker').pickatime({
    default: 'now',
    twelvehour: false, // change to 12 hour AM/PM clock from 24 hour
    donetext: 'OK',
  autoclose: false,
  vibrate: true // vibrate the device when dragging clock hand
});

//Select:
$(document).ready(function() {
    $('select').material_select();
  });