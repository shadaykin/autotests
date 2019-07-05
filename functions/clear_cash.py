from selenium import webdriver	

class Cookie():
	def clear_cash_func():
		profile = webdriver.FirefoxProfile()
		profile.set_preference("browser.cache.disk.enable", False)
		profile.set_preference("browser.cache.memory.enable", False)
		profile.set_preference("browser.cache.offline.enable", False)
		profile.set_preference("network.http.use-cache", False) 
		return profile