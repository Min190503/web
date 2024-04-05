
var modal = document.getElementById("myModal");
var btns = document.querySelectorAll(".cvh p"); // Lấy tất cả các nút "Xem chi tiết"
var span = document.getElementsByClassName("close")[0];

// Khi người dùng nhấn vào nút "Xem chi tiết", hiển thị modal
btns.forEach(function(btn) {
    btn.addEventListener("click", function() {
        modal.style.display = "block";
    });
});

// Khi người dùng nhấn vào nút đóng, ẩn modal
span.onclick = function() {
    modal.style.display = "none";
}

// Khi người dùng nhấn ra ngoài modal, ẩn modal
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}