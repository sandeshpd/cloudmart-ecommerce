document.addEventListener('DOMContentLoaded', function () {
    const sidebarOptions = document.querySelectorAll('.option-link');
    const sections = document.querySelectorAll('.content-section > div');

    sidebarOptions.forEach(option => {
        option.addEventListener('click', function(e) {
            e.preventDefault();

            // Remove 'acitve' class from all sections
            sections.forEach(section => section.classList.remove('active'));

            // Remove 'active' class from all sidebar links
            sidebarOptions.forEach(link => link.classList.remove('active'));

            // Get the target section and add 'active' class
            const targetId = this.getAttribute('data-target');
            const targetSection = document.getElementById(targetId);
            if (targetSection) {
                targetSection.classList.add('active');
            }

            // Add 'active' class to the clicked sidebar link
            this.classList.add('active');
        });
    });
});