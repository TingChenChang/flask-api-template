from flask import Flask

from apis import api_bp
from docs import doc_bp

app = Flask(__name__)

app.config['RESTX_MASK_SWAGGER'] = False

app.register_blueprint(api_bp)
app.register_blueprint(doc_bp)

if __name__ == "__main__":
    app.run(debug=True)
