from dataclasses import dataclass
import os

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
		'host' : os.environ.get("DB_HOST"),
		'port' : int(os.environ.get("DB_PORT")),
		"user": os.environ.get("DB_USER"),
        "passwd": os.environ.get("DB_PASSWORD"),
 		'db' : os.environ.get("DB_NAME")
	}
}[env]
