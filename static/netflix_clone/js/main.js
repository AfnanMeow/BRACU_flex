// Netflix Clone JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // FAQ Accordion
    const faqItems = document.querySelectorAll('.faq-item');

    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');

        question.addEventListener('click', () => {
            // Close all other items
            faqItems.forEach(otherItem => {
                if (otherItem !== item && otherItem.classList.contains('active')) {
                    otherItem.classList.remove('active');
                }
            });

            // Toggle current item
            item.classList.toggle('active');
        });
    });

    // Header scroll effect for browse page
    const headerBrowse = document.querySelector('.header-browse');

    if (headerBrowse) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                headerBrowse.style.backgroundColor = 'var(--netflix-black)';
                headerBrowse.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.5)';
            } else {
                headerBrowse.style.backgroundColor = 'transparent';
                headerBrowse.style.boxShadow = 'none';
            }
        });
    }

    // Login form validation
   // const loginForm = document.querySelector('.login-form');

    //if (loginForm) {
       // loginForm.addEventListener('submit', (e) => {
            //e.preventDefault();

           // const emailInput = document.getElementById('email-login');
           // const passwordInput = document.getElementById('password');
           // let isValid = true;

            // Simple validation
           // if (!emailInput.value.trim()) {
               // isValid = false;
               // emailInput.style.borderBottom = '2px solid #e87c03';
           // } else {
               // emailInput.style.borderBottom = 'none';
          //  }

           // if (!passwordInput.value.trim()) {
               // isValid = false;
              //  passwordInput.style.borderBottom = '2px solid #e87c03';
           // } else {
               // passwordInput.style.borderBottom = 'none';
           // }

            // If valid, redirect to browse page
           // if (isValid) {
               // window.location.href = 'browse.html';
          //  }
       // });
   // }

    // Browse page title card hover effect
    const titleCards = document.querySelectorAll('.title-card');

    //titleCards.forEach(card => {
        //card.addEventListener('mouseover', () => {
            //setTimeout(() => {
                //card.querySelector('.title-card-play').style.opacity = '1';
            //}, 300);
        //});

        //card.addEventListener('mouseout', () => {
            //card.querySelector('.title-card-play').style.opacity = '0';
        //});

        // Add click handler to go to movie page
        //card.addEventListener('click', () => {
            //window.location.href = 'movie.html';
        //});
    //});
});
