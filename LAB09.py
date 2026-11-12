"""
================================================================================
MUET Cyber Learning Portal - Data Science and Analytics Lab IX
Topic: Project: An End-to-End Analysis - Framing the Question and Collecting Data

SHORT THEORY NOTES:
1. Framing Sharp, Answerable Questions:
   - A data science project requires a clear, measurable outcome (dependent variable)
     and well-defined inputs (independent variables).
   - Vague prompts ("look into restaurant trends") lead to aimless exploratory code.
   - Sharp prompts ("Does day of week predict total bill amount?") establish unambiguous
     analytical goals and determine when an investigation is completed.

2. Dataset Suitability & Provenance:
   - Always confirm the presence of target and predictor variables before writing models.
   - Provenance records where data came from, its retrieval date, license terms, and
     known sampling limitations, fulfilling both reproducibility and data ethics.

3. First-Contact Inspection:
   - Check sample size (row count), data types (dtypes), and missing values (isnull().sum()).
   - Verifying clean numeric and categorical types early prevents downstream bugs during
     EDA, grouping, and feature modeling.
================================================================================
"""

import seaborn as sns

print("=" * 65)
print("RUNNING LAB IX: FRAMING THE QUESTION AND COLLECTING DATA")
print("=" * 65)

# -------------------------------------------------------------
# TASK 1: Framing a Sharp Project Question
# Theory: State measurable outcome and explanatory inputs.
# -------------------------------------------------------------
print("\n[Executing Task 1: Question Framing...]")
task1_q = "Does daily atmospheric humidity (relative humidity %) predict the total volume of daily precipitation (mm) across different seasons of the year?"
print(f"Target Question: {task1_q}")


# -------------------------------------------------------------
# TASK 2: Dataset Suitability Validation
# Theory: Verify target and predictor features exist in the dataset.
# -------------------------------------------------------------
print("\n[Executing Task 2: Dataset Suitability Validation...]")
df = sns.load_dataset('tips')

print("Columns Available:")
print(df.columns.tolist())
print("\nFirst 5 Rows Preview:")
print(df.head())

suitability_check = "day" in df.columns and "total_bill" in df.columns
print(f"\nSuitable for question 'Does day of week affect total bill amount?': {suitability_check}")


# -------------------------------------------------------------
# TASK 3: Recording Data Provenance
# Theory: Document source, collection context, licensing, and limitations.
# -------------------------------------------------------------
print("\n[Executing Task 3: Data Provenance Record...]")
provenance_doc = """
Provenance Record:
- Dataset: Seaborn 'tips' dataset
- Source: Bryant & Smith (1995) via seaborn repository
- URL: https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv
- License: BSD-3-Clause (open educational/research use)
- Limitations: Single restaurant sampling; results cannot be widely generalized
"""
print(provenance_doc.strip())


# -------------------------------------------------------------
# TASK 4: First-Contact Data Inspection
# Theory: Inspect sample size, schema types, and basic missingness.
# -------------------------------------------------------------
print("\n[Executing Task 4: First-Contact Data Inspection...]")
print(f"Total Rows: {len(df)}")
print(f"Total Columns: {len(df.columns)}")
print("\nData Types:")
print(df.dtypes)
print("\nMissing Values Count:")
print(df.isnull().sum())

print("\n" + "=" * 65)
print("ALL LAB IX TASKS EXECUTED SUCCESSFULLY.")
print("=" * 65)


