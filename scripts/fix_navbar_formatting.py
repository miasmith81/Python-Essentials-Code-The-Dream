#!/usr/bin/env python3
"""Fix formatting issues in lesson files after navbar insertion."""

import re
from pathlib import Path

lesson_dir = Path(__file__).parent.parent / 'lesson-plans'

for f in lesson_dir.glob('*.html'):
    content = f.read_text(encoding='utf-8')
    original = content
    
    # Fix the bad insertion pattern (CSS right before <style>)
    content = re.sub(
        r'<link rel="stylesheet" href="\.\./assets/css/navbar\.css"><style>',
        '<link rel="stylesheet" href="../assets/css/navbar.css">\n    <style>',
        content
    )
    
    # Fix double blank lines before navbar link
    content = re.sub(
        r'\n    \n    <link rel="stylesheet" href="\.\./assets/css/navbar\.css">',
        '\n    <link rel="stylesheet" href="../assets/css/navbar.css">',
        content
    )
    
    if content != original:
        f.write_text(content, encoding='utf-8')
        print(f'Fixed: {f.name}')

print('Done!')
