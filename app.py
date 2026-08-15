<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">

    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0"
    >

    <meta
        name="description"
        content="Doro Lojistik — modern, güvenilir ve profesyonel lojistik çözümleri."
    >

    <meta
        name="theme-color"
        content="#081a2e"
    >

    <title>Doro Lojistik | Lojistik Çözümleri</title>

    <link
        rel="stylesheet"
        href="{{ url_for('static', filename='css/style.css') }}"
    >
</head>

<body>

<!-- =====================================================
     PAGE LOADER
===================================================== -->

<div class="page-loader" id="pageLoader">

    <div class="loader-inner">

        <div class="loader-logo">
            <img
                src="{{ url_for('static', filename='logo/doro-logo.jpg') }}"
                alt="Doro Lojistik"
                onerror="this.style.display='none'; document.querySelector('.loader-logo-fallback').style.display='block';"
            >

            <span class="loader-logo-fallback">
                DORO
            </span>
        </div>

        <div class="loader-line">
            <span></span>
        </div>

        <div class="loader-status">
            <span>LOJİSTİK SİSTEMİ</span>
            <strong id="loaderPercent">0%</strong>
        </div>

    </div>

</div>


<!-- =====================================================
     CURSOR DECORATION
===================================================== -->

<div class="cursor-dot" id="cursorDot"></div>
<div class="cursor-ring" id="cursorRing"></div>


<!-- =====================================================
     NAVBAR
===================================================== -->

<header class="navbar" id="navbar">

    <div class="container navbar-inner">

        <a href="#home" class="brand">

            <div class="brand-logo">
                <img
                    src="{{ url_for('static', filename='logo/doro-logo.jpg') }}"
                    alt="Doro Lojistik"
                    onerror="this.style.display='none'; document.querySelector('.brand-fallback').style.display='block';"
                >

                <span class="brand-fallback">
                    DORO
                </span>
            </div>

        </a>


        <nav class="desktop-nav">

            <a href="#home" class="nav-link active">
                Ana Sayfa
            </a>

            <a href="#about" class="nav-link">
                Kurumsal
            </a>

            <a href="#services" class="nav-link">
                Hizmetler
            </a>

            <a href="#operations" class="nav-link">
                Operasyon
            </a>

            <a href="#quote" class="nav-link">
                Teklif
            </a>

        </nav>


        <a href="#contact" class="nav-cta">
            <span>İletişime Geç</span>
            <span class="arrow">↗</span>
        </a>


        <button
            class="mobile-menu-button"
            id="mobileMenuButton"
            type="button"
            aria-label="Menüyü aç"
        >
            <span></span>
            <span></span>
        </button>

    </div>


    <div class="mobile-menu" id="mobileMenu">

        <a href="#home">Ana Sayfa</a>
        <a href="#about">Kurumsal</a>
        <a href="#services">Hizmetler</a>
        <a href="#operations">Operasyon</a>
        <a href="#quote">Teklif Al</a>
        <a href="#contact">İletişim</a>

    </div>

</header>


<main>

<!-- =====================================================
     HERO
===================================================== -->

<section class="hero" id="home">

    <div class="hero-video">

        <video
            autoplay
            muted
            loop
            playsinline
            preload="metadata"
        >
            <source
                src="{{ url_for('static', filename='videos/hero-truck.mp4') }}"
                type="video/mp4"
            >
        </video>

    </div>


    <div class="hero-overlay"></div>

    <div class="hero-grid"></div>


    <div class="container hero-content">

        <div class="hero-tag reveal">
            <span class="tag-dot"></span>
            LOJİSTİK & TAŞIMACILIK
        </div>


        <h1 class="hero-title reveal">

            Yükünüzü
            <span>geleceğe</span>
            taşıyoruz.

        </h1>


        <p class="hero-description reveal">

            Operasyonun her aşamasını güven, hız ve
            profesyonel planlama anlayışıyla yönetiyoruz.

        </p>


        <div class="hero-actions reveal">

            <a href="#quote" class="button button-primary">

                <span>Teklif Al</span>

                <span class="button-icon">
                    ↗
                </span>

            </a>


            <a href="#services" class="button button-ghost">

                Hizmetlerimizi İncele

            </a>

        </div>


        <div class="hero-bottom reveal">

            <div class="hero-scroll">

                <span class="scroll-line"></span>

                <span>
                    AŞAĞI KAYDIR
                </span>

            </div>


            <div class="hero-location">

                <span>TR</span>

                <span class="location-line"></span>

                <span>LOGISTICS</span>

            </div>

        </div>

    </div>


    <div class="hero-number">
        01
    </div>

