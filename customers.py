from square.client import Client

client = Client(
    access_token="EAAAEFmAWxrT9lhB_MTp0sK4mID50T6DZBDSu2B3RmihFKWUG-hVnmJhUP9HQerB",
    environment="sandbox"
)

# def create_list_customer():
    
#     result = client.customers.list_customers(

#         cursor = None,
#         limit = 3,
#         sort_field = "DEFAULT",
#         sort_order = "ASC"
#     )

#     if result.is_success():
#         # print(result.body)
#         print(result.body['id'])
#     elif result.is_error():
#         print(result.errors)

# create_list_customer()



# def create_customer():

#     result = client.customers.create_customer(
#         body = {
#             "idempotency_key": "sandbox-sq0idb-tYrDejqbXYsuDP2qf3FkyQ",
#             "given_name": "rumors",
#             "family_name": "super",
#             "company_name": "djenericSol",
#             "nickname": "jahan",
#             "email_address": "test@test.com",
#             "note": "SUPER"
#         }
#     )

#     if result.is_success():
#         print(result.body)
#     elif result.is_error():
#         print(result.errors)


# create_customer()


# def search_customer():
#     result = client.customers.search_customers(
#     body = {}
#     )

#     if result.is_success():
#         print(result.body)
#     elif result.is_error():
#         print(result.errors)

# search_customer()

# def delete_customer():
#     result = client.customers.delete_customer(
#     customer_id = None
#     )

#     if result.is_success():
#         print(result.body)
#     elif result.is_error():
#         print(result.errors)

# delete_customer()


# def retrieve_customer():
#     result = client.customers.retrieve_customer(
#     customer_id = "PJJW2V8DYZA6TXNQHFS4J2DGGC"
#     )

#     if result.is_success():
#         print(result.body)
#     elif result.is_error():
#         print(result.errors)

# retrieve_customer()

def update_customer():
    result = client.customers.update_customer(
        customer_id = "PJJW2V8DYZA6TXNQHFS4J2DGGC",
        body = {
            "given_name": "superb",
            "family_name": "jahan",
            "company_name": "djenericSol",
            "email_address": "test@test.com"
        }
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

update_customer()