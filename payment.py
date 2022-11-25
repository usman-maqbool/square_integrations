from square.client import Client
import os
from settings import SECRET_KEY

# set SQUARE_ACCESS_TOKEN='EAAAEFmAWxrT9lhB_MTp0sK4mID50T6DZBDSu2B3RmihFKWUG-hVnmJhUP9HQerB'

client = Client(
    # access_token=os.environ[SQUARE_ACCESS_TOKEN],
    access_token='EAAAEFmAWxrT9lhB_MTp0sK4mID50T6DZBDSu2B3RmihFKWUG-hVnmJhUP9HQerB',
    environment='sandbox'
    
    )

# List Payments
# def list_payments():
#     result = client.locations.list_locations()

#     if result.is_success():
#         for location in result.body['locations']:
#             print(f"{location['id']}: ", end="")
#             print(f"{location['name']}, ", end="")
#             print(f"{location['address']['address_line_1']}, ", end="")
#             print(f"{location['address']['locality']}")

#     elif result.is_error():
#         for error in result.errors:
#             print(error['category'])
#             print(error['code'])
#             print(error['detail'])

#     result = client.payments.list_payments()

#     if result.is_success():
#         print(result.body)
#     elif result.is_error():
#         print(result.errors)

# list_payments()


    # Create Payment
# def payments_create():
#     result = client.payments.create_payment(
#         body = {
#             "source_id": "cnon:card-nonce-ok",
#             "idempotency_key": "sandbox-sq0idb-tYrDejqbXYsuDP2qf3FkyQ",
#             "amount_money": {
#             "amount": 100,
#             "currency": "USD"
#             },
#             "app_fee_money": {
#             "amount": 31,
#             "currency": "USD"
#             },
#             "autocomplete": False,
#             "customer_id": "PJJW2V8DYZA6TXNQHFS4J2DGGC",
#             "location_id": "LJN570CEHH719",
#             "accept_partial_authorization": True,
#             "buyer_email_address": "test@test.com",
#             "billing_address": {
#             "address_line_1": "Lahore Punjab ",
#             "address_line_2": "Lahore Punjab ",
#             "address_line_3": "Lahore Punjab",
#             "locality": "Local",
#             "sublocality_2": "things",
#             "sublocality_3": "things",
#             "administrative_district_level_1": "Punjab",
#             "administrative_district_level_2": "Punjab",
#             "administrative_district_level_3": "Punjab",
#             "postal_code": "54700",
#             "country": "KH",
#             "first_name": "sarfarz",
#             "last_name": "Jahan"
#             },
#             "note": "no"
#         }
#     )

#     if result.is_success():
#         print(result.body)
#     elif result.is_error():
#         print(result.errors)

# payments_create()


# Update Payments
# def update_payment():
#     result = client.payments.update_payment(
#         payment_id = None,
#         body = {
#             "idempotency_key": "sandbox-sq0idb-tYrDejqbXYsuDP2qf3FkyQ"
#         }
#     )

#     if result.is_success():
#         print(result.body)
#     elif result.is_error():
#         print(result.errors)

# update_payment()


# Cancel Payments


# def cancel_payments():
#     result = client.payments.update_payment(

#         payment_id = None,

#         body = {
#             "idempotency_key": "sandbox-sq0idb-tYrDejqbXYsuDP2qf3FkyQ"
#         }
#     )

#     if result.is_success():
#         print(result.body)
#     elif result.is_error():
#         print(result.errors)

# cancel_payments()


# Complete Payments
def complete_payments():
    result = client.payments.complete_payment(
        payment_id = None,    
        body = {}
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

complete_payments()