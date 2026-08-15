/* =========================================================
   DORO LOJİSTİK
   MAIN JAVASCRIPT
========================================================= */

"use strict";


document.addEventListener("DOMContentLoaded", () => {

    initLoader();

    initNavbar();

    initMobileMenu();

    initRevealAnimations();

    initCursor();

    initQuoteForm();

    initCurrentYear();

    initVideoFallback();

});


/* =========================================================
   PAGE LOADER
========================================================= */

function initLoader() {

    const loader =
        document.getElementById("pageLoader");

    const percent =
        document.getElementById("loaderPercent");

    const line =
        loader?.querySelector(".loader-line span");


    if (!loader) {
        return;
    }


    let progress = 0;

    const interval =
        setInterval(() => {

            const increment =
                Math.random() * 8 + 3;

            progress =
                Math.min(
                    progress + increment,
                    96
                );


            if (percent) {
                percent.textContent =
                    `${Math.floor(progress)}%`;
            }


            if (line) {
                line.style.width =
                    `${progress}%`;
            }

        }, 120);


    const finishLoader = () => {

        clearInterval(interval);

        progress = 100;


        if (percent) {
            percent.textContent = "100%";
        }


        if (line) {
            line.style.width = "100%";
        }


        setTimeout(() => {

            loader.classList.add("loaded");

            document.body.classList.remove("loading");

        }, 350);

    };


    if (document.readyState === "complete") {

        setTimeout(
            finishLoader,
            650
        );

    } else {

        window.addEventListener(
            "load",
            () => {
                setTimeout(
                    finishLoader,
                    500
                );
            },
            {
                once: true
            }
        );

    }


    // Güvenlik fallback'i
    setTimeout(
        finishLoader,
        3500
    );

}


/* =========================================================
   NAVBAR
========================================================= */

function initNavbar() {

    const navbar =
        document.getElementById("navbar");

    if (!navbar) {
        return;
    }


    const updateNavbar =
        () => {

            if (window.scrollY > 40) {
                navbar.classList.add("scrolled");
            } else {
                navbar.classList.remove("scrolled");
            }

        };


    updateNavbar();


    window.addEventListener(
        "scroll",
        updateNavbar,
        {
            passive: true
        }
    );


    const links =
        document.querySelectorAll(
            ".nav-link"
        );


    const sections =
        document.querySelectorAll(
            "main section[id]"
        );


    const observer =
        new IntersectionObserver(
            entries => {

                entries.forEach(entry => {

                    if (!entry.isIntersecting) {
                        return;
                    }


                    const id =
                        entry.target.getAttribute(
                            "id"
                        );


                    links.forEach(link => {

                        link.classList.toggle(
                            "active",
                            link.getAttribute("href") ===
                            `#${id}`
                        );

                    });

                });

            },
            {
                rootMargin:
                    "-30% 0px -60% 0px"
            }
        );


    sections.forEach(section => {

        observer.observe(section);

    });

}


/* =========================================================
   MOBILE MENU
========================================================= */

function initMobileMenu() {

    const button =
        document.getElementById(
            "mobileMenuButton"
        );

    const menu =
        document.getElementById(
            "mobileMenu"
        );


    if (!button || !menu) {
        return;
    }


    button.addEventListener(
        "click",
        () => {

            menu.classList.toggle(
                "open"
            );

        }
    );


    menu.querySelectorAll("a")
        .forEach(link => {

            link.addEventListener(
                "click",
                () => {

                    menu.classList.remove(
                        "open"
                    );

                }
            );

        });

}


/* =========================================================
   SCROLL REVEAL
========================================================= */

function initRevealAnimations() {

    const elements =
        document.querySelectorAll(
            ".reveal, .reveal-image"
        );


    if (!elements.length) {
        return;
    }


    const observer =
        new IntersectionObserver(
            entries => {

                entries.forEach(
                    (entry, index) => {

                        if (
                            !entry.isIntersecting
                        ) {
                            return;
                        }


                        const element =
                            entry.target;


                        const delay =
                            Math.min(
                                index * 50,
                                250
                            );


                        setTimeout(
                            () => {

                                element.classList.add(
                                    "visible"
                                );

                            },
                            delay
                        );


                        observer.unobserve(
                            element
                        );

                    }
                );

            },
            {
                threshold: .12,
                rootMargin:
                    "0px 0px -40px 0px"
            }
        );


    elements.forEach(
        element => observer.observe(element)
    );

}


