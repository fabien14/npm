from flask import Blueprint
from flask_restx import Api, Namespace

api_rpn_namespace = Namespace('rpn', 'RPN Api')

api_rpn_blueprint = Blueprint('rpn', __name__)
api_rpn_api = Api(api_rpn_blueprint,
    title='RPN Api',
    version='1.0',
    doc='/swagger-ui/',
)

api_rpn_api.add_namespace(api_rpn_namespace)

from api_rpn import routes_op, routes_stack
