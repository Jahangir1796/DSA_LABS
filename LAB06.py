"""
================================================================================
MUET Cyber Learning Portal - Data Science and Analytics Lab VI
Topic: The Train/Test Split and a First Model

SHORT THEORY NOTES:
1. Train/Test Split First:
   - Always hold out a test set before preprocessing or modeling.
   - Setting 'random_state' ensures deterministic, reproducible partition splits.
   - The test set acts as an honest surrogate for unseen real-world production data.

2. Scikit-learn Uniform API:
   - Estimator interface standard: model.fit(X_train, y_train) learns weights/rules.
   - Prediction standard: model.predict(X_test) executes inference on new inputs.
   - Common interface allows swapping model architectures with a one-line constructor change.

3. Data Leakage and the Pipeline Architecture:
   - Leaky Workflow: Scaling the whole dataset (X_all) uses test distributions (mean/std).
   - Leak-Free Workflow: StandardScaler must fit ONLY on X_train, then transform both sets.
   - make_pipeline(StandardScaler(), Estimator()) structurally guarantees the scaler 
     learns only from the training fold during pipeline.fit(), eliminating leakage bugs.
================================================================================
"""

from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, r2_score

print("=" * 65)
print("RUNNING LAB VI: THE TRAIN/TEST SPLIT AND A FIRST MODEL")
print("=" * 65)

# Generate synthetic dataset for reproducible experimentation
X, y = make_regression(n_samples=200, n_features=3, noise=10, random_state=0)


# -------------------------------------------------------------
# TASK 1: Implement a Reproducible Train/Test Split
# Theory: Split before touching data; random_state preserves partition layout.
# -------------------------------------------------------------
print("\n[Executing Task 1: Train/Test Split...]")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

print("--- TASK 1 OUTPUT ---")
print(f"X_train shape: {X_train.shape}")
print(f"X_test shape: {X_test.shape}")


# -------------------------------------------------------------
# TASK 2: Basic Model Fit and Predict Cycle
# Theory: Standard fit(train) and predict(test) lifecycle.
# -------------------------------------------------------------
print("\n[Executing Task 2: LinearRegression Fit and Predict...]")
model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("--- TASK 2 OUTPUT ---")
print(f"First five predictions: {predictions[:5].round(2).tolist()}")
print(f"Test Set MAE: {mean_absolute_error(y_test, predictions):.2f}")
print(f"Test Set R^2: {r2_score(y_test, predictions):.3f}")


# -------------------------------------------------------------
# TASK 3: Construct a Leak-Free Scaling Pipeline
# Theory: Pipeline confines scaler fitting exclusively to X_train.
# -------------------------------------------------------------
print("\n[Executing Task 3: Pipeline with StandardScaler & LinearRegression...]")
pipe_linear = make_pipeline(StandardScaler(), LinearRegression())
pipe_linear.fit(X_train, y_train)

pipe_preds = pipe_linear.predict(X_test)
extracted_coefs = pipe_linear.named_steps['linearregression'].coef_

print("--- TASK 3 OUTPUT ---")
print(f"Model coefficients: {extracted_coefs.round(2).tolist()}")
print(f"Pipeline Test R^2: {r2_score(y_test, pipe_preds):.3f}")


# -------------------------------------------------------------
# TASK 4: Algorithm Swapping via Uniform API
# Theory: Swapping estimators requires altering only the constructor.
# -------------------------------------------------------------
print("\n[Executing Task 4: Estimator Swap to DecisionTreeRegressor...]")
pipe_tree = make_pipeline(StandardScaler(), DecisionTreeRegressor(random_state=42))

# Exactly the same fit and predict calls
pipe_tree.fit(X_train, y_train)
tree_preds = pipe_tree.predict(X_test)

print("--- TASK 4 OUTPUT ---")
print(f"First five DecisionTreeRegressor predictions: {tree_preds[:5].round(2).tolist()}")
print(f"DecisionTree Test R^2: {r2_score(y_test, tree_preds):.3f}")

print("\n" + "=" * 65)
print("ALL 5 TASKS EXECUTED SUCCESSFULLY.")
print("=" * 65)

