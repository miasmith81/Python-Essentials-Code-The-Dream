# Index.html Setup Guide
## Python Essentials Curriculum Landing Page

---

## ✅ What Was Implemented

Your enhanced `index.html` now includes:

### 🎯 Core Features
- ✅ **Glassmorphic Navbar** - Sticky navigation with dropdowns for all pages
- ✅ **11 Week Cards** - All weeks with lesson + notebook integration
- ✅ **4 Supplemental Lessons** - Data Viz, APIs, Advanced Pandas, Extended SQL
- ✅ **Progress Tracking** - Visual progress bar with localStorage persistence
- ✅ **Jupyter Notebook Access** - 3 methods per week (Download, Colab, nbviewer)
- ✅ **Setup Instructions** - Tabbed guide for Colab, Local, and VS Code
- ✅ **Achievement System** - Milestone popups at 1, 3, 5, 8, and 11 weeks
- ✅ **Mobile Responsive** - Optimized for 375px+ devices
- ✅ **Retro-Terminal Design** - Matches existing lesson aesthetic

### 📊 Each Week Card Includes
1. **Lesson Link** - Opens interactive HTML lesson
2. **Session 1 Notebook** - Download, Colab, and View buttons
3. **Session 2 Group Notebook** - Download and Colab buttons
4. **Mark Complete Button** - Tracks progress with checkmarks

---

## 🔧 Customization Needed (IMPORTANT)

### 1. Update GitHub Repository Name in URLs

**Current URLs use:** `StrayDogSyn/Python-Essentials-Code-The-Dream`  
**You need to verify this is correct or update to your actual repo URL**

Search for `StrayDogSyn/Python-Essentials-Code-The-Dream` in `index.html` and replace if needed (appears 66 times):
- Colab links (22 times)
- nbviewer links (11 times)  
- Quick links (2 times)
- Footer links (2 times)

**Find & Replace Command:**
```bash
# PowerShell
(Get-Content index.html) -replace 'StrayDogSyn/Python-Essentials-Code-The-Dream', 'YOUR-USERNAME/YOUR-REPO' | Set-Content index.html
```

### 2. Verify Email Address

**Line ~868** in footer:
```html
<a href="mailto:contact@codethedream.org">Contact</a>
```

Update if you want a different contact email.

---

## 📂 File Structure Verification

Your repo already has the correct structure:

```
Python-Essentials-Code-The-Dream/
├── index.html ✅ (with navbar + notebook integration)
├── assets/ ✅
│   ├── css/
│   │   ├── curriculum.css
│   │   ├── branding.css
│   │   └── navbar.css       ✅ (glassmorphic navbar styles)
│   ├── js/
│   │   ├── navigation.js
│   │   ├── progress.js
│   │   ├── code-runner.js
│   │   ├── branding.js
│   │   └── navbar.js        ✅ (global navbar component)
│   └── brands/
├── lesson-plans/ ✅ (all 15 lessons with navbar)
│   ├── lesson_week1_intro_python.html
│   ├── ... (weeks 2-11)
│   └── supplemental_*.html   (4 supplemental lessons)
└── notebook-sessions/ ✅ (existing notebooks)
    ├── week1/ ... week11/
    └── (session notebooks)
```

All file paths in `index.html` match this structure - no changes needed!

---

## 🚀 Testing Locally

### Option 1: Python HTTP Server
```bash
cd C:\Users\EHunt\Repos\Python\CTD
python -m http.server 8000
```
Open browser to: `http://localhost:8000`

### Option 2: VS Code Live Server
1. Install "Live Server" extension in VS Code
2. Right-click `index.html`
3. Select "Open with Live Server"

### What to Test
- [ ] All "Start Lesson →" buttons open lessons
- [ ] Download buttons trigger notebook downloads
- [ ] Colab buttons open new tabs (will 404 until repo is public on GitHub)
- [ ] nbviewer buttons open new tabs (same as above)
- [ ] "Mark Complete" adds checkmark and updates progress bar
- [ ] Setup tabs switch between Colab/Local/VS Code
- [ ] Progress persists on page reload
- [ ] Achievement popup appears at milestones
- [ ] Mobile responsive (test at 375px, 768px, 1024px)

