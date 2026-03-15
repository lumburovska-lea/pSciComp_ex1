# Data

This directory contains all data used and produced by the project, organized by processing stage.

## Stages

| Stage | Path | Description |
|-------|------|-------------|
| Raw | `data/raw/` | Original, unmodified input data. Committed directly to the repository when small ("tiny data"). |
| Final | `data/final/` | Output data produced by scripts. Not tracked in version control. |

## Files

### `data/raw/people.json`
List of people and their course enrollments. Used as input by `scripts/drafts/say_hello.py`.

### `data/final/greeting.txt`
Personalized greetings generated for all people enrolled in the target course. Produced by `scripts/drafts/say_hello.py`.
