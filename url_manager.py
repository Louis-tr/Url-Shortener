import aiofiles as aiof
import json
import os

import config


async def add_url(id, url):
    urls = await get_urls()
    urls[id] = url
    async with aiof.open(config.file, "w") as f:
        await f.write(json.dumps(urls))
        await f.close()

    return True


async def get_url(id):
    urls = await get_urls()
    return urls.get(id)


async def get_urls():
    if not os.path.isfile(config.file):
        return {}

    async with aiof.open(config.file, "r") as f:
        return json.loads(await f.read())
