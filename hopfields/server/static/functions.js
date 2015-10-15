function calculateOffset(x,y){
   var rect = canvas.getBoundingClientRect();
   var point = {x: x-rect.left, y: y-rect.top}
   return point;
}

function sendData(url, grid, success, failure, params) {
   //url to get information from, success = function, failure=function
   var request = new XMLHttpRequest();
   request.open("POST", url, true);
   //request.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');
   //why does setting the request header screw everything up?
   request.send(params);
   request.onreadystatechange = function() {
         if (request.readyState == 4) {
            if (request.status == 200){
               console.log('successful transfer');
               info = request.responseText;
               success(info, grid);
            }
            else{
               failure();
            }
        }
   };
}

function resetNet(url){
   var request = new XMLHttpRequest();
   request.open("GET", url, true);
   //request.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');
   //why does setting the request header screw everything up?
   request.send();
   request.onreadystatechange = function() {
         if (request.readyState == 4) {
            if (request.status == 200){
               console.log('the net was reset');
               info = request.responseText;
            }
            else{
               console.log('not read');
            }
        }
   };
}
function success(input, grid){
   console.log(input);
   return input;
}
function failure(){
   console.log('failed exchange');
}

function processJSON(json, grid){ //form = {'row1': [array], 'row2'[array2]}
   console.log(json);
   arr = JSON.parse(json);
   matrix = grid;
   var count = 0;
   for (var i = 0; i < matrix.length; i++){
      var row = matrix[i];
      for (var j = 0; j < row.length; j++){
         var unit = row[j];
         var input = arr[count];
         unit.active = translate_bin(input);
         count++;
      }
   }
}
function translate_bin(input){
   if (input === 1){
      return true;
   }
   else return false;
}

function createMatrix(n){ //create n * n matrix, filled with undefined values
   var matrix = new Array(n);
   for (var i = 0; i < matrix.length; i++){
      matrix[i] = new Array(n);
   }
   return matrix;
}

function fillMatrix(matrix, unitWidth, startX, startY){ //startX and y are canvas points?
   //fill array with its points by directly modifying its values
   for (var i = 0; i < matrix.length; i++){
      var row = matrix[i];
      var y = startY * (i+1) * unitWidth;
      for (var j = 0; j < row.length; j++){
         var x = startX * (j + 1) * unitWidth;
         row[j] = {'x': x, 'y': y, "active": false}; //object holding unit values
      }
   }
}

function detectClick(matrix, unitWidth, x, y){
   for (var i = 0; i < matrix.length; i++){
      var row = matrix[i];
      for (var j = 0; j < row.length; j++){
         var unit = row[j];
         if (x >= unit.x && y >= unit.y && x < unit.x + unitWidth && y < unit.y + unitWidth){
            unit.active = true;
         }
      }
   }
}

function renderGrid(context, grid, unitWidth){
   clearGrid(context, grid);
   renderLines(context, grid, unitWidth);
   var offset = 1;
   for (var i = 0; i < grid.length; i++){
      var row = grid[i];
      for (var j = 0; j < row.length; j++){
         var unit = row[j];
         if (unit.active){
            context.globalAlpha = .8;
            context.fillStyle = 'blue';
            context.fillRect(unit.x, unit.y, unitWidth-offset, unitWidth-offset);
         }
         else{
            //non active render code
         }
      }
   }
}

function renderLines(context, grid, unitWidth){ //iterate down a column, then a row, rendering a grid
   var width = grid.length * unitWidth;
   var height = width;
   var row = grid[0];
   for (var i = 0; i < row.length; i++){ //row iteration
      var unit = row[i];
      context.globalAlpha = .7;
      context.beginPath();
      context.moveTo(unit.x, unit.y);
      context.lineTo(unit.x, unit.y + height);
      context.stroke();
      context.closePath();
      //final row drawing code
      if (i == row.length -1){
         context.beginPath();
         context.moveTo(unit.x + unitWidth, unit.y);
         context.lineTo(unit.x + unitWidth, unit.y + height);
         context.stroke();
         context.closePath();
      }

   }
   for (var j = 0; j < grid.length; j++){
      var unit = grid[j][0];
      context.globalAlpha = .8;
      context.beginPath();
      context.moveTo(unit.x, unit.y);
      context.lineTo(unit.x + width, unit.y);
      context.stroke();
      context.closePath();
      //final column code drawing
      if (j == grid.length-1){
         context.beginPath();
         context.moveTo(unit.x, unit.y + unitWidth);
         context.lineTo(unit.x + width, unit.y + unitWidth);
         context.stroke();
         context.closePath();
      }
   }

}

