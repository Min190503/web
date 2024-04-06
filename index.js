$(document).ready(function() {
    $('#toggle').click(function() {
        $('nav').slideToggle();
    });

})

$(document).ready(function() {
    var menuOpen = false;
    var pageLoaded = false;

    // Ẩn menu khi trang vừa tải lên và kích thước màn hình nhỏ hơn 480px
    if ($(window).width() < 480) {
        $('nav').hide();
    }
    
    // Kiểm tra trạng thái ban đầu của menu và ẩn nếu nó đã được mở trước đó
    if (!$('nav').is(':hidden')) {
        menuOpen = true;
    }

    // Kích hoạt sự kiện click sau khi trang đã tải hoàn tất và kích thước màn hình lớn hơn hoặc bằng 480px
    if ($(window).width() >= 480) {
        pageLoaded = true;
        $('#toggle').click(function() {
            // Đảo ngược trạng thái của biến menuOpen
            menuOpen = !menuOpen;
            if (menuOpen) {
                $('nav').slideDown();
            } else {
                $('nav').slideUp();
            }
        });
    }
    $('nav a').click(function() {
        if ($(window).width() < 480) {
            $('nav').slideUp();
            menuOpen = false;
        }
    });
});





function toggleChatBox() {
    var chatContainer = document.getElementById("chat-container");
    if (chatContainer.style.display === "none") {
        chatContainer.style.display = "block";
    } else {
        chatContainer.style.display = "none";
    }
}

function sendMessage() {
    var userInput = document.getElementById("user-input").value;
    if (userInput !== "") {
        var chatBox = document.getElementById("chat-box");
        var message = document.createElement("div");
        message.textContent = "Bạn: " + userInput;
        chatBox.appendChild(message);
        document.getElementById("user-input").value = "";
        // Tự động cuộn xuống dưới cùng khi có tin nhắn mới
        chatBox.scrollTop = chatBox.scrollHeight;
    }
}
var faq = {
    "Sản phẩm nào bạn quan tâm?": "Chúng tôi có nhiều sản phẩm đa dạng, bạn có thể xem danh sách sản phẩm trên trang chủ của chúng tôi.",
    "Bạn cung cấp dịch vụ gì?": "Chúng tôi cung cấp các dịch vụ vận chuyển hàng hóa nội địa và quốc tế.",
    "card": "yêu anhhhhh",
    // Thêm các câu hỏi và câu trả lời cố định khác ở đây
};
function displayAnswer(question) {
    var chatBox = document.getElementById("chat-box");
    var answer = faq[question];
    if (answer) {
        var message = document.createElement("div");
        message.textContent = "Em: " + answer;
        chatBox.appendChild(message);
        // Tự động cuộn xuống dưới cùng khi có tin nhắn mới
        chatBox.scrollTop = chatBox.scrollHeight;
    }
}
function sendMessage() {
    var userInput = document.getElementById("user-input").value;
    if (userInput !== "") {
        var chatBox = document.getElementById("chat-box");
        var message = document.createElement("div");
        message.textContent = "Bạn: " + userInput;
        chatBox.appendChild(message);
        displayAnswer(userInput); // Hiển thị câu trả lời nếu có
        document.getElementById("user-input").value = "";
        // Tự động cuộn xuống dưới cùng khi có tin nhắn mới
        chatBox.scrollTop = chatBox.scrollHeight;
    }
}