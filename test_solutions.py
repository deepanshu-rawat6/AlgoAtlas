"""
Test harness for all DSA solutions.

Discovers every ``solution.py`` under the pattern folders and executes it as a
subprocess. A solution passes when it exits with status 0. Files that contain
``assert``-based self-tests in their ``if __name__ == "__main__":`` block are
therefore fully verified; files without asserts are checked for runtime errors.

Run with:  pytest -q
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent
# Directories that are not part of the Python solution set.
EXCLUDED_PARTS = {"website", "node_modules", "__pycache__", ".git"}


def _discover_solution_files() -> list[Path]:
    files = [
        p
        for p in REPO_ROOT.rglob("solution.py")
        if not EXCLUDED_PARTS.intersection(p.parts)
    ]
    return sorted(files)


SOLUTION_FILES = _discover_solution_files()


def _test_id(path: Path) -> str:
    # e.g. arrays_and_hashing/two_sum
    rel = path.relative_to(REPO_ROOT)
    parts = rel.parts
    pattern = parts[0]
    problem = parts[-2]  # the problem folder name
    return f"{pattern}/{problem}"


import pytest


@pytest.mark.parametrize("solution_file", SOLUTION_FILES, ids=[_test_id(p) for p in SOLUTION_FILES])
def test_solution_runs(solution_file: Path) -> None:
    """Each solution file must execute (and pass its self-tests) with exit code 0."""
    result = subprocess.run(
        [sys.executable, str(solution_file)],
        capture_output=True,
        text=True,
        timeout=60,
    )
    assert result.returncode == 0, (
        f"{solution_file} exited with {result.returncode}\n"
        f"--- stdout ---\n{result.stdout}\n--- stderr ---\n{result.stderr}"
    )


def test_solution_files_discovered() -> None:
    """Guard against the discovery glob silently matching nothing."""
    assert len(SOLUTION_FILES) > 0, "No solution.py files were discovered"
