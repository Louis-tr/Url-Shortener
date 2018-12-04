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

    url = urlparse(data["url"])
    if url.netloc == request.host:
        return web.Response(text=urlunparse(url))

    if url.scheme == "":
        url = url._replace(scheme="http")

    id = random_id()
    urls[id] = urlunparse(url)

    return web.Response(text=f"{request.scheme}://{request.host}/{id}")


@routes.get("/{id}")
async def _urls(request):
    id = request.match_info['id'].lower()

    url = urls.get(id)
    if url is None:
        raise web.HTTPNotFound()

    raise web.HTTPFound(url)


async def setup(app):
    app.add_routes(routes)
