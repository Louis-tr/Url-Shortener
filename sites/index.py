from aiohttp import web
import aiohttp_jinja2 as jinja2
import random
import string


routes = web.RouteTableDef()
app = None


def random_id():
    return "".join([random.choice(string.digits + string.ascii_lowercase) for i in range(16)])


@routes.get("/")
async def index(request):
    return jinja2.render_template("/index.html", request, {})


@routes.get("/shorten")
async def shorten(request):
    if request.query.get("url") is None:
        return web.Response(text="")

    id = random_id()
    await app.db.rdb.table("urls").insert({
        "id": id,
        "original": request.query.get("url")
    }).run(app.db.con)

    return web.Response(text=f"{request.host}/{id}")


@routes.get("/{id}")
async def urls(request):
    id = request.match_info['id']

    url = await app.db.rdb.table("urls").get(id).run(app.db.con)
    if url is None:
        raise web.HTTPNotFound()

    raise web.HTTPFound(url["original"])


async def setup(_app):
    global app
    app = _app
    app.add_routes(routes)
