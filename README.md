# CGPA Calculator

> A clean, fast web tool that calculates your Cumulative Grade Point Average — built so Nigerian students can stop fighting with Excel sheets every semester.

![HTML](https://img.shields.io/badge/HTML-5-orange)
![CSS](https://img.shields.io/badge/CSS-3-blue)
![JS](https://img.shields.io/badge/JavaScript-vanilla-yellow)

---

## What it does

Input your courses, credit units, and grades → get your CGPA instantly. Works on both Nigerian 5-point and 4-point grading systems.

## Why I built it

Every semester, half my coursemates were still calculating their CGPA with a calculator and a piece of paper — or worse, trusting a broken spreadsheet they copied from a senior. I wanted a tool that was fast, worked on any phone, and didn't require signing up for anything.

## Features

- ➕ Add / remove courses dynamically
- 🎓 Supports 5-point and 4-point grading scales
- ⚡ Instant recalculation as you type
- 📱 Mobile-friendly — works on any screen
- 💾 No signup, no account, no tracking
- 🌙 Runs fully in the browser (no backend)

## How CGPA works (quick refresher)

```
CGPA = Σ (grade_point × credit_unit) / Σ (credit_unit)
```

For each course: multiply your grade point by that course's credit units. Sum it all up, divide by the total credit units. That's your CGPA.

The calculator does this in real time as you add courses.

## Tech stack

Pure **HTML**, **CSS**, and **flask** — no frameworks, no build step, no dependencies. The entire tool is a single page that works offline once loaded.

## Running it

Just open `index.html` in any browser:

```bash
git clone https://github.com/Iyimoga/CGPA-calculator.git
cd CGPA-calculator
# Open index.html in your browser
```

Or host it for free on GitHub Pages:
1. Settings → Pages → Source: `main` branch
2. Live at `https://iyimoga.github.io/CGPA-calculator/`

## What I learned

- You don't need React for everything — flask and streamlit handles most small tools just fine
- Good UX for a calculator = zero friction to start typing
- Real students will use something if it solves a real problem simply

## About

Built by **[Iyimoga Joseph Nana](https://github.com/Iyimoga)** — because students shouldn't have to do math just to figure out their math grade.
