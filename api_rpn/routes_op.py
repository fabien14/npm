from api_rpn import api_rpn_namespace
from flask_restx import Resource
from rpn.operator import OperatorRPN, OperatorNotExist
from rpn.stacks import Stacks, StacksNotExist
from rpn.calculator import CalculatorRPN, InvalidPileNumberItems
from .model_in_out_endpoint import stack_model, operand_model


@api_rpn_namespace.route('/op')
class Operands(Resource):

    @api_rpn_namespace.marshal_with(operand_model)
    def get(self):
        """
            List all the operand
        """
        return {"op": OperatorRPN.get_keys_lower()}
    

@api_rpn_namespace.route('/op/<string:op>/stacks/<string:stack_id>')
class Calculator(Resource):

    @api_rpn_namespace.response(404, 'Stack not found')
    @api_rpn_namespace.response(404, 'Operand not found')
    @api_rpn_namespace.response(400, 'Invalid stack number items')
    @api_rpn_namespace.marshal_with(stack_model)
    def post(self, op, stack_id):
        """
            Apply an operand to a stack
        """

        try:
            stack_pile = Stacks().get(stack_id)
            operand = OperatorRPN.get(op)
            pile_result = CalculatorRPN().apply(stack_pile, operand)
            return {
                "id": stack_id,
                "values": pile_result.to_list()
            }, 201
        except StacksNotExist:
            api_rpn_namespace.abort(404, 'Stack not found')
        except OperatorNotExist:
            api_rpn_namespace.abort(404, 'Operand not found')
        except InvalidPileNumberItems:
            api_rpn_namespace.abort(400, 'Invalid stack number items')
