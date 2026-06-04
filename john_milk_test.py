"""
John Milk Protocol - Phase 2: Automated Browser Test with Playwright
Carrier: 11.71875 Hz
"""

import asyncio
import json
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from john_milk_logger import log, error, warning

async def run_browser_test():
    from playwright.async_api import async_playwright
    
    report = {
        "timestamp": datetime.now().isoformat(),
        "url": "https://john09289.github.io/BOKEMON-SWARM",
        "canvas_found": False,
        "console_errors": [],
        "console_warnings": [],
        "page_title": None,
        "final_url": None,
        "screenshot": "john_milk_screenshot.png",
        "status": "UNKNOWN"
    }
    
    log("Starting Playwright browser test...")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        
        # Capture console messages
        console_messages = []
        page.on("console", lambda msg: console_messages.append({
            "type": msg.type,
            "text": msg.text
        }))
        
        # Navigate to the game
        log(f"Navigating to {report['url']}")
        try:
            await page.goto(report['url'], wait_until="domcontentloaded", timeout=30000)
            report["final_url"] = page.url
            report["page_title"] = await page.title()
            log(f"Page loaded: {report['page_title']}")
        except Exception as e:
            error(f"Navigation failed: {e}")
            report["status"] = "NAVIGATION_FAILED"
            await browser.close()
            return report
        
        # Wait for canvas
        log("Waiting for canvas element (up to 20 seconds)...")
        canvas_found = False
        for i in range(20):
            canvases = await page.query_selector_all("canvas")
            report["canvas_found"] = len(canvases) > 0
            if len(canvases) > 0:
                canvas_found = True
                log(f"Canvas found after {i+1} seconds! Count: {len(canvases)}")
                break
            log(f"  Second {i+1}: {len(canvases)} canvases, title: {report['page_title']}")
            await asyncio.sleep(1)
        
        if not canvas_found:
            warning("No canvas found after 20 seconds!")
            report["status"] = "NO_CANVAS"
        else:
            report["status"] = "CANVAS_FOUND"
        
        # Collect console errors
        for msg in console_messages:
            if msg["type"] == "error":
                report["console_errors"].append(msg["text"])
            elif msg["type"] == "warning":
                report["console_warnings"].append(msg["text"])
        
        log(f"Console errors: {len(report['console_errors'])}")
        log(f"Console warnings: {len(report['console_warnings'])}")
        
        # Take screenshot
        try:
            await page.screenshot(path=report["screenshot"], full_page=True)
            log(f"Screenshot saved: {report['screenshot']}")
        except Exception as e:
            error(f"Screenshot failed: {e}")
        
        await browser.close()
    
    # Determine final status
    if report["canvas_found"] and len(report["console_errors"]) == 0:
        report["status"] = "ALL_SYSTEMS_GO"
    elif report["canvas_found"]:
        report["status"] = "CANVAS_FOUND_WITH_ERRORS"
    else:
        report["status"] = "BLACK_SCREEN"
    
    log(f"Final status: {report['status']}")
    return report

def main():
    report = asyncio.run(run_browser_test())
    
    # Save report
    with open("john_milk_report.json", "w") as f:
        json.dump(report, f, indent=2)
    
    log("Report saved to john_milk_report.json")
    
    # Print summary
    print("\n" + "=" * 60)
    print("JOHN MILK PROTOCOL - PHASE 2 COMPLETE")
    print("=" * 60)
    print(f"Status: {report['status']}")
    print(f"Canvas found: {report['canvas_found']}")
    print(f"Console errors: {len(report['console_errors'])}")
    print(f"Screenshot: {report['screenshot']}")
    print("=" * 60)
    
    if report["console_errors"]:
        print("\nConsole Errors:")
        for err in report["console_errors"]:
            print(f"  - {err}")
    
    return report["status"]

if __name__ == "__main__":
    status = main()
    sys.exit(0 if status == "ALL_SYSTEMS_GO" else 1)
