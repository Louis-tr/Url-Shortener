from aiohttp import web
import aiohttp_jinja2 as jinja2
import random
import string
import re


router = web.RouteTableDef()


def random_id(id_length):
    return "".join([random.choice(string.digits + string.ascii_lowercase) for i in range(id_length)])


@router.get("/")
async def _index(req):
    return jinja2.render_template("index.html", req, {})


@router.post("/shorten")
async def _shorten(req):
    data = await req.post()
    url = data.get("url")
    if url is None:
        raise web.HTTPBadRequest()

    if not re.match(r"^https?:\/\/.+\..+$", url):
        raise web.HTTPBadRequest

    url_id = random_id(req.app.config.id_length)
    await req.app.db.urls.insert_one({
        "_id": url_id,
        "url": url
    })

    return web.json_response({"url": f"{req.app.config.scheme}://{req.app.config.host}/{url_id}"})


@router.get("/{id}")
async def _urls(req):
    id = req.match_info['id'].lower()
    url = await req.app.db.urls.find_one({"_id": id})
    if url is None:
        raise web.HTTPNotFound()

    raise web.HTTPFound(url["url"])


async def setup(app):
    app.add_routes(router)
