# 🐍 30 Days of Python Projects

> One real-world Python project every day for 30 days. Each project is built on the topic of that day, following the [Asabeneh 30 Days of Python](https://github.com/Asabeneh/30-Days-Of-Python) curriculum — and the complexity increases as the days go by.

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Progress](https://img.shields.io/badge/Progress-1%2F30-4CAF50)
![Status](https://img.shields.io/badge/Status-%F0%9F%9A%80%20In%20Progress-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

## Table of contents
- [Why this repo exists](#why-this-repo-exists)
- [Who this is for](#who-this-is-for)
- [How to use this repo (the learning method)](#how-to-use-this-repo-the-learning-method)
- [Getting started](#getting-started)
- [The 30-day roadmap](#the-30-day-roadmap)
- [Repo structure](#repo-structure)
- [The integrity rule](#the-integrity-rule)
- [After Day 30](#after-day-30)
- [Contributing](#contributing)
- [License](#license)

## Why this repo exists

Instead of 30 days of notes and exercises, this is **30 days of shipped projects** — each one a small real-world tool you could actually use. The arc goes from terminal scripts → data processing → web scraping → web apps → databases → APIs, which is exactly the skill set backend and automation roles look for.

## Who this is for

- Anyone working through **Asabeneh's 30 Days of Python** who wants to *apply* each topic, not just read it.
- Self-taught beginners who learn best by **building**.
- Anyone who wants a public record of consistent work for internships and jobs.

## 🎓 How to use this repo (the learning method)

Every day folder follows the same 3-file pattern:

1. **`README.md`** — the spec: what to build, plus an example of the expected output.
2. **`main.py`** — a *starter*: some code given as an example, the rest marked with `TODO`s for you.
3. **`solution.py`** — the reference solution. **Only open it after you've tried `main.py` yourself** (or been stuck ~30 minutes).

The daily loop: **write it → run it → break it → fix it → only then compare with the solution.** Comparing your attempt against a good one is where the real learning happens — copying solutions without trying first teaches almost nothing.

> This repo is being **beta-tested by its first learner**. If a day's starter is confusing, too hard, or too easy, that's valuable feedback — open an issue so the next person has a smoother ride.

## 🚀 Getting started

Requirements: **Python 3.10+** (check with `python3 --version`).

```bash
# 1. Clone the repo
git clone https://github.com/buabeeyereba/30-days-of-python-projects.git
cd 30-days-of-python-projects

# 2. Run any project, e.g. Day 1
python3 day-01-developer-profile/main.py
```

Each project's folder has its own README with run instructions.

## 📅 The 30-Day Roadmap

| # | Asabeneh Topic | Project | Difficulty |
|---|----------------|---------|------------|
| 1 | Introduction | Developer Profile Card | ⭐ |
| 2 | Variables & Builtin Functions | Job Offer Comparator | ⭐ |
| 3 | Operators | Loan Eligibility & Repayment Estimator | ⭐⭐ |
| 4 | Strings | Password Generator & Strength Analyzer | ⭐⭐ |
| 5 | Lists | Task Manager CLI (v1) | ⭐⭐ |
| 6 | Tuples | Trip Distance Calculator | ⭐⭐ |
| 7 | Sets | Event RSVP & Skill-Match Finder | ⭐⭐ |
| 8 | Dictionaries | Contact Book CLI | ⭐⭐⭐ |
| 9 | Conditionals | Net Pay Estimator (PAYE) | ⭐⭐⭐ |
| 10 | Loops | Weekly Sales Reporter | ⭐⭐⭐ |
| 11 | Functions | Bill Splitter & Tip Calculator | ⭐⭐⭐ |
| 12 | Modules | Dev Environment Checker v2 (Modules) | ⭐⭐⭐ |
| 13 | List Comprehension | Data Cleaner & Extractor | ⭐⭐⭐ |
| 14 | Higher Order Functions | Employee Salary Analyzer | ⭐⭐⭐⭐ |
| 15 | Python Type Errors | Bug Hunt: Type Error Fixer | ⭐⭐⭐ |
| 16 | Python Date Time | Age Calculator & Deadline Tracker | ⭐⭐⭐ |
| 17 | Exception Handling | Bank Transaction Simulator | ⭐⭐⭐⭐ |
| 18 | Regular Expressions | Log Parser & Contact Extractor | ⭐⭐⭐⭐ |
| 19 | File Handling | Note Taking App (Persistent) | ⭐⭐⭐⭐ |
| 20 | Package Manager | Expense Tracker Pro (Rich CLI) | ⭐⭐⭐⭐ |
| 21 | Classes & Objects | Bank Account System (OOP) | ⭐⭐⭐⭐ |
| 22 | Web Scraping | Job Listings Scraper | ⭐⭐⭐⭐ |
| 23 | Virtual Environment | Package Your Own CLI | ⭐⭐⭐⭐ |
| 24 | Statistics | Exam Score Analyzer | ⭐⭐⭐⭐ |
| 25 | Pandas | Sales Dataset Analysis | ⭐⭐⭐⭐ |
| 26 | Python Web | First Web App: Task Manager (Flask) | ⭐⭐⭐⭐⭐ |
| 27 | Python + MongoDB | Task Manager + MongoDB | ⭐⭐⭐⭐⭐ |
| 28 | API | Weather & GitHub API Consumer | ⭐⭐⭐⭐ |
| 29 | Building API | Task Manager REST API (FastAPI) | ⭐⭐⭐⭐⭐ |
| 30 | Conclusions | **Capstone:** Job Application Tracker | ⭐⭐⭐⭐⭐ |

Full details (what each project does, what you learn, sample inputs): see **[ROADMAP.md](ROADMAP.md)**.

## 📁 Repo structure

```
30-days-of-python-projects/
├── README.md                    # this file - start here
├── ROADMAP.md                   # the full 30-day plan (topics + projects)
├── LICENSE                      # MIT - free to use, learn, share
├── .gitignore
├── scripts/
│   ├── new_day.sh               # scaffold a day folder
│   └── push_day.sh              # commit + push today's work
└── day-XX-project-name/         # one folder per day, e.g. day-01-developer-profile
    ├── README.md                # the spec + example output
    ├── main.py                  # starter - your work goes here
    └── solution.py              # reference - only open after you've tried
```

## 🧭 The integrity rule

This is a public learning resource, so it must be **honest**:

- Every project's official deliverable uses **only the concepts officially taught up to that day**.
- When a real project can't avoid a future concept (e.g. `if/else` before Day 9), it is clearly marked as a **preview** in the code, e.g. `# [PREVIEW - Day 9 topic]`, with a one-line explanation.
- If a project needs more than a small preview, the **project moves to the day where the concept is officially taught** — that's why the Environment Checker lives at Day 12 (Modules), not Day 1.

A beginner should never feel lost on any day. That's the promise of this repo.

## 🎯 After Day 30

- Refactor your 3 best projects: add tests (`pytest`), type hints, and a proper `pyproject.toml`.
- Pin this repo on your GitHub profile — it becomes your "proof of work" for internship applications.
- Contribute to open source: pick repos with `good first issue` labels (ideally libraries you used here).
- Keep building: pick 1 project and turn it into a deployed product.

## 🤝 Contributing

This repo is a learning resource first. Contributions that make it more helpful for beginners are welcome:

- **Found a confusing starter or spec?** Open an issue with the day number.
- **Typo or broken example output?** Small PRs are always welcome.
- **Suggest a better project for a day's topic?** Open an issue first so we can discuss it.

## 📄 License

[MIT](LICENSE) — use it, learn from it, share it. If it helps you, a ⭐ and a shout-out are all we ask.

---

Made with ❤️ by **Buabee Yereba** as part of the 30 Days of Python Projects challenge.
Questions or feedback? Open an [issue](https://github.com/buabeeyereba/30-days-of-python-projects/issues) — or reach me at buabeeyereba@gmail.com.
