from pydantic_settings import BaseSettings

class EnvQA(BaseSettings):
    TEST_ENVIRONMENT_NAME: str = "QA"
    
    TEST_USERS: dict = {
        "trader3": "password",
        "trader4": "password"  
    }
    
    DOMAINS: dict = {
        "example_com": "HTTP://WWW.EXAMPLE.COM/"    
    }
    