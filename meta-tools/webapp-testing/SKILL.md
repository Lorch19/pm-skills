---
name: webapp-testing
description: Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser screenshots, and viewing browser logs. TRIGGER when user needs to test a web app, capture screenshots, or automate browser interactions.
---

# Web Application Testing

To test local web applications, write native Python Playwright scripts.

## Decision Tree

```
User task → Is it static HTML?
    ├─ Yes → Read HTML file directly to identify selectors
    │         └─ Write Playwright script using selectors
    │
    └─ No (dynamic webapp) → Is the server already running?
        ├─ No → Start server first, then write Playwright script
        └─ Yes → Reconnaissance-then-action:
            1. Navigate and wait for networkidle
            2. Take screenshot or inspect DOM
            3. Identify selectors from rendered state
            4. Execute actions with discovered selectors
```

## Example: Basic Playwright Script

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('http://localhost:5173')
    page.wait_for_load_state('networkidle')  # CRITICAL: Wait for JS

    # Reconnaissance
    page.screenshot(path='/tmp/inspect.png', full_page=True)

    # Actions using discovered selectors
    page.locator('button:has-text("Submit")').click()
    page.wait_for_selector('.success-message')
    page.screenshot(path='/tmp/result.png')

    browser.close()
```

## Common Pitfall

- **Don't** inspect DOM before waiting for `networkidle` on dynamic apps
- **Do** wait for `page.wait_for_load_state('networkidle')` before inspection

## Best Practices

- Use `sync_playwright()` for synchronous scripts
- Always close the browser when done
- Use descriptive selectors: `text=`, `role=`, CSS selectors, or IDs
- Add waits: `page.wait_for_selector()` or `page.wait_for_timeout()`
- Take screenshots at key points for verification
