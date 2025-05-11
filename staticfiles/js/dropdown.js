document.addEventListener('DOMContentLoaded', () =>{
    const dropdownBtn = document.querySelector('.dropdown-btn');
    const dropdownMenu = document.querySelector('.dropdown-menu');
    const profileDropdown = document.querySelector('.profile-dropdown');
    const profileMenu = document.querySelector('.profile-menu');

    dropdownBtn.addEventListener('click', () => {
        dropdownMenu.classList.toggle('show');
    });

    // TODO: Close dropdownMenu on clicking outside

    profileDropdown.addEventListener('click', (e) => {
        e.stopPropagation();
        profileMenu.classList.toggle('show');
    });

    // Close profileMenu on clicking outside
    document.addEventListener('click', () => {
        profileMenu.classList.remove('show');
    });
})