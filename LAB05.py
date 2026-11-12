"""
================================================================================
MUET Cyber Learning Portal - Data Science and Analytics Lab V
Topic: Descriptive Statistics on a Real Dataset

SHORT THEORY NOTES:
1. Initial Inspection (First-Look Discipline):
   - Always run df.info() and df.describe() before formulating hypotheses or plotting.
   - df.info(): Displays row counts, data types (float, int, category), non-null values, and memory usage.
   - df.describe(): Provides the 5-number summary (min, 25%, 50%, 75%, max) along with count, mean, and std.

2. Centre, Spread, and Shape:
   - Symmetrical Data: Mean ≈ Median (skew ≈ 0).
   - Right-Skewed Data: Mean > Median (positive skew > 0). Extreme high values pull the mean upward.
   - Median (50th percentile) is the honest measure of "typical" value for skewed data because it resists outliers.
   - Spread is measured using Standard Deviation (for normal data) and IQR (Q75 - Q25, robust against outliers).

3. Categorical Distributions:
   - df['col'].value_counts() shows category balance, class dominance, and uncovers data errors/typos early.

4. Grouped Descriptive Summaries:
   - df.groupby('cat_col')['num_col'].describe() breaks metrics down by groups to reveal behavioral differences across sub-populations.
================================================================================
"""

import seaborn as sns
import pandas as pd

# Load dataset
df = sns.load_dataset('tips')

print("=" * 65)
print("RUNNING LAB V: DESCRIPTIVE STATISTICS ON A REAL DATASET")
print("=" * 65)


# -------------------------------------------------------------
# TASK 1: Initial Dataset Inspection
# Theory: df.info() checks structure/types; df.describe() gives numeric summaries.
# -------------------------------------------------------------
print("\n[Executing Task 1: Initial Dataset Inspection...]")
print("--- DF.INFO() ---")
df.info()

print("\n--- DF.DESCRIBE() ---")
print(df.describe())


# -------------------------------------------------------------
# TASK 2: Categorical Distribution Analysis
# Theory: df['col'].value_counts() inspects frequency balance and flags rare/corrupted levels.
# -------------------------------------------------------------
print("\n[Executing Task 2: Categorical Distribution Analysis...]")
freq_table = df['day'].value_counts()
print("Frequency distribution for 'day':")
print(freq_table)


# -------------------------------------------------------------
# TASK 3: Measuring Centre and Spread
# Theory: Mean, Median, and IQR (Q75 - Q25) quantify central tendency and variability.
# -------------------------------------------------------------
print("\n[Executing Task 3: Measuring Centre and Spread...]")
mean_val = df['total_bill'].mean()
median_val = df['total_bill'].median()
q25 = df['total_bill'].quantile(0.25)
q75 = df['total_bill'].quantile(0.75)
iqr_val = q75 - q25

print(f"Mean: {mean_val:.2f}")
print(f"Median: {median_val:.2f}")
print(f"IQR: {iqr_val:.2f} (Q25={q25:.2f}, Q75={q75:.2f})")


# -------------------------------------------------------------
# TASK 4: Grouped Descriptive Summaries
# Theory: groupby().describe() compares metric behavior across categorical segments.
# -------------------------------------------------------------
print("\n[Executing Task 4: Grouped Descriptive Summaries...]")
grouped_summary = df.groupby('time', observed=False)['total_bill'].describe()
print("Grouped summary of total_bill by time:")
print(grouped_summary.round(2))


# -------------------------------------------------------------
# TASK 5: Analysis of Data Shape
# Theory: A positive skew with Mean > Median demonstrates a right-skewed distribution.
# -------------------------------------------------------------
print("\n[Executing Task 5: Analysis of Data Shape...]")
skew_val = df['total_bill'].skew()
print(f"Total Bill Mean: {mean_val:.2f}")
print(f"Total Bill Median: {median_val:.2f}")
print(f"Total Bill Skewness: {skew_val:.2f}")

print("\n" + "=" * 65)
print("ALL 5 TASKS EXECUTED SUCCESSFULLY.")
print("=" * 65)

