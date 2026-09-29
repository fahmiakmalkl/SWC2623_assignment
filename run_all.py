import subprocess
import sys
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

def run(cmd):
    print("\n" + "=" * 60)
    print("RUNNING:", " ".join(cmd))
    print("=" * 60)

    try:
        # 15 second timeout so it never hangs forever
        result = subprocess.run(
            cmd,
            cwd=ROOT,
            text=True,
            capture_output=True,
            timeout=15
        )

        # Print standard output if there is any
        if result.stdout.strip():
            print(result.stdout)
        else:
            print("[No standard output received. Check for syntax errors.]")

        # Print standard error if there is any
        if result.stderr.strip():
            print("STDERR:")
            print(result.stderr)

    except subprocess.TimeoutExpired:
        print("\n[ERROR] Prolog timed out! It is likely waiting for input.")
        print("Check that your .pl file ends with a period (.)")
        print("Moving to Part C...\n")
    except Exception as e:
        print(f"\n[ERROR] {e}\n")

def main():
    print("SMART LEARNING PATHWAY AND CERTIFICATION SYSTEM")
    print("Running ALL parts together...\n")

    # Part A: Haskell
    run(["runghc", "Part_A_Haskell/PartA.hs"])

    # Part B: Prolog (Using -s to load, -g to run main and halt)
    run(["swipl", "-q", "-s", "Part_B_Prolog/PartB.pl", "-g", "main, halt"])

    # Part C: Python
    run([sys.executable, "Part_C_Python/PartC.py"])

    print("\n" + "=" * 60)
    print("ALL PARTS DONE!")
    print("=" * 60)

if __name__ == "__main__":
    main()
