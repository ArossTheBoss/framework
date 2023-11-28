import logging
from clients.rest_client import RestClient

LOG = logging.getLogger(__name__)

class ExampleComService(): 
       
    def __init__(self, config):
        self.rest_client = RestClient()
        self.config = config
        self.response = None
        self.base_url = self._set_base_url()
        
    
    def get_status_code(self):
        url = self.base_url + "/"
        try:
            self.response = self.rest_client.get(url=url, params={})
            LOG.info("")
        except Exception as e:
            LOG.error(e)
        return self.response
    
    def _set_base_url(self):
        self.base_url = self.config['DOMAINS']['example_com']
        return self.base_url
        
        
        
        
    
  
        
    
    
    
    