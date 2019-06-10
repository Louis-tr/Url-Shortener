from aiohttp import web, ClientSession
import aiohttp_jinja2
import jinja2
from motor.motor_asyncio import AsyncIOMotorClient

import routes


class App(web.Application):
    session = None
    db = None

    def __init__(self):
        super().__init__()

        self.db = AsyncIOMotorClient().url_shortener
        self.on_startup.append(self.prepare)
        self.add_routes(routes.router)
        aiohttp_jinja2.setup(
            self,
            loader=jinja2.FileSystemLoader("./templates")
        )

    async def prepare(self, app):
        app.session = ClientSession()

    @property
    def config(self):
        return __import__("config")


app = App()
web.run_app(app, port=8086)
