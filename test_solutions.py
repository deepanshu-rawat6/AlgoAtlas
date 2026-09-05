"""
Test harness for all DSA solutions.

Discovers every solution file (solution.py, solution.cpp, Solution.java) under
the pattern folders and executes it. Python files run directly; C++ files are
compiled with g++ then run; Java files are compiled with javac then run.
A solution passes when it exits with status 0. Files that contain assert-based
self-tests in their main block are therefore fully verified.

Run with:  pytest -q
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).parent
# Directories that are not part of the solution set.
EXCLUDED_PARTS = {"website", "node_modules", "__pycache__", ".git"}


def _discover_solution_files() -> list[Path]:
    globs = ["solution.py", "solution.cpp", "Solution.java"]
    files = [
        p
        for pattern in globs
        for p in REPO_ROOT.rglob(pattern)
        if not EXCLUDED_PARTS.intersection(p.parts)
    ]
    return sorted(files)


SOLUTION_FILES = _discover_solution_files()


def _test_id(path: Path) -> str:
    # e.g. arrays_and_hashing/two_sum/py
    rel = path.relative_to(REPO_ROOT)
    parts = rel.parts
    pattern = parts[0]
    problem = parts[-2]
    lang = path.suffix.lstrip(".")
    return f"{pattern}/{problem}/{lang}"


@pytest.mark.parametrize(
    "solution_file", SOLUTION_FILES, ids=[_test_id(p) for p in SOLUTION_FILES]
)
def test_solution_runs(solution_file: Path) -> None:
    """Each solution must compile (if needed) and run with exit code 0."""
    ext = solution_file.suffix

    if ext == ".py":
        result = subprocess.run(
            [sys.executable, str(solution_file)],
            capture_output=True,
            text=True,
            timeout=60,
        )

    elif ext == ".cpp":
        if not shutil.which("g++"):
            pytest.skip("g++ not found")
        tmpdir = tempfile.mkdtemp()
        try:
            binary = Path(tmpdir) / "solution"
            compile_res = subprocess.run(
                ["g++", "-std=c++17", "-o", str(binary), str(solution_file)],
                capture_output=True,
                text=True,
                timeout=30,
            )
            assert compile_res.returncode == 0, (
                f"Compilation failed:\n{compile_res.stderr}"
            )
            result = subprocess.run(
                [str(binary)],
                capture_output=True,
                text=True,
                timeout=60,
            )
        finally:
            shutil.rmtree(tmpdir, ignore_errors=True)

    elif ext == ".java":
        if not shutil.which("javac"):
            pytest.skip("javac not found")
        tmpdir = tempfile.mkdtemp()
        try:
            compile_res = subprocess.run(
                ["javac", "-d", tmpdir, str(solution_file)],
                capture_output=True,
                text=True,
                timeout=30,
            )
            assert compile_res.returncode == 0, (
                f"Compilation failed:\n{compile_res.stderr}"
            )
            result = subprocess.run(
                ["java", "-ea", "-cp", tmpdir, "Solution"],
                capture_output=True,
                text=True,
                timeout=60,
            )
        finally:
            shutil.rmtree(tmpdir, ignore_errors=True)

    else:
        pytest.skip(f"Unknown extension: {ext}")
        return

    assert result.returncode == 0, (
        f"{solution_file} exited with {result.returncode}\n"
        f"--- stdout ---\n{result.stdout}\n--- stderr ---\n{result.stderr}"
    )


def test_solution_files_discovered() -> None:
    """Guard against the discovery glob silently matching nothing."""
    assert len(SOLUTION_FILES) > 0, "No solution files were discovered"
