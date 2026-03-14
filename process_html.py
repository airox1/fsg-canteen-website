import os, re

for f_name in ['index.html', 'menu.html', 'about.html']:
    with open(f_name, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove inline style
    content = re.sub(r'<style>.*?</style>', '', content, flags=re.DOTALL)
    
    # Check if pages.css is linked
    if 'css/pages.css' not in content:
        content = content.replace('<link rel="stylesheet" href="css/style.css" />', '<link rel="stylesheet" href="css/style.css" />\n  <link rel="stylesheet" href="css/pages.css" />')
        
    # Replace inline script with external script
    content = re.sub(r'<script>.*?</script>', '<script src="js/main.js"></script>', content, flags=re.DOTALL)
    
    # Re-save
    with open(f_name, 'w', encoding='utf-8') as file:
        file.write(content)

print('Done fixing html files')
