document.addEventListener("DOMContentLoaded", () => {

    /* =========================================
       LOADING
    ========================================= */

    const loader = document.getElementById("loader");

    function hideLoader() {
        if (!loader) return;

        setTimeout(() => {
            loader.classList.add("loader-hidden");
        }, 700);
    }

    if (document.readyState === "complete") {
        hideLoader();
    } else {
        window.addEventListener("load", hideLoader, {
            once: true
        });
    }


    /* =========================================
       HEADER
    ========================================= */

    const header =
        document.querySelector(".site-header");

    function updateHeader() {

        if (!header) return;

        if (window.scrollY > 40) {
            header.classList.add("scrolled");
        } else {
            header.classList.remove("scrolled");
        }
    }

    window.addEventListener(
        "scroll",
        updateHeader,
        { passive: true }
    );

    updateHeader();


    /* =========================================
       MOBILE MENU
    ========================================= */

    const menuButton =
        document.querySelector(".menu-toggle");

    const mobileMenu =
        document.querySelector(".mobile-menu");

    if (menuButton && mobileMenu) {

        menuButton.addEventListener("click", () => {

            menuButton.classList.toggle("active");

            mobileMenu.classList.toggle("active");

            document.body.classList.toggle(
                "menu-open"
            );

        });


        mobileMenu
            .querySelectorAll("a")
            .forEach(link => {

                link.addEventListener("click", () => {

                    menuButton.classList.remove(
                        "active"
                    );

                    mobileMenu.classList.remove(
                        "active"
                    );

                    document.body.classList.remove(
                        "menu-open"
                    );

                });

            });
    }


    /* =========================================
       SMOOTH SCROLL
    ========================================= */

    document
        .querySelectorAll('a[href^="#"]')
        .forEach(link => {

            link.addEventListener(
                "click",
                event => {

                    const targetId =
                        link.getAttribute("href");

                    if (
                        !targetId ||
                        targetId === "#"
                    ) {
                        return;
                    }

                    const target =
                        document.querySelector(
                            targetId
                        );

                    if (!target) return;

                    event.preventDefault();

                    const headerHeight =
                        header
                            ? header.offsetHeight
                            : 0;

                    const position =
                        target.getBoundingClientRect()
                            .top
                        +
                        window.scrollY
                        -
                        headerHeight;

                    window.scrollTo({
                        top: position,
                        behavior: "smooth"
                    });

                }
            );

        });


    /* =========================================
       REVEAL ANIMATIONS
    ========================================= */

    const revealElements =
        document.querySelectorAll(
            ".reveal, .reveal-left, .reveal-right, .scale-reveal"
        );


    if (
        "IntersectionObserver" in window
    ) {

        const revealObserver =
            new IntersectionObserver(
                entries => {

                    entries.forEach(entry => {

                        if (
                            entry.isIntersecting
                        ) {

                            entry.target.classList.add(
                                "revealed"
                            );

                            revealObserver.unobserve(
                                entry.target
                            );

                        }

                    });

                },
                {
                    threshold: 0.12,
                    rootMargin:
                        "0px 0px -45px 0px"
                }
            );


        revealElements.forEach(element => {
            revealObserver.observe(element);
        });

    } else {

        revealElements.forEach(element => {
            element.classList.add(
                "revealed"
            );
        });

    }


    /* =========================================
       COUNTERS
    ========================================= */

    const counters =
        document.querySelectorAll(
            "[data-counter]"
        );


    function animateCounter(element) {

        const target =
            Number(
                element.dataset.counter
            );

        const duration = 1800;

        const startTime =
            performance.now();


        function animate(currentTime) {

            const elapsed =
                currentTime -
                startTime;

            const progress =
                Math.min(
                    elapsed / duration,
                    1
                );

            const eased =
                1 -
                Math.pow(
                    1 - progress,
                    4
                );

            const value =
                Math.floor(
                    target * eased
                );

            element.textContent =
                value.toLocaleString(
                    "tr-TR"
                );


            if (progress < 1) {

                requestAnimationFrame(
                    animate
                );

            } else {

                element.textContent =
                    target.toLocaleString(
                        "tr-TR"
                    );

            }

        }


        requestAnimationFrame(
            animate
        );
    }


    if (
        counters.length &&
        "IntersectionObserver" in window
    ) {

        const counterObserver =
            new IntersectionObserver(
                entries => {

                    entries.forEach(entry => {

                        if (
                            entry.isIntersecting
                        ) {

                            animateCounter(
                                entry.target
                            );

                            counterObserver.unobserve(
                                entry.target
                            );

                        }

                    });

                },
                {
                    threshold: 0.65
                }
            );


        counters.forEach(counter => {

            counterObserver.observe(
                counter
            );

        });

    }


    /* =========================================
       HERO VIDEO
    ========================================= */

    const heroVideo =
        document.querySelector(
            ".hero-video"
        );


    if (heroVideo) {

        heroVideo.muted = true;

        const playVideo = () => {

            const promise =
                heroVideo.play();

            if (
                promise &&
                typeof promise.catch ===
                    "function"
            ) {

                promise.catch(() => {});

            }

        };


        heroVideo.addEventListener(
            "loadeddata",
            () => {

                heroVideo.classList.add(
                    "video-ready"
                );

                playVideo();

            },
            {
                once: true
            }
        );


        document.addEventListener(
            "visibilitychange",
            () => {

                if (
                    document.visibilityState ===
                    "visible"
                ) {

                    playVideo();

                }

            }
        );

    }


    /* =========================================
       CARD TILT
    ========================================= */

    const cards =
        document.querySelectorAll(
            "[data-tilt]"
        );


    cards.forEach(card => {

        card.addEventListener(
            "mousemove",
            event => {

                if (
                    window.innerWidth < 850
                ) {
                    return;
                }


                const rect =
                    card.getBoundingClientRect();


                const x =
                    event.clientX -
                    rect.left;

                const y =
                    event.clientY -
                    rect.top;


                const centerX =
                    rect.width / 2;

                const centerY =
                    rect.height / 2;


                const rotateX =
                    (
                        (y - centerY) /
                        centerY
                    ) * -2;


                const rotateY =
                    (
                        (x - centerX) /
                        centerX
                    ) * 2;


                card.style.transform =
                    `
                    perspective(1000px)
                    rotateX(${rotateX}deg)
                    rotateY(${rotateY}deg)
                    translateY(-4px)
                    `;
            }
        );


        card.addEventListener(
            "mouseleave",
            () => {

                card.style.transform =
                    "";

            }
        );

    });


    /* =========================================
       ACTIVE NAV
    ========================================= */

    const sections =
        document.querySelectorAll(
            "section[id]"
        );

    const navLinks =
        document.querySelectorAll(
            '.nav-links a[href^="#"]'
        );


    if (
        sections.length &&
        navLinks.length &&
        "IntersectionObserver" in window
    ) {

        const navObserver =
            new IntersectionObserver(
                entries => {

                    entries.forEach(entry => {

                        if (
                            entry.isIntersecting
                        ) {

                            navLinks.forEach(
                                link => {

                                    link.classList.remove(
                                        "active"
                                    );

                                }
                            );


                            const active =
                                document.querySelector(
                                    `.nav-links a[href="#${entry.target.id}"]`
                                );


                            if (active) {

                                active.classList.add(
                                    "active"
                                );

                            }

                        }

                    });

                },
                {
                    rootMargin:
                        "-25% 0px -60% 0px"
                }
            );


        sections.forEach(section => {

            navObserver.observe(
                section
            );

        });

    }


    /* =========================================
       CONTACT FORM
    ========================================= */

    const form =
        document.getElementById(
            "contact-form"
        );


    if (form) {

        form.addEventListener(
            "submit",
            event => {

                event.preventDefault();


                const button =
                    form.querySelector(
                        'button[type="submit"]'
                    );


                if (!button) return;


                const original =
                    button.innerHTML;


                button.disabled = true;

                button.innerHTML =
                    "Gönderiliyor...";


                setTimeout(() => {

                    button.innerHTML =
                        "Talep Alındı ✓";

                    button.classList.add(
                        "success"
                    );


                    form.reset();


                    setTimeout(() => {

                        button.innerHTML =
                            original;

                        button.disabled =
                            false;

                        button.classList.remove(
                            "success"
                        );

                    }, 2500);

                }, 900);

            }
        );

    }


    /* =========================================
       CURRENT YEAR
    ========================================= */

    document
        .querySelectorAll(
            "[data-current-year]"
        )
        .forEach(element => {

            element.textContent =
                new Date().getFullYear();

        });


    /* =========================================
       IMAGE LOADING
    ========================================= */

    document
        .querySelectorAll("img")
        .forEach(image => {

            image.addEventListener(
                "error",
                () => {

                    image.classList.add(
                        "image-error"
                    );

                }
            );

        });

});
