# Python Essentials - Interactive Curriculum

> **Enhanced curriculum for the Returned Citizen community by StrayDog Syndications LLC**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Live Deployment](https://img.shields.io/badge/status-deployed-success.svg)](https://straydogsyn.github.io/Python-Essentials-Code-The-Dream/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

---

## Table of Contents

- [Overview](#overview)
- [Course Structure](#course-structure)
- [Interactive Lesson Plans](#interactive-lesson-plans)
- [Key Features](#key-features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Repository Structure](#repository-structure)
- [For Educators](#for-educators)
- [For Students](#for-students)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Overview

The **Python Essentials** curriculum is an enhanced, production-ready educational platform that takes students from Python fundamentals through advanced data engineering, web development, and machine learning concepts. This comprehensive program was enhanced and deployed by **[StrayDog Syndications LLC](https://www.straydog-syndications-llc.com/)** specifically for the **Returned Citizen community**.

### Mission
Our mission is to bridge the "Digital Cliff" for justice-impacted learners through accessible, career-aligned education that empowers the next generation of Python programmers.

### Like-Minded Affiliates

We're proud to collaborate with organizations that share our commitment to creating second-chance opportunities through technology:

- **[The Last Mile](https://thelastmile.org/)** - Technology training and education for incarcerated individuals
- **[Justice Through Code](https://centerforjustice.columbia.edu/justicethroughcode)** - Columbia University's coding bootcamp for formerly incarcerated individuals
- **[Code the Dream](https://codethedream.org/)** - Free software development training for people from diverse low-income backgrounds
- **[Reentry Campus Program](https://www.reentrycampusprogram.org/)** - Affordable pathways to post-secondary education for incarcerated individuals
- **[The Second Story Initiative](https://www.straydog-secondstory.org/)** - Transforming lives through education and opportunity

*Together, we're building a future where everyone has access to opportunity.*

### Key Principles

- **Progressive Learning**: Step-by-step skill building with clear learning objectives
- **Real-World Applications**: Practical examples from industry use cases
- **Interactive Experience**: Premium HTML lessons with progress tracking and modern design
- **Best Practices**: Pythonic code patterns and professional development workflows
- **Inclusive Design**: Accessible materials for learners from diverse backgrounds
- **Community Focus**: Built with care for those re-entering the workforce

---

## Course Structure

### **11-Week Intensive Program**

| Week | Topic | Focus Areas | Key Technologies |
|------|-------|-------------|------------------|
| **1** | Introduction to Python | Environment setup, variables, control flow, functions, debugging | Python, VS Code, Git |
| **2** | Data Structures & File Handling | Lists, dictionaries, tuples, sets, CSV/text files, modules | Python stdlib, `csv`, `pathlib` |
| **3** | Advanced Python Skills | OOP, decorators, comprehensions, closures | Classes, `@decorators` |
| **4** | Data Engineering Fundamentals | Pandas basics, Series, DataFrames, ETL patterns | `pandas`, `numpy` |
| **5** | Data Visualization | Matplotlib, Seaborn, interactive plots | `matplotlib`, `seaborn` |
| **6** | SQL & Databases | SQL syntax, queries, database integration | SQLite, `sqlite3` |
| **7** | APIs & Web Scraping | REST APIs, HTTP requests, HTML parsing | `requests`, `BeautifulSoup` |
| **8** | Advanced Pandas | Merging, groupby, pivot tables, time series | `pandas` (advanced) |
| **9** | Introduction to Machine Learning | Supervised learning, model evaluation, scikit-learn | `scikit-learn`, ML basics |
| **10** | Flask Web Development | Routes, templates, forms, sessions | `Flask`, Jinja2, web fundamentals |
| **11** | Deployment & DevOps | Environment variables, Docker, production servers | `Docker`, `gunicorn`, CI/CD |

---

## Interactive Lesson Plans

### **NEW: Premium HTML Lesson Experience**

Each week features a **beautifully designed, interactive HTML lesson** with:

- **Retro Gaming Aesthetic** - Dark theme with cyberpunk-inspired design  
- **Live Progress Tracking** - Visual XP bar and topic completion markers  
- **Syntax-Highlighted Code** - Color-coded examples with skill level badges  
- **Progressive Examples** - From bad practice → novice → intermediate → best practice  
- **Responsive Design** - Works seamlessly on desktop, tablet, and mobile  
- **Smart Navigation** - Sidebar with instant topic jumping  
- **Educational Boxes** - Tips, warnings, explanations, and best practices  

**Access Lessons**: Open any `.html` file in the `lesson-plans/` directory in your web browser.

```bash
# Example: Open Week 2 lesson
open lesson-plans/lesson_week2_data_structures.html  # macOS
start lesson-plans\lesson_week2_data_structures.html  # Windows
xdg-open lesson-plans/lesson_week2_data_structures.html  # Linux
```

---

## Key Features

### **For Students**

- **Self-Paced Learning**: Progress at your own speed with clear milestones
- **Hands-On Practice**: Jupyter notebooks with executable code cells
- **Real Code Examples**: Industry-standard patterns and anti-patterns
- **Immediate Feedback**: Interactive exercises with solution examples
- **Career-Ready Skills**: Technologies used in professional development

### **For Educators**

- **Instructor Guides**: Detailed teaching notes and answer keys
- **Flexible Curriculum**: Modular lessons adaptable to different schedules
- **Assessment Materials**: Weekly assignments with automated test suites
- **Group Activities**: Collaborative exercises designed for pair programming
- **Mentorship Resources**: Guidelines for 1:1 student support

### **Technical Highlights**

- **Version Controlled**: Full Git integration for collaborative development
- **Test-Driven Development**: PyTest-based assignment validation
- **Modern Tooling**: VS Code, virtual environments, pip package management
- **Cloud-Ready**: Docker containerization and deployment strategies
- **Industry Standards**: PEP 8 style guide, type hints, documentation

---

## Prerequisites

### **Required Skills**
- Basic computer literacy (file management, web browsing)
- Willingness to learn and problem-solve
- No prior programming experience needed!

### **Technical Requirements**
- **Operating System**: Windows 10+, macOS 10.14+, or Linux (Ubuntu 20.04+)
- **Python**: Version 3.8 or higher
- **Code Editor**: VS Code (recommended) or any text editor
- **Web Browser**: Modern browser (Chrome, Firefox, Safari, Edge)
- **Internet**: For package installation and resource access

---

## Getting Started

### **1. Clone the Repository**

```bash
git clone https://github.com/StrayDogSyn/Python-Essentials-Code-The-Dream.git
cd Python-Essentials-Code-The-Dream
```

### **2. Set Up Python Environment**

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r python-essentials-v2/requirements.txt
```

### **3. Verify Installation**

```bash
python --version  # Should be 3.8+
jupyter --version  # Verify Jupyter is installed
```

### **4. Launch Your First Lesson**

**Option A: Interactive HTML Lesson**
```bash
# Open in browser
open lesson-plans/lesson_week1_intro_python.html
```

**Option B: Jupyter Notebook**
```bash
# Start Jupyter
jupyter notebook

# Navigate to:
# python-essentials-v2/sessions/week1/session1_intro_to_python.ipynb
```

---

## 📁 Repository Structure

```
CTD/
├── lesson-plans/                    # Interactive HTML lessons (NEW!)
│   ├── lesson_week1_intro_python.html
│   ├── lesson_week2_data_structures.html  ← NEW: Complete with all sections
│   ├── lesson_week3_python_skills.html    ← RENAMED for consistency
│   ├── lesson_week4_data_engineering.html
│   ├── lesson_week5_data_visualization.html
│   ├── lesson_week6_sql_databases.html
│   ├── lesson_week7_apis_scraping.html
│   ├── lesson_week8_advanced_pandas.html
│   ├── lesson_week9_intro_ml.html
│   ├── lesson_week10_flask_web.html
│   └── lesson_week11_deployment.html
│
├── python-essentials-v2/            # Core curriculum materials
│   ├── lessons/                     # Markdown lesson content
│   │   ├── 01IntroToPython.md
│   │   ├── 02DataStructuresAndFileHandling.md
│   │   └── ...
│   │
│   ├── assignments/                 # Weekly homework with test suites
│   │   ├── 01IntroToPython.md
│   │   ├── 02DataStructuresAndFileHandling.md
│   │   └── ...
│   │
│   ├── sessions/                    # Jupyter notebooks for live sessions
│   │   ├── week1/
│   │   │   ├── session1_intro_to_python.ipynb
│   │   │   └── session2_intro_to_python_group.ipynb
│   │   └── ...
│   │
│   ├── instructor-materials/        # Teaching guides and solutions
│   │   ├── week1_instructor.md
│   │   └── ...
│   │
│   ├── instructor_guides/           # Detailed facilitation notes
│   │   ├── week1_instructor_guide.md
│   │   └── ...
│   │
│   └── mentor-guidebook/            # 1:1 mentorship resources
│       ├── assignment-solution-examples/
│       ├── group-lesson-guide/
│       └── README.md
│
├── .gitignore                       # Python project ignore rules
├── fix_notebooks.py                 # Notebook maintenance utility
├── validate_notebooks.py            # Notebook validation script
├── test.py                          # Testing utilities
├── assets/                          # Shared styles, scripts, and brand assets
│   ├── css/branding.css             # Branding styles (non-conflicting classes)
│   ├── js/branding.js               # Branding module (footer, favicon, A/B)
│   └── brands/                      # StrayDog logos and favicon
└── README.md                        # This file
```

---

## For Educators

### **Teaching Workflow**

1. **Pre-Session Prep**
   - Review `instructor_guides/weekN_instructor_guide.md`
   - Test code examples in session notebooks
   - Prepare supplementary materials or real-world examples

2. **Live Session**
   - Use `sessions/weekN/session1_*.ipynb` for demonstration
   - Facilitate group work with `session2_*_group.ipynb`
   - Reference HTML lesson for visual aids and progressive examples

3. **Assignment Review**
   - Students complete assignments from `assignments/`
   - Automated tests validate core functionality
   - Review code quality and provide personalized feedback

4. **Mentorship**
   - Use `mentor-guidebook/` resources for 1:1 support
   - Track student progress through assignment completion
   - Address individual learning gaps

### **Customization Tips**

- **Adjust Pacing**: Lessons are modular—extend or compress as needed
- **Add Examples**: Incorporate industry examples relevant to your students
- **Modify Assignments**: Adapt difficulty based on cohort skill level
- **Create Branches**: Use Git branches for cohort-specific modifications

---

## For Students

### **Weekly Learning Cycle**

**Monday-Tuesday: Learn**
- Read lesson materials (`lessons/` directory)
- Complete interactive HTML lesson (`lesson-plans/`)
- Practice with Jupyter notebooks (`sessions/`)

**Wednesday-Thursday: Practice**
- Work through weekly assignment (`assignments/`)
- Run automated tests: `pytest -v`
- Debug and refine your code

**Friday: Collaborate**
- Attend group session
- Pair program with peers
- Ask questions and share insights

**🔄 Weekend: Review**
- Revisit challenging concepts
- Explore additional resources
- Prepare for next week

### **Getting Help**

1. **Self-Service**
   - Review HTML lesson's "Explanation Boxes" and "Common Pitfalls"
   - Check `mentor-guidebook/assignment-solution-examples/`
   - Search error messages in lesson cheat sheets

2. **Peer Support**
   - Slack discussion channels
   - Study groups and pair programming
   - Code review exchanges

3. **Mentorship**
   - Schedule 1:1 mentor sessions
   - Office hours with instructors
   - Detailed code feedback on assignments

---

## Contributing

We welcome contributions from educators, students, and the developer community!

### **Quick Start for Contributors**

1. **Read the Guidelines**: Check [CONTRIBUTING.md](CONTRIBUTING.md) for detailed instructions
2. **Fork the Repository**: Create your own copy to work on
3. **Make Your Changes**: Follow our style guides and best practices
4. **Submit a Pull Request**: We'll review and provide feedback

See our comprehensive [Contributing Guide](CONTRIBUTING.md) for:
- Code of conduct
- Development workflow
- Style guides (Python, Markdown, HTML)
- Review process
- Recognition and community

### **How to Contribute**

1. **Fork the Repository**
   ```bash
   # Click "Fork" on GitHub, then clone your fork
   git clone https://github.com/YOUR_USERNAME/CTD.git
   ```

2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/improved-week5-examples
   ```

3. **Make Your Changes**
   - Add new examples or exercises
   - Fix typos or clarify explanations
   - Update outdated package versions
   - Improve HTML lesson design

4. **Test Your Changes**
   ```bash
   # Validate notebooks
   python validate_notebooks.py
   
   # Test example code
   python -m pytest
   ```

5. **Submit a Pull Request**
   - Write clear commit messages
   - Describe your changes in PR description
   - Link related issues

### **Contribution Guidelines**

- **Code Style**: Follow PEP 8 for Python code
- **Documentation**: Update README/guides when changing structure
- **Examples**: Ensure all code examples are tested and executable
- **Accessibility**: Maintain inclusive language and design
- **Licenses**: Only contribute content you have rights to share

### **Areas for Contribution**

- 🐛 Bug fixes in code examples
- 📝 Additional practice problems
- 🌐 Translations to other languages
- 🎨 UI/UX improvements for HTML lessons
- Data visualization examples
- 🧪 Additional test cases
- 📚 Supplementary learning resources

---

## Live Deployment

**Access the interactive curriculum online:**

**Live Site:** [https://straydogsyn.github.io/Python-Essentials-Code-The-Dream/](https://straydogsyn.github.io/Python-Essentials-Code-The-Dream/)

The complete Python Essentials curriculum is live on GitHub Pages! Access all 11 weeks of interactive lessons, progress tracking, and hands-on exercises from any device, anywhere. No installation required—just click and start learning!

---

## 🔄 Continuous Integration

This repository uses **GitHub Actions** for automated quality assurance:

- **Python Tests**: Automated testing across Python 3.8-3.11
- 📝 **Code Linting**: Style validation with flake8 and black
- 📓 **Notebook Validation**: Jupyter notebook integrity checks
- 🚀 **Auto-Deployment**: GitHub Pages updates on every push

View build status and test results in the [Actions tab](https://github.com/StrayDogSyn/CTD/actions).

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

**What this means:**
- Free to use for educational purposes
- Modify and adapt for your classroom
- Share with students and colleagues
- Attribution appreciated but not required
- No warranty provided

---

## 🙏 Acknowledgments

---

## Branding Module

**Files**: `assets/css/branding.css`, `assets/js/branding.js`

- Footer credits: “Created with care by StrayDog” (link to StrayDog site)
- Corner logos with alt text from `assets/brands/`
- GitHub links: `https://github.com/StrayDogSyn`, `https://github.com/miasmith81`
- Favicon injection: `assets/brands/favicon-straydog.png`
- Discreet watermark on select pages (`index.html`, `community-partners.html`)
- Supported badge on homepage

**Usage**: include CSS + JS on pages. JS automatically injects favicon and branded footer without altering existing layouts.

### A/B Testing
- Variant assignment: random A/B or via `?variant=A|B`
- Metrics (localStorage): clicks on start lesson, notebook, complete buttons; max scroll depth
- Keys: `sd-ab-variant`, `sd-ab-metrics`
- Variant B sets `data-branding="minimal"` on `<html>` for future conditional styling

### Community Partners Page
- `community-partners.html` highlights Returned Citizen community and Code the Dream students
- Uses existing lesson styles and the watermark effect

### Accessibility & Performance
- Alt text on all logos/icons
- Responsive across device sizes
- Minimal footprint: small PNGs, lightweight CSS/JS

### **Enhanced and Deployed By**

**[StrayDog Syndications LLC](https://www.straydog-syndications-llc.com/)**
- [Eric 'Hunter' Petross](https://github.com/StrayDogSyn) - Lead Developer & Curriculum Enhancement
- [Mia 'Mausi' Smith-Petross](https://github.com/miasmith81) - Co-Developer & Platform Design

This enhanced curriculum features:
- Premium interactive HTML lesson platform with modern design
- Integrated progress tracking and achievement system
- Responsive, accessible interface optimized for all learners
- Professional branding and deployment architecture
- Comprehensive automation scripts for maintenance

### **For the Community**

Specially enhanced for the **Returned Citizen community** and **[Code the Dream](https://codethedream.org)** students. Code the Dream is a nonprofit organization providing free, high-quality technical training to people from diverse backgrounds who aspire to become professional programmers.

### **Contributors**
- **Original Curriculum**: Code the Dream educators and lesson authors
- **Enhancement Team**: StrayDog Syndications LLC
- **Technical Reviewers**: Industry professionals providing feedback
## Contact & Support

- **Repository**: [Python-Essentials-Code-The-Dream](https://github.com/StrayDogSyn/Python-Essentials-Code-The-Dream)
- **Issues**: [GitHub Issues](https://github.com/StrayDogSyn/Python-Essentials-Code-The-Dream/issues)
- **Discussions**: [GitHub Discussions](https://github.com/StrayDogSyn/Python-Essentials-Code-The-Dream/discussions)
- **StrayDog Syndications LLC**: [www.straydog-syndications-llc.com](https://www.straydog-syndications-llc.com/)
- **The Second Story Initiative**: [www.straydog-secondstory.org](https://www.straydog-secondstory.org/)

---

<div align="center">

**Enhanced curriculum for the Returned Citizen community by StrayDog Syndications LLC**

**Bridging the Digital Cliff through accessible, career-aligned education**

*In collaboration with like-minded affiliates*

[⬆ Back to Top](#-python-essentials---interactive-curriculum)

</div>
