# forensics/browser_parser.py
import sqlite3
import os

def parse_chrome_history(history_path):
    if not os.path.exists(history_path):
        raise FileNotFoundError("History file not found")

    try:
        conn = sqlite3.connect(history_path)
        cursor = conn.cursor()
        cursor.execute("SELECT url, title, visit_count FROM urls ORDER BY last_visit_time DESC LIMIT 10")
        results = cursor.fetchall()
        conn.close()
        return results
    except Exception as e:
        raise RuntimeError(f"Failed to parse browser history: {e}")
