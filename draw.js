var canvas = document.getElementById("canvas");

var ctx = canvas.getContext("2d");

draw();

function draw() {
  width = window.innerWidth;
  height = window.innerHeight;

  canvas.width = width;
  canvas.height = height;

  console.log(shapes);

  for (let shape of shapes) {
    if (shape.type == "rect") {
      ctx.fillStyle = shape.colour;
      ctx.fillRect(
        shape.x * width,
        shape.y * height,
        shape.w * width,
        shape.h * height
      );
      ctx.fillStyle = "black";
    } else if (shape.type == "circle") {
      console.log(shape);
      ctx.fillStyle = shape.colour;
      ctx.beginPath();
      ctx.arc(
        shape.x * width,
        shape.y * height,
        shape.r * Math.min(width, height),
        0,
        2 * Math.PI
      );

      ctx.fill();
      ctx.fillStyle = "black";
    }
  }
}
