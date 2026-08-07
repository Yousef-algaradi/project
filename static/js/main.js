// static/js/main.js

// 1. تبديل الثيم
function toggleTheme() {
    const html = document.documentElement;
    const current = html.getAttribute('data-theme');
    const newTheme = current === 'dark' ? 'light' : 'dark';
    html.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
}

// استعادة الثيم المخزن
document.addEventListener('DOMContentLoaded', () => {
    const saved = localStorage.getItem('theme');
    if (saved) document.documentElement.setAttribute('data-theme', saved);
});

// 2. تبديل اللغة
let currentLang = 'ar';
function toggleLanguage() {
    const html = document.documentElement;
    if (currentLang === 'ar') {
        html.setAttribute('dir', 'ltr');
        html.setAttribute('lang', 'en');
        currentLang = 'en';
        document.querySelector('.logo').innerText = '🎓 Academic Advisor';
    } else {
        html.setAttribute('dir', 'rtl');
        html.setAttribute('lang', 'ar');
        currentLang = 'ar';
        document.querySelector('.logo').innerText = '🎓 المستشار الأكاديمي';
    }
}

// 3. قائمة الحساب
function toggleAccountMenu() {
    document.getElementById('accountDropdown').classList.toggle('show');
}
window.onclick = function(event) {
    if (!event.target.closest('.account-menu')) {
        const dropdowns = document.getElementsByClassName('dropdown-content');
        for (let d of dropdowns) { d.classList.remove('show'); }
    }
}

// 4. البطاقات القابلة للطي (للتوافق مع البطاقات القديمة)
function toggleCard(headerElement) {
    const card = headerElement.closest('.card');
    if (card) {
        const body = card.querySelector('.card-body');
        const icon = card.querySelector('.toggle-icon');
        if (body) {
            body.classList.toggle('collapsed');
            if (icon) icon.classList.toggle('open');
        }
    }
}

// 5. لوحة المساعدة
function toggleHelp() {
    document.getElementById('helpPanel').classList.toggle('open');
}

// 6. دالة الـ Toast (يمكن استدعاؤها من أي مكان)
function showToast(message, type = 'info') {
    const container = document.getElementById('toast-container');
    if (!container) {
        // إذا لم توجد الحاوية، ننشئها
        const newContainer = document.createElement('div');
        newContainer.id = 'toast-container';
        document.body.appendChild(newContainer);
        return showToast(message, type);
    }
    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    toast.innerHTML = `
        <span>${message}</span>
        <button onclick="this.parentElement.remove()">&times;</button>
    `;
    container.appendChild(toast);
    
    setTimeout(() => {
        if (toast.parentElement) {
            toast.style.opacity = '0';
            toast.style.transform = 'translateY(20px)';
            setTimeout(() => toast.remove(), 300);
        }
    }, 4500);
}