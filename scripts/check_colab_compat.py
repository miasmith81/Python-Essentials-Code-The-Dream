#!/usr/bin/env python3
"""
Check all notebooks for Colab compatibility issues.
This script identifies cells that might fail in Google Colab.
"""

import json
from pathlib import Path

def check_notebook(notebook_path):
    """Check a notebook for potential Colab issues."""
    issues = []
    
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    for i, cell in enumerate(nb['cells']):
        if cell.get('cell_type') != 'code':
            continue
            
        source = cell.get('source', [])
        if isinstance(source, list):
            code = ''.join(source)
        else:
            code = source
        
        # Check for %run (needs local files)
        if '%run ' in code and 'google.colab' not in code:
            issues.append((i + 1, "%run command (needs local file)", code[:50]))
        
        # Check for %load (needs local files)
        if '%load ' in code:
            issues.append((i + 1, "%load command (needs local file)", code[:50]))
        
        # Check for reading files without creating them first
        # (This is harder to detect automatically)
        
    return issues

def main():
    base_dir = Path("notebook-sessions")
    
    print("=" * 70)
    print("COLAB COMPATIBILITY CHECK")
    print("=" * 70)
    
    total_issues = 0
    
    for nb_path in sorted(base_dir.rglob("*.ipynb")):
        issues = check_notebook(nb_path)
        
        if issues:
            print(f"\n⚠️  {nb_path.relative_to(base_dir)}")
            for cell_num, issue, preview in issues:
                total_issues += 1
                print(f"   Cell {cell_num}: {issue}")
                print(f"   Preview: {preview}...")
        else:
            print(f"✅ {nb_path.relative_to(base_dir)}")
    
    print("\n" + "=" * 70)
    if total_issues:
        print(f"⚠️  Found {total_issues} potential Colab issue(s)")
    else:
        print("✅ All notebooks appear Colab-compatible!")
    print("=" * 70)

if __name__ == "__main__":
    main()
