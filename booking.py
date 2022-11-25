from square.client import Client


client = Client(
    access_token='EAAAEFmAWxrT9lhB_MTp0sK4mID50T6DZBDSu2B3RmihFKWUG-hVnmJhUP9HQerB',
    environment='sandbox'
    )

# def booking_list():

#     result = client.bookings.list_bookings(
#         limit = 3,
#         cursor = "None",
#         location_id = "LJN570CEHH719"
# )

#     if result.is_success():
#         print(result.body)
#     elif result.is_error():
#         print(result.errors)

# booking_list()




# # When a seller does not have the Appointments Plus or Premium subscription plan,
# #  all the API calls targeted at the seller with buyer-level permissions and 
# # those with seller-level readable permissions succeed. However, API calls 
# # targeted at the seller with seller-level writeable permissions fail with a 403 
# # response containing the following error message:


# def create_booking():
#     result = client.bookings.create_booking(
#         body = {
#             "idempotency_key": "sandbox-sq0idb-tYrDejqbXYsuDP2qf3FkyQ",
#             "booking": {
#             "location_id": "LJN570CEHH719",
#             "customer_id": "PJJW2V8DYZA6TXNQHFS4J2DGGC",
#             "location_type": "CUSTOMER_LOCATION"
#             }
#         }
# )

#     if result.is_success():
#         print(result.body)
#     elif result.is_error():
#         print(result.errors)


# create_booking()


# def search_availibilty_booking():
#     result = client.bookings.search_availability(
#         body = {
#             "query": {
#                 "filter": {
#                     # A datetime value in RFC 3339 format indicating when the time range starts.
#                     "start_at_range": {
#                     "start_at": " 2022-11-19T16:39:57-08:00",
#                     "end_at": "2022-12-19T16:39:57-08:00"
#                     },
#                     "location_id": "LJN570CEHH719"
#                 }
#             }
#         }
#     )

#     if result.is_success():
#         print(result.body)
#     elif result.is_error():
#         print(result.errors)


# search_availibilty_booking()

# def retrieve_bussiness_booking_profile():
#     result = client.bookings.retrieve_business_booking_profile(
        
    
#     )
#     if result.is_success():
#         print(result.body)
#     elif result.is_error():
#         print(result.errors)


# retrieve_bussiness_booking_profile()

# def list_team_member():
#     result = client.bookings.list_team_member_booking_profiles(
        
#         bookable_only = True,
#         limit = 3,
#         cursor = None,
#         location_id = "LJN570CEHH719"
#         )

#     if result.is_success():
#         print(result.body)
#     elif result.is_error():
#         print(result.errors)

# list_team_member()

# Retrieve Booking

# def retrieve_booking():
#     result = client.bookings.retrieve_booking(
#         booking_id = "zkras0xv0xwswx"
#     )

#     if result.is_success():
#         print(result.body)
#     elif result.is_error():
#         print(result.errors, "error displaying")

# retrieve_booking()

# Update Booking

# def update_booking():
#     result = client.bookings.update_booking(
#         booking_id = "zkras0xv0xwswx",
#         body = {
#             "idempotency_key": "sandbox-sq0idb-tYrDejqbXYsuDP2qf3FkyQ",
#             "booking": {
#             "version": 2022,
#             "location_id": "LJN570CEHH719",
#             "customer_id": "PJJW2V8DYZA6TXNQHFS4J2DGGC",
#             "location_type": "PHONE"
#             }
#         }
#     )

#     if result.is_success():
#         print(result.body)
#     elif result.is_error():
#         print(result.errors)

# update_booking()



# Cancel booking

def cancel_booking():
    result = client.bookings.cancel_booking(
        booking_id = "zkras0xv0xwswx",
        body = {
            "idempotency_key": "21cb7cbe-ac21-4d43-b912-f0d25aafb9d5",
            "booking_version": 2022
        }
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

cancel_booking()