"""
================================================================================
MUET Cyber Learning Portal - Data Science and Analytics Lab VII
Topic: Creating and Organising Notebooks

SHORT THEORY NOTES:
1. Kernel and State Accumulation:
   - A Jupyter notebook runs on an active kernel that stores all variables in memory.
   - The 'In [n]' counter indicates chronological execution order, not physical layout.
   - Deleting a cell does not wipe its defined variables from the kernel's RAM.
   - Golden Rule: Always run 'Restart Kernel and Run All' to confirm top-to-bottom reproducibility.

2. Cells and Narrative Arc:
   - Alternating Markdown cells (intent/takeaways) with Code cells (implementation) turns
     plain scripts into complete, readable data stories.

3. Keyboard Efficiency and Magics:
   - Esc enters Command Mode (blue bar): 'a' (insert above), 'b' (insert below), 'dd' (delete),
     'm' (Markdown), 'y' (Code). Enter enters Edit Mode (green bar).
   - Line Magics (%): '%timeit' profiles execution speed; '%matplotlib inline' displays charts inline.
   - Shell Commands (!): Exclamation mark prefixes run shell/terminal commands directly (e.g., !dir, !ls).
================================================================================
"""

import os
import timeit

print("=" * 65)
print("RUNNING LAB VII: CREATING AND ORGANISING NOTEBOOKS")
print("=" * 65)


# -------------------------------------------------------------
# TASK 1: Execute and Verify Variable State
# Theory: Demonstrates how the kernel retains variable state across cell deletions.
# -------------------------------------------------------------
print("\n[Executing Task 1: Persistent Variable State Demonstration...]")
# Simulating In [1]: x = 10 (Cell deleted in UI)
# Executing In [2]: print(x)
x = 10  # Persists in kernel memory
print(f"Cell In [2] output (accessing retained variable): x = {x}")


# -------------------------------------------------------------
# TASK 2: Benchmark Code with Magic Commands
# Theory: %timeit profiles execution duration across thousands of runs.
# -------------------------------------------------------------
print("\n[Executing Task 2: Benchmarking Code Execution...]")
# Benchmarking equivalent of: %timeit sum(range(1000))
measured_time = timeit.timeit("sum(range(1000))", number=10000) / 10000
print(f"Command benchmarked: sum(range(1000))")
print(f"Average time per loop: {measured_time * 1e6:.2f} µs")


# -------------------------------------------------------------
# TASK 3: Shell Command Integration
# Theory: '!' invokes OS terminal commands from within a notebook cell.
# -------------------------------------------------------------
print("\n[Executing Task 3: Shell Command Execution (!dir /b)...]")
# Equivalent to running '!dir /b' in Jupyter on Windows
files_in_workspace = os.listdir('.')
print("Directory listing output:")
for entry in files_in_workspace[:8]:
    print(f"  {entry}")


# -------------------------------------------------------------
# TASK 4: Narrative Structure Implementation
# Theory: Interweaving Markdown context with Code execution builds a self-explanatory report.
# -------------------------------------------------------------
print("\n[Executing Task 4: Three-Cell Narrative Structure...]")
print("Cell 1 [Markdown]:")
print("  # Student Exam Score Analysis")
print("Cell 2 [Code]:")
total_students = 50
passed_students = 42
pass_rate = (passed_students / total_students) * 100
print(f"  Pass Rate: {pass_rate:.1f}%")
print("Cell 3 [Markdown]:")
print("  The calculated pass rate is 84.0%, indicating that a clear majority of the cohort successfully met the course completion criteria.")

print("\n" + "=" * 65)
print("ALL 5 TASKS EXECUTED AND VERIFIED SUCCESSFULLY.")
print("=" * 65)

"""
================================================================================
MUET Cyber Learning Portal - Data Science and Analytics Lab VII
Topic: Documenting Analysis with Markdown

SHORT THEORY NOTES:
1. Markdown as Narrative Documentation:
   - A data science notebook is an analytical narrative, not just a script.
   - Documenting in real time captures exploratory decisions, assumptions, and fixes
     while context is fresh, rather than trying to reconstruct intent after the fact.

2. Structure and Formatting:
   - Headings (# H1, ## H2, ### H3): Generate an automatic Table of Contents in Jupyter,
     turning a wall of code into a structured, navigable document.
   - Emphasis: **bold** highlights critical warnings/conclusions; *italics* denotes terms.
   - Inline Code (`code`): Distinguishes functions, variables, and columns from prose.
   - Tables (| col1 | col2 |): Present structured comparisons, schema, and metrics cleanly.

3. Mathematical Precision with LaTeX:
   - Enclosing formulas in $...$ (inline) or $$...$$ (display block) renders exact math.
   - Clear math notation (e.g., z = (x - \mu) / \sigma) removes ambiguity from text descriptions.
================================================================================
"""

print("=" * 65)
print("RUNNING LAB VII: DOCUMENTING ANALYSIS WITH MARKDOWN")
print("=" * 65)


# -------------------------------------------------------------
# TASK 1: Create a Document Structure
# Theory: Hierarchical headings (#, ##, ###) build a navigable document outline.
# -------------------------------------------------------------
print("\n[Executing Task 1: Document Hierarchy Scaffolding...]")
task1_markdown = """# Exploratory Analysis Report

## Methodology

### Data Cleaning
* Handle missing values
* Remove duplicates
* Normalize scales"""

print("--- TASK 1 MARKDOWN SOURCE ---")
print(task1_markdown)


# -------------------------------------------------------------
# TASK 2: Format a Data Summary Table
# Theory: Pipe tables (|) summarize schemas and metrics clearly.
# -------------------------------------------------------------
print("\n[Executing Task 2: Data Summary Table...]")
task2_table = """| Variable Name | Data Type |
| ------------- | --------- |
| Age           | Integer   |
| Name          | String    |
| Salary        | Float     |"""

