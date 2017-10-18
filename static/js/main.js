$(document).ready(function () {
	$('.datepicker').datepicker({
		format: 'dd/mm/yyyy',
		autoclose: true,
		language: 'es'
	});

	$(".select2").select2({
		width : '100%'
	});
});