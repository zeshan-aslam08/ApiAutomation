#############################**Login Testdata**########################################

payload = {
    'email': 'naina+65@xintsolutions.com',
    'password': '123456789'
}

invalid_payload = {
    'email': 'esaytdusaivdsad',
    'password': '6adtsadsadasysadls'
}

invalid_Name_payload = {
    'email': 'esaytdusaivdsad',
    'password': '123456789              '
}

valid_Password_payload = {
    'email': 'naina+65@xintsolutions.com',
    'password': '              '
}

Empty_payload = {
    'email': 'esaytdusaivdsad',
    'password': '6adtsadsadasysadls'
}
################################**Franchise_data**###########################################

franchise_payload = {'corporate_id': '1',
                     'franchise_id': 'MYTM00HH350',
                     'franchise_name': 'Dummy shop',
                     'lat': '31.4592908',
                     'lng': '74.2763764',
                     'franchise_user_name': 'Asad',
                     'phone': '43564567167674',
                     'cnic': '1233211233211',
                     'password': '123456',
                     'franchise_address': '63, Block R 1 Phase 2 joha town lahore',
                     'subscription_fee': '0',
                     'collect_amount': '100'}