"""
================================================================================
MUET Cyber Learning Portal - Data Science and Analytics Lab VI
Topic: Classification: KNN, Decision Trees and Logistic Regression

SHORT THEORY NOTES:
1. Classification Core:
   - Predicts discrete class labels rather than continuous numerical quantities.
   - predict(): Outputs final predicted class label (0 or 1).
   - predict_proba(): Outputs the underlying probability distribution per class.
   - Having probability estimates allows moving decision thresholds to tune precision/recall.

2. Three Decision Mechanisms:
   - K-Nearest Neighbors (KNN): Classifies by majority vote of the k closest neighbors (distance-based, scale-sensitive).
   - Decision Tree: Carves the feature space using orthogonal, axis-aligned yes/no splits (highly interpretable).
   - Logistic Regression: Passes a linear weighted combination of features through a sigmoid S-curve.

3. Complexity and Overfitting Knobs:
   - KNN with k=1 memorizes training data (100% train accuracy), while large k increases bias and underfits.
   - Decision Tree with max_depth=None grows without bounds, memorizing noise and overfitting (100% train accuracy).
   - Low depth (e.g., max_depth=1) acts as a decision stump, risking underfitting.
   - Always tune complexity knobs by evaluating on held-out test data, never on training scores.
================================================================================
"""

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

print("=" * 65)
print("RUNNING LAB VI: CLASSIFICATION (KNN, DECISION TREES, LOGISTIC REGRESSION)")
print("=" * 65)

# Generate synthetic binary classification dataset
X, y = make_classification(n_samples=300, n_features=5, random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=0)


# -------------------------------------------------------------
# TASK 1: Basic Classifier Implementation
# Theory: Standard fit/predict pipeline for classification targets.
# -------------------------------------------------------------
print("\n[Executing Task 1: Logistic Regression Class Labels...]")
clf = LogisticRegression(max_iter=1000)
clf.fit(X_train, y_train)

predicted_labels = clf.predict(X_test)
print(f"Predicted labels count: {len(predicted_labels)}")
print(f"First 10 predicted labels: {predicted_labels[:10].tolist()}")


# -------------------------------------------------------------
# TASK 2: Extracting Prediction Probabilities
# Theory: predict_proba() exposes probabilities for threshold tuning.
# -------------------------------------------------------------
print("\n[Executing Task 2: Prediction Probabilities...]")
probs_first_five = clf.predict_proba(X_test[:5])
print("Probabilities for first 5 test samples [P(Class 0), P(Class 1)]:")
print(probs_first_five.round(4).tolist())


# -------------------------------------------------------------
# TASK 3: KNN Complexity Adjustment
# Theory: k=1 overfits by memorizing; large k averages wide neighborhoods.
# -------------------------------------------------------------
print("\n[Executing Task 3: KNN Complexity Adjustment...]")
knn_k1 = KNeighborsClassifier(n_neighbors=1).fit(X_train, y_train)
knn_k100 = KNeighborsClassifier(n_neighbors=100).fit(X_train, y_train)

acc_k1 = knn_k1.score(X_train, y_train)
acc_k100 = knn_k100.score(X_train, y_train)

print(f"KNN (k=1) Training Accuracy:   {acc_k1:.4f}")
print(f"KNN (k=100) Training Accuracy: {acc_k100:.4f}")


# -------------------------------------------------------------
# TASK 4: Decision Tree Depth Control
# Theory: max_depth controls complexity; unrestricted depth causes overfitting.
# -------------------------------------------------------------
print("\n[Executing Task 4: Decision Tree Depth Control...]")
tree_shallow = DecisionTreeClassifier(max_depth=1, random_state=0).fit(X_train, y_train)
tree_unlimited = DecisionTreeClassifier(max_depth=None, random_state=0).fit(X_train, y_train)

acc_shallow = tree_shallow.score(X_train, y_train)
acc_unlimited = tree_unlimited.score(X_train, y_train)

print(f"Tree (max_depth=1) Training Accuracy:    {acc_shallow:.4f}")
print(f"Tree (max_depth=None) Training Accuracy: {acc_unlimited:.4f}")

print("\n" + "=" * 65)
print("ALL 5 TASKS EXECUTED SUCCESSFULLY.")
print("=" * 65)

