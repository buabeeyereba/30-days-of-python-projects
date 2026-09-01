# 🗺️ ROADMAP — 30 Days of Python Projects

> The full 30-day plan: one real-world Python project per day, built on that day's topic from the [Asabeneh 30 Days of Python](https://github.com/Asabeneh/30-Days-Of-Python) curriculum, with complexity rising as the days go by.

## Table of contents
- [The challenge](#the-challenge)
- [The rules](#the-rules)
- [The integrity rule](#the-integrity-rule)
- [How each day works](#how-each-day-works)
- [Week 1 — Foundations in the terminal (Days 1–7)](#week-1--foundations-in-the-terminal-days-17)
- [Week 2 — Core data structures & functions (Days 8–14)](#week-2--core-data-structures--functions-days-814)
- [Week 3 — Robustness & object-oriented Python (Days 15–21)](#week-3--robustness--object-oriented-python-days-1521)
- [Week 4 — Data: scraping, statistics & pandas (Days 22–25)](#week-4--data-scraping-statistics--pandas-days-2225)
- [Week 5 — Backend: web, database & APIs (Days 26–30)](#week-5--backend-web-database--apis-days-2630)
- [What you'll have by Day 30](#what-youll-have-by-day-30)
- [Requirements](#requirements)
- [Tips to actually finish](#tips-to-actually-finish)

---

## The challenge

Instead of 30 days of notes and exercises, this is **30 days of shipped projects** — each one a small real-world tool you could actually use.

- Everything runs in the **terminal** from Day 1 to Day 20 (that's the rule — no shortcuts).
- From Day 21 onward we enter the professional world: OOP, scraping, data analysis, web apps, databases and APIs.
- The arc mirrors what backend and automation roles actually do — so by Day 30 you have a **portfolio, not just notes**.

## The rules

1. **One project per day**, built on that day's topic from Asabeneh's [30 Days of Python](https://github.com/Asabeneh/30-Days-Of-Python).
2. Every project solves a **real-world problem** — something you'd actually use.
3. Everything runs in the **terminal** until Day 20, then we go web + API.
4. **Complexity increases daily** (⭐ → ⭐⭐⭐⭐⭐).
5. **Push to GitHub every single day** — one commit per day = a green activity graph = proof of consistency for internships.
6. Each project folder gets its own README (interviewers read these).

## The integrity rule

This is a **public learning resource**, so it must be honest:

1. Every project's **official deliverable** uses only the concepts officially taught up to that day.
2. Real projects sometimes can't avoid a future concept (e.g. `if/else` shows up before its official Day 9). When that happens, it's a clearly labelled **preview** — marked `[PREVIEW - Day 9 topic]` in code comments and the README, with a one-line explanation so a beginner is never lost.
3. If a project needs more than a tiny preview, the project itself gets **moved to the day where the concept is officially taught**. (That's exactly what happened to the Environment Checker: it started as Day 1, but it belongs to Day 12 — *Modules*.)

> 💡 Asabeneh's Day 1 topic is *Introduction* (setup + first script), so Day 1's project uses only `print()` and comments — the honest first step.

## How each day works

Same loop every day, ~1–2 hours:

1. **Read** the day's topic in Asabeneh's repo, then the project spec below.
2. **Create** your folder: `mkdir day-XX-project-name`
3. **Write** `main.py` — the starter gives you examples; the rest is `TODO`s for you.
4. **Run it** (`python3 main.py`), break it, fix it — the errors are the learning.
5. **Only then** open `solution.py` and compare approaches.
6. **Write** a short project README (what it does / how to run / what I learned).
7. **Commit + push** with a clear message: `Day N: Topic - Project name`
8. **Update** the progress badge in the main README (`1/30` → `2/30` → …).

> 🛑 **The 20-minute rule:** if you're stuck on a `TODO` for more than ~20 minutes, that's a signal — check the spec again, or take a peek at the solution. Stuck-but-trying is exactly where learning happens; stuck-and-frozen is where people quit.

---

## Week 1 — Foundations in the terminal (Days 1–7)

*Your first week: variables, math, text, and the core data structures. Every project runs in the terminal. If you survive this week, you'll finish the 30 days.*

| # | Asabeneh Topic | Project | Difficulty |
|---|----------------|---------|------------|
| 1 | Introduction | Developer Profile Card | ⭐ |
| 2 | Variables & Builtin Functions | Job Offer Comparator | ⭐ |
| 3 | Operators | Loan Eligibility & Repayment Estimator | ⭐⭐ |
| 4 | Strings | Password Generator & Strength Analyzer | ⭐⭐ |
| 5 | Lists | Task Manager CLI (v1) | ⭐⭐ |
| 6 | Tuples | Trip Distance Calculator | ⭐⭐ |
| 7 | Sets | Event RSVP & Skill-Match Finder | ⭐⭐ |

### Day 1 — Introduction ⭐
**Project: Developer Profile Card**
- Your very first script: prints a profile card you'll paste into your GitHub bio and applications. Uses **only** what Day 1 teaches — `print()` and comments. No imports, no logic, no if/else.
- **Learns:** running a script, `print()`, comments, editing code.
- **Why real-world:** every tool you'll ever run starts with a banner like this — and you need a developer intro card anyway.

### Day 2 — Variables & Builtin Functions ⭐
**Project: Job Offer Comparator**
- Store two job offers (role, company, salary, monthly allowance, commute hours) in variables; use builtins `input()`, `float()`, `round()`, `len()`, `max()`, `min()` to compare and print which offer is better.
- **Learns:** declaring variables, naming conventions, built-in functions.
- **Why real-world:** this is literally you comparing internship offers later this year.

### Day 3 — Operators ⭐⭐
**Project: Loan Eligibility & Repayment Estimator**
- Inputs salary, existing debts, and loan amount; uses arithmetic (`+ - * / // % **`), comparison (`>=`, `<`), and logical (`and`, `or`, `not`) operators to decide eligibility and estimate monthly repayment.
- **Learns:** operator precedence, modulo/floor division, boolean logic.
- **Why real-world:** banks and lenders use exactly this logic for credit decisions.

### Day 4 — Strings ⭐⭐
**Project: Password Generator & Strength Analyzer**
- Generate strong random passwords and score user passwords (length, upper/lower/digits/symbols). Uses string methods, slicing, concatenation, f-strings.
- **Learns:** `str` methods (`upper`, `islower`, `count`, `join`, `strip`), indexing/slicing, f-strings.
- **Why real-world:** security basics every backend developer must know.

### Day 5 — Lists ⭐⭐
**Project: Task Manager CLI (v1)**
- In-memory to-do list: add, remove, mark complete, show pending/done. Uses list methods `append`, `remove`, `pop`, `index`, `sort`.
- **Learns:** creating/modifying lists, list methods, `enumerate`.
- **Why real-world:** every product starts as a task list — and you'll manage your job search tasks in it.

### Day 6 — Tuples ⭐⭐
**Project: Trip Distance Calculator**
- Store coordinates as immutable `(lat, lon)` tuples; compute distance between two cities (haversine formula) and store app settings in a config tuple.
- **Learns:** tuples, unpacking, immutability, why/when tuples > lists.
- **Why real-world:** logistics and ride-hailing apps compute distances constantly.

### Day 7 — Sets ⭐⭐
**Project: Event RSVP & Skill-Match Finder**
- Deduplicate RSVP lists (people can RSVP twice!), compare skill sets of two team members, find common/unique skills, union of interests.
- **Learns:** set operations `union`, `intersection`, `difference`, `symmetric_difference`, `add`, `discard`.
- **Why real-world:** deduplication and membership tests are daily tasks in data work.

---

## Week 2 — Core data structures & functions (Days 8–14)

*Decision-making, loops, functions, modules — the building blocks every real program is made of.*

| # | Asabeneh Topic | Project | Difficulty |
|---|----------------|---------|------------|
| 8 | Dictionaries | Contact Book CLI | ⭐⭐⭐ |
| 9 | Conditionals | Net Pay Estimator (PAYE) | ⭐⭐⭐ |
| 10 | Loops | Weekly Sales Reporter | ⭐⭐⭐ |
| 11 | Functions | Bill Splitter & Tip Calculator | ⭐⭐⭐ |
| 12 | Modules | Dev Environment Checker v2 (Modules) | ⭐⭐⭐ |
| 13 | List Comprehension | Data Cleaner & Extractor | ⭐⭐⭐ |
| 14 | Higher Order Functions | Employee Salary Analyzer | ⭐⭐⭐⭐ |

### Day 8 — Dictionaries ⭐⭐⭐
**Project: Contact Book CLI**
- A menu-driven contact book: add, search, update, delete, list contacts. Keys = names, values = info dicts.
- **Learns:** dict CRUD, `get`, `setdefault`, `items()`, nested dicts, `defaultdict`.
- **Why real-world:** phone apps and CRM systems are dict-shaped data.

### Day 9 — Conditionals ⭐⭐⭐
**Project: Net Pay Estimator (PAYE-style)**
- Input gross salary; apply progressive tax tiers with `if/elif/else` and nested conditions; print net pay after tax + pension deduction.
- **Learns:** `if/elif/else`, nesting, truthiness, ternary expressions.
- **Why real-world:** every salary earner needs this. (Numbers are illustrative — check current official rates before relying on them!)

### Day 10 — Loops ⭐⭐⭐
**Project: Weekly Sales Reporter**
- Enter each day's sales; loops (`for`/`while`) compute total, average, best day, worst day; optional `break`/`continue` for invalid entries.
- **Learns:** `for`, `while`, `range`, `break`, `continue`, accumulators.
- **Why real-world:** reporting/aggregation is 50% of what backend jobs actually do.

### Day 11 — Functions ⭐⭐⭐
**Project: Bill Splitter & Tip Calculator**
- Menu-driven app using well-named functions: `split_bill(total, people, tip_pct=10)`, currency formatting, multiple return values.
- **Learns:** `def`, parameters, default args, keyword args, `return`, scope.
- **Why real-world:** writing reusable functions is the core of writing maintainable code.

### Day 12 — Modules ⭐⭐⭐
**Project: Dev Environment Checker v2 (Modules)**
- Rebuild the environment checker — now it's *officially* this day's project, because modules are the topic: `sys`, `platform`, `shutil`, `os`, and `subprocess` (run `git --version` from Python). Bonus: a team randomizer with `random`.
- **Learns:** `import`, `from ... import`, stdlib discovery, `if __name__ == "__main__"`, `subprocess`.
- **Why real-world:** pre-flight checks are what CI pipelines run before every deploy.
- **Fun fact:** this project originally sat on Day 1 — it moved here so Day 1 stays true to *Introduction*. Git history shows the move!

### Day 13 — List Comprehension ⭐⭐⭐
**Project: Data Cleaner & Extractor**
- Clean a messy dataset in one-liners: extract emails, normalize prices, filter short names, square numbers, flatten nested lists.
- **Learns:** list/dict/set comprehensions, conditional comprehensions.
- **Why real-world:** data cleaning one-liners are a Python developer's superpower.

### Day 14 — Higher Order Functions ⭐⭐⭐⭐
**Project: Employee Salary Analyzer**
- Given a list of employee dicts, use `map`, `filter`, `reduce`, `sorted` with lambdas: raise everyone 10%, filter out low performers, total payroll.
- **Learns:** higher-order functions, `lambda`, `functools.reduce`.
- **Why real-world:** functional-style data pipelines are standard in real codebases.

---

## Week 3 — Robustness & object-oriented Python (Days 15–21)

*Errors, dates, regex, files — then your first classes. This is where your code stops being a script and starts being software.*

| # | Asabeneh Topic | Project | Difficulty |
|---|----------------|---------|------------|
| 15 | Python Type Errors | Bug Hunt: Type Error Fixer | ⭐⭐⭐ |
| 16 | Python Date Time | Age Calculator & Deadline Tracker | ⭐⭐⭐ |
| 17 | Exception Handling | Bank Transaction Simulator | ⭐⭐⭐⭐ |
| 18 | Regular Expressions | Log Parser & Contact Extractor | ⭐⭐⭐⭐ |
| 19 | File Handling | Note Taking App (Persistent) | ⭐⭐⭐⭐ |
| 20 | Package Manager | Expense Tracker Pro (Rich CLI) | ⭐⭐⭐⭐ |
| 21 | Classes & Objects | Bank Account System (OOP) | ⭐⭐⭐⭐ |

### Day 15 — Python Type Errors ⭐⭐⭐
**Project: Bug Hunt: Type Error Fixer**
- A deliberately buggy program (str vs int, `None` usage, wrong argument types). Find each bug, explain it, fix it; add safe type conversion and assertions.
- **Learns:** reading tracebacks, common type errors, `type()`, `isinstance()`, debugging mindset.
- **Why real-world:** debugging is the #1 actual daily skill in every engineering job.

### Day 16 — Python Date Time ⭐⭐⭐
**Project: Age Calculator & Deadline Tracker**
- Enter a birthdate → exact age (years/months/days); add deadlines → countdown in days/hours; format dates nicely.
- **Learns:** `datetime`, `date`, `timedelta`, `strftime`/`strptime`, timezones (intro).
- **Why real-world:** age checks, subscription renewals, deadline systems — all datetime logic.

### Day 17 — Exception Handling ⭐⭐⭐⭐
**Project: Bank Transaction Simulator**
- Deposit/withdraw with validation: `try/except` for invalid amounts, `ValueError`, custom exceptions (`InsufficientFundsError`), `finally` for logging.
- **Learns:** `try/except/else/finally`, raising, custom exceptions, clean error messages.
- **Why real-world:** financial software must fail gracefully — never crash on bad input.

### Day 18 — Regular Expressions ⭐⭐⭐⭐
**Project: Log Parser & Contact Extractor**
- Parse a sample server log: extract all IPs, emails, phone numbers, and timestamps; summarize counts.
- **Learns:** `re` module, patterns, groups, `findall`, `search`, `sub`.
- **Why real-world:** log analysis, data extraction, and validation are core backend tasks.

### Day 19 — File Handling ⭐⭐⭐⭐
**Project: Note Taking App (Persistent)**
- Notes survive restarts: save/load to a text file and JSON; CRUD operations; auto-backup.
- **Learns:** `open()`, read/write/append modes, `with` statements, JSON serialization, `pathlib`.
- **Why real-world:** persistence is the difference between a toy and a real app.

### Day 20 — Package Manager ⭐⭐⭐⭐
**Project: Expense Tracker Pro (Rich CLI)**
- Your first third-party packages: `pip install rich` — build a beautiful CLI with tables, colors, and prompts; `pip freeze > requirements.txt`.
- **Learns:** pip, requirements.txt, virtual packages, reading docs of external libs.
- **Why real-world:** every real project uses pip + requirements. Terminal-only era ends today.

### Day 21 — Classes & Objects ⭐⭐⭐⭐
**Project: Bank Account System (OOP)**
- `Account` base class → `SavingsAccount`, `CurrentAccount` subclasses; encapsulation with `_balance`, methods, `__str__`, `@property`.
- **Learns:** `class`, `__init__`, `self`, inheritance, encapsulation, magic methods.
- **Why real-world:** OOP is the backbone of Django, FastAPI, and most backend codebases.

---

## Week 4 — Data: scraping, statistics & pandas (Days 22–25)

*The data week: pulling data from the web and analyzing it like a data engineer.*

| # | Asabeneh Topic | Project | Difficulty |
|---|----------------|---------|------------|
| 22 | Web Scraping | Job Listings Scraper | ⭐⭐⭐⭐ |
| 23 | Virtual Environment | Package Your Own CLI | ⭐⭐⭐⭐ |
| 24 | Statistics | Exam Score Analyzer | ⭐⭐⭐⭐ |
| 25 | Pandas | Sales Dataset Analysis | ⭐⭐⭐⭐ |

### Day 22 — Web Scraping ⭐⭐⭐⭐
**Project: Job Listings Scraper**
- Scrape a job board (e.g., jobberman/indeed-like page) with `requests` + `BeautifulSoup`; extract title, company, location; save to CSV.
- **Learns:** HTTP requests, HTML parsing, CSS selectors, robots.txt politeness, `csv` module.
- **Why real-world:** scraping is used everywhere for market research — and you'll scrape job boards while job hunting.

### Day 23 — Virtual Environment ⭐⭐⭐⭐
**Project: Package Your Own CLI**
- Turn the Day 21 app into a proper installable package: `venv`, `pyproject.toml`, `pip install -e .`, console entry point `bank-cli`.
- **Learns:** venv/activate, packaging, entry points, dependency isolation.
- **Why real-world:** every professional project ships in an isolated env with a packaging file.

### Day 24 — Statistics ⭐⭐⭐⭐
**Project: Exam Score Analyzer**
- Analyze a class's scores: mean, median, mode, variance, std dev, range; detect outliers; grade distribution.
- **Learns:** `statistics` module, manual implementations, frequency distributions.
- **Why real-world:** data analysis fundamentals — the first thing many internships ask about.

### Day 25 — Pandas ⭐⭐⭐⭐
**Project: Sales Dataset Analysis**
- `pip install pandas`; load a real CSV, inspect, filter, group by, aggregate (sum/mean), export a summary report.
- **Learns:** DataFrames, `read_csv`, `groupby`, `agg`, filtering, `to_csv`.
- **Why real-world:** pandas is the #1 requested data skill in Python job postings.

---

## Week 5 — Backend: web, database & APIs (Days 26–30)

*The payoff week — where you become employable as a backend developer. Terminal scripts become web apps, databases, and APIs.*

| # | Asabeneh Topic | Project | Difficulty |
|---|----------------|---------|------------|
| 26 | Python Web | First Web App: Task Manager (Flask) | ⭐⭐⭐⭐⭐ |
| 27 | Python + MongoDB | Task Manager + MongoDB | ⭐⭐⭐⭐⭐ |
| 28 | API | Weather & GitHub API Consumer | ⭐⭐⭐⭐ |
| 29 | Building API | Task Manager REST API (FastAPI) | ⭐⭐⭐⭐⭐ |
| 30 | Conclusions | **Capstone:** Job Application Tracker | ⭐⭐⭐⭐⭐ |

### Day 26 — Python Web ⭐⭐⭐⭐⭐
**Project: First Web App: Task Manager (Flask)**
- Your Task Manager becomes a website: Flask routes, HTML templates, forms, static CSS, session or file storage.
- **Learns:** Flask, routing, `render_template`, forms, `GET`/`POST`.
- **Why real-world:** the jump from script → web app is where you become employable as a backend dev.

### Day 27 — Python + MongoDB ⭐⭐⭐⭐⭐
**Project: Task Manager + MongoDB**
- Replace file storage with MongoDB: `pymongo` CRUD (insert, find, update, delete), Atlas cloud or local install.
- **Learns:** NoSQL, documents, CRUD with pymongo, `.env` for connection strings.
- **Why real-world:** MongoDB is widely used in startups; you'll also learn what `.env` files are for.

### Day 28 — API ⭐⭐⭐⭐
**Project: Weather & GitHub API Consumer**
- Consume public APIs with `requests`: current weather (open-meteo, no key needed) and your own GitHub profile; parse JSON; handle rate limits/errors.
- **Learns:** REST concepts, JSON parsing, query params, error handling, API keys via `.env`.
- **Why real-world:** every backend job is 90% talking to APIs.

### Day 29 — Building API ⭐⭐⭐⭐⭐
**Project: Task Manager REST API (FastAPI)**
- Build your own API: endpoints (`GET/POST/PUT/DELETE /tasks`), request validation with Pydantic, interactive docs at `/docs`.
- **Learns:** FastAPI, routing, Pydantic models, HTTP methods & status codes, API design.
- **Why real-world:** this is literally the job — building and documenting APIs.

### Day 30 — Conclusions ⭐⭐⭐⭐⭐
**Project: Capstone — Job Application Tracker**
- Combine everything: track job applications (company, role, status, interview dates, notes) with a CLI, FastAPI backend, and simple web UI; store in MongoDB; write a real README with docs.
- **Learns:** systems thinking — integrating CLI + web + API + DB, project structure, documentation.
- **Why real-world:** it's the tool you'll actually use for your internship hunt, and the centerpiece of your portfolio.

---

## What you'll have by Day 30

```
Week 1–2 (Days 1–14): Python fundamentals in the terminal
Week 3   (Days 15–21): Robustness (errors, regex, files) + OOP
Week 4   (Days 22–25): Data: scraping, statistics, pandas
Week 5   (Days 26–30): Backend: Flask → MongoDB → APIs → Capstone
```

By Day 30 you'll have:

- **30 shipped projects**, each solving a real problem
- A **green GitHub contribution graph** — 30 days of proof you show up
- `pip`, virtual environments, and `pandas` experience
- A **web app**, a **database app**, and a **REST API**
- A **capstone project** you'll actually use for your internship hunt
- A complete **backend-developer starter portfolio**

## Requirements

| When | What you need |
|------|---------------|
| Day 1 | Python 3.10+ (`python3 --version`), a terminal, Git, a GitHub account |
| Day 12 | Nothing new — the standard library only |
| Day 20 | `pip` (comes with Python) + your first third-party packages |
| Day 22 | `pip install requests beautifulsoup4` |
| Day 25 | `pip install pandas` |
| Day 26 | `pip install flask` |
| Day 27 | MongoDB (free Atlas cloud account or local install) |
| Day 29 | `pip install fastapi uvicorn pydantic` |

> 💡 Don't install anything early — each week tells you exactly what you need. Installing ahead is fine; the learning is in *why* you need it.

## Tips to actually finish

1. **Commit daily, even if imperfect.** The green graph is your motivation and your proof. A small project today beats a perfect project never.
2. **Respect the 20-minute rule.** Stuck? Re-read the spec, then the solution. Don't burn an evening on one `TODO`.
3. **Type, don't paste.** Muscle memory and your own mistakes are the point.
4. **Label previews** (`# [PREVIEW - Day 9 topic]`) when you reach for a future concept — it keeps the repo honest for everyone.
5. **Note what confused you.** That feedback improves the starter for the next learner — this repo is beta-tested by its first learner: you.
6. **Miss a day?** Don't quit — double up the next day and keep the streak alive. 30/30 is the goal; 28/30 with honesty is still a great repo.

---

Made with ❤️ as part of the **30 Days of Python Projects** challenge — see [README.md](README.md) for the full story.
