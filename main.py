import os

LINE = "Turns out 'works on my machine' was the load-bearing part of our architecture."

assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"

out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
