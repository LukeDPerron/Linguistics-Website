document.addEventListener("DOMContentLoaded", function () {

    if (window.lucide) {
        lucide.createIcons();
    }

    const scrollHeader = document.querySelector('.scroll-header');

    if (scrollHeader) {
        window.addEventListener('scroll', function () {
            if (window.scrollY > 120) {
                scrollHeader.classList.add('show');
            } else {
                scrollHeader.classList.remove('show');
            }
        });
    }

});
