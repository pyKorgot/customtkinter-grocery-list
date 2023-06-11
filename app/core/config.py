from pydantic import BaseSettings


class Settings(BaseSettings):
    database_uri = 'sqlite:///food_tracker.sql'
    base_datetime_format = '%d.%m.%Y'


settings = Settings()
