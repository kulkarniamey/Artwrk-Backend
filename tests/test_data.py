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
        "id":"artist_pallavi",
        "recruiter_id":"recruiter_vdolawat",
        "job_id":"job_1596987093.61326_parimal4567",
    }

    get_all_notifications={
        "operation":"get_all_notifications",
        "authorizationToken":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoicHJhc2hhbnQiLCJ1c2VyX3R5cGUiOiJhcnRpc3QiLCJleHAiOjE1OTQ5NDEzMzl9.7jvoJBNaR3OmCGFuglJPju1cNKxvWgoSKG9wEy6HyW0",
        "id":"artist_huzaif99",
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
        "id":"artist_parimal67",
        "post_id":"post_1598628067.195_parimal67",
    }

    get_job_event={
        "operation":"get_job",
        "authorizationToken":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoicHJhc2hhbnQiLCJ1c2VyX3R5cGUiOiJhcnRpc3QiLCJleHAiOjE1OTQ5NDEzMzl9.7jvoJBNaR3OmCGFuglJPju1cNKxvWgoSKG9wEy6HyW0",
        "id":"recruiter_parimal4567",
        "job_id":"job_1596973848.605142_parimal4567",
    }

    get_profile_event={
        "operation":"get_profile",
        # "authorizationToken":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoicHJhc2hhbnQiLCJ1c2VyX3R5cGUiOiJhcnRpc3QiLCJleHAiOjE1OTQ5NDEzMzl9.7jvoJBNaR3OmCGFuglJPju1cNKxvWgoSKG9wEy6HyW0",
        "user_id":"admin_admin",
    }
    vote_event={
        "operation":"vote",
        "authorizationToken":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoicHJhc2hhbnQiLCJ1c2VyX3R5cGUiOiJhcnRpc3QiLCJleHAiOjE1OTQ5NDEzMzl9.7jvoJBNaR3OmCGFuglJPju1cNKxvWgoSKG9wEy6HyW0",
        "id":"artist_parimal67",
        "post_id":"post_1598628067.195_parimal67",
        "type":"artist"
        }

    rate_post_event={
        "operation":"rate_post",
        "authorizationToken":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoicHJhc2hhbnQiLCJ1c2VyX3R5cGUiOiJhcnRpc3QiLCJleHAiOjE1OTQ5NDEzMzl9.7jvoJBNaR3OmCGFuglJPju1cNKxvWgoSKG9wEy6HyW0",
        "id":"artist_huzaif99",
        "user_id":"artist_avnee",
        "post_id":"post_1598254152.23753_huzaif99",
        "rate_score":5,
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
        "id":"recruiter_vdolawat",
    }

    get_posts_by_user_event={
        "operation":"get_posts_by_user",
        "authorizationToken":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoicHJhc2hhbnQiLCJ1c2VyX3R5cGUiOiJhcnRpc3QiLCJleHAiOjE1OTQ5NDEzMzl9.7jvoJBNaR3OmCGFuglJPju1cNKxvWgoSKG9wEy6HyW0",
        "id":"artist_pdolawat",
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

    get_all_jobs={
        "operation":"get_all_jobs",
        "authorizationToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiYXJ0aXN0X3BydXRodmkyIiwidXNlcl90eXBlIjoiYXJ0aXN0IiwidXNlcm5hbWUiOiJwcnV0aHZpMiIsImV4cCI6MTU5Njg4NTU5Mn0.SyjyBD0rBzGTsuNrgcb0pNCpojIQ7gPcTV1wT_VhWr4"
    }
    get_all_posts={
        "operation":"get_all_posts",
        "authorizationToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiYXJ0aXN0X3BydXRodmkyIiwidXNlcl90eXBlIjoiYXJ0aXN0IiwidXNlcm5hbWUiOiJwcnV0aHZpMiIsImV4cCI6MTU5Njg4NTU5Mn0.SyjyBD0rBzGTsuNrgcb0pNCpojIQ7gPcTV1wT_VhWr4"
    }

    get_all_posts={
        "operation":"get_all_posts",
        "authorizationToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiYXJ0aXN0X3BydXRodmkyIiwidXNlcl90eXBlIjoiYXJ0aXN0IiwidXNlcm5hbWUiOiJwcnV0aHZpMiIsImV4cCI6MTU5Njg4NTU5Mn0.SyjyBD0rBzGTsuNrgcb0pNCpojIQ7gPcTV1wT_VhWr4"
    }

    delete_job_event={
        "operation":"delete_job",
        "id":"recruiter_vdolawat",
        "job_id":"job_1597557659.387179_vdolawat",
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
        "id":"artist_prashant",
        "name":"prashant",
        "username":"p._078",
        "facebook_link":"abc",
        "twitter_link":"def",
        "employer_history":["Artwrk1"],
        "skill_tags":["ASP.NET"],
        "awards_recognition":["6* Codechef"],
        "education_history":["1"],
        "current_employer":"Infosys",
        "del_skill_tags": 0,
        "del_employer_history":0,
        "del_awards_recognition":0,
        "del_education_history":0,
        "del_certificates":0,
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