import sys
from pathlib import Path

# מוסיף את תיקיית האב לנתיב החיפוש של פייתון באופן דינמי
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))