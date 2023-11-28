import logging
from conftest import Cache
from clients.auth_token import AuthToken
from services.domains.example_com.example_com_service import ExampleComService

LOG = logging.getLogger(__name__)

class TestDevEnv():
    # This is just an example of the wiring
    RUNTIME_CONFIG = Cache._config
    
    @classmethod
    def setup_class(cls):
        '''Make all requests up front to save on call times'''
        cls.example_service = ExampleComService(config=cls.RUNTIME_CONFIG)
        cls.response_from_example_service = cls.example_service.get_status_code()
    
    def test_one(self):
        '''Dummy test'''
        resp_status_code = self.response_from_example_service.status_code
        assert resp_status_code == 200, f"Expected status code of 200 but recieved {resp_status_code}"
        
        