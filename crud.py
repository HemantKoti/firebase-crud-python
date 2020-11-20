# Required Imports
import os
from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app

# Initialize Flask App
app = Flask(__name__)

# Initialize Firestore DB
cred = credentials.Certificate('unilends.json')
default_app = initialize_app(cred)
db = firestore.client()
# todo_ref = db.collection('users')
payments = db.collection('payments')


# @app.route('/add', methods=['POST'])
# def create():
#     """
#         create() : Add document to Firestore collection with request body
#         Ensure you pass a custom ID as part of json body in post request
#         e.g. json={'id': '1', 'title': 'Write a blog post'}
#     """
#     try:
#         id = request.json['id']
#         payments.document(id).set(request.json)
#         return jsonify({"success": True}), 200
#     except Exception as e:
#         return f"An Error Occured: {e}"


# @app.route('/list', methods=['GET'])
# def read():
#     """
#         read() : Fetches documents from Firestore collection as JSON
#         todo : Return document that matches query ID
#         all_todos : Return all documents
#     """
#     try:
#         # Check if ID was passed to URL query
#         todo_id = request.args.get('id')
#         if todo_id:
#             todo = todo_ref.document(todo_id).get()
#             return jsonify(todo.to_dict()), 200
#         else:
#             all_todos = [doc.to_dict() for doc in todo_ref.stream()]
#             return jsonify(all_todos), 200
#     except Exception as e:
#         return f"An Error Occured: {e}"


# @app.route('/update', methods=['POST', 'PUT'])
# def update():
#     """
#         update() : Update document in Firestore collection with request body
#         Ensure you pass a custom ID as part of json body in post request
#         e.g. json={'id': '1', 'title': 'Write a blog post today'}
#     """
#     try:
#         id = request.json['id']
#         todo_ref.document(id).update(request.json)
#         return jsonify({"success": True}), 200
#     except Exception as e:
#         return f"An Error Occured: {e}"


# @app.route('/delete', methods=['GET', 'DELETE'])
# def delete():
#     """
#         delete() : Delete a document from Firestore collection
#     """
#     try:
#         # Check for ID in URL query
#         todo_id = request.args.get('id')
#         todo_ref.document(todo_id).delete()
#         return jsonify({"success": True}), 200
#     except Exception as e:
#         return f"An Error Occured: {e}"

account_sid = 'ACf99d181bee7652734862dd42cb0c7601'
auth_token = 'b13582320472c60b71fc7912e7c03ec2'
client = Client(account_sid, auth_token)


def send_sms(msg):
    """
    send sms using twilio
    """
    message = client.messages \
                    .create(
                        body=msg,
                        from_='+18454437370',
                        to='+17169397014'
                    )

    print(message.sid)


@app.route('/addPayment', methods=['POST'])
def addPayments():
    """
    addPayment() : Add a payment to the feed, so that all the users can see it on their feed
    """
    try:
        id = request.json['paymentId']
        print(id)
        payments.document(id).set(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return "An error occurred"


@app.route('/makePayment', methods=['POST'])
def makePayments():
    """
    makePayment() : Making payment on a particular request. Request body contains the payment ID 
    Response will be the success/failure of the payment
    """
    try:
        payment_id = request.body['id']
        if payment_id and payments.document(payment_id).get():
            payments.document(payment_id).update({"paid": True})
            return jsonify({"success": True}), 200
        else:
            raise Exception("Payment Id not found")

    except Exception as e:
        return "An error occurred"


@app.route('/getAll', methods=['POST'])
def getAll():
    """
    getAll() : gets the feed for the current user
    """
    try:

        return jsonify({"success": True}), 200
    except Exception as e:
        return "An error occurred"


port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='127.0.0.1', port=port)
