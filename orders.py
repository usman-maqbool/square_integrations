from square.client import Client


client = Client(
    access_token='EAAAEFmAWxrT9lhB_MTp0sK4mID50T6DZBDSu2B3RmihFKWUG-hVnmJhUP9HQerB',
    environment='sandbox'
)

# Create Order


# def create_order():
#     result = client.orders.create_order(
#         body = {
#             "order": {
#             "location_id": "LJN570CEHH719",
#             "customer_id": "PJJW2V8DYZA6TXNQHFS4J2DGGC"
#             },
#             "idempotency_key": "sandbox-sq0idb-tYrDejqbXYsuDP2qf3FkyQ"
#         }
#     )

#     if result.is_success():
#         print(result.body)
#     elif result.is_error():
#         print(result.errors)

# create_order()

# Batch retrive Order

# def batch_retrieve_order():
#     result = client.orders.batch_retrieve_orders(
#         body = {
#             "location_id": "LJN570CEHH719",
#             "order_ids": [
#                 "something"
#             ]
#         }
#     )

#     if result.is_success():
#         print(result.body)
#     elif result.is_error():
#         print(result.errors)

# batch_retrieve_order()


# Calculate Order

# def calculate_order():
#     result = client.orders.calculate_order(
#         body = {
#             "order": {
#             "location_id": "LJN570CEHH719",
#             "customer_id": "PJJW2V8DYZA6TXNQHFS4J2DGGC",
#             "state": "COMPLETED"
#             }
#         }
#     )

#     if result.is_success():
#         print(result.body,'calculate Order')
#     elif result.is_error():
#         print(result.errors)


# calculate_order()

# Search Order

# def search_order():
#     result = client.orders.search_orders(
#         body = {
#             "location_ids": [
#             "LJN570CEHH719"
#         ],
#         "cursor": None,
#         "limit": 1,
#         "return_entries": True
#         }
#     )

#     if result.is_success():
#         print(result.body)
#     elif result.is_error():
#         print(result.errors)

# search_order()

# Retrieve Order

# def retrieve_order():
#     result = client.orders.retrieve_order(
#         order_id = None
#     )

#     if result.is_success():
#         print(result.body)
#     elif result.is_error():
#         print(result.errors)


# retrieve_order()

# Updateorder

# def update_order():

#     result = client.orders.update_order(
#         order_id = "DREk7wJcyXNHqULq8JJ2iPAsluJZY",
#         body = {
#             "order": {
#         "location_id": "LJN570CEHH719",
#         "customer_id": "PJJW2V8DYZA6TXNQHFS4J2DGGC",
#         "state": "COMPLETED"
#         },
#         "idempotency_key": "sandbox-sq0idb-tYrDejqbXYsuDP2qf3FkyQ"
#         }
#     )

#     if result.is_success():
#         print(result.body)
#     elif result.is_error():
#         print(result.errors)

# update_order()

# Pay Order

# def pay_order():
#     result = client.orders.pay_order(
#         order_id = None,
#         body = {
#             "idempotency_key": "sandbox-sq0idb-tYrDejqbXYsuDP2qf3FkyQ"
#         }
#     )

#     if result.is_success():
#         print(result.body)
#     elif result.is_error():
#         print(result.errors)

# pay_order()

