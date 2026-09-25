import asyncio
import aiohttp
import time

async def check_url(session, semaphore, url, timeout):
    async with semaphore:
        start_time = time.time()
        try:
            async with session.get(url, timeout=timeout) as response:
                latency = round((time.time() - start_time) * 1000, 2)
                return {
                    "url": url,
                    "status": response.status,
                    "latency_ms": latency,
                    "success": response.status < 400
                }
        except asyncio.TimeoutError:
            return {"url": url, "status": "TIMEOUT", "latency_ms": None, "success": False}
        except Exception:
            return {"url": url, "status": "UNREACHABLE", "latency_ms": None, "success": False}

async def run_pulse(urls, max_concurrent, timeout):
    semaphore = asyncio.Semaphore(max_concurrent)
    async with aiohttp.ClientSession() as session:
        tasks = [check_url(session, semaphore, url, timeout) for url in urls]
        return await asyncio.gather(*tasks)