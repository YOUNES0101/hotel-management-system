document.addEventListener('DOMContentLoaded', function () {
    // Get the modal elements
    const signupModal = document.getElementById('signupModal');
    const loginModal = document.getElementById('loginModal');

    // Get the buttons that open the modals
    const openSignupBtn = document.getElementById('openSignupModal');
    const openLoginBtn = document.getElementById('openLoginModal');

    // Get the close buttons
    const closeSignupBtn = document.getElementById('closeSignupModal');
    const closeLoginBtn = document.getElementById('closeLoginModal');

    // When the user clicks the signup button, open the signup modal
    if (openSignupBtn) {
        openSignupBtn.addEventListener('click', function () {
            signupModal.style.display = 'block';
            document.body.style.overflow = 'hidden'; // Prevent scrolling behind modal
        });
    }

    // When the user clicks the login button, open the login modal
    if (openLoginBtn && loginModal) {
        openLoginBtn.addEventListener('click', function () {
            loginModal.style.display = 'block';
            document.body.style.overflow = 'hidden';
        });
    }

    // When the user clicks the close button for signup, close the modal
    if (closeSignupBtn) {
        closeSignupBtn.addEventListener('click', function () {
            signupModal.style.display = 'none';
            document.body.style.overflow = 'auto'; // Re-enable scrolling
        });
    }

    // When the user clicks the close button for login, close the modal
    if (closeLoginBtn && loginModal) {
        closeLoginBtn.addEventListener('click', function () {
            loginModal.style.display = 'none';
            document.body.style.overflow = 'auto';
        });
    }

    // When the user clicks anywhere outside of the modal, close it
    window.addEventListener('click', function (event) {
        if (event.target == signupModal) {
            signupModal.style.display = 'none';
            document.body.style.overflow = 'auto';
        }
        if (loginModal && event.target == loginModal) {
            loginModal.style.display = 'none';
            document.body.style.overflow = 'auto';
        }
    });

    // Optional: Handle switching between login and signup modals
    const switchToLoginLinks = document.querySelectorAll('.switch-to-login');
    const switchToSignupLinks = document.querySelectorAll('.switch-to-signup');

    switchToLoginLinks.forEach(link => {
        if (link && loginModal) {
            link.addEventListener('click', function (e) {
                e.preventDefault();
                signupModal.style.display = 'none';
                loginModal.style.display = 'block';
            });
        }
    });

    switchToSignupLinks.forEach(link => {
        if (link) {
            link.addEventListener('click', function (e) {
                e.preventDefault();
                if (loginModal) loginModal.style.display = 'none';
                signupModal.style.display = 'block';
            });
        }
    });

    // Auto-open modal if there are form errors
    const formErrors = document.querySelector('.errorlist');
    if (formErrors && formErrors.closest('#signupModal')) {
        signupModal.style.display = 'block';
        document.body.style.overflow = 'hidden';
    } else if (formErrors && loginModal && formErrors.closest('#loginModal')) {
        loginModal.style.display = 'block';
        document.body.style.overflow = 'hidden';
    }

})