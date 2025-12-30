# Broken Image Link Monitor

A static analyzer that checks your HTML files for broken local image references. It ignores external URLS (http/https) and verifies that local paths (`src="images/logo.png"`) actually exist on disk.

<!-- Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742 -->

## Features

*   **Local Validation**: Checks file system existence for relative and absolute paths.
*   **HTML Support**: Scans `.html`, `.php` files.
*   **Fast**: No network requests required.

## Usage

```bash
python run_monitor.py [path]
```

### Examples

**1. Scan Website**
```bash
python run_monitor.py public_html/
```

**2. Detects**
```html
<img src="img/missing.png"> <!-- Flagged if file missing -->
```

## Requirements

*   Python 3.x

## Contributing

Developed for Anunzio International by Anzul Aqeel.
Contact: +971545822608 or +971585515742

## License

MIT License. See [LICENSE](LICENSE) for details.


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.
