import json
import os

import environ


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
environ.Env.read_env()

CORS_ORIGINS = [
    "*"
]

# Directories
STATIC_DIR = "static"






