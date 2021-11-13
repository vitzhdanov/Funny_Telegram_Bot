from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста

data = {
    'host': 'ec2-3-248-103-75.eu-west-1.compute.amazonaws.com',
    'user': 'qvxavzxoszeont',
    'port': '5432',
    'password': '164216941c5048324087e1b288154396fd7603007d0932c25ad66de586aa60cd',
    'database': 'dd3apc0rrk9pp6',
    'URI': 'postgres://qvxavzxoszeont:164216941c5048324087e1b288154396fd7603007d0932c25ad66de586aa60cd@ec2-3-248-103-75.eu-west-1.compute.amazonaws.com:5432/dd3apc0rrk9pp6',
    'CLI': 'heroku pg:psql postgresql-vertical-65958 --app postgres-remote'
}