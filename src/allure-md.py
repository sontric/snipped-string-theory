import argparse
import json
from pathlib import Path
from datetime import datetime

def read_allure_results(allure_dir):
    return [
        json.loads(p.read_text(encoding='utf-8'))
        for p in Path(allure_dir).glob("*-result.json")
    ]

def duration_ms(start, stop):
    return (stop - start) / 1000.0 if start and stop else 0

def timestamp_fmt(ms):
    if ms:
        return datetime.fromtimestamp(ms / 1000).isoformat()
    return "N/A"

def format_report(results):
    lines = []
    lines.append("# 🧾 Allure Audit Report\n")
    lines.append("| Test | Status | Start | Stop | Duration (s) | Error Message |")
    lines.append("|------|--------|-------|------|--------------|----------------|")

    for r in results:
        name = r.get("name", "")
        status = r.get("status", "")
        start = r.get("start")
        stop = r.get("stop")
        dur = duration_ms(start, stop)
        start_str = timestamp_fmt(start)
        stop_str = timestamp_fmt(stop)
        msg = r.get("statusDetails", {}).get("message", "")
        msg = msg.replace("\n", " ").replace("|", "\\|") if msg else ""
        lines.append(f"| `{name}` | `{status}` | `{start_str}` | `{stop_str}` | `{dur:.2f}` | {msg} |")

    return lines

def write_report(lines, out_path):
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"✅ Markdown report written to {out_path}")

def main():
    parser = argparse.ArgumentParser()
    
    # NOTE: "allure-results" keyword / folder also referenced in readme.md
    parser.add_argument("--alluredir", default="allure-results", help="Allure results dir")

    parser.add_argument("--output", default="allure-report.md", help="Output .md file")
    args = parser.parse_args()

    results = read_allure_results(args.alluredir)
    report_lines = format_report(results)
    write_report(report_lines, args.output)


if __name__ == "__main__":
    main()
