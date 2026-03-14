import os, re

# 2. REMOVE CURSOR: NONE
for css_file in ['css/style.css', 'css/pages.css']:
    with open(css_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove cursor: none
    content = re.sub(r'cursor:\s*none;', '', content)
    
    # In style.css, modify the .cursor transition
    if 'style.css' in css_file:
        content = content.replace(
            'transition: transform 0.08s ease, width 0.2s ease, height 0.2s ease, background 0.2s ease;',
            'transition: width 0.2s ease, height 0.2s ease, background 0.2s ease;'
        )
        # Add left:0; top:0;
        content = content.replace(
            'background: var(--amber);',
            'background: var(--amber);\n  left: 0;\n  top: 0;'
        )
        
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(content)

# 3. FIX JS CURSOR
with open('js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

new_cursor_js = '''
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
'''

js = re.sub(r'// Custom cursor\s*.*?\}\);.*?\n    \}', new_cursor_js, js, flags=re.DOTALL)

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(js)

# 4. FIX HTML ARIA
for html_file in ['index.html', 'menu.html', 'about.html']:
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()
        
    # Hide decorative items
    html = html.replace('class="station-number"', 'class="station-number" aria-hidden="true"')
    html = html.replace('class="concept-num"', 'class="concept-num" aria-hidden="true"')
    html = html.replace('class="panel-number"', 'class="panel-number" aria-hidden="true"')
    html = html.replace('class="item-icon"', 'class="item-icon" aria-hidden="true"')
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)

print('All CSS, JS, and HTML python tasks complete!')
