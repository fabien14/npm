from api_rpn import api_rpn_namespace
from flask_restx import fields

operand_model = api_rpn_namespace.model('Operand', {
    'op': fields.List(
        fields.String,
        readonly=True,
        description='Operand'
    )
})

stack_ids_model = api_rpn_namespace.model("Stack Ids", {
    "stacks_id": fields.List(
        fields.String,
        readonly=True,
        description="Stacks Id"
    )
})
