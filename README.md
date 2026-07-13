# Python & DSA From Scratch

A calm, no-rush path from zero to Data Structures & Algorithms.
**~30 minutes a day.** Understanding beats speed.

---

## How to Follow This Course

The whole course is a straight line. Do it **top to bottom**, one day at a time. Never skip ahead — each week assumes the one before it.

```
Prep  →  Learn  →  Practice daily  →  Review every 2 weeks  →  next week
```

### The rhythm of a single week

Every week folder follows the **same predictable shape**, so once you learn one, you know them all:

```
weekX/
├── prerequisite.md    ← 1. READ FIRST — mental models & what to watch for
├── day1_*.md          ← 2. the lesson (concepts + traced, step-by-step examples)
├── day1_*.py          ←    your practice file for that day (type it yourself)
├── day2_*.md
├── day2_*.py
├── day3_*.md
├── day4_*.md
└── day5_practice.md   ← 3. PRACTICE DAY — no new concepts, just apply everything
```

**For each day:**
1. Read the `prerequisite.md` once at the **start of the week** — it primes your brain for the week's ideas.
2. Read the day's `.md` lesson. Each one now includes 🧩 *traced walkthroughs* — tables that follow the code line by line so you can see exactly how it reaches the answer.
3. Type the examples into your own `dayX_practice.py` **from memory** — don't copy/paste.
4. Do the exercises at the bottom of the lesson before moving on.

---

## The Two Practice Approaches

Practice happens at **two levels** — both matter, neither is optional.

### 1. Daily practice — `day5_practice.md` (end of every week)
The 5th day of each week has **no new concepts**. It's where you apply that week's ideas through small challenges. This locks in what you just learned while it's fresh.

### 2. Two-week recall reviews — `two_week_practice/`
After every two-week block, step back and prove you still remember. These reviews mix topics across weeks so you build **pattern recognition**, not just short-term recall.

```
two_week_practice/
├── weeks1_2_practice.md      # basics, decisions, loops, strings, lists
├── weeks3_4_5_practice.md    # functions, dictionaries, sets, mixed challenges
├── weeks6_7_practice.md      # DSA basics, arrays, searching, hash maps, stacks, queues
├── weeks8_9_practice.md      # recursion, linked lists, two pointers, trees, graphs
└── week10_capstone.md        # sorting, heaps, sliding window, final review
```

> **How to review:** Try each problem *without* looking at old solutions first. If stuck, write down the *problem shape* before the code. Redo anything you missed the next day, from memory.

---

## The Path (Phases)

### Phase 1 — Python Fundamentals (Weeks 1-3)
Learn to think like a programmer. No algorithms yet — just Python.

```
├── week1/   print & variables → input & types → if/else → comparisons & logic → practice
├── week2/   while loops → for/range → strings → lists → practice
└── week3/   functions → dictionaries → sets & tuples → comprehensions → practice
```

➡️ **After Week 2:** do `two_week_practice/weeks1_2_practice.md`.

### Phase 2 — Problem-Solving (Weeks 4-5)
Small coding challenges using what you learned. Builds the "thinking" muscle.

```
├── week4_5/
│   ├── prerequisite.md         ← problem-solving patterns (two-pointer, one-pass, etc.)
│   ├── easy_challenges.md      ← 15 mini problems  (+ easy_challenges.py to solve in)
│   └── medium_challenges.md    ← 10 harder ones     (+ medium_challenges.py)
```

➡️ **After Week 5:** do `two_week_practice/weeks3_4_5_practice.md`.

### Phase 3 — Intermediate Python (Weeks 6-9)
Fill the CS50P-style topics before DSA: exceptions, libraries, testing, files, regex, OOP, and advanced Python.

```
├── week6_exceptions_libraries/    exceptions → raising/debugging → imports → CLI & JSON → practice
├── week7_testing_file_io/         assert → pytest → read/write files → CSV → practice
├── week8_regex_oop/               regex basics → groups/sub → classes → inheritance → practice
└── week9_advanced_python_project/ type hints → *args/**kwargs → generators → project structure → final project
```

➡️ **After Week 7:** do `weeks6_7_practice.md`.  **After Week 9:** do `weeks8_9_practice.md`.

### Phase 4 — DSA Patterns (Weeks 1-5 of the DSA track)
Now you're ready for DSA with a stronger Python base. Same daily rhythm — each week has a `prerequisite.md` plus day-by-day lessons.

> **New to Big O?** Start with the visual primer in `dsa_weeks/time_complexity_playground/` (`01_big_o_story.md` → `07_pattern_quiz.md`) before Week 1.

```
└── dsa_weeks/
    ├── time_complexity_playground/   ← optional visual Big O primer (read first)
    ├── week1/    what is DSA → Big O → arrays → searching → practice
    ├── week2/    hash maps → sets → stacks → queues → practice
    ├── week3/    recursion → linked lists → list operations → two pointers → practice
    ├── week4/    trees → tree DFS → tree BFS → grids & graphs → practice
    └── week5/    basic sorting → merge sort → heaps → sliding window → final practice
```

➡️ **Finish with** `two_week_practice/week10_capstone.md` — the final pattern review.

> The DSA track also lives as a standalone repo: [SagarDevExpo/dsa-weeks](https://github.com/SagarDevExpo/dsa-weeks).

---

## The Rules
1. **Type every line yourself** — don't copy/paste.
2. **Read the `prerequisite.md` before starting each week.**
3. **Run your code after every section** — see what happens.
4. **Do the exercises** — reading alone doesn't work.
5. **Never skip the practice** — both the daily `day5` *and* the two-week reviews.
6. **Stuck for 10 minutes? Move on** — come back tomorrow with fresh eyes.

## How to Run
```bash
cd python-from-scratch/week1
python3 day1_practice.py
```