"""
================================================================================
MUET Cyber Learning Portal - Data Science and Analytics Lab V
Topic: Distributions and Outlier Detection

SHORT THEORY NOTES:
1. Shape Verification (Histograms & KDE):
   - Always plot distributions before modeling to detect skewness, symmetry, or multimodality.
   - Unimodal indicates a single dominant group; bimodal/multimodal indicates mixed populations.
   - Positive skewness (> 0) features a long right tail with Mean > Median.

2. IQR Rule (Robust Outlier Detection):
   - IQR = Q3 - Q1 (middle 50% of data).
   - Bounds: [Q1 - 1.5*IQR, Q3 + 1.5*IQR]. Matches box-plot whisker criteria.
   - Quartiles are rank-based, so extreme values cannot inflate or drag the boundaries.
   - Primary standard for skewed or non-normal data distributions.

3. Z-Score Rule (Parametric Detection):
   - Formula: z = (x - mean) / std. Flags values where |z| > 3.
   - Assumes a roughly Gaussian (normal) distribution following the empirical 68-95-99.7 rule.
   - Vulnerable to masking on skewed data because extreme tail values inflate 'std'.

4. Error vs. Signal Decision:
   - Error: Physically impossible or corrupted values (e.g., age = 220, temp = -999). Fix or delete.
   - Signal: Genuine extreme behavior (e.g., massive fraud transactions, peak spenders). Retain and investigate.
================================================================================
"""

import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import numpy as np

# Load benchmark dataset
df = sns.load_dataset('tips')

print("=" * 65)
print("RUNNING LAB V: DISTRIBUTIONS AND OUTLIER DETECTION")
print("=" * 65)


# -------------------------------------------------------------
# TASK 1: Visualizing Distribution Shape
# Theory: Histograms and KDE curves reveal modality and skewness.
# -------------------------------------------------------------
print("\n[Executing Task 1: Distribution Visualization...]")
ax1 = sns.histplot(df['total_bill'], kde=True, bins=25)
ax1.set_title('Distribution of total_bill')
ax1.figure.savefig('task1_dist.png', dpi=120, bbox_inches='tight')

skew_val = df['total_bill'].skew()
print(f"Skewness of total_bill: {skew_val:.2f}")
print("Observed Shape: Unimodal, right-skewed with a prominent right tail extending to ~50.")


# -------------------------------------------------------------
# TASK 2: Implementing the IQR Rule
# Theory: Quartile boundaries remain robust against extreme values.
# -------------------------------------------------------------
print("\n[Executing Task 2: IQR Outlier Detection...]")
col = df['total_bill']
q1 = col.quantile(0.25)
q3 = col.quantile(0.75)
iqr = q3 - q1

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

iqr_outliers = df[(col < lower_bound) | (col > upper_bound)]

print(f"Q1: {q1:.2f}, Q3: {q3:.2f}, IQR: {iqr:.2f}")
print(f"Bounds: [{lower_bound:.2f}, {upper_bound:.2f}]")
print(f"Total IQR Outliers Flagged: {len(iqr_outliers)}")
print(iqr_outliers[['total_bill', 'tip']].to_string(index=True))


# -------------------------------------------------------------
# TASK 3: Z-Score Outlier Detection
# Theory: |z| > 3 flags points over 3 standard deviations from the mean.
# -------------------------------------------------------------
print("\n[Executing Task 3: Z-Score Outlier Detection...]")
mean_val = col.mean()
std_val = col.std()
z_scores = (col - mean_val) / std_val

z_outliers = df[np.abs(z_scores) > 3]

print(f"Mean: {mean_val:.2f}, Std: {std_val:.2f}")
print(f"Records where |z| > 3 (Total: {len(z_outliers)}):")
print(z_outliers[['total_bill', 'tip']].to_string(index=True))


# -------------------------------------------------------------
# TASK 4: Outlier Investigation and Decision
# Theory: Distinguish between data entry errors and genuine signals.
# -------------------------------------------------------------
print("\n[Executing Task 4: Outlier Decision...]")
selected_outlier_idx = 170
selected_bill = df.loc[selected_outlier_idx, 'total_bill']
selected_tip = df.loc[selected_outlier_idx, 'tip']

print(f"Selected Outlier: Index {selected_outlier_idx} (total_bill = {selected_bill}, tip = {selected_tip})")
print("Decision: SIGNAL (Keep)")
print("Reasoning: A $50.81 bill with a $10.00 tip represents legitimate high-end dining spend.")

print("\n" + "=" * 65)
print("ALL TASKS COMPLETED SUCCESSFULLY.")
print("=" * 65)



