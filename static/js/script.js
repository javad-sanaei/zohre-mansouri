// ===== STATE MANAGEMENT =====
const App = {
    // State
    isLoading: true,
    isScrolled: false,
    activeSection: 'home',
    mobileMenuOpen: false,
    stats: [
        { value: 1248, current: 0, suffix: '+', label: 'دانش‌آموز موفق' },
        { value: 15, current: 0, suffix: '', label: 'سال تجربه' },
        { value: 98, current: 0, suffix: '%', label: 'قبولی دانشگاه' },
        { value: 856, current: 0, suffix: '+', label: 'رتبه برتر' }
    ],
    skills: [
        { name: 'مشاوره تخصصی کنکور', value: 98, current: 0 },
        { name: 'انتخاب رشته', value: 95, current: 0 },
        { name: 'مدیریت استرس', value: 92, current: 0 },
        { name: 'تحصیل در خارج', value: 88, current: 0 }
    ],

    // ===== INITIALIZATION =====
    init() {
        this.initLoading();
        this.initScrollEffects();
        this.initMobileMenu();
        this.initSmoothScroll();
        this.initForm();
        this.initSwiper();
        this.initParticles();
        this.initTypewriter();
        this.initGSAP();
        this.initLazyLoading();
        this.initParallax();
        this.initHoverEffects();
        this.initServiceCardsClick();
    },

    // ===== LOADING SCREEN =====
    initLoading() {
        const loadingScreen = document.querySelector('.loading-screen');
        const loadingProgress = document.querySelector('.loading-progress-bar');
        const loadingText = document.querySelector('.luxury-loader-text');

        let progress = 0;
        const interval = setInterval(() => {
            progress += Math.random() * 3 + 1;

            if (progress >= 100) {
                progress = 100;
                clearInterval(interval);

                setTimeout(() => {
                    loadingScreen.classList.add('loading-complete');

                    setTimeout(() => {
                        this.startCounters();
                        this.startSkills();
                    }, 500);
                }, 500);
            }

            if (loadingProgress) {
                loadingProgress.style.width = `${progress}%`;
            }

            if (loadingText) {
                const dots = '.'.repeat(Math.floor(progress / 10) % 4);
                loadingText.textContent = `ZM${dots}`;
            }
        }, 50);

        setTimeout(() => {
            if (progress < 100) progress = 100;
        }, 2000);
    },

    // ===== TYPEWRITER EFFECT =====
    initTypewriter() {
        const typewriterElement = document.querySelector('.typewriter-text');
        if (!typewriterElement) return;

        const phrases = [
            'دکتری تخصصی مشاوره تحصیلی',
            'فارغ‌التحصیل دانشگاه تهران',
            'مشاور برتر ایران 1403',
            'عضو سازمان مشاوران کشور'
        ];

        let phraseIndex = 0;
        let charIndex = 0;
        let isDeleting = false;
        let isWaiting = false;

        const type = () => {
            const currentPhrase = phrases[phraseIndex];

            if (isDeleting) {
                typewriterElement.textContent = currentPhrase.substring(0, charIndex - 1);
                charIndex--;
            } else {
                typewriterElement.textContent = currentPhrase.substring(0, charIndex + 1);
                charIndex++;
            }

            if (!isDeleting && charIndex === currentPhrase.length) {
                isDeleting = true;
                isWaiting = true;
                setTimeout(() => { isWaiting = false; }, 2000);
            }

            if (isDeleting && charIndex === 0) {
                isDeleting = false;
                phraseIndex = (phraseIndex + 1) % phrases.length;
            }

            const speed = isDeleting ? 50 : 100;
            const delay = isWaiting ? 2000 : speed;

            setTimeout(type, delay);
        };

        type();
    },

    // ===== SCROLL EFFECTS =====
    initScrollEffects() {
        window.addEventListener('scroll', () => {
            const navbar = document.querySelector('.navbar');
            if (window.scrollY > 100) {
                navbar.classList.add('scrolled');
                this.isScrolled = true;
            } else {
                navbar.classList.remove('scrolled');
                this.isScrolled = false;
            }

            this.updateActiveSection();
            this.toggleBackToTop();
            this.parallaxEffect();
        });
    },

    updateActiveSection() {
        const sections = document.querySelectorAll('section[id]');
        const scrollPosition = window.scrollY + 200;

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionBottom = sectionTop + section.offsetHeight;
            const sectionId = section.getAttribute('id');

            if (scrollPosition >= sectionTop && scrollPosition <= sectionBottom) {
                this.activeSection = sectionId;

                document.querySelectorAll('.nav-link').forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === `#${sectionId}`) {
                        link.classList.add('active');
                    }
                });
            }
        });
    },

    toggleBackToTop() {
        const backToTop = document.querySelector('.back-to-top');
        if (window.scrollY > 500) {
            backToTop.classList.add('show');
        } else {
            backToTop.classList.remove('show');
        }
    },

    parallaxEffect() {
        const scrolled = window.scrollY;
        const parallaxElements = document.querySelectorAll('[data-parallax]');

        parallaxElements.forEach(el => {
            const speed = el.dataset.parallax || 0.5;
            const yPos = -(scrolled * speed);
            el.style.transform = `translateY(${yPos}px)`;
        });
    },

    // ===== COUNTERS =====
    startCounters() {
        this.stats.forEach((stat, index) => {
            let current = 0;
            const target = stat.value;
            const increment = target / 50;
            const counterElement = document.querySelector(`.stat-number-${index}`);

            if (!counterElement) return;

            const interval = setInterval(() => {
                current += increment;
                if (current >= target) {
                    current = target;
                    clearInterval(interval);
                }

                counterElement.textContent = Math.floor(current) + stat.suffix;
            }, 30);
        });
    },

    startSkills() {
        this.skills.forEach((skill, index) => {
            const skillBar = document.querySelector(`.skill-progress-${index}`);
            const percentElement = document.querySelector(`.skill-percent-${index}`);

            if (!skillBar || !percentElement) return;

            setTimeout(() => {
                skillBar.style.width = `${skill.value}%`;

                let current = 0;
                const target = skill.value;
                const increment = target / 50;

                const interval = setInterval(() => {
                    current += increment;
                    if (current >= target) {
                        current = target;
                        clearInterval(interval);
                    }

                    percentElement.textContent = `${Math.floor(current)}%`;
                }, 30);
            }, index * 200);
        });
    },

    // ===== MOBILE MENU =====
    initMobileMenu() {
        const menuBtn = document.querySelector('.mobile-menu-btn');
        const navMenu = document.querySelector('.nav-menu');

        if (!menuBtn || !navMenu) return;

        menuBtn.addEventListener('click', () => {
            this.mobileMenuOpen = !this.mobileMenuOpen;
            navMenu.classList.toggle('active');
            menuBtn.classList.toggle('active');
            menuBtn.setAttribute('aria-expanded', this.mobileMenuOpen);

            document.body.style.overflow = this.mobileMenuOpen ? 'hidden' : 'auto';
        });

        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', () => {
                navMenu.classList.remove('active');
                menuBtn.classList.remove('active');
                this.mobileMenuOpen = false;
                document.body.style.overflow = 'auto';
            });
        });

        window.addEventListener('resize', () => {
            if (window.innerWidth > 992) {
                navMenu.classList.remove('active');
                menuBtn.classList.remove('active');
                this.mobileMenuOpen = false;
                document.body.style.overflow = 'auto';
            }
        });
    },

    // ===== SERVICE CARDS CLICK (برای موبایل) =====
    initServiceCardsClick() {
        const serviceCards = document.querySelectorAll('.service-card');

        serviceCards.forEach(card => {
            card.addEventListener('click', function(e) {
                // فقط توی موبایل
                if (window.innerWidth <= 768 && !e.target.closest('.service-link')) {
                    this.classList.toggle('active');
                }
            });
        });
    }

    // ===== SMOOTH SCROLL =====
    initSmoothScroll() {
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', (e) => {
                e.preventDefault();
                const targetId = anchor.getAttribute('href');

                if (targetId === '#' || !targetId) return;

                const targetElement = document.querySelector(targetId);

                if (targetElement) {
                    const offsetTop = targetElement.offsetTop - 100;

                    window.scrollTo({
                        top: offsetTop,
                        behavior: 'smooth'
                    });
                }
            });
        });

        // Back to top
        document.querySelector('.back-to-top').addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    },

    // ===== FORM HANDLING =====
    initForm() {
        const form = document.getElementById('contactForm');

        if (form) {
            form.addEventListener('submit', (e) => {
                e.preventDefault();

                const formData = new FormData(form);
                const submitBtn = form.querySelector('button[type="submit"]');
                const originalText = submitBtn.innerHTML;
                submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> در حال ارسال...';
                submitBtn.disabled = true;

                console.log('Sending to:', form.action);
                console.log('Form data:', Object.fromEntries(formData));

                fetch(form.action, {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest'
                    }
                })
                .then(response => {
                    console.log('Response status:', response.status);
                    return response.json();
                })
                .then(data => {
                    console.log('Response data:', data);
                    if (data.success) {
                        submitBtn.innerHTML = '<i class="fas fa-check"></i> ارسال شد!';
                        submitBtn.style.background = 'linear-gradient(135deg, #00C853, #00E676)';
                        form.reset();
                        this.showToast(data.message || 'درخواست شما با موفقیت ارسال شد', 'success');
                    } else {
                        submitBtn.innerHTML = originalText;
                        this.showToast(data.message || 'خطایی رخ داد', 'error');
                        console.log('Form errors:', data.errors);
                    }
                })
                .catch(error => {
                    console.error('Fetch error:', error);
                    submitBtn.innerHTML = originalText;
                    this.showToast('خطا در ارتباط با سرور', 'error');
                })
                .finally(() => {
                    submitBtn.disabled = false;
                    setTimeout(() => {
                        submitBtn.innerHTML = originalText;
                        submitBtn.style.background = '';
                    }, 3000);
                });
            });
        }
    },

    // ===== TOAST NOTIFICATION =====
    showToast(message, type = 'success') {
        const toast = document.createElement('div');
        toast.className = `toast toast-${type}`;
        toast.innerHTML = `
            <i class="fas ${type === 'success' ? 'fa-check-circle' : 'fa-exclamation-circle'}"></i>
            <span>${message}</span>
        `;
        toast.setAttribute('role', 'alert');

        document.body.appendChild(toast);

        setTimeout(() => {
            toast.style.animation = 'slideInLeft 0.3s ease reverse';
            setTimeout(() => toast.remove(), 300);
        }, 3000);
    },

    // ===== SWIPER SLIDER =====
    initSwiper() {
        if (typeof Swiper === 'undefined') return;

        new Swiper('.testimonials-slider', {
            slidesPerView: 1,
            spaceBetween: 30,
            loop: true,
            autoplay: {
                delay: 5000,
                disableOnInteraction: false,
            },
            pagination: {
                el: '.swiper-pagination',
                clickable: true,
            },
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            },
            effect: 'fade',
            fadeEffect: { crossFade: true },
            speed: 1000,
        });
    },

    // ===== PARTICLES BACKGROUND =====
    initParticles() {
        const particlesContainer = document.getElementById('hero-particles');
        if (!particlesContainer) return;

        const particleCount = 50;

        for (let i = 0; i < particleCount; i++) {
            const particle = document.createElement('div');

            const size = Math.random() * 10 + 2;
            const x = Math.random() * 100;
            const y = Math.random() * 100;
            const duration = Math.random() * 20 + 10;
            const delay = Math.random() * 10;

            Object.assign(particle.style, {
                position: 'absolute',
                width: `${size}px`,
                height: `${size}px`,
                left: `${x}%`,
                top: `${y}%`,
                background: `radial-gradient(circle, ${
                    Math.random() > 0.5 ? 'var(--primary)' : 'var(--secondary)'
                }, transparent)`,
                borderRadius: '50%',
                opacity: Math.random() * 0.3 + 0.1,
                animation: `float ${duration}s ease-in-out infinite`,
                animationDelay: `${delay}s`,
                pointerEvents: 'none'
            });

            particlesContainer.appendChild(particle);
        }
    },

    // ===== GSAP ANIMATIONS =====
    initGSAP() {
        if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') return;

        gsap.registerPlugin(ScrollTrigger);

        gsap.utils.toArray('section').forEach(section => {
            gsap.from(section, {
                scrollTrigger: {
                    trigger: section,
                    start: 'top 80%',
                    end: 'bottom 20%',
                    toggleActions: 'play none none reverse'
                },
                opacity: 0,
                y: 100,
                duration: 1,
                ease: 'power3.out'
            });
        });

        gsap.utils.toArray('.stat-card').forEach((card, index) => {
            gsap.from(card, {
                scrollTrigger: { trigger: '.hero-stats', start: 'top 80%' },
                scale: 0,
                rotation: 360,
                duration: 1,
                delay: index * 0.1,
                ease: 'back.out(1.7)'
            });
        });
    },

    // ===== LAZY LOADING IMAGES =====
    initLazyLoading() {
        if ('IntersectionObserver' in window) {
            const imageObserver = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const img = entry.target;
                        img.src = img.dataset.src;
                        img.classList.add('fade-in');
                        observer.unobserve(img);
                    }
                });
            });

            document.querySelectorAll('img[data-src]').forEach(img => {
                imageObserver.observe(img);
            });
        }
    },

    // ===== PARALLAX BACKGROUND =====
    initParallax() {
        document.querySelectorAll('[data-parallax-bg]').forEach(el => {
            const speed = el.dataset.parallaxBg || 0.5;

            window.addEventListener('scroll', () => {
                const scrolled = window.scrollY;
                const yPos = -(scrolled * speed);
                el.style.backgroundPositionY = `${yPos}px`;
            });
        });
    },

    // ===== HOVER EFFECTS =====
    initHoverEffects() {
        const profileContainer = document.querySelector('.profile-container');
        if (profileContainer) {
            profileContainer.addEventListener('mousemove', (e) => {
                const rect = profileContainer.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;

                const centerX = rect.width / 2;
                const centerY = rect.height / 2;

                const rotateX = (y - centerY) / 20;
                const rotateY = (centerX - x) / 20;

                profileContainer.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
            });

            profileContainer.addEventListener('mouseleave', () => {
                profileContainer.style.transform = 'perspective(1000px) rotateX(0) rotateY(0)';
            });
        }
    }
};

