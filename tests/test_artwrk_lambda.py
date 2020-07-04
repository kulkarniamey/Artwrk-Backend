from tests.test_data import TestData
import unittest
from artwrk.artwrk_lambda.artwrk_lambda import lambda_handler

test_data=TestData()

class TestArtWrkLambda(unittest.TestCase):
    def tearDown(self):
        lambda_handler(test_data.delete_user_event,"context")  
    def test_lambda_handler(self):
        self.assertEqual(lambda_handler(test_data.create_user_event,"context"),test_data.success)
        self.assertEqual(lambda_handler(test_data.sign_in_event,"context"),test_data.sign_in_success)
        self.assertEqual(lambda_handler(test_data.forgot_password_event,"context"),test_data.success)
        self.assertEqual(lambda_handler(test_data.resend_otp_event,"context"),test_data.success)
        self.assertEqual(lambda_handler(test_data.change_password_event,"context"),test_data.failed)
        self.assertEqual(lambda_handler(test_data.upvote_event,"context"),test_data.success)
        self.assertEqual(lambda_handler(test_data.change_password_authenticated_event,"context"),test_data.success)
        
        

if __name__=='__main__':
    unittest.main()