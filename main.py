import asyncio
from config import get_target_urls, CONCURRENT_LIMIT, DEFAULT_TIMEOUT
from core.engine import run_pulse
from core.reporter import export_json, generate_markdown_summary

async def main():
    target_urls = get_target_urls()
    
    if not target_urls:
        print("⚠️ No URLs provided. Exiting.")
        return

    print(f"\n⚡ Running AsyncPulse [Targets: {len(target_urls)} | Max Concurrency: {CONCURRENT_LIMIT}]\n")
    
    results = await run_pulse(target_urls, CONCURRENT_LIMIT, DEFAULT_TIMEOUT)
    
    for res in results:
        status_icon = "✅" if res["success"] else "❌"
        latency_str = f"{res['latency_ms']}ms" if res['latency_ms'] else "N/A"
        print(f"{status_icon} {res['url']:<42} | Status: {str(res['status']):<11} | Latency: {latency_str}")

    print("\n" + "="*60)
    
    export_json(results)
    generate_markdown_summary(results)

if __name__ == "__main__":
    asyncio.run(main())