"""
================================================================================
MUET Cyber Learning Portal - Data Science and Analytics Lab V
Topic: Correlation and Feature Relationships

SHORT THEORY NOTES:
1. Pearson Correlation Matrix (df.corr()):
   - Measures linear association between numeric variables from -1 to +1.
   - Values near +1 indicate a strong direct relationship; near -1 indicate a strong inverse relationship.
   - Useful for pinpointing candidate predictors for a target variable.

2. Multicollinearity:
   - Occurs when two or more independent predictors correlate strongly with each other (e.g., total_bill and size, r ~ 0.60).
   - In linear regression models, multicollinearity can inflate coefficient variance and make weights unstable.

3. Pearson r Only Measures Straight Lines:
   - A correlation coefficient of ~0 does NOT mean there is no relationship; it only means there is no LINEAR relationship.
   - Non-linear relationships (e.g., parabolas, U-curves) can have r = 0 while being completely deterministic.
   - Always inspect scatter plots alongside correlation numbers (the Anscombe lesson).

4. Categorical Comparisons & Confounders:
   - Group differences (e.g., smoker vs. non-smoker) can easily be confounded by lurking variables (e.g., party size, time).
   - Correlation does not imply causation; never conclude group status causes an outcome without controlling for confounders.
================================================================================
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

print("=" * 65)
print("RUNNING LAB V: CORRELATION AND FEATURE RELATIONSHIPS")
print("=" * 65)

# Load dataset and prepare derived feature
df = sns.load_dataset('tips')
df['tip_pct'] = df['tip'] / df['total_bill'] * 100


# -------------------------------------------------------------
# TASK 1: Compute Feature Correlation Matrix
# Theory: df.corr() highlights predictors linearly related to target.
# -------------------------------------------------------------
print("\n[Executing Task 1: Correlation Matrix...]")
corr_matrix = df[['total_bill', 'tip', 'size', 'tip_pct']].corr()
print("Correlation Matrix:")
print(corr_matrix.round(2))

strongest_pred = corr_matrix['tip'].drop('tip').abs().idxmax()
strongest_r = corr_matrix.loc['tip', strongest_pred]
print(f"Strongest linear correlation with target 'tip': {strongest_pred} (r = {strongest_r:.2f})")


# -------------------------------------------------------------
# TASK 2: Detecting Multicollinearity
# Theory: Strong predictor-to-predictor correlations destabilize regression.
# -------------------------------------------------------------
print("\n[Executing Task 2: Multicollinearity Check...]")
r_pred = df['total_bill'].corr(df['size'])
print(f"Predictor pair: total_bill and size")
print(f"Correlation coefficient: {r_pred:.4f}")


# -------------------------------------------------------------
# TASK 3: Linearity Validation via Scatter Plot
# Theory: Pearson r misses curves; scatter plots verify linear assumptions.
# -------------------------------------------------------------
print("\n[Executing Task 3: Non-Linearity Check...]")
np.random.seed(42)
x_curve = np.linspace(-5, 5, 100)
y_curve = x_curve**2
r_curve = np.corrcoef(x_curve, y_curve)[0, 1]

fig3, ax3 = plt.subplots()
ax3.scatter(x_curve, y_curve, color='tab:blue', alpha=0.7)
ax3.set_title(f'Non-Linear U-Shape (r = {r_curve:.4f})')
ax3.set_xlabel('X')
ax3.set_ylabel('Y = X^2')

fig3.savefig('task3_scatter.png', dpi=120, bbox_inches='tight')
plt.close(fig3)

print(f"Correlation of X and X^2: {r_curve:.4f}")
print("Saved 'task3_scatter.png'. Scatter plot confirms strong non-linear pattern despite r ~ 0.")


# -------------------------------------------------------------
# TASK 4: Categorical Comparison Analysis
# Theory: Grouped metrics identify baseline variations across categories.
# -------------------------------------------------------------
print("\n[Executing Task 4: Categorical Comparison...]")
grouped_summary = df.groupby('smoker', observed=False)['tip_pct'].describe()
print("Summary of tip_pct by smoker:")
print(grouped_summary.round(2))


# -------------------------------------------------------------
# TASK 5: Confounder Check Demonstration
# Theory: Check for lurking variables that correlate with group splits.
# -------------------------------------------------------------
print("\n[Executing Task 5: Confounder Check...]")
bill_by_smoker = df.groupby('smoker', observed=False)['total_bill'].mean()
size_by_smoker = df.groupby('smoker', observed=False)['size'].mean()
print("Mean total_bill by smoker:")
print(bill_by_smoker.round(2))
print("Mean party size by smoker:")
print(size_by_smoker.round(2))

print("\n" + "=" * 65)
print("ALL 5 TASKS EXECUTED SUCCESSFULLY.")
print("=" * 65)