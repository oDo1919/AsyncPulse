import json
from datetime import datetime

def export_json(results, filepath="pulse_report.json"):
    data = {
        "timestamp": datetime.now().isoformat(),
        "total_targets": len(results),
        "results": results
    }
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)
    print(f"📁 Raw log saved to: {filepath}")

def generate_markdown_summary(results, filepath="SUMMARY.md"):
    successful = sum(1 for r in results if r["success"])
    failed = len(results) - successful
    
    latencies = [r["latency_ms"] for r in results if r["latency_ms"] is not None]
    avg_latency = round(sum(latencies) / len(latencies), 2) if latencies else 0

    markdown_content = f"""# ⚡ AsyncPulse Health Report

**Generated on:** `{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}`

### Overview
* **Total Endpoints Tested:** {len(results)}
* **Successful (2xx/3xx):** {successful}
* **Failed / Unreachable:** {failed}
* **Average Latency:** {avg_latency} ms

### Detailed Results

| Status | Target Endpoint | HTTP Code | Latency |
| :---: | :--- | :---: | :---: |
"""
    for r in results:
        icon = "✅" if r["success"] else "❌"
        latency_str = f"{r['latency_ms']} ms" if r["latency_ms"] else "N/A"
        markdown_content += f"| {icon} | `{r['url']}` | `{r['status']}` | {latency_str} |\n"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(markdown_content)
    print(f"📊 Summary report saved to: {filepath}")