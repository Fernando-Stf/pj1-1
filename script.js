// ========================
// Navigation & Scroll
// ========================

const navbar = document.getElementById('navbar');
const navbarToggle = document.getElementById('navbar-toggle');
const navbarMenu = document.getElementById('navbar-menu');
const navLinks = document.querySelectorAll('.nav-link');

// Navbar scroll effect
window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

function setMenuOpen(open) {
    navbarToggle.classList.toggle('active', open);
    navbarMenu.classList.toggle('active', open);
    document.body.classList.toggle('menu-open', open);
    navbarToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    navbarToggle.setAttribute('aria-label', open ? 'Fechar menu' : 'Abrir menu');
}

navbarToggle.addEventListener('click', () => {
    setMenuOpen(!navbarMenu.classList.contains('active'));
});

navLinks.forEach(link => {
    link.addEventListener('click', () => setMenuOpen(false));
});

document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && navbarMenu.classList.contains('active')) {
        setMenuOpen(false);
        navbarToggle.focus();
    }
});

window.addEventListener('resize', () => {
    if (window.innerWidth > 960 && navbarMenu.classList.contains('active')) {
        setMenuOpen(false);
    }
});

// ========================
// Scroll Animations
// ========================

const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.animation = 'fadeIn 0.8s ease-out forwards';
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

// Observe elements
document.querySelectorAll('.sobre-content, .servico-card, .barbeiro-card, .depoimento-card, .experiencia-item').forEach(el => {
    observer.observe(el);
});

// ========================
// Galeria & Lightbox
// ========================

const lightbox = document.getElementById('lightbox');
const lightboxImage = document.querySelector('.lightbox-image');
const lightboxClose = document.querySelector('.lightbox-close');
const lightboxPrev = document.querySelector('.lightbox-prev');
const lightboxNext = document.querySelector('.lightbox-next');
const galeriaExpands = document.querySelectorAll('.galeria-expand');
const galeriaItems = document.querySelectorAll('.galeria-item img');

let currentImageIndex = 0;
const allImages = Array.from(galeriaItems).map(img => img.src);

function openGalleryAt(index) {
    currentImageIndex = index;
    openLightbox(allImages[index]);
}

galeriaExpands.forEach((btn, index) => {
    btn.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        openGalleryAt(index);
    });
});

document.querySelectorAll('.galeria-item').forEach((item, index) => {
    item.addEventListener('click', () => openGalleryAt(index));
    item.setAttribute('tabindex', '0');
    item.setAttribute('role', 'button');
    item.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            openGalleryAt(index);
        }
    });
});

// Close lightbox
lightboxClose.addEventListener('click', closeLightbox);
lightbox.addEventListener('click', (e) => {
    if (e.target === lightbox) closeLightbox();
});

// Keyboard navigation
document.addEventListener('keydown', (e) => {
    if (!lightbox.classList.contains('active')) return;

    if (e.key === 'Escape') closeLightbox();
    if (e.key === 'ArrowLeft') previousImage();
    if (e.key === 'ArrowRight') nextImage();
});

lightboxPrev.addEventListener('click', previousImage);
lightboxNext.addEventListener('click', nextImage);

function openLightbox(imageSrc) {
    lightboxImage.src = imageSrc;
    lightbox.classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeLightbox() {
    lightbox.classList.remove('active');
    document.body.style.overflow = '';
}

function nextImage() {
    currentImageIndex = (currentImageIndex + 1) % allImages.length;
    openLightbox(allImages[currentImageIndex]);
}

function previousImage() {
    currentImageIndex = (currentImageIndex - 1 + allImages.length) % allImages.length;
    openLightbox(allImages[currentImageIndex]);
}

// ========================
// Smooth Scroll for Buttons
// ========================

const scrollButtons = document.querySelectorAll('a[href^="#"]');

scrollButtons.forEach(button => {
    button.addEventListener('click', (e) => {
        const href = button.getAttribute('href');

        // Skip if it's an external link (WhatsApp, tel, etc)
        if (href.startsWith('#')) {
            const target = document.querySelector(href);
            if (target && href !== '#agendar') {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth' });
            }
        }
    });
});

// ========================
// Hero Scroll Indicator
// ========================

const heroScroll = document.querySelector('.hero-scroll');
if (heroScroll) {
    heroScroll.addEventListener('click', () => {
        const sobre = document.getElementById('sobre');
        if (sobre) {
            sobre.scrollIntoView({ behavior: 'smooth' });
        }
    });
}

// ========================
// Performance: Lazy Loading
// ========================

if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src || img.src;
                img.classList.remove('lazy');
                observer.unobserve(img);
            }
        });
    });

    document.querySelectorAll('img[data-src]').forEach(img => {
        imageObserver.observe(img);
    });
}

// ========================
// Accessibility
// ========================

// Focus management
document.addEventListener('keydown', (e) => {
    if (e.key === 'Tab') {
        document.body.classList.add('keyboard-nav');
    }
});

document.addEventListener('mousedown', () => {
    document.body.classList.remove('keyboard-nav');
});

// ========================
// Performance Monitoring
// ========================

// Log when page is fully loaded
window.addEventListener('load', () => {
    if (window.performance && window.performance.timing) {
        const perfData = window.performance.timing;
        const pageLoadTime = perfData.loadEventEnd - perfData.navigationStart;
        console.log('Page load time:', pageLoadTime + 'ms');
    }
});

// ========================
// Service Worker Registration
// ========================

if ('serviceWorker' in navigator && location.protocol === 'https:') {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js').catch(() => {
            // Service worker registration failed, continue normally
        });
    });
}
