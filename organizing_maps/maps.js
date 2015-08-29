/*
How to improve classification and vector matching?
Similarity to biological systems?

How does it work?

Uses?
   -Classification tool


Stages: Ordering and Convergence



*/

function distance(x1,y1,x2, y2){
   var val =  Math.sqrt(Math.abs(Math.pow(x2-x1,2)+ Math.pow(y2-y1,2)));
   return val;
}

function Map(input, dimension, size, unit_size, canvas){
   this.dimension = dimension;
   this.inputs = inputs; //form of vectors, or raw input?
   this.units = []; //hold all units, vectors and inputs?, do you need object?
   this.radius = Math.max(canvas.width, canvas.height)/2;
   this.size = size; //size = number of units in row?
   this.bmu = null;
   this.unit_size = unit_size; //width and height-> is this even a thing?

   this.learning_rate = .9;
   this.start_rate = .9;
   this.turn = 0;
   this.canvas = canvas;
   this.context = canvas.getContext('2d');

   this.init();
}

Map.prototype = {
   init: function(){
      this.create_units();
   },
   update: function(){

   },
   read_inputs: function(iterations){
      for (var i = 0; i < iterations; i++){
         //random index of inputs
         var index = parseInt((this.inputs.length) * Math.random());
         inputVector = this.inputs[index];
         //console.log(inputVector);
         this.read_input(inputVector, iterations);
      }
   },
   read_input: function(inputVector, iterations){ //iterate through inputs
      var radius = this.radius;
      var learning = this.learning_rate;

      var bmu = this.find_bmu(inputVector);
      ////console.log(bmu);
      this.adjust_units(learning, radius, bmu, inputVector);
      this.turn++;
      this.adjust_vars(iterations);
      this.render();
   },
   adjust_vars: function(iterations){
      this.calc_radius(iterations);
      this.calc_learning(iterations);
      //console.log("learning: "+ this.learning_rate);
      //console.log("radius: " + this.radius);
   },
   create_units: function(){
      for (var i = 0; i< this.size; i++){
         for (var j = 0; j< this.size; j++){
            var unit_size = this.unit_size;
            var x = i * unit_size;
            var y = j * unit_size;
            var unit = new Map_unit(x,y, this.unit_size, this.dimension, this.context);
            this.units.push(unit);
         }
      }
   },
   find_bmu: function(inputVector){ //what to use as discrimination function?
      //mean squared error?
      var bmu;
      var error = 9999999; //lowest deviation from ideal = bmu
      for (var i = 0; i< this.units.length; i++){
         var unit = this.units[i];
         var u_error = 0;
         for (var j = 0; j < unit.weights.length; j++){ //input vector size === dimension of unit weights
            u_error += Math.pow(inputVector[j] - unit.weights[j], 2);
         }
         if (u_error < error){
            ////console.log('bmu assigned, error = ' + u_error);
            error = u_error;
            bmu = unit;
         }
      }
      //console.log(bmu);
      return bmu;

   },
   adjust_units: function(learning, radius, bmu, vector){ //inside BMU radius
      if (learning === undefined || radius === undefined || bmu === undefined){
         alert('broken inputs for unit adjustment');
      }
      for (var i = 0; i< this.units.length; i++){
         var unit = this.units[i]; //copies location in memory?
         if (this.in_radius(radius, bmu, unit) || bmu === unit){
            ////console.log('adjusted unit');
            unit.adjust(learning, bmu, radius, vector);
         }
      }
   },
   in_radius: function(radius, bmu, target){
      if (target.x > bmu.x - radius &&  target.x + target.size < bmu.x + radius
         && target.y > bmu.y - radius && target.y + target.size < bmu.y + radius){
            return true;
         }
      else return true;
   },
   calc_radius: function(iterations){ //might be nice to print out 100 iterations and see how value changes
      var radius = this.radius;
      var gamma = iterations/Math.log(radius);
      ////console.log(gamma);
      var new_radius = radius * Math.pow(Math.E, -this.turn/gamma);
      this.radius = new_radius;
   },
   calc_learning: function(iterations){
      var new_learning = this.start_rate*Math.pow(Math.E, -this.turn/iterations);
   //   //console.log(new_learning);
      this.learning_rate = new_learning;
   },
   clear: function(){
      this.context.clearRect(0,0, this.canvas.width, this.canvas.height);
   },
   render: function(){
      for (var i = 0; i< this.units.length; i++){
         this.units[i].render();
      }
   }

}

function Map_unit(x,y, size, inputDimension, context){
   this.weights = [];
   this.color = '';
   this.x = x; //top left
   this.y = y; //top left
   this.size = size;
   this.context = context;
   this.inputDimension = inputDimension;

   this.init();
}

Map_unit.prototype = {
   init: function(){
      this.gen_weights();
      this.calc_color();
   },
   render: function(){
      //render using color and position;, use gradient?
      this.context.beginPath();
      this.context.fillStyle = this.color;
      this.context.fillRect(this.x, this.y, this.size, this.size);
      this.context.closePath();
   },
   calc_color: function(){
      //use weights to select color
      //color is weight * 255 and then assigned to RGB values
      var color = 'rgba('
      for (var i = 0; i< this.weights.length; i++){
         color += parseInt(this.weights[i] * 255) + ',';
      }
      var color = color.substring(0, color.length-1);
      color += ',155)';
      this.color = color;
   },
   gen_weights: function(){
      for (var i = 0; i< this.inputDimension; i++){
         this.weights.push(Math.random());
      }
   },
   adjust: function(learning_rate, bmu, radius, vector){
      //only called if in radius, probably not that efficient as
      ////console.log('called');
      var dist= -(Math.pow(distance(this.x, this.y, bmu.x, bmu.y),2));
      var bottom = 2*Math.pow(radius,2);
      var omega = Math.pow(Math.E,dist/bottom);
      var learning = learning_rate;
      ////console.log(dist, bottom, omega, learning);
      var adjust = learning * omega;
      for (var i = 0; i< this.weights.length; i++){
            var error = vector[i] - this.weights[i];
            this.weights[i] += adjust * error;
      }
      this.calc_color();
   },

}