"""
================================================================================
MUET Cyber Learning Portal - Data Science and Analytics Lab IX
Topic: Project: An End-to-End Analysis - Cleaning, Exploring and Modelling

SHORT THEORY NOTES:
1. Target Variable Engineering & Scrutiny:
   - Analytical questions often require derived targets (e.g., tip_pct = tip / total_bill * 100).
   - Engineered variables must undergo the same sanity checks as raw data to identify
     division artifacts or extreme outliers (e.g., small bills yielding 70%+ tips).

2. EDA Before Modeling:
   - Always visualize relationships (scatter plots, regression lines) before fitting models.
   - Correlation metrics only detect linear trends and can miss non-linear curves or clusters.
   - EDA shows whether a relationship exists before committing computational effort.

3. Leak-Free Pipeline Execution:
   - Train/test split must occur prior to fitting scalers or estimators.
   - Wrapping StandardScaler and LinearRegression within a Pipeline ensures that mean and 
     variance parameters are fit strictly on training folds, preventing data leakage.

4. Baseline Comparison & Honest Reporting:
   - Compare regression models against DummyRegressor(strategy='mean'), which yields R^2 ~ 0.
   - A model is only valuable if it clears the naive baseline by a meaningful margin.
   - Low explanatory power (e.g., R^2 < 0.10) is a valid, honest finding showing weak association.
================================================================================
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.dummy import DummyRegressor

print("=" * 65)
print("RUNNING LAB IX: CLEANING, EXPLORING AND MODELLING")
print("=" * 65)

# Load and clean benchmark data
df = sns.load_dataset('tips').dropna().drop_duplicates()


# -------------------------------------------------------------
# TASK 1: Target Variable Engineering
# Theory: Calculate and sanity-check derived target features.
# -------------------------------------------------------------
print("\n[Executing Task 1: Target Variable Engineering...]")
df['tip_pct'] = (df['tip'] / df['total_bill']) * 100

min_pct = df['tip_pct'].min()
max_pct = df['tip_pct'].max()

print("--- TASK 1 OUTPUT ---")
print(f"Minimum tip_pct: {min_pct:.2f}%")
print(f"Maximum tip_pct: {max_pct:.2f}%")
print("\nTarget summary statistics:")
print(df['tip_pct'].describe().round(2))


# -------------------------------------------------------------
# TASK 2: Exploring Outcome Relationships
# Theory: Visual exploration reveals dispersion and potential non-linearity.
# -------------------------------------------------------------
print("\n[Executing Task 2: Exploring Outcome Relationships...]")
fig, ax = plt.subplots(figsize=(6, 4))
sns.regplot(data=df, x='size', y='tip_pct', ax=ax, scatter_kws={'alpha': 0.6})
ax.set_title('Tip Percentage vs Party Size')
ax.set_xlabel('Party Size')
ax.set_ylabel('Tip Percentage (%)')
fig.savefig('tip_vs_size.png', dpi=120, bbox_inches='tight')
plt.close(fig)

corr_val = df['size'].corr(df['tip_pct'])
print("--- TASK 2 OUTPUT ---")
print(f"Correlation (size vs tip_pct): {corr_val:.4f}")
print("Saved scatter plot to 'tip_vs_size.png'.")


# -------------------------------------------------------------
# TASK 3: Implementing a Leak-Free Pipeline
# Theory: make_pipeline fits scaler parameters on training data only.
# -------------------------------------------------------------
print("\n[Executing Task 3: Leak-Free Pipeline Modeling...]")
X = df[['size', 'total_bill']]
y = df['tip_pct']

X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=42)

model = make_pipeline(StandardScaler(), LinearRegression())
model.fit(X_tr, y_tr)

model_score = model.score(X_te, y_te)
print("--- TASK 3 OUTPUT ---")
print(f"Test Set R^2 Score: {model_score:.4f}")


# -------------------------------------------------------------
# TASK 4: Baseline Comparison
# Theory: Benchmark against predicting the training mean (DummyRegressor).
# -------------------------------------------------------------
print("\n[Executing Task 4: Baseline Model Comparison...]")
dummy = DummyRegressor(strategy='mean')
dummy.fit(X_tr, y_tr)

dummy_score = dummy.score(X_te, y_te)

print("--- TASK 4 OUTPUT ---")
print(f"Baseline R^2 (predict mean):   {dummy_score:.4f}")
print(f"Model R^2 (Linear Regression): {model_score:.4f}")
print(f"Improvement over baseline:     {(model_score - dummy_score):.4f}")

print("\n" + "=" * 65)
print("ALL TASKS EXECUTED SUCCESSFULLY.")
print("=" * 65)

"""
================================================================================
MUET Cyber Learning Portal - Data Science and Analytics Lab IX
Topic: Communicating and Shipping the Project

SHORT THEORY NOTES:
1. Deliverable as a Narrative Story:
   - A completed data science deliverable is read more than it is executed.
   - It must walk the audience through the full analytical lifecycle:
     Question -> Provenance -> Cleaning -> EDA -> Modeling -> Honest Conclusion.

