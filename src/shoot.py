import asyncio, sys
from playwright.async_api import async_playwright
URL='http://127.0.0.1:8765/'
async def main():
    async with async_playwright() as p:
        try: b=await p.chromium.launch()
        except Exception: b=await p.chromium.launch(executable_path='/usr/bin/google-chrome')
        for name,w,h,dpr in [('mobile-390',390,844,2),('desktop-1440',1440,900,1)]:
            pg=await b.new_page(viewport={'width':w,'height':h},device_scale_factor=dpr)
            await pg.goto(URL,wait_until='networkidle')
            await pg.evaluate("async()=>{for(let y=0;y<document.body.scrollHeight;y+=400){window.scrollTo(0,y);await new Promise(r=>setTimeout(r,250));}window.scrollTo(0,0);}")
            H=await pg.evaluate("document.documentElement.scrollHeight")
            await pg.set_viewport_size({'width':w,'height':H})
            await pg.wait_for_timeout(9000)
            await pg.screenshot(path=f'/workspace/finesse-health/screenshots/{name}.png',full_page=True)
            sw=await pg.evaluate("document.documentElement.scrollWidth"); print(name,'scrollWidth',sw)
            await pg.set_viewport_size({'width':w,'height':h})
            if name.startswith('mobile'):
                await pg.click('.nav-toggle'); await pg.wait_for_timeout(300)
                await pg.screenshot(path='/workspace/finesse-health/screenshots/mobile-390-menu-open.png')
        await b.close()
asyncio.run(main())