</section>


<!-- =====================================================
     INTRO
===================================================== -->

<section class="intro section" id="about">

    <div class="container">

        <div class="section-heading">

            <div class="eyebrow reveal">
                DORO LOJİSTİK
            </div>

            <h2 class="reveal">
                Lojistik yalnızca
                <em>taşımak</em> değildir.
            </h2>

        </div>


        <div class="intro-grid">

            <div class="intro-image reveal-image">

                <img
                    src="{{ url_for('static', filename='images/filo.jpg') }}"
                    alt="Doro Lojistik filosu"
                    loading="lazy"
                >

                <div class="image-label">
                    <span>01</span>
                    OPERASYONEL GÜÇ
                </div>

            </div>


            <div class="intro-copy">

                <p class="large-copy reveal">
                    Doğru planlama, doğru zamanlama ve
                    operasyonun her noktasını kontrol altında
                    tutmakla başlar.
                </p>


                <p class="body-copy reveal">
                    Doro Lojistik için her taşıma, başlangıç
                    noktasından teslimata kadar planlanan bir
                    süreçtir. Kara taşımacılığından konteyner
                    operasyonlarına kadar farklı ihtiyaçlara
                    uygun çözümler oluşturmayı hedefliyoruz.
                </p>


                <a href="#services" class="text-link reveal">
                    <span>Çözümlerimizi keşfet</span>
                    <span>↗</span>
                </a>

            </div>

        </div>

    </div>

</section>


<!-- =====================================================
     MARQUEE
===================================================== -->

<div class="marquee">

    <div class="marquee-track">

        <span>ROAD TRANSPORTATION</span>
        <i>✦</i>

        <span>LOGISTICS</span>
        <i>✦</i>

        <span>FREIGHT</span>
        <i>✦</i>

        <span>GLOBAL SOLUTIONS</span>
        <i>✦</i>

        <span>ROAD TRANSPORTATION</span>
        <i>✦</i>

        <span>LOGISTICS</span>
        <i>✦</i>

        <span>FREIGHT</span>
        <i>✦</i>

    </div>

</div>


<!-- =====================================================
     SERVICES
===================================================== -->

