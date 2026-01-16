# Index.html Quick Customization Reference
## Copy-Paste Commands for Fast Setup

---

## ⚡ FASTEST SETUP (2 Minutes)

### 1. Update GitHub Username (If Needed)

**Current:** `StrayDogSyn/Python-Essentials-Code-The-Dream`  
**Appears:** 66 times (Colab links, nbviewer links, footer)

**PowerShell Command:**
```powershell
cd C:\Users\EHunt\Repos\Projects\Python-Essentials-Code-The-Dream
(Get-Content index.html) -replace 'StrayDogSyn/Python-Essentials-Code-The-Dream', 'YOUR-USERNAME/YOUR-REPO' | Set-Content index.html
```

**Verify it's correct first!** Your repo URL structure should be:
- GitHub: `https://github.com/StrayDogSyn/Python-Essentials-Code-The-Dream`
- Colab: `https://colab.research.google.com/github/StrayDogSyn/Python-Essentials-Code-The-Dream/blob/main/...`

---

### 2. Update Email (Optional)

**Line ~868:**
```html
<a href="mailto:contact@codethedream.org">Contact</a>
```

---

### 3. Test Locally

```powershell
cd C:\Users\EHunt\Repos\Projects\Python-Essentials-Code-The-Dream
python -m http.server 8000
```

Open: `http://localhost:8000`

---

### 4. Deploy to GitHub Pages

```bash
git add index.html INDEX_SETUP_GUIDE.md INDEX_QUICK_REFERENCE.md
git commit -m "feat: add comprehensive landing page with notebook integration"
git push origin main
```

**Enable Pages:**
1. Go to: `https://github.com/StrayDogSyn/Python-Essentials-Code-The-Dream/settings/pages`
2. Source: **Deploy from a branch**
3. Branch: **main**, Folder: **/ (root)**
4. Click **Save**

**Live URL:** `https://straydogsyn.github.io/CTD/`

---

## 🎨 Common Customizations

### Change Course Title (Line ~149)
```html
<!-- Before -->
<h1 class="logo">▸ Python Essentials</h1>

<!-- After -->
<h1 class="logo">▸ Your Course Name</h1>
```

### Change Tagline (Line ~150)
```html
<!-- Before -->
<p class="tagline">Interactive Curriculum for Code The Dream</p>

<!-- After -->
<p class="tagline">Your Custom Tagline</p>
```

### Change Colors (Lines ~12-22)
```css
:root {
    --accent-cyan: #00f0ff;    /* Primary buttons, links */
    --accent-magenta: #ff00ff; /* Secondary accent */
    --accent-green: #00ff41;   /* Success, completed */
    --accent-yellow: #ffff00;  /* Info banners */
}
```

---

## 🧪 Testing Checklist

### Local Testing (Before Deploy)
- [ ] Start HTTP server: `python -m http.server 8000`
- [ ] Open `http://localhost:8000`
- [ ] Click "Start Lesson →" for Week 1 (should open lesson)
- [ ] Click "⬇️ Session 1" (should download .ipynb)
- [ ] Click "🚀 Colab" (opens new tab, may 404 until deployed)
- [ ] Click "👁️ View" (opens new tab, may 404 until deployed)
- [ ] Click "Mark Complete ✓" (adds checkmark, updates progress)
- [ ] Reload page (progress persists)
- [ ] Test mobile (F12, toggle device toolbar, 375px)

### Live Testing (After Deploy)
- [ ] Visit `https://straydogsyn.github.io/CTD/`
- [ ] All Colab buttons work (open in Colab)
- [ ] All nbviewer buttons work (render notebooks)
- [ ] All lesson links work
- [ ] Progress tracking works
- [ ] Mobile responsive
- [ ] Achievement popups appear

---

## 🐛 Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| Colab links 404 | Repo not public → Settings → Change visibility |
| Downloads don't work locally | Use HTTP server, not `file://` |
| Progress not saving | Don't use incognito/private mode |
| Lesson links 404 | Verify `lesson-plans/` folder exists |
| Notebook buttons 404 | Verify `notebook-sessions/` folders exist |
| Mobile layout broken | Update browser, test in Chrome |

---

## 📊 What Students See

### Each Week Card Includes:
1. **Week Number & Title** - Large, prominent
2. **Topics List** - Key concepts covered
3. **"Start Lesson →"** - Opens HTML lesson
4. **Session 1 Notebook** - Download, Colab, View buttons
5. **Session 2 Group Notebook** - Download, Colab buttons
6. **"Mark Complete ✓"** - Tracks progress

### Progress Bar (Top Right):
- Shows: "3/11 Complete (27%)"
- Visual bar fills as weeks completed
- Persists across page reloads

### Achievement Popups:
- Week 1: "First Week Complete! 🎉"
- Week 3: "3 Weeks Down! 🔥"
- Week 5: "Halfway There! ⭐"
- Week 8: "8 Weeks Complete! 💪"
- Week 11: "CURRICULUM COMPLETE! 🏆"

---

## 📱 Mobile-Responsive Features

- ✅ Single column layout on phones (<768px)
- ✅ Touch-friendly buttons (44px+ targets)
- ✅ Notebook buttons stack vertically on mobile
- ✅ Readable fonts (16px minimum)
- ✅ No horizontal scroll
- ✅ Fixed progress bar

---

## 🎯 File Paths (Already Correct!)

Your repo structure matches the HTML paths:

```
CTD/
├── index.html ✅
├── lesson-plans/
│   ├── lesson_week1_intro_python.html ✅
│   ├── lesson_week2_data_structures.html ✅
│   └── ... (weeks 3-11) ✅
└── notebook-sessions/
    ├── week1/
    │   ├── session1_intro_to_python.ipynb ✅
    │   └── session2_intro_to_python_group.ipynb ✅
    └── ... (weeks 2-11) ✅
```

**No file path changes needed!**

---

## 🚀 Deployment Commands Summary

```bash
# 1. Navigate to repo
cd C:\Users\EHunt\Repos\Python\CTD

# 2. (Optional) Update GitHub username
(Get-Content index.html) -replace 'StrayDogSyn/Python-Essentials-Code-The-Dream', 'YOUR/REPO' | Set-Content index.html

# 3. Test locally
python -m http.server 8000
# Visit http://localhost:8000

# 4. Commit and push
git add .
git commit -m "feat: add comprehensive landing page with notebook integration"
git push origin main

# 5. Enable GitHub Pages in repo settings
# 6. Wait 2-3 minutes
# 7. Visit https://straydogsyn.github.io/CTD/
```

---

## ✅ Done!

**You now have:**
- ✅ Professional landing page
- ✅ Jupyter notebook integration (3 access methods per week)
- ✅ Progress tracking with achievements
- ✅ Mobile-responsive design
- ✅ Setup instructions (Colab/Local/VS Code)
- ✅ Retro-terminal aesthetic

**Next:** Test locally → Deploy to GitHub Pages → Share with students! 🎉

---

**Questions?** See `INDEX_SETUP_GUIDE.md` for detailed documentation.
