from django.core.management.utils import get_random_secret_key

CONFIG_STRING = (
    """
SECRET_KEY='%s'
DEBUG=True
ALLOWED_HOSTS=.localhost, .127.0.0.1
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
""".strip()
    % get_random_secret_key()
)

# Writing our configuration file to '.env'
with open(".env", "w") as env:
    env.write(CONFIG_STRING)
    print("\n .env has been generated \n")
