#!/usr/bin/env python3
"""Fix notebook cells where source lines are missing newlines."""

import json
from pathlib import Path

def fix_notebook(path):
    """Fix a notebook's cell source formatting."""
    modified = False
    
    with open(path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    for cell in nb.get('cells', []):
        source = cell.get('source', [])
        
        if isinstance(source, list) and len(source) > 1:
            # Check if lines are missing newlines
            fixed_source = []
            for i, line in enumerate(source):
                if i < len(source) - 1 and not line.endswith('\n'):
                    fixed_source.append(line + '\n')
                    modified = True
                else:
                    fixed_source.append(line)
            cell['source'] = fixed_source
    
    if modified:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
        return True
    return False

def main():
    base_dir = Path("notebook-sessions")
    
    print("=" * 60)
    print("FIXING NOTEBOOK SOURCE FORMATTING")
    print("=" * 60)
    
    fixed_count = 0
    
    for nb_path in sorted(base_dir.rglob("*.ipynb")):
        if fix_notebook(nb_path):
            print(f"✅ Fixed: {nb_path.name}")
            fixed_count += 1
        else:
            print(f"   OK: {nb_path.name}")
    
    print("=" * 60)
    print(f"Fixed {fixed_count} notebook(s)")
    print("=" * 60)

if __name__ == "__main__":
    main()
