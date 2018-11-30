from aiohttp import web, ClientSession
import aiohttp_jinja2
import jinja2

import secrets
from utils import database
from sites import index


startup_sites = [index]


async def prepare(app):
    app["http_session"] = ClientSession()
    app.secrets = secrets
    app.db = database
    await app.db.setup()

    for site in startup_sites:
        await site.setup(app)


app = web.Application()
app.on_startup.append(prepare)
app.router.add_static('/static', "./static")
aiohttp_jinja2.setup(
    app,
    loader=jinja2.FileSystemLoader("./contents/templates")
)
web.run_app(app, port=8086)
