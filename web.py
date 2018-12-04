from aiohttp import web, ClientSession
import aiohttp_jinja2
import jinja2

import routes
import url_manager


startup_sites = [routes]


class App(web.Application):
    def __init__(self):
        super().__init__()
        self.on_startup.append(self.prepare)
        self.router.add_static('/static', "./frontend/static")
        aiohttp_jinja2.setup(
            self,
            loader=jinja2.FileSystemLoader("./frontend/templates")
        )

    async def prepare(self, app):
        app["http_session"] = ClientSession()
        app.loop.create_task(url_manager.save_loop())

        for site in startup_sites:
            await site.setup(app)

    @property
    def config(self):
        return __import__("config")


app = App()
web.run_app(app, port=8086)
