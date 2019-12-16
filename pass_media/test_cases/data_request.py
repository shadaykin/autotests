account = {
	"phone": "+79096201687",
	"first_name": "test_name",
	"last_name": "test_last_name",
	"nickname": "test_nick",
	"emails_confirmed": [],
	"emails_unconfirmed": [],
	"gender": "m",
	"phone_country": "RU",
	"city": "Moscow",
	"city_guid": None,
	"birthdate": "11.01.1990",
	"age": 29,
	"required_fields": [],
	"optional_fields": [],
	"required_empty_only": False,
	"password_change_date": 0}

account_empty = {
	"phone": "+79096201687",
	"first_name": "",
	"last_name": "",
	"nickname": "",
	"emails_confirmed": [],
	"emails_unconfirmed": [],
	"gender": "",
	"phone_country": "RU",
	"city": "",
	"city_guid": None,
	"birthdate": None,
	"age": None,
	"required_fields": [],
	"optional_fields": [],
	"required_empty_only": False,
	"password_change_date": 0}


higher_ed = {
	"level":"higher",
	"institutions": [
		{"country":
			{"id": 1, "title": "Россия"},
		"city":
			{"id":375, "title": "Москва"},
		"university":
			{"id": 602, "title": "НИУ МЭИ"},
		"speciality": "спец",
		"degree": "Бакалавр",
		"year": "2020"}]
}


		
higher_unf_ed = {
	"level": "higher_unfinished",
	"institutions": [
		{"country":
			{"id": 1, "title": "Россия"},
		"city":
				{"id": 375, "title": "Москва"},
		"university":
				{"id": 602, "title": "НИУ МЭИ"},
		"speciality": "спец",
		"degree": "Бакалавр",
		"year": "2020"}]
}

general_ed = {
	"level": "general",
	"institutions": [
		{"year": "2020"}]
}
		
general_unf_ed = {
	"level": "general_unfinished",
	"institutions": [
		{"year": "2020"}]
}
		
special_ed = {
	"level": "special",
	"institutions": [
		{"speciality": "спец", "year": "2020"}]
}
		
special_unf_ed = {
	"level": "special_unfinished",
	"institutions": [
		{"speciality": "спец", "year": "2020"}]
}
