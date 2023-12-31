import logging
from conftest import Cache
from clients.auth_token import AuthToken
from services.domains.example_com.example_com_service import ExampleComService
from ui.scraper import SeleniumTrial

LOG = logging.getLogger(__name__)

class TestDevEnv():
    # This is just an example of the wiring
    RUNTIME_CONFIG = Cache._config
    
    @classmethod
    def setup_class(cls):
        '''Make all requests up front to save on call times'''
        cls.example_service = ExampleComService(config=cls.RUNTIME_CONFIG)
        cls.response_from_example_service = cls.example_service.get_status_code()
        
        cls.ui = SeleniumTrial()
        cls.paragraph = cls.ui.find_paragraph()
    
    @classmethod
    def teardown_class(cls):
        cls.ui.driver.close()
      
    
    def test_api(self):
        '''Dummy test 1'''
        resp_status_code = self.response_from_example_service.status_code
        assert resp_status_code == 200, f"Expected status code of 200 but recieved {resp_status_code}"
    
    def test_ui(self):
        '''Dummy test 1'''
        assert "This domain" in self.paragraph, "P tag did not contain expected text"
        
        
        