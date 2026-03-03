import os

class Settings:
    PROJECT_NAME = "MiBackend"
    DEBUG = os.getenv("DEBUG", "False") == "True"
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    DATABASE_PATH = os.getenv("DATABASE_PATH",
            "/home/lunarlau/Trabajo/'Proyectos para Portfolio'/Full-Stack/Databases/WorldBank/")
    SECRET_KEY = os.getenv("SECRET_KEY", "1234")

settings = Settings()
