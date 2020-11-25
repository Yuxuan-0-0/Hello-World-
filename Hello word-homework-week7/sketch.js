// https://kylemcdonald.github.io/cv-examples/

var capture;
var w = 640;
var h = 480;
var xPos = 0;
var yPos = 0;

function setup() {
    capture = createCapture({
        audio: false,
        video: {
            width: w,
            height: h
        }
    }, function() {
        console.log('capture ready.')
    });
    capture.elt.setAttribute('playsinline', '');
    capture.size(w, h);
    createCanvas(w, h);
    capture.hide();
}

var targetColor = [168, 147, 119];

function draw() {
    var sampling = false;
    var sumPosition = createVector(0, 0);

    background(255,255,255)

    capture.loadPixels();
    if (capture.pixels.length > 0) { // don't forget this!
    
        if (mouseIsPressed &&
            mouseX > 0 && mouseX < width &&
            mouseY > 0 && mouseY < height) {
            targetColor = capture.get(mouseX, mouseY);
            sampling = true;
        }

        var w = capture.width,
            h = capture.height;
        var i = 0;
        var pixels = capture.pixels;
        var thresholdAmount = select('#thresholdAmount').value();
        thresholdAmount /= 100.; // this is the slider range
        thresholdAmount *= 255 * 3; // this is the maximum value
        var total = 0;
        for (var y = 0; y < h; y++) {
            for (var x = 0; x < w; x++) {
                var diff =
                    Math.abs(pixels[i + 0] - targetColor[0]) +
                    Math.abs(pixels[i + 1] - targetColor[1]) +
                    Math.abs(pixels[i + 2] - targetColor[2]);
                var outputValue = 0;
                if (diff < thresholdAmount) {
                    outputValue = 255;
                    sumPosition.x += x;
                    sumPosition.y += y;
                    total++;
                }
                pixels[i++] = outputValue; // set red
                pixels[i++] = outputValue; // set green
                pixels[i++] = outputValue; // set blue
                i++; // skip alpha
            }
        }
        
        sumPosition.div(total);

        console.log("x,y", sumPosition.x, sumPosition.y)
        
    }

    if (!sampling) {
        capture.updatePixels();
    }

    image(capture, 0, 0, 320, 240);

    ellipse(320+sumPosition.y, height-sumPosition.x, 50, 50)

}

