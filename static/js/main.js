// static/js/main.js

(function () {
    'use strict';

    // ========== Theme ==========
    window.toggleTheme = function () {
        const html = document.documentElement;
        const current = html.getAttribute('data-theme');
        const newTheme = current === 'dark' ? 'light' : 'dark';
        html.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        updateThemeIcon(newTheme);
    };

    function initTheme() {
        const saved = localStorage.getItem('theme');
        const theme = saved || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
        document.documentElement.setAttribute('data-theme', theme);
        updateThemeIcon(theme);
    }

    function updateThemeIcon(theme) {
        const icon = document.querySelector('.navbar .icon-btn i.fa-moon, .navbar .icon-btn i.fa-sun');
        if (icon) {
            if (theme === 'dark') {
                icon.classList.remove('fa-moon');
                icon.classList.add('fa-sun');
            } else {
                icon.classList.remove('fa-sun');
                icon.classList.add('fa-moon');
            }
        }
    }

    // ========== Language ==========
    let currentLang = localStorage.getItem('lang') || 'ar';

    window.toggleLanguage = function () {
        const html = document.documentElement;
        const logo = document.querySelector('.logo');
        if (currentLang === 'ar') {
            html.setAttribute('dir', 'ltr');
            html.setAttribute('lang', 'en');
            currentLang = 'en';
            if (logo) logo.innerHTML = '<i class="fas fa-graduation-cap logo-icon"></i><span>Academic Advisor</span>';
        } else {
            html.setAttribute('dir', 'rtl');
            html.setAttribute('lang', 'ar');
            currentLang = 'ar';
            if (logo) logo.innerHTML = '<i class="fas fa-graduation-cap logo-icon"></i><span>المستشار الأكاديمي</span>';
        }
        localStorage.setItem('lang', currentLang);
    };

    function initLanguage() {
        const saved = localStorage.getItem('lang');
        if (saved === 'en') {
            currentLang = 'en';
            document.documentElement.setAttribute('dir', 'ltr');
            document.documentElement.setAttribute('lang', 'en');
            const logo = document.querySelector('.logo');
            if (logo) logo.innerHTML = '<i class="fas fa-graduation-cap logo-icon"></i><span>Academic Advisor</span>';
        } else {
            currentLang = 'ar';
            document.documentElement.setAttribute('dir', 'rtl');
            document.documentElement.setAttribute('lang', 'ar');
        }
    }

    // ========== Account Dropdown ==========
    window.toggleAccountMenu = function () {
        const dropdown = document.getElementById('accountDropdown');
        if (dropdown) dropdown.classList.toggle('show');
    };

    function closeDropdownOnOutsideClick(event) {
        if (!event.target.closest('.account-menu')) {
            document.querySelectorAll('.dropdown-content').forEach(d => d.classList.remove('show'));
        }
    }

    function closeDropdownOnEscape(event) {
        if (event.key === 'Escape') {
            document.querySelectorAll('.dropdown-content').forEach(d => d.classList.remove('show'));
        }
    }

    // ========== Collapsible Cards ==========
    window.toggleCard = function (headerElement) {
        const card = headerElement.closest('.card, .major-card-full');
        if (!card) return;
        const body = card.querySelector('.card-body');
        const icon = card.querySelector('.toggle-icon');
        if (body) {
            body.classList.toggle('collapsed');
            if (icon) icon.classList.toggle('open');
        }
    };

    // ========== Help Panel ==========
    window.toggleHelp = function () {
        const panel = document.getElementById('helpPanel');
        if (panel) panel.classList.toggle('open');
    };

    function closeHelpOnEscape(event) {
        if (event.key === 'Escape') {
            const panel = document.getElementById('helpPanel');
            if (panel && panel.classList.contains('open')) panel.classList.remove('open');
        }
    }

    // ========== Toast System ==========
    window.showToast = function (message, type = 'info') {
        const allowedTypes = ['success', 'danger', 'warning', 'info'];
        if (!allowedTypes.includes(type)) type = 'info';

        let container = document.getElementById('toast-container');
        if (!container) {
            container = document.createElement('div');
            container.id = 'toast-container';
            container.setAttribute('aria-live', 'polite');
            container.setAttribute('aria-atomic', 'true');
            document.body.appendChild(container);
        }

        const toast = document.createElement('div');
        toast.className = `toast toast-${type}`;
        toast.setAttribute('role', 'alert');

        const messageSpan = document.createElement('span');
        messageSpan.textContent = message;
        toast.appendChild(messageSpan);

        const closeButton = document.createElement('button');
        closeButton.setAttribute('aria-label', 'إغلاق');
        closeButton.innerHTML = '&times;';
        closeButton.addEventListener('click', () => dismissToast(toast));
        toast.appendChild(closeButton);

        container.appendChild(toast);

        setTimeout(() => dismissToast(toast), 4500);
    };

    function dismissToast(toast) {
        if (!toast.parentElement) return;
        toast.style.opacity = '0';
        toast.style.transform = 'translateY(20px)';
        setTimeout(() => {
            if (toast.parentElement) toast.remove();
        }, 300);
    }

    // ========== Init ==========
    function init() {
        initTheme();
        initLanguage();
        document.addEventListener('click', closeDropdownOnOutsideClick);
        document.addEventListener('keydown', closeDropdownOnEscape);
        document.addEventListener('keydown', closeHelpOnEscape);

        const mobileToggle = document.getElementById('mobileMenuToggle');
        if (mobileToggle && !mobileToggle.dataset.listenerAttached) {
            const navbarActions = document.getElementById('navbarActions');
            if (navbarActions) {
                mobileToggle.addEventListener('click', () => {
                    const expanded = mobileToggle.getAttribute('aria-expanded') === 'true' ? 'false' : 'true';
                    mobileToggle.setAttribute('aria-expanded', expanded);
                    navbarActions.classList.toggle('active');
                });
                document.addEventListener('click', (event) => {
                    if (!navbarActions.contains(event.target) && event.target !== mobileToggle) {
                        mobileToggle.setAttribute('aria-expanded', 'false');
                        navbarActions.classList.remove('active');
                    }
                });
                mobileToggle.dataset.listenerAttached = 'true';
            }
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
function showChangeMajorModal() {
    document.getElementById('changeMajorModal').style.display = 'flex';
}
function hideChangeMajorModal() {
    document.getElementById('changeMajorModal').style.display = 'none';
}
function confirmChangeMajor() {
    window.location.href = "{{ url_for('university.change_major') }}";
}