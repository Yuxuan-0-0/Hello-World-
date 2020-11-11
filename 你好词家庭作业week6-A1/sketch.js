var img;
var d = 8;

function preload(){ //加载图片文件
  img = loadImage("46.jpg");
}

function setup() {
  createCanvas(800, 450);
  background(img); 
}

function draw() {
  image(img, 0, 0, 0, 0);
  noStroke();
  mouseX = -d;
  mouseY = -d;
}

function draw() {
  fill(285, 70)
  ellipse(mouseX, mouseY, d, d)
}