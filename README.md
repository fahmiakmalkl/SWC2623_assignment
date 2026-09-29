# SWC2623 Coursework 2: Smart Learning Pathway and Certification System

This repository contains the group assignment for SWC2623, implementing the "Smart Learning Pathway and Certification System" using three different programming paradigms:
- Part A: Functional Programming (Haskell)
- Part B: Logic Programming (Prolog)
- Part C: Multi-Paradigm Programming (Python)

## Group Members
1. MUHAMMAD FAUZAAN BIN NAZRUDDIN (AM2512021170)
2. DANIAL AMIR ASYRAF BIN SAIFUDDIN (AM2512021021)
3. MUHAMMAD FAHMI AKMAL BIN MOHD ZIN (AM2512021804)

## Project Structure
Part_A_Haskell/PartA.hs
Part_B_Prolog/PartB.pl
Part_C_Python/part_c.py
run_all.py
README.md

## Environment Setup (How to install the required software)

You MUST install the required software before running the project. We have provided a Devcontainer configuration that automatically installs everything for you.

### Option 1: GitHub Codespaces (Auto-Install)
If you are opening this repository in GitHub Codespaces, the environment will automatically install Haskell (GHC), SWI-Prolog, and Python (pandas) using the provided .devcontainer/devcontainer.json file. 

If it does not automatically install, open the terminal in Codespaces and run this command manually:
sudo apt-get update && sudo apt-get install -y ghc swi-prolog && pip install pandas

### Option 2: Local Machine (Manual Install)
If you are running this on your own computer, you must install the following:

1. Python 3.8+ and Pandas:
   Run this in your terminal: pip install pandas

2. SWI-Prolog:
   Download from: https://www.swi-prolog.org/Download.html
   Ensure 'swipl' is added to your system PATH.

3. Haskell (GHC):
   Download from: https://www.haskell.org/downloads/
   Ensure 'runghc' is available in your terminal.

## How to Run All Parts
We have provided a master script (run_all.py) that automatically runs Part A (Haskell), Part B (Prolog), and Part C (Python) sequentially.

1. Open your terminal in the root folder.
2. Run the master script:
   python run_all.py
3. The terminal will display the outputs for all three parts one after another.

## How to Run Individual Parts
If you wish to run a specific part independently, use the following commands:

Part A: Haskell
runghc Part_A_Haskell/PartA.hs

Part B: Prolog
swipl -q Part_B_Prolog/PartB.pl -g main -t halt

Part C: Python
python Part_C_Python/part_c.py

## Notes on Data Consistency
All three parts use the exact same learner IDs (Ali, Siti, Ahmad, Nur, Danial) and module names to ensure a valid comparison across paradigms. The primary goal of Part C was to demonstrate Python's multi-paradigm capabilities (Object-Oriented and Functional Programming) rather than perfectly matching the score distributions from Part A.
