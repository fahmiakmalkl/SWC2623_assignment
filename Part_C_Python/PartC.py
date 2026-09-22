"""
SWC2623 - Part C: Multi-Paradigm Programming (Python)
Integrated Learner Dashboard
"""

from typing import List, Dict, Optional
from functools import reduce
import pandas as pd


# ============================================================
# Performance thresholds (documented)
# ============================================================
# >= 85  → Excellent
# >= 80  → High Achiever   (boundary)
# >= 70  → Good
# >= 50  → Satisfactory
# <  50  → Needs Improvement


# ============================================================
# Learner class (Object-Oriented)
# ============================================================
class Learner:
    def __init__(self, learner_id: str, name: str,
                 completed_modules: Optional[List[str]] = None,
                 scores: Optional[Dict[str, float]] = None):
      
        if not isinstance(learner_id, str) or learner_id.strip() == "":
            raise ValueError("learner_id must be a non-empty string")
        if not isinstance(name, str) or name.strip() == "":
            raise ValueError("name must be a non-empty string")

        self.learner_id = learner_id.strip()
        self.name = name.strip()

        if completed_modules is None:
            self.completed_modules = []
        else:
            self.completed_modules = list(completed_modules)

        if scores is None:
            self.scores = {}
        else:
            self.scores = dict(scores)

        # Check every score is valid (0 to 100)
        for module_name in self.scores:
            score = self.scores[module_name]
            if not isinstance(score, (int, float)):
                raise ValueError("Score must be a number")
            if score < 0 or score > 100:
                raise ValueError("Score must be between 0 and 100")

    def average_score(self) -> float:
        if len(self.scores) == 0:
            return 0.0

        total = 0.0
        count = 0
        for score in self.scores.values():
            total = total + score
            count = count + 1

        average = total / count
        return average

    def classify_performance(self) -> str:
        avg = self.average_score()

        if avg >= 85:
            return "Excellent"
        elif avg >= 80:
            return "High Achiever"
        elif avg >= 70:
            return "Good"
        elif avg >= 50:
            return "Satisfactory"
        else:
            return "Needs Improvement"


# ============================================================
# Create sample data
# ============================================================
def create_sample_learners() -> List[Learner]:
    learners = []

    ali = Learner(
        "L001", "Ali",
        ["programming", "database", "web_development",
         "object_oriented_programming", "data_structures", "software_project"],
        {"programming": 88, "database": 85, "web_development": 90,
         "object_oriented_programming": 92, "data_structures": 87,
         "software_project": 91}
    )
    learners.append(ali)

    siti = Learner(
        "L002", "Siti",
        ["programming", "database", "web_development"],
        {"programming": 78, "database": 82, "web_development": 75}
    )
    learners.append(siti)

    ahmad = Learner(
        "L003", "Ahmad",
        ["programming", "object_oriented_programming"],
        {"programming": 70, "object_oriented_programming": 68}
    )
    learners.append(ahmad)

    nur = Learner(
        "L004", "Nur",
        ["programming", "database", "object_oriented_programming", "data_structures"],
        {"programming": 95, "database": 88,
         "object_oriented_programming": 91, "data_structures": 89}
    )
    learners.append(nur)

    danial = Learner(
        "L005", "Danial",
        ["programming", "database"],
        {"programming": 65, "database": 72}
    )
    learners.append(danial)

    return learners


# ============================================================
# Functional-style operations
# ============================================================

def get_high_achievers(learners: List[Learner]) -> List[Learner]:
    """filter + lambda"""
    result = list(filter(lambda l: l.average_score() >= 80, learners))
    return result


def get_averages(learners: List[Learner]) -> List[float]:
    """map + lambda"""
    result = list(map(lambda l: l.average_score(), learners))
    return result


def rank_learners(learners: List[Learner]) -> List[Learner]:
    """sorted (higher-order function)"""
    result = sorted(learners, key=lambda l: l.average_score(), reverse=True)
    return result


def total_modules_completed(learners: List[Learner]) -> int:
    """reduce + lambda"""
    result = reduce(lambda acc, l: acc + len(l.completed_modules), learners, 0)
    return result


# ============================================================
# Pandas summary table
# ============================================================
def create_summary_dataframe(learners: List[Learner]) -> pd.DataFrame:
    records = []

    for l in learners:
        row = {
            "ID": l.learner_id,
            "Name": l.name,
            "Modules Completed": len(l.completed_modules),
            "Average Score": round(l.average_score(), 2),
            "Performance": l.classify_performance()
        }
        records.append(row)

    df = pd.DataFrame(records)
    df = df.sort_values(by="Average Score", ascending=False)
    df = df.reset_index(drop=True)
    return df


