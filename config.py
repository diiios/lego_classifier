class Config:
  DB_USER = 'admin'
  DB_PASSWORD = 'password'
  DB_HOST = 'localhost'
  DB_PORT = '5433'
  DB_NAME = 'lego_db'
  DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

config = Config()