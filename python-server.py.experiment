# Runs the Python API routes as one server
# @see https://github.com/ashleysommer/sanic-dispatcher

# TODO: how to run this python on the same port as the Next app?
# TODO: run automatically on yarn dev/yarn start

from sanic import Sanic, response
from sanic_dispatcher import SanicDispatcherMiddlewareController
# Example using Flask as well
#from flask import Flask, make_response, current_app as flask_app

# TODO: get all .py API routes automatically instead (take inspiration from Next.js code or even reuse it to precompute the routes)
from pages.api.data import app as DataApiRoute
from pages.api.my_dashboard.dashboard import app as MyDashboard_DashboardApiRoute

# We need a main app, on which to put the controller middleware that dispatch to child apps
main_app = Sanic(__name__)

dispatcher = SanicDispatcherMiddlewareController(main_app)

# child_flask_app = Flask("MyChildFlaskApp")

@main_app.middleware("response")
async def modify_response(request, response):
    response.body = response.body + b"\nModified by Sanic Response middleware!"
    response.headers['Content-Length'] = len(response.body)
    return response

# Route of the API, we could display a message to developers here
@main_app.route("/api")
async def index(request):
    return response.text("Hello World from {}".format(request.app.name))

#@child_flask_app.route("/")
#def index():
#    app = flask_app
#    return make_response("Hello World from {}".format(app.import_name))

# http://127.0.0.1:8001/api/data/ 
# TODO: the dangling "/" is mandatory as the moment, to be investigated
dispatcher.register_sanic_application(DataApiRoute, '/api/data', apply_middleware=True)
dispatcher.register_sanic_application(MyDashboard_DashboardApiRoute, '/api/my_dashboard/dashboard', apply_middleware=True)
# TODO: automatically differentiate Sanic and Flask
# Uncomment to activate dispatching a flask API route as well
# dispatcher.register_wsgi_application(child_flask_app.wsgi_app, '/flaskchild', apply_middleware=True)

if __name__ == "__main__":
    main_app.run(port=8001, debug=True)
