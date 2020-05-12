
stand_for_test = 'stage'  # ['stage', 'test', 'extra', 'prod']

browser = 'chrome'  # ['chrome', 'firefox', 'safari']

options = dict(
	phone='+79096201687',
	phone2='80012345678',
	phone_no_pwd='%2B80036985214',
	birthdate='11.04.2000',
	password='111111xX',
	email='autotestpm@yandex.ru',
	email_busy='shadayka152+test@gmail.com',
	prod='https://pass.media',
	test='https://passport.test-201.zxz.su',
	stage='https://passport.test-301.zxz.su',
	extra='https://passport.test-202.zxz.su',
	cas='https://localhost111',
	oauth_pub='client_id=3sKYH0pUqZ8bkOG0RGn9aHXrN8pervq89XAP9TMa',
	oauth_conf='client_id=XTEOEH9aM80A46ZMUojVahecHG5yVwHz8wtnlwak' +
			   '&client_secret=vYOS9J5oFMpcuTcZfk6J8uJNfERegieDC96jSxM6EbFOHBbouB2vZFE4hXxxSh5gtgbVAgrzt8Nq3GRMCLhrpX1t7HTlYooFEIFkfm3APEY6UGlqXySVahDR5IK4U1ys',
	api_key_prod='96618d5e24e19e760600296fb3d9dad1f529e08caa8c18f17c1a3b0f410a48cb',
	api_key='c41350d8e80f15e2dca47fc5637cf208ac9b015feecdcdff8ea319f68ed89a51'
)


endpoints_email = dict(
	email='/api/emails/',
	email_confirm='/api/emails/confirm/',
	email_remove='/api/emails/remove/',
	send_email_conf='/api/send_email_confirmation/'
)

emails_excess = dict(
	email1='shadayka152+1@gmail.com',
	email2='shadayka152+2@gmail.com',
	email3='shadayka152+3@gmail.com',
	email4='shadayka152+4@gmail.com',
	email5='shadayka152+5@gmail.com'
)

endpoints_account =dict(
	edit='/api/accounts/edit/',
	register='/api/accounts/register/',
	logout='/cas/logout/',
	change_pwd='/api/accounts/edit/change_password/',
	check_pwd='/api/actions/check_restore_password/',
	city='/api/cities/autocomplete/',#?q=Мос
	ed='/api/education/profiles/',
	ed_country='/api/education/countries/',#?q=Рос
	ed_city='/api/education/cities/',#?q=Мос&country=2
	ed_univ='/api/education/universities/',#?q=ниу мэи&country_id=2,
	check_phone='/api/actions/check_phone/?phone=',
	subcription='/api/subscriptions/',
	promo='/api/promos/'
	)

endpoints_service = dict(
	service_info='/api/service_info/?service=',
	app_info='/api/application_info/?',
	pmid='/api/accounts/pass_id/',
	api_key='/api/users/'
)
