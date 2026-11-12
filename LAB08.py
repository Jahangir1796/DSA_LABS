# """
# ================================================================================
# MUET Cyber Learning Portal - Data Science and Analytics Lab VIII
# Topic: Version Control with Git - Concepts and Setup

# SHORT THEORY NOTES:
# 1. Version Control Mental Model:
#    - Replaces manual messy copies (e.g., report_final_v2_final.ipynb) with a single
#      repository tracking an immutable, chronological history of changes.
#    - Commits are complete project snapshots, not isolated diff fragments.
#    - Every commit pairs an SHA hash, timestamp, author signature, and descriptive intent.

# 2. Git Configuration & Repository Setup:
#    - git config --global sets user.name and user.email to sign each commit snapshot.
#    - git init creates a hidden .git directory storing object databases and refs.

# 3. Reproducibility in Data Science:
#    - A reproducible analysis requires pinning the exact code state that produced a result.
#    - The commit hash acts as a permanent fingerprint verifying which model/data script was run.
#    - Best Practice Exclusion: Version notebooks, scripts, and requirements.txt. Keep 
#      massive raw datasets (GBs), binary caches, and secret credentials out of the repo.
# ================================================================================
# """

# import subprocess
# import os

# print("=" * 65)
# print("RUNNING LAB VIII: GIT VERSION CONTROL CONCEPTS AND SETUP")
# print("=" * 65)


# def run_command(cmd, cwd=None):
#     """Executes shell command safely and prints formatted stdout."""
#     res = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)
#     if res.stdout.strip():
#         print(res.stdout.strip())
#     if res.stderr.strip():
#         print(res.stderr.strip())
#     return res


# # -------------------------------------------------------------
# # TASK 1: Configure Git User Identity
# # Theory: Every commit binds author identity globally.
# # -------------------------------------------------------------
# print("\n[Executing Task 1: Global Identity Configuration...]")
# run_command('git config --global user.name "Jahangir"')
# run_command('git config --global user.email "23bscys034@student.muet.edu.pk"')
# run_command('git config --global init.defaultBranch main')

# print("Config verification:")
# run_command('git config --list')


# # -------------------------------------------------------------
# # TASK 2: Initialize a Local Repository
# # Theory: git init establishes the local .git directory database.
# # -------------------------------------------------------------
# repo_dir = os.path.join(os.getcwd(), 'ds_analysis')
# os.makedirs(repo_dir, exist_ok=True)
# print(f"\n[Executing Task 2: Repository Initialization in {repo_dir}...]")
# run_command('git init', cwd=repo_dir)


# # -------------------------------------------------------------
# # TASK 3: Create a Project Snapshot
# # Theory: Stage (git add) and freeze state (git commit) with clear intent.
# # -------------------------------------------------------------
# print("\n[Executing Task 3: Baseline Commit Snapshot...]")
# txt_file = os.path.join(repo_dir, 'analysis.txt')
# with open(txt_file, 'w') as f:
#     f.write("Baseline dataset summary: 244 records loaded.\n")

# run_command('git add analysis.txt', cwd=repo_dir)
# run_command('git commit -m "Initial commit: create baseline data summary"', cwd=repo_dir)


# # -------------------------------------------------------------
# # TASK 4: Simulate Versioning for Reproducibility
# # Theory: Subsequent commit tracking evolutionary analysis iterations.
# # -------------------------------------------------------------
# print("\n[Executing Task 4: Incremental Commit Snapshot...]")
# with open(txt_file, 'a') as f:
#     f.write("Updated summary: removed 4 outliers using IQR rule.\n")

# run_command('git add analysis.txt', cwd=repo_dir)
# run_command('git commit -m "Update analysis: apply IQR outlier filtering"', cwd=repo_dir)

# print("\nFull Git History Log:")
# run_command('git log --oneline', cwd=repo_dir)

# print("\n" + "=" * 65)
# print("ALL 5 TASKS EXECUTED AND LOGGED SUCCESSFULLY.")
# print("=" * 65)


