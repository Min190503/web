
var modal = document.getElementById("myModal");
var btns = document.querySelectorAll(".cvh p"); 
var span = document.getElementsByClassName("close")[0];


btns.forEach(function(btn) {
    btn.addEventListener("click", function() {
        modal.style.display = "block";
    });
});

span.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}


