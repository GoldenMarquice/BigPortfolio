document.querySelectorAll('.nav-link a').forEach(option => {
    option.addEventListener('click', function (event){
        event.preventDefault();

        const targetId = this.getAttribute('href').substring(1);

        document.getElementById(targetId).scrollIntoView({
            behavior: 'smooth'
        });
    });
});