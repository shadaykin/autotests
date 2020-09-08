
enviroment = 'test_202'
gateway = 'yakassa'

tokens = dict(
    test_201='2efe49abccad96de57e7c96923eccf90f6b1886c',
    test_202='740ea2823503035e6fdef524db3ad81f77ea705c',
    test_301='2efe49abccad96de57e7c96923eccf90f6b1886c',
    other_201='79448704ddc07dd3831bd2e1daffb9d45351b401',
    other_202='5731680f5fc4c1079d4adc2ed17ed351138655df',
    other_301='3f2c75e7ff014f579dcb18aa5e3348d4fdc6b470'
)

email = 'shadayka152+test@gmail.com'
order_options = dict(
    return_url='https://uma.preprod.zxz.su/',
    fail_url='https://localhost'
)


enviroments = dict(
    test_201='https://merch.test-201.zxz.su/',
    test_202='https://merch.test-202.zxz.su/',
    test_301='https://merch.test-301.zxz.su/'
)

processing_endpoints = dict(
    order='api/processing/order/',
    deposit='api/processing/order/%s/deposit/',
    cancel='api/processing/order/%s/cancel/',
    binding='api/processing/binding/',
    refund='api/processing/order/%s/refund/'
)

cards_gpb = dict(
    cvc='123',
    expiration_month='12',
    expiration_year='24',
    success_num='4111111111111111',
    block_to_limit='4444444444446666',
    access_denied='4444444411111111',
    error_3DS='4444444499999999',
    error_3DS_2='5555555555555557',
    password='12345678')

cards_yakassa = dict(
    cvc='123',
    expiration_month='12',
    expiration_year='24',
    success_num='4111111111111111',
    block_to_limit='5555555555554600',
    card_expired='5555555555554543',
    error_3DS='5555555555554592',
    password='12345678')


