// Main JavaScript file for the project
document.addEventListener('DOMContentLoaded', function() {
    console.log('Main JavaScript loaded');
    
    // Add any global JavaScript functionality here
    
    // Example: Add smooth scrolling for anchor links
    const links = document.querySelectorAll('a[href^="#"]');
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
});