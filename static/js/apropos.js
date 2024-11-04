const teamMembers = document.querySelectorAll('.team-member');
const nextBtn = document.querySelector('.next-btn');
const prevBtn = document.querySelector('.prev-btn');

let index = 0;
let totalMembers = teamMembers.length;

function showMembers() {
    const membersToShow = window.innerWidth <= 768 ? 1 : 3;

    const start = index;
    const end = start + membersToShow;

    teamMembers.forEach((member, i) => {
        member.style.display = i >= start && i < end ? 'block' : 'none';
    });
}

nextBtn?.addEventListener('click', () => {
    index = (index + 1) % totalMembers;
    showMembers();
});

prevBtn?.addEventListener('click', () => {
    index = (index - 1 + totalMembers) % totalMembers;
    showMembers();
});

window.addEventListener('resize', showMembers);
document.addEventListener('DOMContentLoaded', showMembers);
