class TestData:
    create_user_event={
        "operation":"create_user",
        "username":"prashant3",
        "email":"pdolawat654@gmail.com",
        "password":"jnec12345",
        "type":"artist",
        }

    delete_user_event={
        "operation":"delete_user",
        "user_id":"artist_prashant3",
        "email":"pdolawat654@gmail.com",
        }

    upvote_event={
        "operation":"upvote",
        "user_id":"abcd786",
        "post_id":"posts",
        "upvoter_id":"artist_prashant64321"
        }


    sign_in_event={
        "operation":"sign_in",
        "username":"pdolawat654@gmail.com",
        "password":"prashant",
        "type":"artist"
        }

    reset_password_event={
        "operation":"reset_password",
        "username":"prashant3",
        "password":"jnec789",
        "type":"artist",
        "otp":"184500"
        }

    change_password_event={
        "operation":"change_password",
        "user_id":"artist_prashant3",
        "old_password":"jnec789",
        "new_password":"jnec989"
        }

    apply_job_event={
        "operation":"apply_job",
        "authorizationToken":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoicHJhc2hhbnQiLCJ1c2VyX3R5cGUiOiJhcnRpc3QiLCJleHAiOjE1OTQ5NDEzMzl9.7jvoJBNaR3OmCGFuglJPju1cNKxvWgoSKG9wEy6HyW0",
        "id":"artist_vanshika",
        "recruiter_id":"recruiter_hrithik",
        "job_id":"job_timestamp_hrithik",
    }

    get_all_notifications={
        "operation":"get_all_notifications",
        "authorizationToken":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoicHJhc2hhbnQiLCJ1c2VyX3R5cGUiOiJhcnRpc3QiLCJleHAiOjE1OTQ5NDEzMzl9.7jvoJBNaR3OmCGFuglJPju1cNKxvWgoSKG9wEy6HyW0",
        "id":"artist_vanshika",
    }
    connect_to_users={
        "operation":"connect_to_users",
        "authorizationToken":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoicHJhc2hhbnQiLCJ1c2VyX3R5cGUiOiJhcnRpc3QiLCJleHAiOjE1OTQ5NDEzMzl9.7jvoJBNaR3OmCGFuglJPju1cNKxvWgoSKG9wEy6HyW0",
        "id":"artist_pallavi",
        "other_id":"artist_vanshika",
    }

    get_post_event={
        "operation":"get_post",
        "authorizationToken":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoicHJhc2hhbnQiLCJ1c2VyX3R5cGUiOiJhcnRpc3QiLCJleHAiOjE1OTQ5NDEzMzl9.7jvoJBNaR3OmCGFuglJPju1cNKxvWgoSKG9wEy6HyW0",
        "id":"artist_parimal1234",
        "post_id":"post_timestamp_userId",
    }

    get_job_event={
        "operation":"get_job",
        "authorizationToken":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoicHJhc2hhbnQiLCJ1c2VyX3R5cGUiOiJhcnRpc3QiLCJleHAiOjE1OTQ5NDEzMzl9.7jvoJBNaR3OmCGFuglJPju1cNKxvWgoSKG9wEy6HyW0",
        "id":"recruiter_parimal4567",
        "job_id":"job_1596792042.175569_parimal4567",
    }

    get_profile_event={
        "operation":"get_profile",
        # "authorizationToken":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoicHJhc2hhbnQiLCJ1c2VyX3R5cGUiOiJhcnRpc3QiLCJleHAiOjE1OTQ5NDEzMzl9.7jvoJBNaR3OmCGFuglJPju1cNKxvWgoSKG9wEy6HyW0",
        "user_id":"artist_pallavi",
    }
    vote_event={
        "operation":"vote",
        "authorizationToken":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoicHJhc2hhbnQiLCJ1c2VyX3R5cGUiOiJhcnRpc3QiLCJleHAiOjE1OTQ5NDEzMzl9.7jvoJBNaR3OmCGFuglJPju1cNKxvWgoSKG9wEy6HyW0",
        "id":"artist_parimal786",
        "post_id":"post_1595584445.81924_parimal786",
        "other_id":"artist_avnee",
        "type":"artist"
        }
    mark_as_read_event={
        "operation":"mark_as_read",
        "authorizationToken":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoicHJhc2hhbnQiLCJ1c2VyX3R5cGUiOiJhcnRpc3QiLCJleHAiOjE1OTQ5NDEzMzl9.7jvoJBNaR3OmCGFuglJPju1cNKxvWgoSKG9wEy6HyW0",
        "user_id":"admin",
        }
    get_unverified_recruiter_list_event={

        "operation":"get_unverified_recruiter_list",
        "authorizationToken":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoicHJhc2hhbnQiLCJ1c2VyX3R5cGUiOiJhcnRpc3QiLCJleHAiOjE1OTQ5NDEzMzl9.7jvoJBNaR3OmCGFuglJPju1cNKxvWgoSKG9wEy6HyW0",
        "id":"samyak",
        "type":"admin",
    }

    get_all_jobs_by_user_event={
        "operation":"get_all_jobs_by_user",
        "authorizationToken":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoicHJhc2hhbnQiLCJ1c2VyX3R5cGUiOiJhcnRpc3QiLCJleHAiOjE1OTQ5NDEzMzl9.7jvoJBNaR3OmCGFuglJPju1cNKxvWgoSKG9wEy6HyW0",
        "id":"recruiter_avnee",
    }

    get_posts_by_user_event={
        "operation":"get_posts_by_user",
        "authorizationToken":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoicHJhc2hhbnQiLCJ1c2VyX3R5cGUiOiJhcnRpc3QiLCJleHAiOjE1OTQ5NDEzMzl9.7jvoJBNaR3OmCGFuglJPju1cNKxvWgoSKG9wEy6HyW0",
        "id":"artist_avnee345",
    }
    verify_delete_recruiter_event={
        "operation":"verify_delete_recruiter",
        "authorizationToken":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoicHJhc2hhbnQiLCJ1c2VyX3R5cGUiOiJhcnRpc3QiLCJleHAiOjE1OTQ5NDEzMzl9.7jvoJBNaR3OmCGFuglJPju1cNKxvWgoSKG9wEy6HyW0",
        "id":"samyak",
        "type":"admin",
        "recruiter_id":"recruiter_hrithik",
        "activity":"delete",
    }

    forgot_password_event={
        "operation":"forgot_password",
        "username":"pdolawat654@gmail.com",
        "type":"artist"
        }
    verify_account_event={
        "operation":"verify_account",
        "username":"prashant3",
        "type":"artist",
        "otp":"184500"
        }
    
    get_searched_profile_event={
        "operation":"get_searched_profile",
        "search": "parimal"
    }

    delete_post_event={
        "operation":"delete_post",
        "id":"recruiter_parimal4567",
        "post_id":"post_1596715232.334853_parimal4567"
    }

    delete_job_event={
        "operation":"delete_job",
        "id":"recruiter_parimal4567",
        "job_id":"job_1596714541.107103_parimal4567",
        "authorizationToken":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiYXJ0aXN0X3BydXRodmkyIiwidXNlcl90eXBlIjoiYXJ0aXN0IiwidXNlcm5hbWUiOiJwcnV0aHZpMiIsImV4cCI6MTU5NjcyNDI0Mn0.B_6Zb_La1wgSb4_mR_tcvoUP_59P1gJ00emFONO9NxQ"
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

    update_profile_event={
        "operation":"update_profile",
        "authorizationToken":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoicHJhc2hhbnQiLCJ1c2VyX3R5cGUiOiJhcnRpc3QiLCJleHAiOjE1OTQ5NDEzMzl9.7jvoJBNaR3OmCGFuglJPju1cNKxvWgoSKG9wEy6HyW0",
        "id":"artist_pdolawat",
        "name":"prashant",
        "username":"p._078",
        "facebook_link":"abc",
        "twitter_link":"def",
        # "employer_history":["Artwrk1"],
        # "skill_tags":["ASP.NET"],
        # "awards_recognition":["6* Codechef"],
        # "education_history":["1"],
        "current_employer":"Infosys",
        "del_skill_tags": 0,
        "del_employer_history":0,
        "del_awards_recognition":0,
        "del_education_history":0,
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