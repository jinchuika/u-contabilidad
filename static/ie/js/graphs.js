queue()
    .defer(d3.json, "/pagos/api/factura/")
    .await(makeGraphs);

function makeGraphs(error, projectsJson) {
	
	var cuentasPorPagar = projectsJson;
	var dateFormat = d3.time.format("%Y-%m-%d");
	cuentasPorPagar.forEach(function(d) {
		d["fecha_vencimiento"] = dateFormat.parse(d["fecha_vencimiento"]);
		d["fecha_vencimiento"].setDate(1);
		d["saldo"] = +d["saldo"];
	});

	//Create a Crossfilter instance
	var ndx = crossfilter(cuentasPorPagar);

	//Define Dimensions
	var dateDim = ndx.dimension(function(d) { return d["fecha_vencimiento"]; });
	var proveedorDim = ndx.dimension(function(d) { return d["proveedor"]; });
	var diasDim = ndx.dimension(function(d) { return d["dias"]; });
	var totalDonationsDim  = ndx.dimension(function(d) { return d["saldo"]; });


	//Calculate metrics
	var numProjectsByDate = dateDim.group(); 
	var numProjectsByResourceType = proveedorDim.group();

	var totalSaldoDias = diasDim.group().reduceSum(function(d) {
		return d["saldo"];
	});

	var all = ndx.groupAll();
	var totalDonations = ndx.groupAll().reduceSum(function(d) {return d["saldo"];});

	var max_dias = totalSaldoDias.top(1)[0].value;

	//Define values (to be used in charts)
	var minDate = dateDim.bottom(1)[0]["fecha_vencimiento"];
	var maxDate = dateDim.top(1)[0]["fecha_vencimiento"];

    //Charts
	var timeChart = dc.barChart("#time-chart");
	var proveedorChar = dc.rowChart("#resource-type-row-chart");
	var diasChart = dc.rowChart("#us-chart");
	var cuentasChart = dc.numberDisplay("#number-projects-nd");
	var saldoChart = dc.numberDisplay("#total-donations-nd");

	cuentasChart
		.formatNumber(d3.format("d"))
		.valueAccessor(function(d){return d; })
		.group(all);

	saldoChart
		.formatNumber(d3.format("d"))
		.valueAccessor(function(d){return d; })
		.group(totalDonations)
		.formatNumber(d3.format(".3s"));

	timeChart
		.width(700)
		.height(260)
		.margins({top: 10, right: 50, bottom: 30, left: 50})
		.dimension(dateDim)
		.group(numProjectsByDate)
		.transitionDuration(500)
		.x(d3.time.scale().domain([minDate, maxDate]))
		.elasticY(true)
		.yAxisLabel("Cantidad")
		.yAxis().ticks(4);

	proveedorChar
        .width(550)
        .height(350)
        .dimension(proveedorDim)
        .group(numProjectsByResourceType)
        .xAxis().ticks(4);

    diasChart
        .width(500)
        .height(550)
        .dimension(diasDim)
        .group(totalSaldoDias)
        .colors(d3.scale.ordinal().range(['#ff7f00', '#f7db2a', '#cdf727', '#4daf4a', '#f76827']))
        .xAxis().ticks(4);

    dc.renderAll();

};