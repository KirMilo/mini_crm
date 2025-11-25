from pydantic import BaseModel


class DbSettings(BaseModel):
    url: str = "sqlite+aiosqlite:///./mini_crm.db"


class Settings(BaseModel):
    db: DbSettings = DbSettings()


settings = Settings()
