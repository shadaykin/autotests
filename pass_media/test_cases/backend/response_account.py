higher_ed = {
	"level": "higher",
	"institutions": [
		{"id": 20327, "year": 2020, "speciality": "спец",
		"country": {"id": 1, "title": "Россия", "code": "RU"},
		"city": {"id": 375, "country" : 1, "title": "Москва", "area": None, "region": None},
		"degree": "Бакалавр", "education": 20259,
		"university": {"id": 602, "title": "НИУ МЭИ", "country": 1, "city": 375}}
	]}
	
higher_unf_ed =	{
	"level": "higher_unfinished",
	"institutions": [
		{"id":20327,"year": 2020, "speciality": "спец",
		"country": {"id": 1, "title": "Россия", "code": "RU"},
		"city":{"id": 375, "country": 1, "title": "Москва", "area": None, "region": None},
		"degree": "Бакалавр", "education": 20259,
		"university": {"id": 602, "title": "НИУ МЭИ", "country": 1, "city": 375}}
	]}
	
general_ed = {
	'institutions': [
		{'id': 20363, 'year': 2020, 'education': 20291}],
	'level': 'general'}
	
general_unf_ed = {
	'institutions': [
		{'id': 20363, 'year': 2020, 'education': 20291}],
	'level': 'general_unfinished'}

special_ed = {
	'level': 'special',
	'institutions': [
		{'id': 20366, 'speciality': 'спец', 'education': 20291, 'year': 2020}]}

special_unf_ed = {
	'level': 'special_unfinished',
	'institutions': [
		{'id': 20366, 'speciality': 'спец', 'education': 20291, 'year': 2020}]}

check_phone = {
	"success": True, "confirmed": True, "inactive": False,
	"has_password": True, "restore_password_window": 0}

check_phone_no_pwd = {
	"success": True, "confirmed": True, "inactive": False,
	"has_password": False, "restore_password_window": 0}

check_unreg_phone = {
	"success": False, "confirmed": False, "inactive": False,
	"has_password": False, "restore_password_window": 0}


