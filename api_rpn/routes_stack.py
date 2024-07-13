from api_rpn import api_rpn_namespace
from flask_restx import Resource
from rpn.stacks import Stacks
from .model_in_out_endpoint import stack_ids_model


@api_rpn_namespace.route('/stacks')
class StacksEndpoint(Resource):

    @api_rpn_namespace.marshal_with(stack_ids_model)
    def get(self):
        """
            List the available stacks
        """

        return {"stacks_id": list(Stacks().stacks)}