// Assuming you've included the fireworks-js library
const fireworksContainer = document.createElement('div');
fireworksContainer.classList.add('fireworks-container');
document.body.appendChild(fireworksContainer);

const fireworks = new Fireworks(fireworksContainer, { /* options */ });
fireworks.start();
