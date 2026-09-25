Markdown
# ⚡ AsyncPulse

An asynchronous, non-blocking network health checker and API performance monitor built with Python, `asyncio`, and `aiohttp`.

## Overview
AsyncPulse evaluates the availability and latency of multiple network endpoints concurrently. By utilizing connection pools and asynchronous I/O, it tests hundreds of URLs in parallel while bounding system resources.

## Features
- **Concurrent Execution:** Non-blocking async engine for high-throughput endpoint monitoring.
- **Concurrency Bounding:** Uses `asyncio.Semaphore` to cap active requests and prevent socket exhaustion.
- **Fault Tolerance:** Captures connection timeouts, DNS failures, and HTTP error status codes (4xx/5xx).
- **Automated Reporting:** Generates structured JSON logs (`pulse_report.json`) and Markdown summary tables (`SUMMARY.md`).

## Architecture
```text
AsyncPulse/
├── core/
│   ├── engine.py       # Asynchronous HTTP client & execution pool
│   └── reporter.py     # JSON logger & Markdown generator
├── config.py           # Configuration settings & interactive prompt
├── main.py             # CLI application entry point
└── README.md           # System documentation