print("--- TASK 2 TABLE SOURCE ---")
print(task2_table)


# -------------------------------------------------------------
# TASK 3: Inline Code and Emphasis
# Theory: Combines bold warnings, italicized terms, and inline backticks.
# -------------------------------------------------------------
print("\n[Executing Task 3: Inline Code and Emphasis...]")
task3_sentence = "**Warning:** Never apply *standardization* with `pd.read_csv()` loaded data before completing the train-test split to avoid data leakage."

print("--- TASK 3 PROSE STRING ---")
print(task3_sentence)


# -------------------------------------------------------------
# TASK 4: Render Mathematical Notation
# Theory: Display LaTeX ($$...$$) ensures unambiguous mathematical communication.
# -------------------------------------------------------------
print("\n[Executing Task 4: LaTeX Math Rendering...]")
task4_latex = "$$ z = \\frac{x - \\mu}{\\sigma} $$"

print("--- TASK 4 LATEX FORMULA ---")
print(task4_latex)

print("\n" + "=" * 65)
print("ALL LAB VII TASKS DEMONSTRATED AND READY.")
print("=" * 65)

"""
================================================================================
MUET Cyber Learning Portal - Data Science and Analytics Lab VII
Topic: Visualising, Reproducing and Sharing

SHORT THEORY NOTES:
1. Inline Visualisation:
   - '%matplotlib inline' renders figures directly beneath the originating code cell.
   - Narrative Context: Placing an analytical expectation above a plot and an interpretation
     below it ensures the chart communicates its story independently.

2. Reproducibility Guarantee (Restart and Run All):
   - The interactive kernel holds state invisibly in RAM across cell deletions and re-runs.
   - 'Restart Kernel and Run All' clears RAM and executes cells strictly from top to bottom.
   - A notebook is only verified as reproducible when it executes cleanly on a blank slate.

3. Exporting with nbconvert:
   - Static HTML: 'jupyter nbconvert --to html notebook.ipynb' builds a shareable report
     that any stakeholder can open in a web browser without installing Python or Jupyter.
   - Plain Script: 'jupyter nbconvert --to script notebook.ipynb' converts cells into a
     standard .py script suitable for production pipelines or scheduled cron jobs.

4. Privacy and Output Discipline:
   - An .ipynb file is a JSON document containing both code and all execution outputs.
   - Hardcoded API keys or printed Personally Identifiable Information (PII) persist inside
     the raw JSON file even if code cells are altered.
   - Always clear outputs before committing to shared repositories or version control.
================================================================================
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

print("=" * 65)
print("RUNNING LAB VII: VISUALISING, REPRODUCING AND SHARING")
print("=" * 65)


# -------------------------------------------------------------
# TASK 1: Inline Visualization Implementation
# Theory: Flank inline figures with analytical Markdown context.
# -------------------------------------------------------------
print("\n[Executing Task 1: Inline Chart Setup...]")
df_tips = sns.load_dataset('tips')
fig1, ax1 = plt.subplots(figsize=(6, 4))
sns.histplot(df_tips['total_bill'], kde=True, ax=ax1, color='tab:blue')
ax1.set_title('Total Bill Distribution')
ax1.set_xlabel('Total Bill ($)')
ax1.set_ylabel('Frequency')
fig1.savefig('task1_inline_preview.png', dpi=120, bbox_inches='tight')
plt.close(fig1)

print("Markdown Context Above: We visualize the distribution of customer bills to check whether spending clusters around a central average or exhibits a right-sided skew with high-spend tables.")
print("Saved preview to 'task1_inline_preview.png'. Output shows a unimodal, right-skewed distribution centered between $15 and $18.")


# -------------------------------------------------------------
# TASK 2: Reproducibility Verification Process
# Theory: Clean sequential dependencies guarantee error-free execution.
# -------------------------------------------------------------
print("\n[Executing Task 2: Linear Dependency Execution...]")
# Cell 1: Define baseline parameter
base_amount = 50

# Cell 2: Apply calculation rule
tax_rate = 0.08
total_with_tax = base_amount * (1 + tax_rate)

# Cell 3: Display reproducible output
print(f"Final calculated total: ${total_with_tax:.2f}")


# -------------------------------------------------------------
# TASK 3 & 4: Exporting via nbconvert
# Theory: Converting .ipynb files to static HTML reports and reusable .py scripts.
# -------------------------------------------------------------
print("\n[Executing Task 3 & 4: Export Commands Simulation...]")
cmd_html = "jupyter nbconvert --to html analysis.ipynb"
cmd_script = "jupyter nbconvert --to script analysis.ipynb"

print(f"HTML Export Command:   {cmd_html}")
print("Expected Output: [NbConvertApp] Writing ... bytes to analysis.html")
print(f"Script Export Command: {cmd_script}")
print("Expected Output: [NbConvertApp] Writing ... bytes to analysis.py")

# Sample script header produced by nbconvert
script_header = """#!/usr/bin/env python
# coding: utf-8

# In[1]:"""
print("\nFirst three lines of exported script:")
print(script_header)


# -------------------------------------------------------------
# TASK 5: Privacy and Output Discipline Check
# Theory: .ipynb JSON structure stores embedded outputs and execution states.
# -------------------------------------------------------------
print("\n[Executing Task 5: Security Review Note...]")
print("Reminder: Strip sensitive credentials and clear cell outputs before Git commit.")

print("\n" + "=" * 65)
print("ALL TASKS AND THEORY NOTES EXECUTED SUCCESSFULLY.")
print("=" * 65)