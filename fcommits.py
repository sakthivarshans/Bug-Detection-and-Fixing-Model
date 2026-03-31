import os
import random
import subprocess
from datetime import datetime, timedelta

# ================= CONFIG =================
REPO_PATH = r"D:\commit\calc\Bug-Detection-and-Fixing-Model"   # <- your local repo path (raw string for Windows)
FILE_NAME = "activity.txt"       # file to update

START_DATE = datetime(2025, 2, 14)
END_DATE = datetime.now()

MIN_COMMITS = 50
MAX_COMMITS = 100
# ========================================

def run_git(cmd, env=None):
    """Run a git command inside the repo and print output or error."""
    result = subprocess.run(cmd, cwd=REPO_PATH, shell=True, env=env,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print(f"Error running '{cmd}': {result.stderr}")
    else:
        print(result.stdout.strip())

def make_commit(commit_time):
    """Create a single commit at the specified datetime."""
    env = os.environ.copy()
    date_str = commit_time.strftime("%Y-%m-%d %H:%M:%S")
    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str

    file_path = os.path.join(REPO_PATH, FILE_NAME)

    # --- Force a real change for Git by appending a unique line
    unique_line = f"{date_str} | {random.randint(1000,9999)} | {os.urandom(8).hex()}\n"
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(unique_line)

    # --- Random commit messages
    messages = [
        "update logic", "fix bug", "improve code",
        "refactor", "minor changes", "cleanup",
        "optimize", "update file"
    ]
    msg = random.choice(messages)

    # --- Add file and commit
    run_git(f"git add {FILE_NAME}", env)
    run_git(f'git commit -m "{msg}"', env)

def main():
    current_date = START_DATE

    while current_date <= END_DATE:
        commits_today = random.randint(MIN_COMMITS, MAX_COMMITS)
        print(f"{current_date.date()} -> {commits_today} commits")

        for _ in range(commits_today):
            # Random time in the day
            rand_seconds = random.randint(0, 86399)
            commit_time = current_date + timedelta(seconds=rand_seconds)
            make_commit(commit_time)

        current_date += timedelta(days=1)

    # --- Push all commits to GitHub
    print("\n🚀 Pushing all commits to GitHub...")
    run_git("git push origin main")
    print("✅ Done!")

if __name__ == "__main__":
    main()