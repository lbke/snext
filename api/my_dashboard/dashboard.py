# @see https://vercel.com/docs/runtimes
# @see https://sanic.readthedocs.io/en/stable/
from sanic import Sanic
from sanic.response import json
app = Sanic("dashboard")


@app.route('/')
@app.route('/<path:path>')
async def index(request, path=""):
    return json({'hello': path})