---

## 🌐 Publishing to GitHub Pages

### Step 1: Commit & Push
```bash
cd C:\Users\EHunt\Repos\Python\CTD
git add index.html INDEX_SETUP_GUIDE.md
git commit -m "feat: add comprehensive landing page with notebook integration"
git push origin main
```

### Step 2: Enable GitHub Pages
1. Go to `https://github.com/StrayDogSyn/Python-Essentials-Code-The-Dream/settings/pages`
2. **Source:** Deploy from a branch
3. **Branch:** main
4. **Folder:** / (root)
5. Click "Save"

### Step 3: Wait & Verify
- Wait 2-3 minutes for deployment
- Visit: `https://straydogsyn.github.io/CTD/`
- Test all Colab and nbviewer buttons (should work now)

---

## 🎨 Design Features

### Color Scheme (CSS Variables)
```css
--bg-dark: #0a0e27           /* Deep space blue background */
--bg-medium: #1a1f3a         /* Medium space blue */
--bg-card: #2a2f4a           /* Card backgrounds */
--accent-cyan: #00f0ff       /* Primary accent - cyan glow */
--accent-magenta: #ff00ff    /* Secondary accent - magenta */
--accent-green: #00ff41      /* Success/completion - matrix green */
--accent-yellow: #ffff00     /* Warnings/info */
```

### Typography
- **Body Text:** Segoe UI (readable, professional)
- **Headers/Code:** IBM Plex Mono, Space Mono (retro-terminal feel)
- **Loaded from Google Fonts** (offline fallback to monospace)

### Responsive Breakpoints
- **Desktop:** 1400px max container width
- **Tablet:** 768px (single column grid)
- **Mobile:** 428px (adjusted padding)
- **iPhone SE:** 375px (minimum supported)

---

## 🎯 How Students Use This Page

