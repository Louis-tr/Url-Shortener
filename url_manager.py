import json
import traceback
import os
import asyncio

import config


urls = {}
if os.path.isfile(config.file):
    with open(config.file) as f:
        urls = json.load(f)


async def save_loop():
    while True:
        try:
            await asyncio.sleep(10)
            with open(config.file, "w") as f:
                json.dump(urls, f)
                f.close()
        except:
            traceback.print_exc()
