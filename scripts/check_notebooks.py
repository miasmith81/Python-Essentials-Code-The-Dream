#!/usr/bin/env python3
"""Check all notebooks for syntax errors in code cells."""

import json
import ast
from pathlib import Path

def check_notebook(path):
    """Check a notebook for Python syntax errors."""
    errors = []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        for i, cell in enumerate(nb.get('cells', []), 1):
            if cell.get('cell_type') == 'code':
                source = cell.get('source', [])
                if isinstance(source, list):
                    code = ''.join(source)
                else:
                    code = source
                
                # Skip cells with magic commands or shell commands (they're IPython-specific)
                lines = code.split('\n')
                # Filter out magic commands and shell commands
                python_lines = [line for line in lines 
                               if not line.strip().startswith('%') 
                               and not line.strip().startswith('!')]
                code = '\n'.join(python_lines)
                
                # Skip empty cells after filtering
                if not code.strip():
                    continue
                    
                try:
                    ast.parse(code)
                except SyntaxError as e:
                    errors.append((i, str(e), code[:100]))
                    
    except Exception as e:
        errors.append((0, f"File error: {e}", ""))
    
    return errors

def main():
    base_dir = Path("notebook-sessions")
    
    print("=" * 70)
    print("NOTEBOOK SYNTAX CHECK")
    print("=" * 70)
    
    total_errors = 0
    
    for nb_path in sorted(base_dir.rglob("*.ipynb")):
        errors = check_notebook(nb_path)
        
        if errors:
            print(f"\n❌ {nb_path.relative_to(base_dir)}")
            for cell_num, error, snippet in errors:
                total_errors += 1
                print(f"   Cell {cell_num}: {error}")
                if snippet:
                    print(f"   Preview: {snippet[:60]}...")
        else:
            print(f"✅ {nb_path.relative_to(base_dir)}")
    
    print("\n" + "=" * 70)
    if total_errors:
        print(f"❌ Found {total_errors} syntax error(s)")
    else:
        print("✅ All notebooks passed syntax check!")
    print("=" * 70)

if __name__ == "__main__":
    main()
