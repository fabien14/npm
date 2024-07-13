from flask import Flask
from api_rpn import api_rpn_blueprint

app = Flask(__name__)
app.config['RESTX_MASK_SWAGGER'] = False
app.register_blueprint(api_rpn_blueprint)

if __name__ == "__main__":
    app.run()
