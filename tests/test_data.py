class TestData:
    create_user_event={
        "operation":"create_user",
        "username":"prashant3",
        "email":"alumnijnec@gmail.com",
        "password":"jnec123",
        "type":"artist",
        }

    delete_user_event={
        "operation":"delete_user",
        "user_id":"artist_prashant3",
        "email":"alumnijnec@gmail.com",
        }

    upvote_event={
        "operation":"upvote",
        "user_id":"abcd786",
        "post_id":"posts",
        "upvoter_id":"artist_prashant64321"
        }


    sign_in_event={
        "operation":"sign_in",
        "username":"prashant3",
        "password":"jnec123",
        "type":"artist"
        }

    reset_password_event={
        "operation":"reset_password",
        "username":"prashant3",
        "password":"jnec789",
        "type":"artist",
        "otp":"902001"
        }

    change_password_event={
        "operation":"change_password",
        "user_id":"artist_prashant3",
        "old_password":"jnec123",
        "new_password":"jnec989"
        }

    forgot_password_event={
        "operation":"forgot_password",
        "username":"prashant3",
        "type":"artist"
        }
    
    send_notification_event={
        "operation":"send_notification",
        "list":["artist_hritik","artist_naya_notification"],
        "notification":"artist"
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