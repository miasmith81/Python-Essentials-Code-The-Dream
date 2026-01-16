#!/usr/bin/env python3
"""
Script to add navbar CSS and JS references to all lesson plan HTML files.
Non-invasive: checks if already present before adding.
"""

import os
import re
from pathlib import Path

# Project root
PROJECT_ROOT = Path(__file__).parent.parent
LESSON_PLANS_DIR = PROJECT_ROOT / "lesson-plans"

# References to add
NAVBAR_CSS = '<link rel="stylesheet" href="../assets/css/navbar.css">'
NAVBAR_JS = '<script src="../assets/js/navbar.js" defer></script>'

def process_html_file(filepath: Path) -> tuple[bool, str]:
    """
    Add navbar CSS and JS references to an HTML file.
    Returns (modified, message).
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    messages = []
    
    # Check if navbar CSS already present
    if 'navbar.css' not in content:
        # Find the last stylesheet link or the end of head section to insert CSS
        # Try to insert after other CSS links
        css_pattern = r'(<link[^>]*stylesheet[^>]*>)(\s*)'
        css_matches = list(re.finditer(css_pattern, content, re.IGNORECASE))
        
        if css_matches:
            # Insert after the last CSS link
            last_css = css_matches[-1]
            insert_pos = last_css.end()
            content = content[:insert_pos] + '\n    <link rel="stylesheet" href="../assets/css/navbar.css">' + content[insert_pos:]
            messages.append("Added navbar.css link")
        else:
            # Try inserting before <style> or </head>
            style_open = content.find('<style>')
            if style_open != -1:
                content = content[:style_open] + NAVBAR_CSS + '\n    ' + content[style_open:]
                messages.append("Added navbar.css link (before <style>)")
            else:
                head_close = content.find('</head>')
                if head_close != -1:
                    content = content[:head_close] + '    ' + NAVBAR_CSS + '\n' + content[head_close:]
                    messages.append("Added navbar.css link (before </head>)")
                else:
                    messages.append("WARNING: Could not find location for CSS")
    else:
        messages.append("navbar.css already present")
    
    # Check if navbar JS already present
    if 'navbar.js' not in content:
        # Find position to insert JS - before </body> or after other scripts
        body_close = content.rfind('</body>')
        
        if body_close != -1:
            # Check for existing scripts before </body>
            script_pattern = r'(<script[^>]*></script>)\s*</body>'
            script_match = re.search(script_pattern, content, re.IGNORECASE)
            
            if script_match:
                # Insert after last script
                insert_pos = script_match.start(1) + len(script_match.group(1))
                content = content[:insert_pos] + '\n    ' + NAVBAR_JS + content[insert_pos:]
                messages.append("Added navbar.js script")
            else:
                # Insert before </body>
                content = content[:body_close] + '    ' + NAVBAR_JS + '\n' + content[body_close:]
                messages.append("Added navbar.js script (before </body>)")
        else:
            messages.append("WARNING: Could not find </body>")
    else:
        messages.append("navbar.js already present")
    
    # Write if modified
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, "; ".join(messages)
    else:
        return False, "; ".join(messages)

def main():
    """Process all HTML files in lesson-plans directory."""
    print("=" * 60)
    print("Adding Navbar References to Lesson Plans")
    print("=" * 60)
    
    if not LESSON_PLANS_DIR.exists():
        print(f"ERROR: Directory not found: {LESSON_PLANS_DIR}")
        return
    
    html_files = list(LESSON_PLANS_DIR.glob("*.html"))
    print(f"\nFound {len(html_files)} HTML files in {LESSON_PLANS_DIR}\n")
    
    modified_count = 0
    skipped_count = 0
    
    for filepath in sorted(html_files):
        modified, message = process_html_file(filepath)
        status = "✓ MODIFIED" if modified else "○ SKIPPED"
        if modified:
            modified_count += 1
        else:
            skipped_count += 1
        print(f"{status}: {filepath.name}")
        print(f"         {message}")
    
    print("\n" + "=" * 60)
    print(f"Summary: {modified_count} files modified, {skipped_count} files skipped")
    print("=" * 60)

if __name__ == "__main__":
    main()