<section class="services section" id="services">

    <div class="container">

        <div class="services-header">

            <div>

                <div class="eyebrow reveal">
                    HİZMETLER
                </div>

                <h2 class="section-title reveal">
                    İhtiyaca göre
                    <br>
                    <em>tasarlanan</em> çözümler.
                </h2>

            </div>


            <p class="section-intro reveal">
                Taşımacılık ve lojistik operasyonlarının
                farklı ihtiyaçlarına uygun, planlı ve
                profesyonel çözümler.
            </p>

        </div>


        <div class="services-list">


            <!-- SERVICE 01 -->

            <article class="service-card reveal">

                <div class="service-number">
                    01
                </div>

                <div class="service-image">

                    <img
                        src="{{ url_for('static', filename='images/tir.jpg') }}"
                        alt="Karayolu taşımacılığı"
                        loading="lazy"
                    >

                </div>

                <div class="service-content">

                    <h3>
                        Karayolu
                        <br>
                        Taşımacılığı
                    </h3>

                    <p>
                        Yüklerin güvenli ve planlı şekilde
                        karayolu üzerinden taşınmasına yönelik
                        çözümler.
                    </p>

                    <span class="service-arrow">
                        ↗
                    </span>

                </div>

            </article>


            <!-- SERVICE 02 -->

            <article class="service-card service-card-reverse reveal">

                <div class="service-number">
                    02
                </div>

                <div class="service-image">

                    <img
                        src="{{ url_for('static', filename='images/gemi-konteyner.jpg') }}"
                        alt="Konteyner taşımacılığı"
                        loading="lazy"
                    >

                </div>

                <div class="service-content">

                    <h3>
                        Konteyner
                        <br>
                        Taşımacılığı
                    </h3>

                    <p>
                        Liman ve karayolu operasyonlarını
                        bir araya getiren konteyner çözümleri.
                    </p>

                    <span class="service-arrow">
                        ↗
                    </span>

                </div>

            </article>


            <!-- SERVICE 03 -->

            <article class="service-card reveal">

                <div class="service-number">
                    03
                </div>

                <div class="service-image">

                    <img
                        src="{{ url_for('static', filename='images/international.jpg') }}"
                        alt="Uluslararası lojistik"
                        loading="lazy"
                    >

                </div>

                <div class="service-content">

                    <h3>
                        Uluslararası
                        <br>
                        Lojistik
                    </h3>

                    <p>
                        Farklı rotalar ve operasyon ihtiyaçları
                        için planlanan uluslararası taşımacılık
                        çözümleri.
                    </p>

                    <span class="service-arrow">
                        ↗
                    </span>

                </div>

            </article>


            <!-- SERVICE 04 -->

            <article class="service-card service-card-reverse reveal">

                <div class="service-number">
                    04
                </div>

                <div class="service-image">

                    <img
                        src="{{ url_for('static', filename='images/depo-yukleme.jpg') }}"
                        alt="Depo ve yükleme operasyonu"
                        loading="lazy"
                    >

                </div>

                <div class="service-content">

                    <h3>
                        Depo &amp;
                        <br>
                        Operasyon
                    </h3>

                    <p>
                        Yükleme, depolama ve sevkiyat süreçlerinin
                        koordinasyonuna yönelik operasyonel yaklaşım.
                    </p>

                    <span class="service-arrow">
                        ↗
                    </span>

                </div>

            </article>

        </div>

    </div>

</section>


<!-- =====================================================
     FULL IMAGE BREAK
===================================================== -->

<section class="image-break">

    <div class="image-break-image">

        <img
            src="{{ url_for('static', filename='images/tir-2.jpg') }}"
            alt="Lojistik taşımacılığı"
            loading="lazy"
        >

    </div>


    <div class="image-break-overlay"></div>


    <div class="container image-break-content">

        <div class="eyebrow">
            HAREKETİN GÜCÜ
        </div>

        <h2>
            Yolun her
            <br>
            <em>kilometresinde.</em>
        </h2>

        <a href="#quote" class="button button-light">
            Operasyonunuzu Planlayın
            <span>↗</span>
        </a>

    </div>

</section>


<!-- =====================================================
     OPERATIONS
===================================================== -->

<section class="operations section" id="operations">

    <div class="container">

        <div class="section-top-row">

            <div>

                <div class="eyebrow reveal">
                    OPERASYON
                </div>

                <h2 class="section-title reveal">
                    Planlı.
                    <br>
                    <em>Kontrollü.</em>
                    <br>
                    Kesintisiz.
                </h2>

            </div>


            <p class="section-intro reveal">
                Bir taşımanın başarısı yalnızca yolda değil,
                yolculuk başlamadan önce yapılan planlamada
                belirlenir.
            </p>

        </div>


        <div class="process">

            <div class="process-line"></div>


            <div class="process-item reveal">

                <span class="process-number">
                    01
                </span>

                <h3>
                    İhtiyacı
                    <br>
                    Anlıyoruz
                </h3>

                <p>
                    Yük, rota, zamanlama ve operasyon
                    gereksinimlerini değerlendiriyoruz.
                </p>

            </div>


            <div class="process-item reveal">

                <span class="process-number">
                    02
                </span>

                <h3>
                    Planı
                    <br>
                    Oluşturuyoruz
                </h3>

                <p>
                    Operasyona uygun taşıma ve sevkiyat
                    planını oluşturuyoruz.
                </p>

            </div>


            <div class="process-item reveal">

                <span class="process-number">
                    03
                </span>

                <h3>
                    Süreci
                    <br>
                    Yönetiyoruz
                </h3>

                <p>
                    Taşımanın farklı aşamalarını
                    koordineli şekilde takip ediyoruz.
                </p>

            </div>


            <div class="process-item reveal">

                <span class="process-number">
                    04
                </span>

                <h3>
                    Teslimatı
                    <br>
                    Tamamlıyoruz
                </h3>

                <p>
                    Sürecin son adımına kadar operasyonun
                    kontrolünü sürdürüyoruz.
                </p>

            </div>

        </div>

    </div>

