from api_rpn import api_rpn_namespace
from flask_restx import Resource
from flask import request
from rpn.stacks import Stacks, StacksAlreadyExist, StacksNotExist
from rpn.pile import PileRPN, InvalidValuePileRPN
from .model_in_out_endpoint import stack_id_model, stack_ids_model, stack_model, stack_value_model


@api_rpn_namespace.route('/stacks')
class StacksEndpoint(Resource):

    @api_rpn_namespace.marshal_with(stack_ids_model)
    def get(self):
        """
            List the available stacks
        """

        return {"stacks_id": list(Stacks().stacks)}
    
    @api_rpn_namespace.response(400, 'Stack id already exists')
    @api_rpn_namespace.marshal_with(stack_id_model)
    @api_rpn_namespace.expect(stack_id_model, validate=True)
    def post(self):
        """
            Create a new stack
        """

        stack_id_arg = request.json["stack_id"]

        try:
            Stacks().add(stack_id_arg)
        except StacksAlreadyExist:
            api_rpn_namespace.abort(400, 'Stack id already exists')

        return {"stack_id": stack_id_arg}, 201

 
@api_rpn_namespace.route('/stacks/<string:stack_id>')
class StackEndpoint(Resource):

    @api_rpn_namespace.response(404, 'Stack not found')
    @api_rpn_namespace.marshal_with(stack_model)
    def get(self, stack_id):
        """
            Get a stack
        """
        try:
            stack_pile = Stacks().get(stack_id)
            return {
                "id": stack_id,
                "values": stack_pile.to_list()
            }
        except StacksNotExist:
            api_rpn_namespace.abort(404, 'Stack not found')
    
    @api_rpn_namespace.response(404, 'Stack not found')
    @api_rpn_namespace.response(400, 'Invalid value')
    @api_rpn_namespace.marshal_with(stack_model)
    @api_rpn_namespace.expect(stack_value_model, validate=True)
    def post(self, stack_id):
        """
            Push a new value to a stack
        """

        stack_value_arg = request.json["value"]

        try:
            Stacks().get(stack_id).add(stack_value_arg)
            stack_pile: PileRPN = Stacks().get(stack_id)
            return {
                "id": stack_id,
                "values": stack_pile.to_list()
            }, 201
        except StacksNotExist:
            api_rpn_namespace.abort(404, 'Stack not found')
        except InvalidValuePileRPN:
            api_rpn_namespace.abort(400, 'Invalid value')

    @api_rpn_namespace.response(404, 'Stack not found')
    def delete(self, stack_id):
        """
            Delete a stack
        """

        try:
            Stacks().delete(stack_id)
        except StacksNotExist:
            api_rpn_namespace.abort(404, 'Stack not found')