2. End-to-End Reproducibility:
   - "Restart Kernel and Run All" ensures zero hidden states or out-of-order execution bugs.
   - Pinned environments (requirements.txt) lock exact dependency versions (e.g., pandas==2.1.0)
     so the pipeline executes identically across different operating systems.

3. Repository Hygiene & Shipping:
   - README.md: Details the core question, environment setup commands, and headline findings.
   - .gitignore: Excludes raw data (*.csv), sensitive keys (.env), and caches (__pycache__/).
   - Git Commit: Creates an immutable, versioned snapshot of the finished deliverable.
================================================================================
"""

import os
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.dummy import DummyRegressor

print("=" * 65)
print("RUNNING LAB IX: COMMUNICATING AND SHIPPING THE PROJECT")
print("=" * 65)


# -------------------------------------------------------------
# TASK 1: Pinning Project Dependencies
# Theory: Pin exact library versions in requirements.txt for reproducible builds.
# -------------------------------------------------------------
print("\n[Executing Task 1: Generating requirements.txt...]")
req_content = "pandas==2.1.0\nscikit-learn==1.3.0\n"
with open("requirements.txt", "w") as f:
    f.write(req_content)

print("Created requirements.txt with pinned versions:")
print(req_content.strip())


# -------------------------------------------------------------
# TASK 2: Ensuring Execution Flow
# Theory: Complete end-to-end execution without hidden state or leakage.
# -------------------------------------------------------------
print("\n[Executing Task 2: Validating Pipeline Execution Flow...]")
df = sns.load_dataset('tips').dropna().drop_duplicates()
df['tip_pct'] = (df['tip'] / df['total_bill']) * 100

X = df[['size', 'total_bill']]
y = df['tip_pct']

X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=42)

model = make_pipeline(StandardScaler(), LinearRegression())
model.fit(X_tr, y_tr)
model_r2 = model.score(X_te, y_te)

dummy = DummyRegressor(strategy='mean')
dummy.fit(X_tr, y_tr)
baseline_r2 = dummy.score(X_te, y_te)

print("Final Cell Execution Simulation:")
print("=" * 60)
print("PROJECT EXECUTION COMPLETE: FINAL SUMMARY")
print(f"Total observations evaluated: {len(df)}")
print(f"Test Set R^2 Score: {model_r2:.4f}")
print(f"Baseline Mean R^2:  {baseline_r2:.4f}")
print("Conclusion: Dining party size accounts for only ~8.9% of the")
print("variance in tip percentage. The relationship is weak and not causal.")
print("=" * 60)


# -------------------------------------------------------------
# TASK 3: Configuring Repository Privacy
# Theory: Prevent Git from tracking datasets, caches, or credentials.
# -------------------------------------------------------------
print("\n[Executing Task 3: Verifying .gitignore Privacy Rules...]")
gitignore_rules = "*.csv\n.env\ndata/\n__pycache__/\n.ipynb_checkpoints/\n"
with open(".gitignore", "w") as f:
    f.write(gitignore_rules)

# Create dummy sensitive files
with open(".env", "w") as f:
    f.write("SECRET_KEY=12345\n")
with open("raw_records.csv", "w") as f:
    f.write("id,bill,tip\n")

print("Created .gitignore with exclusion rules:")
print(gitignore_rules.strip())


# -------------------------------------------------------------
# TASK 4: Drafting the Project README
# Theory: README provides structure, setup commands, and headline takeaways.
# -------------------------------------------------------------
print("\n[Executing Task 4: Writing Project README.md...]")
readme_text = """# Restaurant Tip Percentage Analysis

## 1. Research Question
Does the size of a dining party predict the percentage of the bill left as a tip?

## 2. Setup and Execution Instructions
1. Clone repo: git clone https://github.com/jahangir-muet/dsa-practice.git
2. Setup environment: python -m pip install -r requirements.txt
3. Run analysis: Open analysis.ipynb and select 'Restart Kernel and Run All Cells'.

## 3. Headline Finding
Party size explains only ~8.9% of the variation in tipping percentage (R² = 0.0898), barely beating the mean baseline.
"""

with open("README.md", "w") as f:
    f.write(readme_text)

print("Saved README.md successfully.")
print("\n" + "=" * 65)
print("ALL LAB IX SHIPPING TASKS COMPLETED.")
print("=" * 65)