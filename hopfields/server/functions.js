function calculateOffset(x,y){
   var rect = canvas.getBoundingClientRect();
   var point = {x: x-rect.left, y: y-rect.top}
   return point;
}
function returnRect(){
   var rect =  context.getImageData(10,10, 28, 28);
   return rect;
}
function simpleHttpRequest(url, success, failure, params) {
   //url to get information from, success = function, failure=function
   var request = new XMLHttpRequest();
   request.open("POST", url, true);
   request.send(params);
   request.onreadystatechange = function() {
         if (request.readyState == 4) {
            if (request.status == 200) console.log('sent');
            //alert(request.responseText);
            else if (failure) //what is failure sent to?
            alert(request.status, request.statusText);
        }
   };
}
function convertPixels(pixelData){
   var total =  pixelData[3];
   return total/255;
}

function createMatrix(n){ //create n * n matrix, filled with undefined values
   var matrix = new Array(n);
   for (var i = 0; i < array.length; i++){
      array[i] = new Array(n);
   }
   return matrix;
}

function fillMatrix(matrix, unitWidth, startX, startY){ //startX and y are canvas points?
   //fill array with its points by directly modifying its values
   for (var i = 0; i < matrix.length; i++){
      var row = matrix[i];
      var y = startY * (i+1);
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

}

function renderLines(context, grid, unitWidth){
   var width = grid.length * unitWidth;
   var length = width;
   for (var i = 0; i < grid.length; i++){
      var row = grid[i];
      for (var j = 0; j < row.length; j++){
         var unit = row[j];
         
      }
   }
}
