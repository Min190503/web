$(document).ready(function() {
    $('#toggle').click(function() {
        $('nav').slideToggle();
    });
})






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