from core.conf.environ import env

if not env("DEBUG"):
    ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(" ")
    CORS_ALLOWED_ORIGINS = env("CORS_ALLOWED_ORIGINS").split(" ")

    # at this point CSRF only needed for admin actions
    CSRF_TRUSTED_ORIGINS = env("CSRF_TRUSTED_ORIGINS").split(" ")
    CSRF_COOKIE_HTTPONLY = True
    CSRF_COOKIE_SECURE = True
    print("NOT DEBUG!")