function clearGrid(context, grid){
   var width = grid.length * unitWidth;
   var height = width;
   context.clearRect(0,0, 1000, 1000);
}

function resetGrid(grid){
   //iterate through all, turn values to 0
   grid.forEach(function(row, i, array){
      array.forEach(function(val,j, row2){
         row2[j] = 0;
      });
   });
}

function createMatrix(n){ //create n * n matrix, filled with undefined values
   var matrix = new Array(n);
   for (var i = 0; i < matrix.length; i++){
      matrix[i] = new Array(n);
   }
   return matrix;
}

//fill used for resets as well
function fillMatrix(matrix, unitWidth, startX, startY){ //startX and y are canvas points?
   //fill array with its points by directly modifying its values
   for (var i = 0; i < matrix.length; i++){
      var row = matrix[i];
      var y = startY * (i+1) * unitWidth;
      for (var j = 0; j < row.length; j++){
         var x = startX * (j + 1) * unitWidth;
         row[j] = {'x': x, 'y': y, "active": false}; //object holding unit values
      }
   }
}

function detectClick(matrix, unitWidth, x, y){
   for (var i = 0; i < matrix.length; i++){
      var row = matrix[i];
      for (var j = 0; j < row.length; j++){
         var unit = row[j];
         if (x >= unit.x && y >= unit.y && x < unit.x + unitWidth && y < unit.y + unitWidth){
            unit.active = true;
         }
      }
   }
}

function renderGrid(context, grid, unitWidth){
   clearGrid(context, grid);
   renderLines(context, grid, unitWidth);
   var offset = 1;
   for (var i = 0; i < grid.length; i++){
      var row = grid[i];
      for (var j = 0; j < row.length; j++){
         var unit = row[j];
         if (unit.active){
            context.globalAlpha = .8;
            context.fillStyle = 'blue';
            context.fillRect(unit.x, unit.y, unitWidth-offset, unitWidth-offset);
         }
         else{
            //non active render code
         }
      }
   }
}

function renderLines(context, grid, unitWidth){ //iterate down a column, then a row, rendering a grid
   var width = grid.length * unitWidth;
   var height = width;
   var row = grid[0];
   for (var i = 0; i < row.length; i++){ //row iteration
      var unit = row[i];
      context.globalAlpha = .7;
      context.beginPath();
      context.moveTo(unit.x, unit.y);
      context.lineTo(unit.x, unit.y + height);
      context.stroke();
      context.closePath();
      //final row drawing code
      if (i == row.length -1){
         context.beginPath();
         context.moveTo(unit.x + unitWidth, unit.y);
         context.lineTo(unit.x + unitWidth, unit.y + height);
         context.stroke();
         context.closePath();
      }

   }
   for (var j = 0; j < grid.length; j++){
      var unit = grid[j][0];
      context.globalAlpha = .8;
      context.beginPath();
      context.moveTo(unit.x, unit.y);
      context.lineTo(unit.x + width, unit.y);
      context.stroke();
      context.closePath();
      //final column code drawing
      if (j == grid.length-1){
         context.beginPath();
         context.moveTo(unit.x, unit.y + unitWidth);
         context.lineTo(unit.x + width, unit.y + unitWidth);
         context.stroke();
         context.closePath();
      }
   }

}

function clearGrid(context){
   var width = grid.length * unitWidth;
   var height = width;
   context.clearRect(0,0, 1000, 1000);
}
