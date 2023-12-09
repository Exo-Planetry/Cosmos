// Get all elements with the class "toggle-btn" for planet info or moons
const toggleButtons = document.querySelectorAll('.toggle-btn');

// Iterate through each toggle button and add a click event listener
toggleButtons.forEach(button => {
    button.addEventListener('click', () => {
        // Toggle the visibility of the next sibling element (planet info or moon list)
        const infoSection = button.nextElementSibling;
        infoSection.classList.toggle('show');
    });
});

