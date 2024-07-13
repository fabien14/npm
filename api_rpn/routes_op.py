from api_rpn import api_rpn_namespace
from flask_restx import Resource
from rpn.operator import OperatorRPN
from .model_in_out_endpoint import operand_model


@api_rpn_namespace.route('/op')
class Operands(Resource):

    @api_rpn_namespace.marshal_with(operand_model)
    def get(self):
        """
            List all the operand
        """
        return {"op": OperatorRPN.get_keys_lower()}