"""
================================================================================
MUET Cyber Learning Portal - Data Science and Analytics Lab VIII
Topic: The Everyday Git Loop

SHORT THEORY NOTES:
1. The Three Git Areas:
   - Working Directory: The actual project directory where files are created/edited.
   - Staging Area (Index): Intermediate staging zone where selected changes are prepared via 'git add'.
   - Repository: Permanent committed history secured as snapshots using 'git commit'.

2. The Critical Role of .gitignore:
   - Tells Git which patterns (*.csv, data/, .env, __pycache__/) to permanently ignore.
   - Must be written BEFORE the first commit because Git only ignores untracked files.
   - Once a file is committed, it remains inside Git history even if later deleted.

3. Commit Messages and Remote Synchronization:
   - Commits should use the imperative mood ("Add feature X", not "added" or "stuff").
   - 'git remote add origin <url>' connects the local repository to GitHub.
   - 'git push -u origin main' uploads snapshots for backup and collaboration.
================================================================================
"""

import os
import subprocess

print("=" * 65)
print("RUNNING LAB VIII: THE EVERYDAY GIT LOOP")
print("=" * 65)

def exec_cmd(cmd, cwd=None):
    """Utility function to run and print shell command execution."""
    print(f"\n$ {cmd}")
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)
    if res.stdout.strip():
        print(res.stdout.strip())
    if res.stderr.strip():
        print(res.stderr.strip())
    return res

# -------------------------------------------------------------
# TASK 1: Initialize Repository and Ignore Files
# Theory: Initialize repo and write .gitignore before staging files.
# -------------------------------------------------------------
project_dir = os.path.join(os.getcwd(), 'dsa-practice')
os.makedirs(project_dir, exist_ok=True)

exec_cmd('git init', cwd=project_dir)

# Create .gitignore to block data files and CSVs
gitignore_path = os.path.join(project_dir, '.gitignore')
with open(gitignore_path, 'w') as f:
    f.write("data/\n*.csv\n")

# Create test data files that should be ignored
os.makedirs(os.path.join(project_dir, 'data'), exist_ok=True)
with open(os.path.join(project_dir, 'sample.csv'), 'w') as f:
    f.write("id,val\n1,10\n")
with open(os.path.join(project_dir, 'data', 'raw.txt'), 'w') as f:
    f.write("raw uncleaned text\n")

print("--- TASK 1 STATUS OUTPUT (verifying ignored files) ---")
exec_cmd('git status', cwd=project_dir)


# -------------------------------------------------------------
# TASK 2: Manage the Staging Area
# Theory: Selective staging using 'git add' isolates atomic changes.
# -------------------------------------------------------------
with open(os.path.join(project_dir, 'feature_a.txt'), 'w') as f:
    f.write("Implementation details for feature A.\n")
with open(os.path.join(project_dir, 'feature_b.txt'), 'w') as f:
    f.write("Implementation details for feature B.\n")

exec_cmd('git add feature_a.txt', cwd=project_dir)

print("--- TASK 2 STATUS OUTPUT (one staged, others untracked) ---")
exec_cmd('git status', cwd=project_dir)


# -------------------------------------------------------------
# TASK 3: Create a Meaningful Commit
# Theory: Group staged changes into a labeled commit snapshot.
# -------------------------------------------------------------
exec_cmd('git add .gitignore feature_b.txt', cwd=project_dir)
exec_cmd('git commit -m "Add feature components and configure gitignore"', cwd=project_dir)

print("--- TASK 3 COMMIT LOG ---")
exec_cmd('git log -n 1', cwd=project_dir)


# -------------------------------------------------------------
# TASK 4: Connect and Push to Remote
# Theory: Establish remote tracking origin and push local main branch.
# -------------------------------------------------------------
print("--- TASK 4 REMOTE CONFIGURATION SYNTAX ---")
print("$ git remote add origin https://github.com/jahangir-muet/dsa-practice.git")
print("$ git branch -M main")
print("$ git push -u origin main")

print("\n" + "=" * 65)
print("ALL TASKS EXECUTED SUCCESSFULLY.")
print("=" * 65)