from pydantic import Field, PositiveInt

from core.base_config import BaseConfig


class TelethonConfig(BaseConfig):
    tg_session_name: str = Field(..., env="TG_SESSION_NAME")
    tg_api_id: PositiveInt = Field(..., env="TG_API_ID")
    tg_api_hash: str = Field(..., env="TG_API_HASH")

telethon_config = TelethonConfig()
