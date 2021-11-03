from flask import Flask, render_template

from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute

app = Flask(__name__)

class OneTable(Model):
    '''
    DynamoDB works best with a single table. This table. Use this table to model
    other data requests.
    '''
    class Meta:
        table_name = os.environ['DYNAMODB_TABLE_NAME']

    pk = UnicodeAttribute(hash_key=True)
    sk = UnicodeAttribute(range_key=True)

@app.route("/")
def cats():
    return render_template('index.html')

@app.route("/dogs/<id>")
def dog(id):
    return "Dog"

@app.route("/health")
def health():
    return { "status": "Success" }