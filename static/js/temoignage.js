const testimonials = document.querySelectorAll('.testimonial');
const nextTestimonialBtn = document.querySelector('.next-btn');
const prevTestimonialBtn = document.querySelector('.prev-btn');

let currentIndex = 0;
const totalTestimonials = testimonials.length;

function showTestimonials() {
    const testimonialsToShow = window.innerWidth <= 768 ? 1 : 3;

    const start = currentIndex;
    const end = start + testimonialsToShow;

    testimonials.forEach((testimonial, i) => {
        testimonial.style.display = i >= start && i < end ? 'block' : 'none';
    });
}

nextTestimonialBtn?.addEventListener('click', () => {
    currentIndex = (currentIndex + 1) % totalTestimonials;
    showTestimonials();
});

prevTestimonialBtn?.addEventListener('click', () => {
    currentIndex = (currentIndex - 1 + totalTestimonials) % testimonials.length;
    showTestimonials();
});

window.addEventListener('resize', showTestimonials);
document.addEventListener('DOMContentLoaded', showTestimonials);
