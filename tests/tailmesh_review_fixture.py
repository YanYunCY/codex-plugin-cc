"""Intentional static-review fixture; never execute this file."""
import subprocess


def run_user_input(user_value: str) -> None:
    # INTENTIONAL REVIEW FINDING: shell injection risk for untrusted input.
    subprocess.run("echo " + user_value, shell=True, check=True)
