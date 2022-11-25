
from square.client import Client


client = Client(
    access_token='EAAAEFmAWxrT9lhB_MTp0sK4mID50T6DZBDSu2B3RmihFKWUG-hVnmJhUP9HQerB',
    environment='sandbox'
)




# def create_checkout():
#     result = client.checkout.create_checkout(
#     location_id = "location_id0",
#     body = {
#         "idempotency_key": "86ae1696-b1e3-4328-af6d-f1e04d947ad6",
#         "order": {
#         "order": {
#             "location_id": "location_id",
#             "reference_id": "reference_id",
#             "customer_id": "customer_id",
#             "line_items": [
#             {
#                 "name": "Printed T Shirt",
#                 "quantity": "2",
#                 "applied_taxes": [
#                 {
#                     "tax_uid": "38ze1696-z1e3-5628-af6d-f1e04d947fg3"
#                 }
#                 ],
#                 "applied_discounts": [
#                 {
#                     "discount_uid": "56ae1696-z1e3-9328-af6d-f1e04d947gd4"
#                 }
#                 ],
#                 "base_price_money": {
#                 "amount": 1500,
#                 "currency": "USD"
#                 }
#             },
#             {
#                 "name": "Slim Jeans",
#                 "quantity": "1",
#                 "base_price_money": {
#                 "amount": 2500,
#                 "currency": "USD"
#                 }
#             },
#             {
#                 "name": "Woven Sweater",
#                 "quantity": "3",
#                 "base_price_money": {
#                 "amount": 3500,
#                 "currency": "USD"
#                 }
#             }
#             ],
#             "taxes": [
#             {
#                 "uid": "38ze1696-z1e3-5628-af6d-f1e04d947fg3",
#                 "type": "INCLUSIVE",
#                 "percentage": "7.75",
#                 "scope": "LINE_ITEM"
#             }
#             ],
#             "discounts": [
#             {
#                 "uid": "56ae1696-z1e3-9328-af6d-f1e04d947gd4",
#                 "type": "FIXED_AMOUNT",
#                 "amount_money": {
#                 "amount": 100,
#                 "currency": "USD"
#                 },
#                 "scope": "LINE_ITEM"
#             }
#             ]
#         },
#         "idempotency_key": "12ae1696-z1e3-4328-af6d-f1e04d947gd4"
#         },
#         "ask_for_shipping_address": True,
#         "merchant_support_email": "merchant+support@website.com",
#         "pre_populate_buyer_email": "example@email.com",
#         "pre_populate_shipping_address": {
#         "address_line_1": "1455 Market St.",
#         "address_line_2": "Suite 600",
#         "locality": "San Francisco",
#         "administrative_district_level_1": "CA",
#         "postal_code": "94103",
#         "country": "US",
#         "first_name": "Jane",
#         "last_name": "Doe"
#         },
#         "redirect_url": "https://merchant.website.com/order-confirm",
#         "additional_recipients": [
#         {
#             "location_id": "057P5VYJ4A5X1",
#             "description": "Application fees",
#             "amount_money": {
#             "amount": 60,
#             "currency": "USD"
#             }
#         }
#         ]
#     }
#     )

#     if result.is_success():
#         print(result.body)
#     elif result.is_error():
#         print(result.errors)

# create_checkout()

# def list_payment():

#     result = client.checkout.list_payment_links(
#     cursor = None,
#     limit = 4
#     )

#     if result.is_success():
#         print(result.body)
#     elif result.is_error():
#         print(result.errors)

# list_payment()



# def create_payment_link():

#     result = client.checkout.create_payment_link(
#         body = {
#             "idempotency_key": "sandbox-sq0idb-tYrDejqbXYsuDP2qf3FkyQ",
#             "quick_pay": {
#             "name": "jahan",
#             "price_money": {
#                 "amount": 423,
#                 "currency": "USD"
#             },
#             "location_id": "LJN570CEHH719"
#             }
#         }
#     )

#     if result.is_success():
#         print(result.body)
#     elif result.is_error():
#         print(result.errors)

# create_payment_link()



# def delete_payments_link():

#     result = client.checkout.delete_payment_link(
#     id = "ZIXERTIM5HLFZC44"
#     )

#     if result.is_success():
#         print(result.body)
#     elif result.is_error():
#         print(result.errors)

# delete_payments_link()



# def retrieve_payment_link():
#     result = client.checkout.retrieve_payment_link(
#         id = "KV3W4HYV5XQ6COJR" 
#     )

#     if result.is_success():
#         print(result.body)
#     elif result.is_error():
#         print(result.errors)


# retrieve_payment_link()


def update_payment_link():
    result = client.checkout.update_payment_link(
       id = "UOWZFNVTUYGDAZEL",
        body = {
            "payment_link": {
            "version": 3,
            "created_at": "2022-11-25T15:56:55Z",
            "payment_note": "nothinf"
            }
        }
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

update_payment_link()