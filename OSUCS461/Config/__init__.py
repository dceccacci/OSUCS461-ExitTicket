from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

env = "prod"
API_VERSION = 'v1'
SERVER = 'osucapstone.com'
FRONTEND = 'osucapstone.com'

@dataclass(repr=False)
class BaseConfig:
    reload: bool = True
    use_colors: bool = True
    port: int = 8855

@dataclass
class LocalConfig(BaseConfig):
    host: str = "127.0.0.1"

@dataclass
class StagingConfig(BaseConfig):
    host: str = "staging.osucapstone.com"

@dataclass
class ProdConfig(BaseConfig):
    host: str = os.getenv("DB_HOST", "default_host")

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
		'host': os.getenv("DB_HOST", "default_host"),
		'port': int(os.getenv("DB_PORT", 3306)),
		"user": os.getenv("DB_USER", "default_user"),
        "passwd": os.getenv("DB_PASSWORD", "default_passwd"),
 		'db': os.getenv("DB_NAME", 'osucs461')
	}
}[env]

print("host:" + os.getenv("DB_HOST", "default_host"))
print("host" + int(os.getenv("DB_PORT", 3306)))