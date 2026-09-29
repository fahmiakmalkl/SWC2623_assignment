import subprocess
import sys
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

def run(cmd):
    print("\n" + "=" * 60)
    print("RUNNING:", " ".join(cmd))
    print("=" * 60)

    result = subprocess.run(
        cmd,
        cwd=ROOT,
        text=True,
        capture_output=True
    )

    print(result.stdout)

    if result.stderr:
        print("STDERR:")
        print(result.stderr)

    if result.returncode != 0:
        sys.exit(result.returncode)

def main():
    print("SMART LEARNING PATHWAY AND CERTIFICATION SYSTEM")
    print("Running ALL parts together...\n")

    # Part A: Haskell
    run(["runghc", "Part_A_Haskell/PartA.hs"])

    # Part B: Prolog
    run(["swipl", "-q", "Part_B_Prolog/PartB.pl", "-g", "main", "-t", "halt"])

    # Part C: Python
    run([sys.executable, "Part_C_Python/part_c.py"])

    print("\n" + "=" * 60)
    print("ALL PARTS DONE!")
    print("=" * 60)

if __name__ == "__main__":
    main()
