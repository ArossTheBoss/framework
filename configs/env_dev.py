from pydantic_settings import BaseSettings

class EnvDev(BaseSettings):
    
    TEST_ENVIRONMENT_NAME: str = "DEV"
    
    TEST_USERS: dict = {
        "trader1": "password",
        "trader2": "password"  
    }
    
    DOMAINS: dict = {
        "example_com": "HTTP://WWW.EXAMPLE.COM/"    
    }
    
    DATABSES: dict = {
        "mongo": "connection details",
        "postgress": "connection details"  
    }
    
    
    
    