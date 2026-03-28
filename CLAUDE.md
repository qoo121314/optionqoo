# CLAUDE.md — optionqoo

## Project Overview

This is a minimal educational Python project focused on **options trading payoff analysis**. It contains Jupyter notebooks that calculate and visualize payoff diagrams for standard options positions (long/short calls and puts).

The project was created in October 2016 and is primarily useful as a reference or teaching aid for understanding options payoff structures.

---

## Repository State

The current working directory is empty — the original notebooks were committed and then reverted. The notebook source is preserved in git history (commit `e08960f`).

To restore the original notebooks:
```bash
git checkout e08960f -- "Q1-longCall-shortCall.ipynb" "Q2-Long and Short put.ipynb"
```

---

## Technology Stack

| Component | Details |
|-----------|---------|
| Language | Python 3.5.2 |
| Notebooks | Jupyter (`.ipynb`, nbformat 4) |
| Numerical computation | NumPy |
| Visualization | Matplotlib |

No backend, database, web framework, or build system. No `requirements.txt` or environment config files — dependencies are standard scientific Python.

---

## Notebooks

### Q1-longCall-shortCall.ipynb — Call Options

Analyzes payoff for long call and short call positions.

```python
K = 9100              # Strike price
Premium_91Call = 195  # Call option premium

Payoff_longCall  = np.maximum(standard - K, 0) - Premium_91Call
Payoff_shortCall = -Payoff_longCall
Sum              = Payoff_longCall + Payoff_shortCall  # Always 0 (perfect hedge)
```

### Q2-Long and Short put.ipynb — Put Options

Analyzes payoff for long put and short put positions.

```python
K = 9100              # Strike price
Premium_91put = 18.5  # Put option premium

Payoff_shortput = np.minimum(standard - K, 0) + Premium_91put
Payoff_longput  = -Payoff_shortput
Sum             = Payoff_longput + Payoff_shortput  # Always 0 (perfect hedge)
```

---

## Payoff Formula Conventions

| Position | Formula |
|----------|---------|
| Long Call | `max(S - K, 0) - Premium` |
| Short Call | `-max(S - K, 0) + Premium` |
| Long Put | `max(K - S, 0) - Premium` |
| Short Put | `-max(K - S, 0) + Premium` = `min(S - K, 0) + Premium` |

Where `S` is the underlying asset price at expiration and `K` is the strike price.

The sum of any long + short position for the same strike/premium is always 0.

---

## Development Workflow

### Running Notebooks

```bash
jupyter notebook
```

Open the desired `.ipynb` file in the Jupyter UI. Run cells sequentially (Shift+Enter).

### Adding New Option Analysis

Follow the established pattern in existing notebooks:

1. Import `numpy` and `matplotlib.pyplot`
2. Define parameters: strike `K`, premium
3. Build price range: `standard = np.arange(K - interval, K + interval)`
4. Calculate payoffs using vectorized NumPy operations
5. Plot with `plt.plot()` and display with `plt.show()`

### No Tests, No CI

There are no automated tests, linters, or CI/CD pipelines configured.

---

## Git Conventions

- Branch: feature work goes on descriptive branches; `master` is the primary branch
- Commit messages are short and descriptive (e.g., `optionQ1&Q2`, `:octocat: Added .gitattributes`)
- The `.gitattributes` file normalizes line endings across platforms
- The `.gitignore` covers Windows/macOS OS artifacts (`Thumbs.db`, `.DS_Store`)

---

## Notes for AI Assistants

- **No external dependencies to install** — NumPy and Matplotlib are assumed available in the Python environment (standard Anaconda distribution).
- **No environment variables or secrets** — All parameters are hardcoded inline in notebooks.
- **Notebooks are self-contained** — Each notebook is independent; there are no shared modules or imports between them.
- **Naming convention**: Notebooks use descriptive filenames like `Q1-longCall-shortCall.ipynb`. New notebooks should follow the `Q<N>-<description>.ipynb` pattern.
- **Current working directory is empty** — If asked to work on the notebooks, restore them from git history first (see "Repository State" above).
- **Python version**: Original code targets Python 3.5.2 (Anaconda "Python [Root]" kernel), but the code is compatible with any modern Python 3.x.
