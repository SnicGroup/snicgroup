const listPaternaire = document.querySelectorAll('.partenaire');
const btnSuiv = document.querySelector(".btn-suiv");
const btnPrev = document.querySelector(".btn-prev");

let indexDepart = 0;
let totalPartenaire = listPaternaire.length;

function showPartenaire() {
    const membersToShow = window.innerWidth <= 768 ? 1 : 4;

    const start = indexDepart;
    const end = start + membersToShow;

    listPaternaire.forEach((member, i) => {
        member.style.display = i >= start && i < end ? 'block' : 'none';
    });
}

btnSuiv?.addEventListener('click', () => {
    indexDepart = (indexDepart + 1) % totalPartenaire;
    showPartenaire();
});

btnPrev?.addEventListener('click', () => {
    indexDepart = (indexDepart - 1 + totalPartenaire) % totalPartenaire;
    showPartenaire();
});

setInterval( () => {
    indexDepart = (indexDepart + 1) % totalPartenaire;
    showPartenaire()
}, 3000)

window.addEventListener('resize', showPartenaire);
document.addEventListener('DOMContentLoaded', showPartenaire);
