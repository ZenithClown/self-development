//got the original example from here
//https://bl.ocks.org/e9t/6073cd95c2a515a9f0ba


var app = angular.module('codepen', ['rzModule']);

app.controller('MainCtrl', function ($scope, $interval, $window, $q) {
	var vm = this;


	vm.inputLayerHeight = 15;
	vm.hiddenLayersCount = 2;
	vm.hiddenLayersDepths = [10, 10, 10, 10, 10];
	vm.outputLayerHeight = 5;

	var networkGraph = {
		"nodes": []
	};


	var width = $window.innerWidth - 15;
	var height = 400,
		nodeSize = 15;

	var color = d3.scale.category20();

	angular.element($window).on('resize', function () {
		console.log($window.innerWidth);
		width = $window.innerWidth;
		draw();
	});




	vm.inputLayerHeightSlider = {
		value: 15,
		options: {
			floor: 5,
			ceil: 20,
			showTicks: true,
			id: 'input-height-step-slider',
			onChange: function (id) {
				console.log('on end ' + id); // logs 'on end slider-id'
				vm.inputLayerHeight = vm.inputLayerHeightSlider.value;
				draw();
			}
		}
	};

	vm.hiddenLayerCountSlider = {
		value: 2,
		options: {
			floor: 1,
			ceil: 4,
			showTicks: true,
			id: 'hidden-count-step-slider',
			onChange: function (id) {
				console.log('on end ' + id); // logs 'on end slider-id'
				vm.hiddenLayersCount = vm.hiddenLayerCountSlider.value;
				draw();
			}
		}
	};

	vm.outputLayerHeightSlider = {
		value: 5,
		options: {
			floor: 2,
			ceil: 10,
			showTicks: true,
			id: 'output-height-step-slider',
			onChange: function (id) {
				console.log('on end ' + id); // logs 'on end slider-id'
				vm.outputLayerHeight = vm.outputLayerHeightSlider.value;
				draw();
			}
		}
	};

	$scope.$watchGroup(['vm.inputLayerHeight', 'vm.hiddenLayersCount', 'vm.outputLayerHeight'], function (newVal, oldVal) {
		//vm.inputLayerHeight = ;
		//vm.hiddenLayersCount = ;
		//vm.outputLayerHeight = ;
	});



	vm.draw = draw;


	function buildNodeGraph() {
		var newGraph = {
			"nodes": []
		};

		//construct input layer
		var newFirstLayer = [];
		for (var i = 0; i < vm.inputLayerHeight; i++) {
			var newTempLayer = { "label": "i" + i, "layer": 1 };
			newFirstLayer.push(newTempLayer);
		}

		//construct hidden layers
		var hiddenLayers = [];
		for (var hiddenLayerLoop = 0; hiddenLayerLoop < vm.hiddenLayersCount; hiddenLayerLoop++) {
			var newHiddenLayer = [];
			//for the height of this hidden layer
			for (var i = 0; i < vm.hiddenLayersDepths[hiddenLayerLoop]; i++) {
				var newTempLayer = { "label": "h" + hiddenLayerLoop + i, "layer": (hiddenLayerLoop + 2) };
				newHiddenLayer.push(newTempLayer);
			}
			hiddenLayers.push(newHiddenLayer);
		}

		//construct output layer
		var newOutputLayer = [];
		for (var i = 0; i < vm.outputLayerHeight; i++) {
			var newTempLayer = { "label": "o" + i, "layer": vm.hiddenLayersCount + 2 };
			newOutputLayer.push(newTempLayer);
		}

		//add to newGraph
		var allMiddle = newGraph.nodes.concat.apply([], hiddenLayers);
		newGraph.nodes = newGraph.nodes.concat(newFirstLayer, allMiddle, newOutputLayer);

		return newGraph;

	}




	function drawGraph(networkGraph, svg) {
		var graph = networkGraph;
		var nodes = graph.nodes;

		// get network size
		var netsize = {};
		nodes.forEach(function (d) {
			if (d.layer in netsize) {
				netsize[d.layer] += 1;
			} else {
				netsize[d.layer] = 1;
			}
			d["lidx"] = netsize[d.layer];
		});

		// calc distances between nodes
		var largestLayerSize = Math.max.apply(
			null, Object.keys(netsize).map(function (i) { return netsize[i]; }));

		var xdist = width / Object.keys(netsize).length,
			ydist = (height - 15) / largestLayerSize;

		// create node locations
		nodes.map(function (d) {
			d["x"] = (d.layer - 0.5) * xdist;
			d["y"] = (((d.lidx - 0.5) + ((largestLayerSize - netsize[d.layer]) / 2)) * ydist) + 10;
		});

		// autogenerate links
		var links = [];
		nodes.map(function (d, i) {
			for (var n in nodes) {
				if (d.layer + 1 == nodes[n].layer) {
					links.push({ "source": parseInt(i), "target": parseInt(n), "value": 1 })
				}
			}
		}).filter(function (d) { return typeof d !== "undefined"; });

		// draw links
		var link = svg.selectAll(".link")
			.data(links)
			.enter().append("line")
			.attr("class", "link")
			.attr("x1", function (d) { return nodes[d.source].x; })
			.attr("y1", function (d) { return nodes[d.source].y; })
			.attr("x2", function (d) { return nodes[d.target].x; })
			.attr("y2", function (d) { return nodes[d.target].y; })
			.style("stroke-width", function (d) { return Math.sqrt(d.value); });

		// draw nodes
		var node = svg.selectAll(".node")
			.data(nodes)
			.enter().append("g")
			.attr("transform", function (d) {
				return "translate(" + d.x + "," + d.y + ")";
			}
			);

		var circle = node.append("circle")
			.attr("class", "node")
			.attr("r", nodeSize)
			.style("fill", function (d) { return color(d.layer); });


		node.append("text")
			.attr("dx", "-.35em")
			.attr("dy", ".35em")
			.attr("font-size", ".6em")
			.text(function (d) { return d.label; });
	}



	function draw() {

		if (!d3.select("svg")[0]) {

		} else {
			//clear d3
			d3.select('svg').remove();
		}



		var svg = d3.select("#neuralNet").append("svg")
			.attr("width", width)
			.attr("height", height);

		console.log("drawing   " + new Date());
		networkGraph = buildNodeGraph();
		//buildNodeGraph();
		drawGraph(networkGraph, svg);
	}




	function init() {

		draw()
	}

	//main
	init()




});





// example is based on the numpy neural network tutorial featured here
// https://iamtrask.github.io/2015/07/12/basic-python-network/
'use strict';

function sigmoid(ddx) {
	return function (x) {
		return ddx ?
			x * (1 - x) :
			1.0 / (1 + Math.exp(-x));
	};
}
