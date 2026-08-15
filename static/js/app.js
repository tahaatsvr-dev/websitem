/* =========================================================
   DORO LOJİSTİK
   INTERACTION ENGINE
========================================================= */

document.addEventListener("DOMContentLoaded", () => {

    const body = document.body;
    const loader = document.getElementById("loader");
    const loaderPercent = document.getElementById("loaderPercent");
    const loaderBar = document.querySelector(".loader-line span");

    body.classList.add("loading");


    /* =====================================================
       LOADER
    ===================================================== */

    let progress = 0;

    const loaderTimer = setInterval(() => {

        progress += Math.floor(Math.random() * 7) + 3;

        if (progress >= 100) {
            progress = 100;
            clearInterval(loaderTimer);
        }

        if (loaderPercent) {
            loaderPercent.textContent = `${progress}%`;
        }

        if (loaderBar) {
            loaderBar.style.width = `${progress}%`;
        }

    }, 70);


    const hideLoader = () => {

        setTimeout(() => {

            loader.classList.add("hidden");

            body.classList.remove("loading");

            setTimeout(() => {
                loader.remove();
            }, 900);

        }, 450);

    };


    if (document.readyState === "complete") {
        hideLoader();
    } else {
        window.addEventListener("load", hideLoader);
    }


    /* =====================================================
       NAVBAR
    ===================================================== */

    const navbar = document.getElementById("navbar");

    const updateNavbar = () => {

        if (window.scrollY > 60) {
            navbar.classList.add("scrolled");
        } else {
            navbar.classList.remove("scrolled");
        }

    };

    window.addEventListener("scroll", updateNavbar, {
        passive: true
    });

    updateNavbar();


    /* =====================================================
       MOBILE MENU
    ===================================================== */

    const mobileBtn = document.getElementById("mobileMenuBtn");
    const mobileMenu = document.getElementById("mobileMenu");

    if (mobileBtn && mobileMenu) {

        mobileBtn.addEventListener("click", () => {

            mobileMenu.classList.toggle("open");

        });


        mobileMenu.querySelectorAll("a").forEach(link => {

            link.addEventListener("click", () => {

                mobileMenu.classList.remove("open");

            });

        });

    }


    /* =====================================================
       SMOOTH ANCHOR
    ===================================================== */

    document.querySelectorAll('a[href^="#"]').forEach(link => {

        link.addEventListener("click", event => {

            const targetId = link.getAttribute("href");

            if (!targetId || targetId === "#") {
                return;
            }

            const target = document.querySelector(targetId);

            if (!target) {
                return;
            }

            event.preventDefault();

            target.scrollIntoView({
                behavior: "smooth",
                block: "start"
            });

        });

    });


    /* =====================================================
       SCROLL REVEAL
    ===================================================== */

    const revealElements =
        document.querySelectorAll(".reveal");


    const revealObserver = new IntersectionObserver(
        entries => {

            entries.forEach(entry => {

                if (!entry.isIntersecting) {
                    return;
                }

                entry.target.classList.add("visible");

                revealObserver.unobserve(entry.target);

            });

        },
        {
            threshold: .12,
            rootMargin: "0px 0px -50px 0px"
        }
    );


    revealElements.forEach((element, index) => {

        element.style.transitionDelay =
            `${Math.min(index * 40, 240)}ms`;

        revealObserver.observe(element);

    });


    /* =====================================================
       COUNTERS
    ===================================================== */

    const counters =
        document.querySelectorAll(".counter");

    const animateCounter = element => {

        const target =
            parseInt(element.dataset.target, 10);

        if (!Number.isFinite(target)) {
            return;
        }

        const duration = 1800;

        const startTime = performance.now();

        const update = currentTime => {

            const elapsed =
                currentTime - startTime;

            const progress =
                Math.min(elapsed / duration, 1);

            const eased =
                1 - Math.pow(1 - progress, 3);

            const current =
                Math.floor(target * eased);

            element.textContent =
                current.toLocaleString("tr-TR");

            if (progress < 1) {
                requestAnimationFrame(update);
            } else {
                element.textContent =
                    target.toLocaleString("tr-TR");
            }

        };

        requestAnimationFrame(update);
    };


    const counterObserver = new IntersectionObserver(
        entries => {

            entries.forEach(entry => {

                if (!entry.isIntersecting) {
                    return;
                }

                animateCounter(entry.target);

                counterObserver.unobserve(entry.target);

            });

        },
        {
            threshold: .6
        }
    );


    counters.forEach(counter => {
        counterObserver.observe(counter);
    });


    /* =====================================================
       HERO VIDEO FALLBACK
    ===================================================== */

    const heroVideo =
        document.querySelector(".hero-video");

    if (heroVideo) {

        heroVideo.addEventListener("error", () => {

            heroVideo.style.display = "none";

        });

        heroVideo.play().catch(() => {
            // Tarayıcı otomatik oynatmayı engellerse
            // poster görseli kullanılmaya devam eder.
        });

    }


    /* =====================================================
       IMAGE FALLBACK
    ===================================================== */

    document.querySelectorAll("img").forEach(img => {

        img.addEventListener("error", () => {

            img.style.opacity = "0";

            const parent = img.parentElement;

            if (parent) {
                parent.style.background =
                    "linear-gradient(135deg,#0b1b2d,#10263d)";
            }

        });

    });


    /* =====================================================
       CONTACT FORM
    ===================================================== */

    const form =
        document.getElementById("contactForm");

    const formMessage =
        document.getElementById("formMessage");


    if (form) {

        form.addEventListener("submit", event => {

            event.preventDefault();

            if (!formMessage) {
                return;
            }

            formMessage.style.display = "block";

            formMessage.textContent =
                "Talebiniz hazırlandı. Form gönderimini aktif etmek için e-posta/CRM bağlantısı eklenebilir.";

            form.reset();

        });

    }


    /* =====================================================
       ACTIVE NAVIGATION
    ===================================================== */

    const sections =
        document.querySelectorAll("main section[id]");

    const navLinks =
        document.querySelectorAll(".nav-link");


    const sectionObserver =
        new IntersectionObserver(
            entries => {

                entries.forEach(entry => {

                    if (!entry.isIntersecting) {
                        return;
                    }

                    const id =
                        entry.target.getAttribute("id");

                    navLinks.forEach(link => {

                        link.classList.remove("active");

                        if (
                            link.getAttribute("href") ===
                            `#${id}`
                        ) {
                            link.classList.add("active");
                        }

                    });

                });

            },
            {
                threshold: .35
            }
        );


    sections.forEach(section => {
        sectionObserver.observe(section);
    });


    /* =====================================================
       CURSOR GLOW
    ===================================================== */

    const cursorGlow =
        document.getElementById("cursorGlow");

    if (
        cursorGlow &&
        window.matchMedia("(pointer:fine)").matches
    ) {

        window.addEventListener("mousemove", event => {

            cursorGlow.style.left =
                `${event.clientX}px`;

            cursorGlow.style.top =
                `${event.clientY}px`;

            cursorGlow.style.opacity = "1";

        });

    }


    /* =====================================================
       IMAGE PARALLAX
    ===================================================== */

    const parallaxImages =
        document.querySelectorAll(
            ".about-image-main img, .statement-image img"
        );


    window.addEventListener("scroll", () => {

        if (
            window.matchMedia(
                "(prefers-reduced-motion: reduce)"
            ).matches
        ) {
            return;
        }

        const scrollY = window.scrollY;

        parallaxImages.forEach(img => {

            const rect =
                img.parentElement.getBoundingClientRect();

            if (
                rect.bottom < 0 ||
                rect.top > window.innerHeight
            ) {
                return;
            }

            const offset =
                (window.innerHeight / 2 - rect.top) * .025;

            img.style.transform =
                `translateY(${offset}px) scale(1.04)`;

        });

    }, {
        passive: true
    });

});
