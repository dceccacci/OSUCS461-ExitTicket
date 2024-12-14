from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

env = "prod"
API_VERSION = 'v1'
SERVER = 'ceccaccd.mysql.pythonanywhere-services.com'
FRONTEND = 'ceccaccd.pythonanywhere.com'

@dataclass(repr=False)
class BaseConfig:
    reload: bool = True
    use_colors: bool = True
    port: int = int(os.getenv("PORT", 80))

@dataclass
class LocalConfig(BaseConfig):
    host: str = "127.0.0.1"

@dataclass
class StagingConfig(BaseConfig):
    host: str = "staging.osucapstone.com"

@dataclass
class ProdConfig(BaseConfig):
    host: str = os.getenv("HOST", "0.0.0.0")
    

configs = {
    "local" : LocalConfig(),
    "sandbox" : StagingConfig(),
    "prod" : ProdConfig()
}

FASTAPI_CONFIG = configs[env]

MySQL = {
	'local' : {
		'host' : '127.0.0.1',
		'port' : 3306,
		"user": "xxx",
        "passwd": "xxxx",
 		'db' : 'osucs461'
	},
	'sandbox' : {
		'host' : 'xxxx',
		'port' : 3306,
		"user": "xxx",
        "passwd": "xxxx",
 		'db' : 'osucs461'
	},
	'prod' : {
		'host': os.getenv("DB_HOST", "35.233.244.43"),
		'port': int(os.getenv("DB_PORT", 3306)),
		"user": os.getenv("DB_USER", "root"),
        "passwd": os.getenv("DB_PASSWORD"),
 		'db': os.getenv("DB_NAME", "osucs461")
	}
}[env]