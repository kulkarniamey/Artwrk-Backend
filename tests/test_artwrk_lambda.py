from tests.test_data import TestData
import unittest
from artwrk_common_lambda import lambda_handler
test_data=TestData()

class TestArtWrkLambda(unittest.TestCase):
    # def tearDown(self):
    #     lambda_handler(test_data.delete_user_event,"context")  
    def test_lambda_handler(self):
        # self.assertEqual(lambda_handler(test_data.create_user_event,"context"),test_data.success)
        # self.assertEqual(lambda_handler(test_data.sign_in_event,"context"),test_data.success)
        #self.assertEqual(lambda_handler(test_data.forgot_password_event,"context"),test_data.success)
        # self.assertEqual(lambda_handler(test_data.resend_otp_event,"context"),test_data.success)
        # self.assertEqual(lambda_handler(test_data.verify_account_event,"context"),test_data.success)
        # self.assertEqual(lambda_handler(test_data.reset_password_event,"context"),test_data.success)
        # self.assertEqual(lambda_handler(test_data.change_password_event,"context"),test_data.success)
        #self.assertEqual(lambda_handler(test_data.update_profile_event,"context"),test_data.success)
        # self.assertEqual(lambda_handler(test_data.apply_job_event,"context"),test_data.success)
        # self.assertEqual(lambda_handler(test_data.connect_to_users,"context"),test_data.success)
        # self.assertEqual(lambda_handler(test_data.get_all_notifications,"context"),test_data.success)
        #self.assertEqual(lambda_handler(test_data.get_post_event,"context"),test_data.success)
        self.assertEqual(lambda_handler(test_data.get_profile_event,"context"),test_data.success)
        # self.assertEqual(lambda_handler(test_data.vote_event,"context"),test_data.success)
        # self.assertEqual(lambda_handler(test_data.mark_as_read_event,"context"),test_data.success)
        # self.assertEqual(lambda_handler(test_data.get_unverified_recruiter_list_event,"context"),test_data.success)
        #self.assertEqual(lambda_handler(test_data.verify_delete_recruiter_event,"context"),test_data.success)
        # self.assertEqual(lambda_handler(test_data.get_all_jobs_by_user_event,"context"),test_data.success)
        # self.assertEqual(lambda_handler(test_data.get_posts_by_user_event,"context"),test_data.success)
        # self.assertEqual(lambda_handler(test_data.get_searched_profile_event,"context"),test_data.success)
        # self.assertEqual(lambda_handler(test_data.delete_post_event,"context"),test_data.success)
        #self.assertEqual(lambda_handler(test_data.delete_job_event,"context"),test_data.success)

if __name__=='__main__':
    unittest.main()