</section>


<!-- =====================================================
     FACILITY
===================================================== -->

<section class="facility section">

    <div class="container">

        <div class="facility-grid">

            <div class="facility-main reveal-image">

                <img
                    src="{{ url_for('static', filename='images/depo.jpg') }}"
                    alt="Lojistik depo"
                    loading="lazy"
                >

            </div>


            <div class="facility-side">

                <div class="eyebrow reveal">
                    OPERASYONEL ALTYAPI
                </div>

                <h2 class="reveal">
                    Lojistiğin
                    <br>
                    görünmeyen
                    <br>
                    <em>tarafı.</em>
                </h2>

                <p class="reveal">
                    Başarılı bir taşımanın arkasında yalnızca
                    araçlar değil; planlama, koordinasyon,
                    depolama ve operasyon süreçleri bulunur.
                </p>


                <div class="mini-image reveal-image">

                    <img
                        src="{{ url_for('static', filename='images/depo-2.jpg') }}"
                        alt="Depo operasyonu"
                        loading="lazy"
                    >

                </div>

            </div>

        </div>

    </div>

</section>


<!-- =====================================================
     FLEET
===================================================== -->

<section class="fleet section">

    <div class="fleet-background">

        <img
            src="{{ url_for('static', filename='images/filo.jpg') }}"
            alt=""
            loading="lazy"
        >

    </div>

    <div class="fleet-overlay"></div>


    <div class="container fleet-content">

        <div class="eyebrow reveal">
            FİLO &amp; HAREKET
        </div>

        <h2 class="reveal">
            Yükünüz
            <br>
            <em>yolda.</em>
        </h2>

        <p class="reveal">
            Operasyonun ihtiyaçlarına göre planlanan
            taşıma süreçleriyle yükünüzün hareketini
            güvenilir bir operasyon anlayışıyla yönetiyoruz.
        </p>

    </div>

</section>


<!-- =====================================================
     AI QUOTE
===================================================== -->

<section class="quote section" id="quote">

    <div class="container">

        <div class="quote-header">

            <div>

                <div class="eyebrow reveal">
                    DORO SMART QUOTE
                </div>

                <h2 class="section-title reveal">
                    Taşımanızı
                    <br>
                    <em>planlayalım.</em>
                </h2>

            </div>


            <p class="section-intro reveal">
                Temel taşıma bilgilerinizi paylaşın.
                Sistemimiz talebinizi oluşturup size özel
                değerlendirme için hazırlasın.
            </p>

        </div>


        <div class="quote-box reveal">

            <form id="quoteForm" autocomplete="off">

                <div class="form-heading">

                    <span>01</span>

                    <h3>
                        Taşıma detayları
                    </h3>

                </div>


                <div class="form-grid">

                    <label class="field">

                        <span>
                            Nereden *
                        </span>

                        <input
                            type="text"
                            name="origin"
                            placeholder="Şehir / ülke"
                            required
                        >

                    </label>


                    <label class="field">

                        <span>
                            Nereye *
                        </span>

                        <input
                            type="text"
                            name="destination"
                            placeholder="Şehir / ülke"
                            required
                        >

                    </label>


                    <label class="field">

                        <span>
                            Yük türü *
                        </span>

                        <input
                            type="text"
                            name="cargo"
                            placeholder="Örn. genel kargo"
                            required
                        >

                    </label>


                    <label class="field">

                        <span>
                            Yaklaşık ağırlık
                        </span>

                        <input
                            type="text"
                            name="weight"
                            placeholder="Örn. 12 ton"
                        >

                    </label>


                    <label class="field">

                        <span>
                            Araç / taşıma tipi *
                        </span>

                        <select name="vehicle" required>

                            <option value="">
                                Seçiniz
                            </option>

                            <option value="Komple Tır">
                                Komple Tır
                            </option>

                            <option value="Konteyner">
                                Konteyner
                            </option>

                            <option value="Proje Taşımacılığı">
                                Proje Taşımacılığı
                            </option>

                            <option value="Diğer">
                                Diğer
                            </option>

                        </select>

                    </label>


                    <label class="field">

                        <span>
                            İletişim tercihi
                        </span>

                        <input
                            type="text"
                            name="email"
                            placeholder="E-posta (opsiyonel)"
                        >

                    </label>

                </div>


                <div class="form-divider"></div>


                <div class="form-heading">

                    <span>02</span>

                    <h3>
                        İletişim bilgileriniz
                    </h3>

                </div>


                <div class="form-grid">

                    <label class="field">

                        <span>
                            Ad soyad *
                        </span>

                        <input
                            type="text"
                            name="name"
                            placeholder="Adınız ve soyadınız"
                            required
                        >

                    </label>


                    <label class="field">

                        <span>
                            Telefon *
                        </span>

                        <input
                            type="tel"
                            name="phone"
                            placeholder="Telefon numaranız"
                            required
                        >

                    </label>

                </div>


                <div class="form-footer">

                    <p>
                        Formu gönderdiğinizde talebiniz
                        değerlendirilmek üzere oluşturulur.
                    </p>


                    <button
                        class="submit-button"
                        type="submit"
                        id="quoteSubmit"
                    >

                        <span class="button-text">
                            Teklif Talebi Oluştur
                        </span>

                        <span class="button-loading">
                            Gönderiliyor...
                        </span>

                        <span class="submit-icon">
                            ↗
                        </span>

                    </button>

                </div>


                <div
                    class="quote-result"
                    id="quoteResult"
                ></div>

            </form>

        </div>

    </div>

