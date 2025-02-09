// ... (Your sign-in/sign-up button code) ...

// Navigation button clicks
document.getElementById('home-btn').addEventListener('click', function() {
    window.location.href = 'index.html'; // Navigate to index.html (home)
});

document.getElementById('aboutus-btn').addEventListener('click', function() {
    window.location.href = 'aboutus.html'; // Navigate to aboutus.html
});

document.getElementById('resources-btn').addEventListener('click', function() {
    scrollToSection('resources'); // Scroll to resources section on index.html
});

document.getElementById('donation-btn').addEventListener('click', function() {
    scrollToSection('donations'); // Scroll to donations section on index.html
});

document.getElementById('language-btn').addEventListener('click', function() {
    // Implement language selection logic here
    alert("Language selection coming soon!");
});


function scrollToSection(sectionId) {
    if (sectionId) {
        const targetElement = document.getElementById(sectionId);
        if (targetElement) {
            targetElement.scrollIntoView({ behavior: 'smooth' });
        }
    } else {
        window.scrollTo({ top: 0, behavior: 'smooth' }); // Scroll to top
    }
}
// ... (Other button event listeners) ...

document.getElementById('resources-btn').addEventListener('click', function() {
    window.location.href = 'resources.html';  // Navigate to resources.html
});

// ... (Rest of your script.js code) ...
// ... (Other button event listeners) ...

document.getElementById('signin-btn').addEventListener('click', function() {
    window.location.href = 'sign_in.html'; // Redirect to sign_in.html
});

// ... (Rest of your script.js code) ...

// Sign-in form submission (example - you'll need backend integration)
document.getElementById('signin-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // Here, you would typically send the email and password to your server
    // for authentication.  This is a simplified example:
    if (email === "test@example.com" && password === "password") {
        alert("Sign in successful!");
        // Redirect to a logged-in page or update the UI
        window.location.href = "index.html"; // Or wherever you want to redirect
    } else {
        alert("Invalid email or password.");
    }

    // In a real application, you would use fetch or XMLHttpRequest to
    // send the form data to your backend for authentication.
});
document.addEventListener('DOMContentLoaded', function() {
    // ... (Other event listeners) ...

    document.getElementById('signup-btn').addEventListener('click', function() {
        window.location.href = 'sign_up.html'; // Redirect to sign_up.html
    });

    document.getElementById('signup-form').addEventListener('submit', function(event) {
        event.preventDefault();

        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        const confirmPassword = document.getElementById('confirm_password').value;

        // Client-side validation (example) - ALWAYS do server-side validation too
        if (password !== confirmPassword) {
            alert("Passwords do not match.");
            return; // Stop form submission
        }

        // *** VERY IMPORTANT ***
        // Send data to your server for user registration
        // (This is a placeholder - replace with server-side code)
        // Example using fetch (you'll need to adapt it):
        fetch('/register', { // Replace '/register' with your server endpoint
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) { // Assuming your server sends a success message
                alert("Sign up successful!");
                window.location.href = "sign_in.html"; // Redirect to sign-in page
            } else {
                alert(data.message || "Sign up failed."); // Display error message from server
            }
        })
        .catch(error => {
            console.error("Error:", error);
            alert("An error occurred during sign up.");
        });

    });

});