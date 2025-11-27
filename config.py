MYSQL_USER = "root"
MYSQL_PASSWORD = "adis"
MYSQL_HOST = "localhost"
MYSQL_DB = "ai_doc_platform"

SQLALCHEMY_DATABASE_URI = (
    f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}?charset=utf8"
)

SECRET_KEY = "supersecretkey"
