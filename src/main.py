import requests
import base64


BASE_URL = "https://akash-rpc.w3coins.io/block?height="


def get_transactions_info(block_nb):
    try:
        response = requests.get(BASE_URL + str(block_nb))

    except Exception as e:
        print(
            f"Error occured when you tried to get a transaction info from block {block_nb}: {e}"
        )
        return

    if response.status_code != 200:
        print(f"Error! Status code: {response.status_code}")
        return

    json_data = response.json()

    try:
        transactions = json_data["result"]["block"]["data"]["txs"]

    except Exception as e:
        print(f"No such json key: {e}")
        return

    if len(transactions) == 0:
        print(f"There is no any transaction in block {block_nb}")
        return

    for transaction in transactions:
        try:
            decoded_transaction = base64.b64decode(transaction)
        except Exception as e:
            print(f"Transaction decoding error: {e}")
            return

        print(decoded_transaction)
