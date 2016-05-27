#Accountable Politics
#test_forms.py

import unittest
import forms

class Test_Forms(unittest.TestCase):
    
    #TEST CASE SETUP#
    @classmethod
    def setUpClass(self):
        print("Initializing Test Instances...")
        
        print("> Creating Users: ", end='')
        #create a test user
        models.User.create_user(
            username="test_models_user",
            email="test_models_user@example.com",
            password="test_models_user_pw"
            )
        self.user = models.User.get(models.User.username == "test_models_user")
        
        print("User1 created", end='')
    
    def 
    
    
if __name__ == "__main__":
    unittest.main()