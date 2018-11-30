from aiohttp import web
import aiohttp_jinja2 as jinja2
import random
import string

import url_manager as urls
import config


routes = web.RouteTableDef()


def random_id():
    return "".join([random.choice(string.digits + string.ascii_lowercase) for i in range(config.id_length)])


@routes.get("/")
async def _index(request):
    return jinja2.render_template("/index.html", request, {})


@routes.post("/shorten")
async def _shorten(request):
    data = await request.post()
    if data.get("url") is None:
        raise web.HTTPBadRequest()

    id = random_id()
    await urls.add_url(id, data["url"])

    return web.Response(text=f"{request.scheme}://{request.host}/{id}")


@routes.get("/{id}")
async def _urls(request):
    id = request.match_info['id']

    url = await urls.get_url(id)
    if url is None:
        raise web.HTTPNotFound()

    raise web.HTTPFound(url)


async def setup(app):
    app.add_routes(routes)
