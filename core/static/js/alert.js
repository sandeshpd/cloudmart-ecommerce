document.addEventListener('DOMContentLoaded', function () {
    const messageContainer = document.getElementById("message-container");
    if (messageContainer) {
        setTimeout(() => {
            messageContainer.style.display = 'none';
        }, 5000);
    }
});