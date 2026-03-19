/**
 * ═══════════════════════════════════════════════════════════════════════════════
 * Global Navbar Component - Python Essentials Curriculum
 * Non-invasive navigation injection for all pages
 * ═══════════════════════════════════════════════════════════════════════════════
 */

(function() {
    'use strict';

    // Configuration
    const CONFIG = {
        brand: {
            title: 'Python Essentials',
            logo: 'assets/brands/favicon-straydog.png',
            homeUrl: 'index.html'
        },
        // Detect if we're in a subdirectory
        basePath: detectBasePath()
    };

    // Navigation structure
    const NAV_ITEMS = [
        {
            label: 'Home',
            url: 'index.html',
            icon: '🏠'
        },
        {
            label: 'Lessons',
            icon: '📚',
            dropdown: true,
            items: [
                { header: 'Core Curriculum' },
                { label: 'Week 1: Intro to Python', url: 'lesson-plans/lesson_week1_intro_python.html', week: 1 },
                { label: 'Week 2: Data Structures', url: 'lesson-plans/lesson_week2_data_structures.html', week: 2 },
                { label: 'Week 3: Python Skills', url: 'lesson-plans/lesson_week3_python_skills.html', week: 3 },
                { label: 'Week 4: Data Engineering', url: 'lesson-plans/lesson_week4_data_engineering.html', week: 4 },
                { label: 'Week 5: Data Wrangling', url: 'lesson-plans/lesson_week5_data_wrangling.html', week: 5 },
                { label: 'Week 6: Data Cleaning', url: 'lesson-plans/lesson_week6_data_cleaning.html', week: 6 },
                { label: 'Week 7: Advanced Cleaning', url: 'lesson-plans/lesson_week7_advanced_cleaning.html', week: 7 },
                { label: 'Week 8: Databases & SQL', url: 'lesson-plans/lesson_week8_databases_sql.html', week: 8 },
                { label: 'Week 9: Intro to ML', url: 'lesson-plans/lesson_week9_intro_ml.html', week: 9 },
                { label: 'Week 10: Flask Web', url: 'lesson-plans/lesson_week10_flask_web.html', week: 10 },
                { label: 'Week 11: Deployment', url: 'lesson-plans/lesson_week11_deployment.html', week: 11 },
                { divider: true },
                { header: 'Supplemental' },
                { label: 'Data Visualization', url: 'lesson-plans/supplemental_data_visualization.html', supp: true },
                { label: 'APIs & Scraping', url: 'lesson-plans/supplemental_apis_scraping.html', supp: true },
                { label: 'Advanced Pandas', url: 'lesson-plans/supplemental_advanced_pandas.html', supp: true },
                { label: 'SQL Extended', url: 'lesson-plans/supplemental_sql_extended.html', supp: true }
            ]
        },
        {
            label: 'Resources',
            icon: '📖',
            dropdown: true,
            items: [
                { label: 'Mentor Guidebook', url: 'python-essentials-v2/mentor-guidebook/README.md' },
                { label: 'Assignments', url: 'python-essentials-v2/assignments/' },
                { label: 'Instructor Guides', url: 'python-essentials-v2/instructor_guides/' },
                { divider: true },
                { label: 'GitHub Repository', url: 'https://github.com/StrayDogSyn/Python-Essentials-Code-The-Dream', external: true }
            ]
        },
        {
            label: 'Notebooks',
            icon: '📓',
            dropdown: true,
            items: [
                { header: 'Week 1: Intro to Python' },
                { label: 'Session 1 - Solo Practice', url: 'https://colab.research.google.com/github/StrayDogSyn/Python-Essentials-Code-The-Dream/blob/main/notebook-sessions/week1/session1_intro_to_python.ipynb', external: true, colab: true },
                { label: 'Session 2 - Group Work', url: 'https://colab.research.google.com/github/StrayDogSyn/Python-Essentials-Code-The-Dream/blob/main/notebook-sessions/week1/session2_intro_to_python_group.ipynb', external: true, colab: true },
                { divider: true },
                { header: 'Week 2: Data Structures' },
                { label: 'Session 1 - Solo Practice', url: 'https://colab.research.google.com/github/StrayDogSyn/Python-Essentials-Code-The-Dream/blob/main/notebook-sessions/week2/session1_data_structures.ipynb', external: true, colab: true },
                { label: 'Session 2 - Group Work', url: 'https://colab.research.google.com/github/StrayDogSyn/Python-Essentials-Code-The-Dream/blob/main/notebook-sessions/week2/session2_data_structures_group.ipynb', external: true, colab: true },
                { divider: true },
                { header: 'Week 3: Python Skills' },
                { label: 'Session 1 - Solo Practice', url: 'https://colab.research.google.com/github/StrayDogSyn/Python-Essentials-Code-The-Dream/blob/main/notebook-sessions/week3/session1_more_python_skills.ipynb', external: true, colab: true },
                { label: 'Session 2 - Group Work', url: 'https://colab.research.google.com/github/StrayDogSyn/Python-Essentials-Code-The-Dream/blob/main/notebook-sessions/week3/session2_more_python_skills_group.ipynb', external: true, colab: true },
                { divider: true },
                { header: 'Week 4: Data Engineering' },
                { label: 'Session 1 - Solo Practice', url: 'https://colab.research.google.com/github/StrayDogSyn/Python-Essentials-Code-The-Dream/blob/main/notebook-sessions/week4/session1_intro_to_data_engineering.ipynb', external: true, colab: true },
                { label: 'Session 2 - Group Work', url: 'https://colab.research.google.com/github/StrayDogSyn/Python-Essentials-Code-The-Dream/blob/main/notebook-sessions/week4/session2_intro_to_data_engineering_group.ipynb', external: true, colab: true },
                { divider: true },
                { header: 'Week 5: Data Wrangling' },
                { label: 'Session 1 - Solo Practice', url: 'https://colab.research.google.com/github/StrayDogSyn/Python-Essentials-Code-The-Dream/blob/main/notebook-sessions/week5/session1_data_wrangling_aggregation.ipynb', external: true, colab: true },
                { label: 'Session 2 - Group Work', url: 'https://colab.research.google.com/github/StrayDogSyn/Python-Essentials-Code-The-Dream/blob/main/notebook-sessions/week5/session2_data_wrangling_aggregation_group.ipynb', external: true, colab: true },
                { divider: true },
                { header: 'Week 6: Data Cleaning' },
                { label: 'Session 1 - Solo Practice', url: 'https://colab.research.google.com/github/StrayDogSyn/Python-Essentials-Code-The-Dream/blob/main/notebook-sessions/week6/session1_data_cleaning_validation.ipynb', external: true, colab: true },
                { label: 'Session 2 - Group Work', url: 'https://colab.research.google.com/github/StrayDogSyn/Python-Essentials-Code-The-Dream/blob/main/notebook-sessions/week6/session2_data_cleaning_validation_group.ipynb', external: true, colab: true },
                { divider: true },
                { header: 'Week 7: Advanced Cleaning' },
                { label: 'Session 1 - Solo Practice', url: 'https://colab.research.google.com/github/StrayDogSyn/Python-Essentials-Code-The-Dream/blob/main/notebook-sessions/week7/session1_advanced_data_cleaning.ipynb', external: true, colab: true },
                { divider: true },
                { header: 'Week 8: Databases & SQL' },
                { label: 'Session 1 - Solo Practice', url: 'https://colab.research.google.com/github/StrayDogSyn/Python-Essentials-Code-The-Dream/blob/main/notebook-sessions/week8/session1_sql_databases.ipynb', external: true, colab: true },
                { label: 'Session 2 - Group Work', url: 'https://colab.research.google.com/github/StrayDogSyn/Python-Essentials-Code-The-Dream/blob/main/notebook-sessions/week8/session2_sql_databases_group.ipynb', external: true, colab: true },
                { divider: true },
                { header: 'Week 9: Intro to ML' },
                { label: 'Session 1 - Solo Practice', url: 'https://colab.research.google.com/github/StrayDogSyn/Python-Essentials-Code-The-Dream/blob/main/notebook-sessions/week9/session1_intro_to_ml.ipynb', external: true, colab: true },
                { label: 'Session 2 - Group Work', url: 'https://colab.research.google.com/github/StrayDogSyn/Python-Essentials-Code-The-Dream/blob/main/notebook-sessions/week9/session2_intro_to_ml_group.ipynb', external: true, colab: true },
                { divider: true },
                { header: 'Week 10: Flask Web' },
                { label: 'Session 1 - Solo Practice', url: 'https://colab.research.google.com/github/StrayDogSyn/Python-Essentials-Code-The-Dream/blob/main/notebook-sessions/week10/session1_flask_web.ipynb', external: true, colab: true },
                { label: 'Session 2 - Group Work', url: 'https://colab.research.google.com/github/StrayDogSyn/Python-Essentials-Code-The-Dream/blob/main/notebook-sessions/week10/session2_flask_web_group.ipynb', external: true, colab: true },
                { divider: true },
                { header: 'Week 11: Deployment' },
                { label: 'Session 1 - Solo Practice', url: 'https://colab.research.google.com/github/StrayDogSyn/Python-Essentials-Code-The-Dream/blob/main/notebook-sessions/week11/session1_deployment.ipynb', external: true, colab: true },
                { label: 'Session 2 - Group Work', url: 'https://colab.research.google.com/github/StrayDogSyn/Python-Essentials-Code-The-Dream/blob/main/notebook-sessions/week11/session2_deployment_group.ipynb', external: true, colab: true }
            ]
        }
    ];

    /**
     * Detect base path for relative URLs
     */
    function detectBasePath() {
        const path = window.location.pathname;
        if (path.includes('/lesson-plans/')) {
            return '../';
        } else if (path.includes('/python-essentials-v2/')) {
            return '../../';
        } else if (path.includes('/notebook-sessions/')) {
            return '../';
        }
        return '';
    }

    /**
     * Resolve URL with base path
     */
    function resolveUrl(url) {
        if (!url) return '#';
        if (url.startsWith('http') || url.startsWith('#')) return url;
        return CONFIG.basePath + url;
    }

    /**
     * Check if current page matches URL
     */
    function isActivePage(url) {
        if (!url || url === '#') return false;
        const currentPath = window.location.pathname.toLowerCase();
        const targetPath = url.toLowerCase().replace(/^\.\.\//, '').replace(/^\.\//, '');
        return currentPath.includes(targetPath.split('/').pop().replace('.html', ''));
    }

    /**
     * Create the navbar HTML
     */
    function createNavbar() {
        const nav = document.createElement('nav');
        nav.className = 'global-navbar';
        nav.setAttribute('role', 'navigation');
        nav.setAttribute('aria-label', 'Main navigation');

        nav.innerHTML = `
            <div class="navbar-container">
                <!-- Brand -->
                <a href="${resolveUrl(CONFIG.brand.homeUrl)}" class="navbar-brand" aria-label="Home">
                    <img src="${resolveUrl(CONFIG.brand.logo)}" alt="" class="navbar-logo">
                    <span class="navbar-title">${CONFIG.brand.title}</span>
                </a>

                <!-- Mobile Toggle -->
                <button class="navbar-toggle" aria-label="Toggle navigation" aria-expanded="false">
                    <span></span>
                    <span></span>
                    <span></span>
                </button>

                <!-- Navigation Links -->
                <ul class="navbar-nav">
                    ${NAV_ITEMS.map(item => createNavItem(item)).join('')}
                </ul>
            </div>
        `;

        return nav;
    }

    /**
     * Create a navigation item
     */
    function createNavItem(item) {
        if (item.dropdown) {
            return `
                <li class="nav-dropdown">
                    <a href="#" class="nav-link dropdown-toggle" aria-haspopup="true" aria-expanded="false">
                        <span class="nav-icon">${item.icon || ''}</span>
                        ${item.label}
                    </a>
                    <div class="dropdown-menu" role="menu">
                        ${item.items.map(subItem => createDropdownItem(subItem)).join('')}
                    </div>
                </li>
            `;
        }

        const isActive = isActivePage(item.url);
        const href = item.scrollTo ? item.url : resolveUrl(item.url);
        
        return `
            <li>
                <a href="${href}" class="nav-link${isActive ? ' active' : ''}"${item.scrollTo ? ' data-scroll-to="true"' : ''}>
                    <span class="nav-icon">${item.icon || ''}</span>
                    ${item.label}
                </a>
            </li>
        `;
    }

    /**
     * Create a dropdown item
     */
    function createDropdownItem(item) {
        if (item.divider) {
            return '<div class="dropdown-divider"></div>';
        }
        if (item.header) {
            return `<div class="dropdown-header">${item.header}</div>`;
        }

        const isActive = isActivePage(item.url);
        const href = resolveUrl(item.url);
        const externalAttrs = item.external ? ' target="_blank" rel="noopener noreferrer"' : '';
        const colabClass = item.colab ? ' colab-link' : '';
        
        return `
            <a href="${href}" class="dropdown-item${isActive ? ' active' : ''}${colabClass}" role="menuitem"${externalAttrs}>
                ${item.week ? `<span class="week-num">W${item.week}</span>` : ''}
                ${item.supp ? '<span class="week-num" style="background: linear-gradient(135deg, #00ff41, #ffff00);">+</span>' : ''}
                ${item.colab ? '<span class="colab-badge">▶</span>' : ''}
                <span>${item.label}</span>
                ${item.external && !item.colab ? '<span style="opacity: 0.5; font-size: 0.8em;">↗</span>' : ''}
            </a>
        `;
    }

    /**
     * Initialize event listeners
     */
    function initEventListeners() {
        // Mobile toggle
        const toggle = document.querySelector('.navbar-toggle');
        const nav = document.querySelector('.navbar-nav');
        
        if (toggle && nav) {
            toggle.addEventListener('click', () => {
                const isOpen = nav.classList.toggle('open');
                toggle.classList.toggle('active');
                toggle.setAttribute('aria-expanded', isOpen);
            });
        }

        // Mobile dropdown toggles
        const dropdowns = document.querySelectorAll('.nav-dropdown');
        dropdowns.forEach(dropdown => {
            const link = dropdown.querySelector('.dropdown-toggle');
            if (link && window.innerWidth <= 900) {
                link.addEventListener('click', (e) => {
                    e.preventDefault();
                    dropdown.classList.toggle('open');
                });
            }
        });

        // Scroll behavior for navbar
        let lastScroll = 0;
        window.addEventListener('scroll', () => {
            const navbar = document.querySelector('.global-navbar');
            if (!navbar) return;

            const currentScroll = window.pageYOffset;
            
            if (currentScroll > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }

            lastScroll = currentScroll;
        }, { passive: true });

        // Smooth scroll for in-page links
        document.querySelectorAll('.nav-link[data-scroll-to="true"]').forEach(link => {
            link.addEventListener('click', (e) => {
                const target = document.querySelector(link.getAttribute('href'));
                if (target) {
                    e.preventDefault();
                    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                    // Close mobile menu if open
                    nav?.classList.remove('open');
                    toggle?.classList.remove('active');
                }
            });
        });

        // Close mobile menu on outside click
        document.addEventListener('click', (e) => {
            if (nav?.classList.contains('open') && 
                !e.target.closest('.navbar-nav') && 
                !e.target.closest('.navbar-toggle')) {
                nav.classList.remove('open');
                toggle?.classList.remove('active');
            }
        });

        // Handle escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && nav?.classList.contains('open')) {
                nav.classList.remove('open');
                toggle?.classList.remove('active');
                toggle?.focus();
            }
        });
    }

    /**
     * Inject CSS if not already loaded
     */
    function injectCSS() {
        if (document.querySelector('link[href*="navbar.css"]')) return;
        
        const link = document.createElement('link');
        link.rel = 'stylesheet';
        link.href = resolveUrl('assets/css/navbar.css');
        document.head.appendChild(link);
    }

    /**
     * Initialize navbar
     */
    function init() {
        // Don't initialize if navbar already exists
        if (document.querySelector('.global-navbar')) return;

        // Inject CSS
        injectCSS();

        // Create and insert navbar
        const navbar = createNavbar();
        document.body.insertBefore(navbar, document.body.firstChild);

        // Add body class for padding
        document.body.classList.add('has-navbar');

        // Initialize event listeners
        initEventListeners();

        // Adjust any existing fixed elements
        const progressContainer = document.querySelector('.progress-container');
        if (progressContainer) {
            progressContainer.style.top = 'var(--navbar-height)';
        }

        const progressText = document.querySelector('.progress-text');
        if (progressText) {
            progressText.style.top = 'calc(var(--navbar-height) + 10px)';
        }
    }

    // Run on DOMContentLoaded
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

})();
