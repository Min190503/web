//Menu mb&tb
$(document).ready(function() {
    $('#toggle').click(function() {
        $('nav').slideToggle();
    });

})

$(document).ready(function() {
    var menuOpen = false;
    var pageLoaded = false;

    if ($(window).width() < 1024) {
        $('nav').hide();
    }
    
  
    if (!$('nav').is(':hidden')) {
        menuOpen = true;
    }

  
    if ($(window).width() >= 1024) {
        pageLoaded = true;
        $('#toggle').click(function() {
           
            menuOpen = !menuOpen;
            if (menuOpen) {
                $('nav').slideDown();
            } else {
                $('nav').slideUp();
            }
        });
    }
    $('nav a').click(function() {
        if ($(window).width() < 1024) {
            $('nav').slideUp();
            menuOpen = false;
        }
    });
});




//Box chat
function toggleChatBox() {
    var chatContainer = document.getElementById("chat-container");
    if (chatContainer.style.display === "none") {
        chatContainer.style.display = "block";
    } else {
        chatContainer.style.display = "none";
    }
}



//Câu hỏi
var faq = {
    "Địa chỉ": "Số 2, Trường Sa, Bình Thạnh, Tp.HCM.",
    "Bạn cung cấp dịch vụ gì": "Chúng tôi cung cấp các dịch vụ vận chuyển hàng hóa nội địa và quốc tế.",
};
function displayAnswer(question) {
    var chatBox = document.getElementById("chat-box");
    var answer = faq[question];
    if (answer) {
        var message = document.createElement("div");
        message.textContent = "Chúng tôi: " + answer;
        chatBox.appendChild(message);
    
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


//back to top
$(document).ready(function(){
    $(window).scroll(function(){
        if($(this).scrollTop() > 300){
            $('#backtop').fadeIn();
        }else{
            $('#backtop').fadeOut();
        }
    });
    $('#backtop').click(function(){
        $('html, body').animate({scrollTop: 0}, 500);
    });
    
});;