### Recommended Workflow
1. **First Visit:** Read setup instructions (#setup section)
2. **Choose Access Method:** Colab (easiest), Local (offline), or VS Code (pro)
3. **Week-by-Week:**
   - Click "Start Lesson →" to read theory
   - Download/Open Session 1 notebook for practice
   - Complete Session 2 notebook with group
   - Click "Mark Complete ✓" when done
4. **Track Progress:** Watch progress bar fill, unlock achievements

### Access Method Comparison

| Method | Pros | Best For | Requirements |
|--------|------|----------|--------------|
| **🚀 Colab** | No setup, free GPU, auto-saves | Beginners, mobile learners | Google account, internet |
| **💻 Local** | Offline, fast, full control | Serious learners | Python 3.8+, 500MB space |
| **🔧 VS Code** | Professional IDE, debugging | Developers | VS Code, extensions |

---

## 📊 Progress Tracking Details

### How It Works
```javascript
// Saves to browser localStorage
localStorage.setItem('python-essentials-progress', '[1,3,5]');

// Persists across:
✅ Page reloads
✅ Browser restarts
✅ Days/weeks later

// Does NOT persist:
❌ Clearing browser data
❌ Incognito/private mode
❌ Different browsers
❌ Different devices
```

### Achievement Milestones
- **Week 1:** "First Week Complete! You've started your Python journey!"
- **Week 3:** "3 Weeks Down! You're building momentum!"
- **Week 5:** "Halfway There! You're crushing it!"
- **Week 8:** "8 Weeks Complete! Almost at the finish line!"
- **Week 11:** "CURRICULUM COMPLETE! You're now a Python pro! 🏆"

---

## 🔧 Advanced Customization

### Change Course Title
**Line ~149:**
```html
<h1 class="logo">▸ Python Essentials</h1>
<!-- Change to: -->
<h1 class="logo">▸ Your Course Name</h1>
```

### Change Tagline
**Line ~150:**
```html
<p class="tagline">Interactive Curriculum for Code The Dream</p>
```

### Update Description
**Lines ~151-156:**
```html
<p class="header-description">
    Your custom description here...
</p>
```

### Modify Colors
**Lines ~12-22 (CSS :root variables):**
```css
:root {
    --accent-cyan: #00f0ff;  /* Change primary accent */
    --accent-green: #00ff41; /* Change success color */
    /* etc. */
}
```

### Add Custom Achievement
**Line ~939 in JavaScript:**
```javascript
} else if (count === 6) {
    message = '🌟 Your Custom Milestone!';
}
```

---

## 🐛 Troubleshooting

### Issue: Colab/nbviewer Links Show 404
**Cause:** Repository not public on GitHub  
**Fix:** Go to repo Settings → Change visibility to Public

### Issue: Download Buttons Don't Work Locally
**Cause:** Testing with `file://` protocol  
**Fix:** Use HTTP server (`python -m http.server 8000`)

### Issue: Progress Not Saving
**Cause:** Browser in private/incognito mode  
**Fix:** Use normal browsing mode

### Issue: Lesson Links 404
**Cause:** `lesson-plans/` folder path incorrect  
**Fix:** Verify folder structure matches expected paths

### Issue: Mobile Layout Broken
**Cause:** Browser too old  
**Fix:** Update browser or test in Chrome/Firefox/Safari

---

## 📱 Mobile Experience

### Optimizations Included
- ✅ Single column grid on mobile (<768px)
- ✅ Touch-friendly buttons (min 44px targets)
- ✅ Vertical notebook button layout on small screens
- ✅ Readable font sizes (16px minimum)
- ✅ No horizontal scroll (overflow-x: hidden)
- ✅ Collapsible setup tabs
- ✅ Fixed progress bar and indicator

### Test Devices
- iPhone SE (375px)
- iPhone 12/13/14 (390px)
- Android phones (360px-428px)
- iPad (768px+)
- Desktop (1024px+)

---

## 🎓 Student Instructions Template

Copy this to share with students:

---

**Welcome to Python Essentials! 🐍**

**Getting Started:**
1. Visit: `https://straydogsyn.github.io/CTD/`
2. Scroll to "Getting Started with Jupyter Notebooks"
3. Choose Colab (easiest), Local (offline), or VS Code (pro)
4. Start with Week 1!

**Each Week:**
- Read the lesson (theory + examples)
- Practice in Session 1 notebook (hands-on coding)
- Collaborate in Session 2 notebook (group activity)
- Mark complete and track your progress!

**Tips:**
- Work sequentially (Week 1 → Week 11)
- Spend 4-6 hours per week
- Complete notebooks for best learning
- Ask for help in community Slack/Discord!

**Goal:** Complete all 11 weeks, unlock all achievements! 🏆

---

## ✅ Final Checklist

Before sharing with students:

- [ ] GitHub username updated in all URLs (if needed)
- [ ] Email address updated in footer
- [ ] Tested locally with HTTP server
- [ ] All lesson links work
- [ ] All notebook downloads work
- [ ] Committed and pushed to GitHub
- [ ] GitHub Pages enabled
- [ ] Tested live site
- [ ] Colab buttons work on live site
- [ ] nbviewer buttons work on live site
- [ ] Progress tracking works
- [ ] Mobile responsive verified
- [ ] Shared URL with students!

---

## 📞 Support

If you encounter issues:

1. **Check file paths:** Ensure `lesson-plans/` and `notebook-sessions/` folders exist
2. **Verify repo structure:** Match the structure shown in this guide
3. **Test locally first:** Use HTTP server before deploying
4. **Check browser console:** Press F12, look for JavaScript errors
5. **Clear cache:** Hard refresh (Ctrl+Shift+R or Cmd+Shift+R)

---

## 🎉 You're Done!

Your Python Essentials curriculum now has:
- ✅ Professional landing page
- ✅ Integrated Jupyter notebooks (3 access methods)
- ✅ Progress tracking system
- ✅ Achievement milestones
- ✅ Mobile-responsive design
- ✅ Setup instructions for all skill levels
- ✅ Retro-terminal aesthetic

**Next Steps:**
1. Test everything locally
2. Update GitHub username if needed
3. Deploy to GitHub Pages
4. Share with students
5. Collect feedback and iterate!

**Questions?** Check the troubleshooting section or inspect the HTML/CSS/JS for detailed comments.

---

**Built with ❤️ for Code The Dream Fellows**
