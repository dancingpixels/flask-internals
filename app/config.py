
class Config():
	DEBUG = False
	TESTING = False
	SECRET_KEY = "When shall we abandon React?"

	DB_NAME = "production-db"
	DB_USERNAME = "admin"
	DB_PASSWORD = "example"

	SESSION_COOKIE_SECURE = True

class ProductionConfig(Config):
	# production attributes will be inherited from the Config Class
	pass

class Development(Config):
	DEBUG = True

	DB_NAME = "development-db"
	DB_USERNAME = "admin"
	DB_PASSWORD = "example"


	SESSION_COOKIE_SECURE = False

class TestingConfig():
	TESTING = True

	DB_NAME = "development-db"
	DB_USERNAME = "admin"
	DB_PASSWORD = "example"

	SESSION_COOKIE_SECURE = False

		