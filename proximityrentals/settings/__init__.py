import environment

if environment.env() == "production":
    from .production import *
elif environment.env() == "development":
    from .development import *
