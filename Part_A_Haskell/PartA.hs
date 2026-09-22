import Data.List (maximumBy)
import Data.Ord (comparing)

-- 1. Define the Immutable Dataset Structure
data Learner = Learner
  { learnerId    :: Int
  , learnerName  :: String
  , moduleScores :: [Double]
  } deriving (Show, Eq)

-- Dataset containing at least 5 learners 
-- (includes normal cases, a boundary case of exactly 80.0, and a tie case)
assessmentData :: [Learner]
assessmentData = 
  [ Learner 101 "Ali"   [85.0, 90.0, 78.5]  -- Normal (> 80)
  , Learner 102 "Siti"     [80.0, 80.0, 80.0]  -- Boundary (Exactly 80.0)
  , Learner 103 "Ahmad" [95.0, 92.0, 98.0]  -- Tie Candidate 1 (Avg: 95.0)
  , Learner 104 "Nur"   [94.0, 96.0, 95.0]  -- Tie Candidate 2 (Avg: 95.0)
  , Learner 105 "Danial"   [50.0, 70.0, 60.0]  -- Normal (< 80)
  ]

-- 2. Pure function to calculate each learner's average score
averageScore :: Learner -> Double
averageScore (Learner _ _ []) = 0.0
averageScore (Learner _ _ scores) = sum scores / fromIntegral (length scores)

-- 3. Function to return high-achieving learners (average score >= 80)
highAchievers :: [Learner] -> [Learner]
highAchievers = filter (\l -> averageScore l >= 80.0)

-- 4. Function to identify the single top-performing learner with a tie-breaking rule
-- TIE RULE: If multiple learners share the highest average score,
-- the learner with the lowest ID is selected.
topLearner :: [Learner] -> Learner
topLearner [] = error "The assessment dataset is empty."
topLearner learners = maximumBy tieBreakComparator learners
  where
    tieBreakComparator l1 l2 =
      case compare (averageScore l1) (averageScore l2) of
        EQ -> compare (learnerId l2) (learnerId l1) -- Lower ID wins the tie
        other -> other

-- 6. Main execution demonstrating normal, boundary, and tie test cases
main :: IO ()
main = do
  putStrLn "=== Learner Assessment Analysis ==="
  
  -- Display all learners and their calculated averages
  putStrLn "\n--- 1. Individual Averages ---"
  mapM_ (\l -> putStrLn $ "ID: " ++ show (learnerId l) ++ 
   " | Name: " ++ learnerName l ++ " | Avg: " ++ show (averageScore l)) assessmentData

  -- Display high achievers (>= 80, including boundary case)
  putStrLn "\n--- 2. High-Achieving Learners (Average >= 80) ---"
  let achievers = highAchievers assessmentData
  mapM_ (\l -> putStrLn $ " - " ++ learnerName l ++ " (Avg: " ++ show (averageScore l) ++ ")") achievers

  -- Display top performer with tie rule handled
  putStrLn "\n--- 3. Top-Performing Learner ---"
  putStrLn "Tie Rule: In case of identical top averages, the learner with the lowest ID is selected."
  let top = topLearner assessmentData
  putStrLn $ "Selected Top Performer: " ++ learnerName top ++ " (ID: " ++ show (learnerId top) ++ 
   ", Avg: " ++ show (averageScore top) ++ ")"