</section>


<!-- =====================================================
     CONTACT CTA
===================================================== -->

<section class="contact-cta" id="contact">

    <div class="container">

        <div class="contact-cta-inner">

            <div class="eyebrow reveal">
                BİRLİKTE ÇALIŞALIM
            </div>

            <h2 class="reveal">
                Bir sonraki
                <br>
                <em>yükünüz</em> için
                konuşalım.
            </h2>

            <a href="#quote" class="button button-light reveal">

                Teklif Talebi Oluştur

                <span>↗</span>

            </a>

        </div>

    </div>

</section>

</main>


<!-- =====================================================
     FOOTER
===================================================== -->

<footer class="footer">

    <div class="container">

        <div class="footer-main">

            <div class="footer-brand">

                <div class="footer-logo">
                    <img
                        src="{{ url_for('static', filename='logo/doro-logo.jpg') }}"
                        alt="Doro Lojistik"
                        onerror="this.style.display='none';"
                    >
                </div>

                <p>
                    Lojistik süreçleriniz için
                    planlı, profesyonel ve
                    çözüm odaklı yaklaşım.
                </p>

            </div>


            <div class="footer-column">

                <span class="footer-title">
                    MENÜ
                </span>

                <a href="#home">Ana Sayfa</a>
                <a href="#about">Kurumsal</a>
                <a href="#services">Hizmetler</a>
                <a href="#quote">Teklif Al</a>

            </div>


            <div class="footer-column">

                <span class="footer-title">
                    HİZMETLER
                </span>

                <a href="#services">
                    Karayolu
                </a>

                <a href="#services">
                    Konteyner
                </a>

                <a href="#services">
                    Uluslararası
                </a>

                <a href="#services">
                    Operasyon
                </a>

            </div>


            <div class="footer-column">

                <span class="footer-title">
                    İLETİŞİM
                </span>

                <a href="#quote">
                    Teklif Talebi
                </a>

                <a href="#quote">
                    Operasyon
                </a>

                <a href="#home">
                    Doro Lojistik
                </a>

            </div>

        </div>


        <div class="footer-bottom">

            <span>
                © <span id="currentYear"></span> Doro Lojistik
            </span>

            <span>
                LOGISTICS / TRANSPORTATION
            </span>

            <a href="#home">
                YUKARI ↑
            </a>

        </div>

    </div>

</footer>


<script
    src="{{ url_for('static', filename='js/app.js') }}"
    defer
></script>

</body>
</html>
