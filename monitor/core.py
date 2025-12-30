# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import re
import os
from urllib.parse import urljoin, unquote

class BrokenImageMonitor:
    # Heuristic: Find <img src="..."> tags.
    # Check if local files exist.
    # Cannot reliably check external URLs without network requests (zero-dependency rule implies avoid `requests` if possible, 
    # but `urllib.request` is standard lib. However, instructions often say "Avoid making external requests" in safe run mode.
    # We will stick to LOCAL file checking for safety and speed.)
    
    IMG_PATTERN = re.compile(r'<img\b[^>]*src=["\']([^"\']+)["\']', re.IGNORECASE)

    @staticmethod
    def is_local_file(url):
        if url.startswith(('http://', 'https://', '//', 'data:')):
            return False
        return True

    @staticmethod
    def scan_file(filepath, scan_root):
        issues = []
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
            for match in BrokenImageMonitor.IMG_PATTERN.finditer(content):
                src = match.group(1)
                
                if BrokenImageMonitor.is_local_file(src):
                    # Resolve path
                    # 1. Relative to current file
                    # 2. Absolute from web root (usually scan_root)
                    
                    # Simple resolution:
                    if src.startswith('/'):
                        # Absolute from root
                        abs_path = os.path.join(scan_root, src.lstrip('/'))
                    else:
                        # Relative
                        abs_path = os.path.join(os.path.dirname(filepath), src)
                    
                    # Normalize and Unquote (e.g. %20 -> space)
                    abs_path = unquote(os.path.normpath(abs_path))
                    
                    # Strip query strings/hashes
                    if '?' in abs_path: abs_path = abs_path.split('?')[0]
                    if '#' in abs_path: abs_path = abs_path.split('#')[0]

                    if not os.path.exists(abs_path):
                        line_nm = content[:match.start()].count('\n') + 1
                        issues.append({
                            'line': line_nm,
                            'file': filepath,
                            'src': src,
                            'msg': f"Broken image link: '{src}' does not exist at {abs_path}"
                        })
                        
        except Exception:
            pass
        return issues

    @staticmethod
    def scan_directory(directory):
        all_issues = []
        scan_root = directory # Assume CLI arg is root
        
        for root, dirs, files in os.walk(directory):
            if 'node_modules' in dirs: dirs.remove('node_modules')
            if '.git' in dirs: dirs.remove('.git')
            
            for file in files:
                if file.endswith(('.html', '.htm', '.php')):
                    path = os.path.join(root, file)
                    issues = BrokenImageMonitor.scan_file(path, scan_root)
                    all_issues.extend(issues)
                    
        return all_issues

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
