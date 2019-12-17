
stand_for_test = 'prod'

options = dict(
	phone='+79096201687',
	password='111111xX',
	email='autotestpm@yandex.ru',
	email_busy='shadayka152+test@gmail.com',
	prod='https://pass.media',
	test='https://passport.jw-test.zxz.su',
	stage='https://passport.jw-test-301.zxz.su',
	extra='https://passport.jw-test-202.zxz.su',
	cas='https://localhost111',
	oauth_pub='client_id=3sKYH0pUqZ8bkOG0RGn9aHXrN8pervq89XAP9TMa',
	oauth_conf='client_id=XTEOEH9aM80A46ZMUojVahecHG5yVwHz8wtnlwak' +
			   '&client_secret=vYOS9J5oFMpcuTcZfk6J8uJNfERegieDC96jSxM6EbFOHBbouB2vZFE4hXxxSh5gtgbVAgrzt8Nq3GRMCLhrpX1t7HTlYooFEIFkfm3APEY6UGlqXySVahDR5IK4U1ys'

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
	change_pwd='/api/accounts/edit/change_password/',
	check_pwd='/api/actions/check_restore_password/',
	city='/api/cities/autocomplete/',#?q=Мос
	ed='/api/education/profiles/',
	ed_country='/api/education/countries/',#?q=Рос
	ed_city='/api/education/cities/',#?q=Мос&country=2
	ed_univ='/api/education/universities/',#?q=ниу мэи&country_id=2
	)

endpoints_service = dict(
	service_info='/api/service_info/?service=',
	pmid='/api/accounts/pass_id/',
	api_key='/api/users/'
)