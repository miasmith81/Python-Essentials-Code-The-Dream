# Shared Assets

Centralized styling, scripts, and brand assets for the Python Essentials curriculum.

---

## Styles (`css/`)

| File | Description |
|------|-------------|
| `curriculum.css` | Base theme, badges, progress bar, sections, code example blocks |
| `branding.css` | StrayDog branding styles (footer, watermarks, logos) |
| `navbar.css` | **NEW** - Glassmorphic sticky navbar with responsive dropdowns |

---

## Scripts (`js/`)

| File | Description |
|------|-------------|
| `navigation.js` | Section navigation activation and smooth scrolling |
| `progress.js` | Reading progress indicator (XP bar) |
| `code-runner.js` | Copy code and guide to run in notebooks |
| `branding.js` | Branding module (footer injection, favicon, A/B testing) |
| `navbar.js` | **NEW** - Self-initializing global navbar component |

---

## Brand Assets (`brands/`)

- `favicon-straydog.png` - Site favicon
- Logo files for StrayDog Syndications branding

---

## Navbar Component

The global navbar provides consistent navigation across all pages:

### Features
- **Glassmorphic Design**: Frosted glass effect with `backdrop-filter: blur(20px)`
- **Sticky Positioning**: Fixed at top, shrinks on scroll
- **Dropdown Menus**: Lessons (11 weeks + supplemental), Resources, Notebooks
- **Mobile Responsive**: Hamburger menu with touch-friendly dropdowns
- **Non-Invasive**: Self-initializes without modifying existing page structure
- **Path-Aware**: Auto-detects subdirectory depth for correct URL resolution

### Usage

Add to `<head>`:
```html
<link rel="stylesheet" href="assets/css/navbar.css">
```

Add before `</body>`:
```html
<script src="assets/js/navbar.js" defer></script>
```

**From subdirectories** (e.g., `lesson-plans/`):
```html
<link rel="stylesheet" href="../assets/css/navbar.css">
<script src="../assets/js/navbar.js" defer></script>
```

---

## Best Practices

- Link CSS and JS from lessons to unify design and behavior
- Keep page weight under 1MB and mobile-first
- Use CSS variables from `curriculum.css` for consistent theming
- Test on multiple viewport sizes before deployment

