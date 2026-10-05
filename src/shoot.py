"""Capture full-page screenshots of home + terms at mobile 390 and desktop 1440.

Requires local preview: python3 -m http.server 8765
"""
import asyncio
from playwright.async_api import async_playwright

BASE = "http://127.0.0.1:8765"
PAGES = [
    ("home", "/"),
    ("terms", "/terms-and-disclaimer.html"),
]
VIEWPORTS = [
    ("mobile-390", 390, 844, 2),
    ("desktop-1440", 1440, 900, 1),
]
OUT = "/workspace/finesse-health/screenshots"
BLOCK = (
    "google.com/maps",
    "maps.googleapis",
    "maps.gstatic",
    "googletagmanager",
    "google-analytics",
)

async def capture(browser, page_name, path, vp_name, w, h, dpr):
    print(f"start {page_name} {vp_name}", flush=True)
    pg = await browser.new_page(viewport={"width": w, "height": h}, device_scale_factor=dpr)

    async def handler(route):
        url = route.request.url
        if any(b in url for b in BLOCK):
            await route.abort()
        else:
            await route.continue_()

    await pg.route("**/*", handler)
    await pg.goto(BASE + path, wait_until="domcontentloaded", timeout=30000)
    await pg.wait_for_timeout(1200)
    await pg.evaluate("""async () => {
      const h = Math.max(document.body.scrollHeight, document.documentElement.scrollHeight);
      for (let y = 0; y < h; y += 600) {
        window.scrollTo(0, y);
        await new Promise(r => setTimeout(r, 50));
      }
      window.scrollTo(0, 0);
    }""")
    await pg.wait_for_timeout(300)
    out = f"{OUT}/{page_name}-{vp_name}.png"
    await pg.screenshot(path=out, full_page=True)
    sw = await pg.evaluate("document.documentElement.scrollWidth")
    print(page_name, vp_name, "scrollWidth", sw, "->", out, flush=True)
    if page_name == "home" and vp_name.startswith("mobile"):
        await pg.set_viewport_size({"width": w, "height": h})
        await pg.click(".nav-toggle")
        await pg.wait_for_timeout(250)
        menu_out = f"{OUT}/home-mobile-390-menu-open.png"
        await pg.screenshot(path=menu_out)
        print("menu-open ->", menu_out, flush=True)
    await pg.close()

async def main():
    async with async_playwright() as p:
        try:
            browser = await p.chromium.launch(args=["--no-sandbox", "--disable-dev-shm-usage"])
        except Exception:
            browser = await p.chromium.launch(
                executable_path="/usr/bin/google-chrome",
                args=["--no-sandbox", "--disable-dev-shm-usage"],
            )
        for page_name, path in PAGES:
            for vp_name, w, h, dpr in VIEWPORTS:
                await capture(browser, page_name, path, vp_name, w, h, dpr)
        await browser.close()
    print("done", flush=True)

asyncio.run(main())
