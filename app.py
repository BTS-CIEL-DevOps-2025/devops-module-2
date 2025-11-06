from flask import Flask, render_template, request
from azure.identity import ClientSecretCredential
from azure.mgmt.resource import SubscriptionClient

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    subscription_name = None
    subscription_id = None
    error = None

    if request.method == 'POST':
        tenant_id = request.form['tenant_id']
        client_id = request.form['client_id']
        client_secret = request.form['client_secret']

        try:
            # Authenticate using the provided credentials
            credential = ClientSecretCredential(
                tenant_id=tenant_id,
                client_id=client_id,
                client_secret=client_secret
            )

            # Get subscription info
            subscription_client = SubscriptionClient(credential)
            subscriptions = list(subscription_client.subscriptions.list())

            if subscriptions:
                subscription_name = subscriptions[0].display_name
                subscription_id = subscriptions[0].subscription_id
            else:
                error = "No subscriptions found :(" + str(len(subscriptions))

        except Exception as e:
            error = f"Authentication failed: {str(e)}"

    return render_template('index.html', subscription_name=subscription_name, subscription_id=subscription_id error=error)

if __name__ == '__main__':
    app.run(debug=True)