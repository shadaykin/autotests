
enviroment = 'test_202'
gateway = 'gpb'

tokens = dict(
    test_201='6186fcdfb79316b97050652571cf3075e76a2c5c',
    test_202='740ea2823503035e6fdef524db3ad81f77ea705c',
    test_301='2edda4a529b9184688f46d82c61dc7d98cef43ed',
    other_201='5460cddbb9460e9a02f368451f80c5c85806a14e',
    other_202='5731680f5fc4c1079d4adc2ed17ed351138655df',
    other_301='645c120d3accdbcb902d757399eff755e1f69f0a'
)

email = 'shadayka152@gmail.com'
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