# ============================================================
# Print the full dashboard
# ============================================================
def print_dashboard(learners: List[Learner]) -> None:
    print("=" * 70)
    print("INTEGRATED LEARNER DASHBOARD")
    print("=" * 70)

    # 1. Individual details
    print("\n--- Individual Learner Details ---")
    for learner in learners:
        print("\n" + learner.name + " (" + learner.learner_id + ")")
        print("  Completed modules :", learner.completed_modules)
        print("  Scores            :", learner.scores)
        print("  Average           :", round(learner.average_score(), 2))
        print("  Classification    :", learner.classify_performance())

    # 2. High achievers
    print("\n--- High Achievers (average >= 80) ---")
    high = get_high_achievers(learners)
    if len(high) == 0:
        print("  None")
    else:
        for l in high:
            print("  •", l.name + ":", round(l.average_score(), 2),
                  "(" + l.classify_performance() + ")")

    # 3. Ranking
    print("\n--- Ranked by Average Score ---")
    ranked = rank_learners(learners)
    rank = 1
    for l in ranked:
        print("  " + str(rank) + ". " + l.name.ljust(10),
              str(round(l.average_score(), 2)).rjust(6),
              "[" + l.classify_performance() + "]")
        rank = rank + 1

    # 4. Aggregate statistics
    print("\n--- Aggregate Statistics ---")
    total = total_modules_completed(learners)
    averages = get_averages(learners)
    class_avg = sum(averages) / len(averages)
    print("  Total modules completed across all learners :", total)
    print("  Class average                               :", round(class_avg, 2))

    # 5. Pandas table
    print("\n--- Pandas Summary Table ---")
    df = create_summary_dataframe(learners)
    print(df.to_string(index=False))


# ============================================================
# Test cases
# ============================================================
def run_tests() -> None:
    print("\n" + "=" * 70)
    print("TEST CASES")
    print("=" * 70)

    learners = create_sample_learners()

    # Test 1: Normal case
    print("\n[Test 1] Normal – Ali average and classification")
    ali = None
    for l in learners:
        if l.name == "Ali":
            ali = l
            break

    avg = ali.average_score()
    cls = ali.classify_performance()
    print("  Expected  : average ≈ 88.83, classification = Excellent")
    print("  Actual    : average =", round(avg, 2), ", classification =", cls)
    if avg > 85 and cls == "Excellent":
        print("  Result    : PASS")
    else:
        print("  Result    : FAIL")

    # Test 2: Boundary case (exactly 80)
    print("\n[Test 2] Boundary – average == 80")
    boundary = Learner(
        "L999", "Boundary",
        ["programming", "database"],
        {"programming": 80, "database": 80}
    )
    avg_b = boundary.average_score()
    cls_b = boundary.classify_performance()
    print("  Expected  : average = 80.0, classification = High Achiever")
    print("  Actual    : average =", avg_b, ", classification =", cls_b)
    if avg_b == 80.0 and cls_b == "High Achiever":
        print("  Result    : PASS")
    else:
        print("  Result    : FAIL")

    # Test 3: Invalid input
    print("\n[Test 3] Invalid input – score > 100")
    try:
        bad = Learner("L000", "Bad", scores={"programming": 105})
        print("  Result    : FAIL (should raise error)")
    except ValueError as e:
        print("  Expected  : ValueError raised")
        print("  Actual    :", e)
        print("  Result    : PASS")

    # Test 4: No scores
    print("\n[Test 4] Edge – no scores")
    empty = Learner("L888", "Empty")
    avg_e = empty.average_score()
    cls_e = empty.classify_performance()
    print("  Expected  : average = 0.0, classification = Needs Improvement")
    print("  Actual    : average =", avg_e, ", classification =", cls_e)
    if avg_e == 0.0 and cls_e == "Needs Improvement":
        print("  Result    : PASS")
    else:
        print("  Result    : FAIL")

    # Test 5: Functional check
    print("\n[Test 5] Functional – high achievers")
    high = get_high_achievers(learners)
    names = []
    for l in high:
        names.append(l.name)
    print("  Expected  : contains Ali and Nur")
    print("  Actual    :", names)
    if "Ali" in names and "Nur" in names:
        print("  Result    : PASS")
    else:
        print("  Result    : FAIL")


# ============================================================
# Main program
# ============================================================
if __name__ == "__main__":
    learners = create_sample_learners()
    print_dashboard(learners)
    run_tests()
