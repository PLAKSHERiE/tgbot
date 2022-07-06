from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("ip")

# webhook settings
WEBHOOK_HOST = env.str("WEBHOOK_HOST")
WEBHOOK_PATH = ''
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = env.str("WEBAPP_HOST")
WEBAPP_PORT = env.str("WEBAPP_PORT")