"""
================================================================================
MUET Cyber Learning Portal - Data Science and Analytics Lab VI
Topic: Evaluation in Practice: Confusion Matrix and the Right Metrics

SHORT THEORY NOTES:
1. The Confusion Matrix & Classification Report:
   - Confusion Matrix maps four outcomes: True Negative (TN), False Positive (FP),
     False Negative (FN), and True Positive (TP).
   - classification_report provides precision, recall, and F1-score per class.
   - Precision = TP / (TP + FP): Measures correctness of positive alarms.
   - Recall = TP / (TP + FN): Measures how many real positive cases were caught.
   - F1-Score = Harmonic mean of Precision and Recall.

2. The Imbalanced Data Trap:
   - On imbalanced datasets (e.g., 97% normal, 3% fraud), accuracy is dominated
     by the majority class. A model that predicts majority every time achieves 97%
     accuracy with 0% minority recall.
   - For honest evaluation on imbalanced data, optimize and score using 'f1' or 'recall'.

3. Leak-Free Cross-Validation via Pipeline:
   - A single train/test split can yield lucky or unlucky partitions.
   - cross_val_score averages performance across k independent folds.
   - Placing a StandardScaler inside make_pipeline within cross_val_score guarantees
     the scaler is fit ONLY on each fold's training portion, eliminating test-leakage.
================================================================================
"""

from sklearn.datasets import make_classification
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score

print("=" * 65)
print("RUNNING LAB VI: EVALUATION IN PRACTICE (CONFUSION MATRIX & METRICS)")
print("=" * 65)


# -------------------------------------------------------------
# TASK 1: Generate a Classification Report
# Theory: Generates precision, recall, and F1 across each discrete class.
# -------------------------------------------------------------
print("\n[Executing Task 1: Classification Report...]")
y_true_1 = [0, 1, 0, 1, 0]
y_pred_1 = [0, 0, 0, 1, 0]

print("--- TASK 1 OUTPUT ---")
print(classification_report(y_true_1, y_pred_1))


# -------------------------------------------------------------
# TASK 2: Compute a Confusion Matrix
# Theory: Maps TN, FP, FN, and TP in a 2D matrix structure.
# -------------------------------------------------------------
print("\n[Executing Task 2: Confusion Matrix...]")
y_true_2 = [1, 0, 1, 1, 0, 1]
y_pred_2 = [1, 1, 1, 0, 0, 1]

cm = confusion_matrix(y_true_2, y_pred_2)
print("--- TASK 2 OUTPUT ---")
print("Confusion Matrix:")
print(cm)


# -------------------------------------------------------------
# TASK 3: Cross-Validation with Custom Scoring
# Theory: Evaluates performance using F1 rather than misleading accuracy.
# -------------------------------------------------------------
print("\n[Executing Task 3: Cross-Validation with scoring='f1'...]")
X_synth, y_synth = make_classification(n_samples=200, n_features=5, random_state=42)
rf_model = RandomForestClassifier(random_state=42)

f1_cv = cross_val_score(rf_model, X_synth, y_synth, cv=5, scoring='f1')

print("--- TASK 3 OUTPUT ---")
print(f"F1 Scores per fold: {f1_cv.round(4).tolist()}")
print(f"Mean F1 Score: {f1_cv.mean():.4f}")


# -------------------------------------------------------------
# TASK 4: Leak-Free Evaluation with Pipelines
# Theory: StandardScaler inside pipeline ensures fold-level fitting without leakage.
# -------------------------------------------------------------
print("\n[Executing Task 4: Leak-Free Pipeline inside cross_val_score...]")
X_imb, y_imb = make_classification(n_samples=300, n_features=6, weights=[0.8], random_state=42)

leak_free_pipe = make_pipeline(StandardScaler(), KNeighborsClassifier())
pipe_scores = cross_val_score(leak_free_pipe, X_imb, y_imb, cv=5, scoring='f1')

print("--- TASK 4 OUTPUT ---")
print(f"Pipeline Cross-Validation F1 Scores: {pipe_scores.round(4).tolist()}")
print(f"Pipeline Mean F1 Score: {pipe_scores.mean():.4f}")

print("\n" + "=" * 65)
print("ALL 5 TASKS EXECUTED SUCCESSFULLY.")
print("=" * 65)