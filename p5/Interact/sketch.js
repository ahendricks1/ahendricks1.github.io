function setup() {
    createCanvas(1200, 1200);
    }
function draw() {
    if (mouseIsPressed) {
    fill(random(100),random(150),random(100));
    } else {
    fill(random(250), random(250),random(200));
    }
    ellipse(mouseX, mouseY, 80, 80);
}