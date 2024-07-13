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

stack_id_model = api_rpn_namespace.model("Stack Id", {
    "stack_id": fields.String(
        required=True,
        description="Stack Id"
    )
})

stack_model = api_rpn_namespace.model("Stack", {
    "id": fields.String(
        readonly=True,
        description="stack id"
    ),
    "values": fields.List(
        fields.Integer,
        readonly=True,
        description="stack list values"
    )
})

stack_value_model = api_rpn_namespace.model("Stack value", {
    "value": fields.Integer(
        request=True,
        description="stack value"
    )
})
