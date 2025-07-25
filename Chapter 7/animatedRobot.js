document.getElementById("lefteye").style.backgroundColor = "pink";
document.getElementById("head").style.transform = "rotate(10deg)";
// Put a 2‐pixel‐wide, solid black border around his body.
document.getElementById("body").style.border = "10px orange solid";
// Round the corners of his mouth.
document.getElementById("mouth").style.borderRadius = "10px";
// Put yellow dots around his right eye.
document.getElementById("righteye").style.border = "4px red dotted";
// Change his left arm’s color.
document.getElementById("leftarm").style.backgroundColor = "#7FFF00";
// Change the text color.
document.getElementById("body").style.color = "#FF0000";
// Give Douglas hair.
document.getElementById("head").style.borderTop = "50px grey solid";

var rightEye = document.getElementById("righteye");
rightEye.addEventListener("click", moveUpDown);

function moveUpDown(e) {
    var robotPart = e.target;
    var top = 0;
    var id = setInterval(frame, 10) // draw every 10ms

    function frame() {
        robotPart.style.top = top + '%';
        top++;
        if (top === 20) {
            clearInterval(id);
        }
    }
}

var leftArm = document.getElementById("leftarm");
leftArm.addEventListener("click", moveRightLeft);

function moveRightLeft(e) {
    var robotPart = e.target;
    var left = 0;
    var id = setInterval(frame, 10) // draw every 10ms

    function frame() {
        robotPart.style.left = left + '%';
        left++;
        if (left === 70) {
            clearInterval(id);
        }
    }
}