const roles = [
    "Python-разработчик",
    "Digital-маркетолог",
    "Web-разработчик",
    "Маркетолог-аналитик",
];

const roleElement = document.querySelector(".hero-role-highlight");

let roleIndex = 0;
let characterIndex = 0;
let deleting = false;

function typeRole() {
    const currentRole = roles[roleIndex];

    if (!deleting) {
        roleElement.textContent = currentRole.slice(
            0,
            characterIndex + 1
        );

        characterIndex++;

        if (characterIndex === currentRole.length) {
            deleting = true;

            setTimeout(typeRole, 1800);
            return;
        }
    } else {
        roleElement.textContent = currentRole.slice(
            0,
            characterIndex - 1
        );

        characterIndex--;

        if (characterIndex === 0) {
            deleting = false;
            roleIndex = (roleIndex + 1) % roles.length;
        }
    }

    const speed = deleting ? 50 : 100;

    setTimeout(typeRole, speed);
}

typeRole();