/* =========================================================
   CUSTOM CURSOR
========================================================= */

function initCursor() {

    const dot =
        document.getElementById(
            "cursorDot"
        );

    const ring =
        document.getElementById(
            "cursorRing"
        );


    if (!dot || !ring) {
        return;
    }


    if (
        !window.matchMedia(
            "(pointer: fine)"
        ).matches
    ) {
        return;
    }


    let mouseX = 0;
    let mouseY = 0;

    let ringX = 0;
    let ringY = 0;


    document.addEventListener(
        "mousemove",
        event => {

            mouseX = event.clientX;
            mouseY = event.clientY;


            dot.style.left =
                `${mouseX}px`;

            dot.style.top =
                `${mouseY}px`;

        }
    );


    const animate =
        () => {

            ringX +=
                (mouseX - ringX) * .16;

            ringY +=
                (mouseY - ringY) * .16;


            ring.style.left =
                `${ringX}px`;

            ring.style.top =
                `${ringY}px`;


            requestAnimationFrame(
                animate
            );

        };


    animate();


    document.querySelectorAll(
        "a, button, input, select"
    ).forEach(
        element => {

            element.addEventListener(
                "mouseenter",
                () => {

                    ring.style.width =
                        "50px";

                    ring.style.height =
                        "50px";

                    ring.style.background =
                        "rgba(239,123,34,.08)";

                }
            );


            element.addEventListener(
                "mouseleave",
                () => {

                    ring.style.width =
                        "34px";

                    ring.style.height =
                        "34px";

                    ring.style.background =
                        "transparent";

                }
            );

        }
    );

}


/* =========================================================
   QUOTE FORM
========================================================= */

function initQuoteForm() {

    const form =
        document.getElementById(
            "quoteForm"
        );

    const button =
        document.getElementById(
            "quoteSubmit"
        );

    const result =
        document.getElementById(
            "quoteResult"
        );


    if (!form || !button || !result) {
        return;
    }


    form.addEventListener(
        "submit",
        async event => {

            event.preventDefault();


            if (!form.checkValidity()) {

                form.reportValidity();

                return;

            }


            button.classList.add(
                "loading"
            );


            result.classList.remove(
                "show"
            );


            const formData =
                new FormData(form);


            const payload =
                Object.fromEntries(
                    formData.entries()
                );


            try {

                const response =
                    await fetch(
                        "/api/quote",
                        {
                            method: "POST",

                            headers: {
                                "Content-Type":
                                    "application/json"
                            },

                            body:
                                JSON.stringify(
                                    payload
                                )
                        }
                    );


                const data =
                    await response.json();


                if (!response.ok) {
                    throw new Error(
                        data.message ||
                        "İstek gönderilemedi."
                    );
                }


                result.innerHTML = `
                    <strong>Talebiniz oluşturuldu.</strong><br>
                    Talep numaranız:
                    <strong>${escapeHtml(data.request_id)}</strong>
                    <br>
                    Ekibimiz tarafından değerlendirilmek üzere
                    kaydınız oluşturuldu.
                `;


                result.classList.add(
                    "show"
                );


                form.reset();


                result.scrollIntoView({
                    behavior: "smooth",
                    block: "center"
                });


            } catch (error) {

                result.innerHTML = `
                    <strong>Bir sorun oluştu.</strong><br>
                    ${escapeHtml(
                        error.message ||
                        "Lütfen tekrar deneyin."
                    )}
                `;


                result.classList.add(
                    "show"
                );

            } finally {

                button.classList.remove(
                    "loading"
                );

            }

        }
    );

}


/* =========================================================
   VIDEO
========================================================= */

function initVideoFallback() {

    const video =
        document.querySelector(
            ".hero-video video"
        );


    if (!video) {
        return;
    }


    video.addEventListener(
        "error",
        () => {

            const wrapper =
                document.querySelector(
                    ".hero-video"
                );


            if (!wrapper) {
                return;
            }


            wrapper.style.background =
                "url('/static/images/tir-2.jpg') center / cover no-repeat";

        }
    );

}


/* =========================================================
   CURRENT YEAR
========================================================= */

function initCurrentYear() {

    const element =
        document.getElementById(
            "currentYear"
        );


    if (!element) {
        return;
    }


    element.textContent =
        new Date().getFullYear();

}


/* =========================================================
   HTML ESCAPE
========================================================= */

function escapeHtml(value) {

    return String(value)
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");

}// Doro Lojistik - Main JavaScript
