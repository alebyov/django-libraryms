from core.conf.environ import env

STORAGES = {
    "default": {
        "BACKEND": env("DEFAULT_FILE_STORAGE", cast=str, default="django.core.files.storage.FileSystemStorage"),
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}
if not env("DEBUG"):
    STORAGES["default"]["staticfiles"] = "whitenoise.storage.CompressedManifestStaticFilesStorage"

if env("USE_S3"):
    STORAGES["default"]["BACKEND"] = "storages.backends.s3boto3.S3Boto3Storage"

AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID", default=None)
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY", default=None)
AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME", default=None)
AWS_S3_REGION_NAME = env("AWS_S3_REGION_NAME", default=None)
AWS_S3_CUSTOM_DOMAIN = env("AWS_S3_CUSTOM_DOMAIN", default=None)
AWS_DEFAULT_ACL = env("AWS_DEFAULT_ACL", default="public-read")

AWS_QUERYSTRING_AUTH = False
AWS_S3_FILE_OVERWRITE = True
