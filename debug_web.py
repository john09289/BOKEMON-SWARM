import asyncio
import json
from playwright.async_api import async_playwright

async def diagnose():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        errors = []
        page.on("console", lambda msg: 
            errors.append({"type": msg.type, "text": msg.text}) 
            if msg.type in ("error", "warning") else None
        )
        
        page.on("pageerror", lambda err: 
            errors.append({"type": "unhandled", "text": str(err)})
        )
        
        try:
            await page.goto("https://john09289.github.io/BOKEMON-SWARM", 
                            wait_until="domcontentloaded", timeout=30000)
            await page.wait_for_timeout(15000)
            canvas = await page.query_selector("canvas")
            if not canvas:
                errors.append({"type": "info", "text": "No canvas element found – Pygame display not created."})
            else:
                errors.append({"type": "info", "text": "Canvas element found."})
                # Take screenshot
                await page.screenshot(path="game_screenshot.png")
                errors.append({"type": "info", "text": "Screenshot saved to game_screenshot.png"})
        except Exception as e:
            errors.append({"type": "exception", "text": str(e)})
        
        await browser.close()
        return errors

if __name__ == "__main__":
    results = asyncio.run(diagnose())
    with open("debug_report.json", "w") as f:
        json.dump(results, f, indent=2)
    print("Report saved to debug_report.json")
    for r in results:
        print(f"[{r['type']}] {r['text']}")
