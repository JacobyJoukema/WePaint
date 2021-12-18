var canvas = document.getElementById("canvas");

var ctx = canvas.getContext("2d");

console.log(shapes);

for (let shape of shapes) {
  if (shape.type == "rect") {
    ctx.fillStyle = shape.colour;
    ctx.fillRect(shape.x, shape.y, shape.w, shape.h);
    ctx.fillStyle = "black";
  } else if (shape == "circle") {
    ctx.fillStyle = shape.colour;
    ctx.beginPath();
    ctx.arc(100, 75, 50, 0, 2 * Math.PI);
    ctx.fill();
  }
}