// ===== SCROLL PROGRESS BAR =====
window.addEventListener('scroll', () => {
    const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrolled = (winScroll / height) * 100;

    const progressBar = document.querySelector('.scroll-progress');
    if (progressBar) {
        progressBar.style.width = scrolled + '%';
    }
});

// ===== INITIALIZE APP =====
document.addEventListener('DOMContentLoaded', () => {
    App.init();
});

// ===== AOS INITIALIZATION =====
if (typeof AOS !== 'undefined') {
    AOS.init({
        duration: 1000,
        once: true,
        offset: 100,
        easing: 'cubic-bezier(0.23, 1, 0.32, 1)',
        disable: window.innerWidth < 768
    });
}

// ===== PREVENT SCROLL ON MOBILE MENU =====
window.addEventListener('resize', () => {
    if (window.innerWidth > 992) {
        const navMenu = document.querySelector('.nav-menu');
        const menuBtn = document.querySelector('.mobile-menu-btn');

        if (navMenu) navMenu.classList.remove('active');
        if (menuBtn) menuBtn.classList.remove('active');
        document.body.style.overflow = 'auto';
    }
});

// ===== ABOUT VIDEO CONTROLS =====
document.addEventListener('DOMContentLoaded', function() {
    const videoPlayBtn = document.getElementById('videoPlayBtn');
    if (videoPlayBtn) {
        const video = document.querySelector('.video-wrapper video');

        videoPlayBtn.addEventListener('click', function() {
            this.classList.add('hidden');
            video.play();
        });

        // Show button again when video ends
        video.addEventListener('ended', function() {
            videoPlayBtn.classList.remove('hidden');
        });

        // Also show on pause
        video.addEventListener('pause', function() {
            videoPlayBtn.classList.remove('hidden');
        });
    }
});

// ===== NEW ACHIEVEMENT COUNTERS =====
function startAchievementCounters() {
    const counters = document.querySelectorAll('.achievement-card .counter');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const counter = entry.target;
                const target = parseInt(counter.dataset.target);
                let current = 0;
                const increment = target / 40;

                const interval = setInterval(() => {
                    current += increment;
                    if (current >= target) {
                        current = target;
                        clearInterval(interval);
                    }
                    counter.textContent = Math.floor(current);
                }, 40);

                observer.unobserve(counter);
            }
        });
    }, { threshold: 0.5 });

    counters.forEach(counter => observer.observe(counter));
}

document.addEventListener('DOMContentLoaded', startAchievementCounters);