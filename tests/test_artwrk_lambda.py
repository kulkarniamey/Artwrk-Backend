import unittest
from artwrk.artwrk_lambda.artwrk_lambda import lambda_handler

create_user_event={
    "operation":"create_user",
    "username":"prashant3",
    "email":"alumnijnec@gmail.com",
    "password":"jnec123",
    "type":"artist",
    }

sign_in_event={
    "operation":"sign_in",
    "username":"prashant3",
    "password":"jnec123",
    "type":"artist"
    }

change_password_event={
    "operation":"change_password",
    "username":"prashant3",
    "password":"jnec789",
    "type":"artist",
    "otp":"902001"
    }

change_password_authenticated_event={
    "operation":"change_password_authenticated",
    "user_id":"artist_prashant3",
    "old_password":"jnec123",
    "new_password":"jnec989"
    }

forgot_password_event={
    "operation":"forgot_password",
    "username":"prashant3",
    "type":"artist"
    }

resend_otp_event={
    "operation":"resend_otp",
    "username":"prashant3",
    "type":"artist"
    }

invalid_request_event={
    "operation":"create_user",
    "username":"prashant3",
    }

upvote_event={
    "operation":"upvote",
    "user_id":"abcd786",
    "post_id":"posts",
    }

get_posts_by_artists_event={
    "operation":"get_posts_by_artists",
    "user_id":"abcd786",
}

get_jobs_by_user_event={
    "operation":"get_jobs_by_user",
    "user_id":"1234",
    "type":"recruiter"
}

delete_user_event={
     "operation":"delete_user",
     "user_id":"artist_prashant3",
     "email":"alumnijnec@gmail.com",
    }

sign_in_success={
    'statusCode': 200,
    'token': {
    'user_id': 'artist_prashant3',
    'user_type': 'artist',
    'username': 'prashant3',
    'verified': 'False'
    }
}

success={
    "statusCode":200
    }

request_failed={
    "statusCode":403
    }

failed={
    "statusCode":409
    }
    
class TestArtWrkLambda(unittest.TestCase):
    def tearDown(self):
        lambda_handler(delete_user_event,"context")  
    def test_lambda_handler(self):
        self.assertEqual(lambda_handler(create_user_event,"context"),success)
        self.assertEqual(lambda_handler(sign_in_event,"context"),sign_in_success)
        self.assertEqual(lambda_handler(forgot_password_event,"context"),success)
        self.assertEqual(lambda_handler(resend_otp_event,"context"),success)
        self.assertEqual(lambda_handler(change_password_event,"context"),failed)
        self.assertEqual(lambda_handler(upvote_event,"context"),success)
        self.assertEqual(lambda_handler(get_posts_by_artists_event,"context"),success)
        self.assertEqual(lambda_handler(get_jobs_by_user_event,"context"),success)
        self.assertEqual(lambda_handler(change_password_authenticated_event,"context"),success)
        
        

if __name__=='__main__':
    unittest.main()