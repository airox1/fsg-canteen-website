document.addEventListener("DOMContentLoaded", () => {
    
    // Custom cursor requestAnimationFrame
    const cursor = document.getElementById('cursor');
    if (cursor) {
        let mouseX = 0, mouseY = 0;
        let cursorX = 0, cursorY = 0;
        
        document.addEventListener('mousemove', e => {
            mouseX = e.clientX;
            mouseY = e.clientY;
        });
        
        function animateCursor() {
            cursorX += (mouseX - cursorX) * 0.15;
            cursorY += (mouseY - cursorY) * 0.15;
            cursor.style.transform = `translate3d(-50%, -50%, 0) translate3d(${cursorX}px, ${cursorY}px, 0)`;
            requestAnimationFrame(animateCursor);
        }
        requestAnimationFrame(animateCursor);
        
        document.querySelectorAll('a, button, .station, .tab-btn').forEach(el => {
            el.addEventListener('mouseenter', () => cursor.classList.add('expanded'));
            el.addEventListener('mouseleave', () => cursor.classList.remove('expanded'));
        });
    }


    // Nav scroll effect
    const nav = document.getElementById('nav');
    if (nav) {
        window.addEventListener('scroll', () => {
            nav.classList.toggle('scrolled', window.scrollY > 40);
        });
    }

    // Mobile nav toggle
    const toggle = document.getElementById('navToggle');
    const links = document.getElementById('navLinks');
    if (toggle && links) {
        toggle.addEventListener('click', () => {
            links.classList.toggle('open');
        });
        links.querySelectorAll('a').forEach(a => {
            a.addEventListener('click', () => links.classList.remove('open'));
        });
    }

    // Tab switching for Menu page
    const tabs = document.querySelectorAll('.tab-btn');
    const panels = document.querySelectorAll('.menu-panel');

    if (tabs.length > 0 && panels.length > 0) {
        function activateTab(id) {
            tabs.forEach(t => t.classList.toggle('active', t.dataset.tab === id));
            panels.forEach(p => p.classList.toggle('active', p.id === id));
        }

        tabs.forEach(btn => {
            btn.addEventListener('click', () => {
                activateTab(btn.dataset.tab);
                history.replaceState(null, '', '#' + btn.dataset.tab);
            });
        });

        // Activate from URL hash on load
        const hash = location.hash.replace('#', '');
        if (hash && ['fried', 'steamed', 'grilled'].includes(hash)) {
            activateTab(hash);
        }
    }
});
