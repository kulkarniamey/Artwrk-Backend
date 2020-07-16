from artwrk.requests.artwrk_lambda_requests import RequestValidator
import jwt

request_validator=RequestValidator()
def lambda_handler(event, context):
    operation=event['operation']
    operations = {
        'create_user': request_validator.create_user_request(event),
        'delete_user': request_validator.delete_user_request(event),
        'sign_in': request_validator.sign_in_request(event),
        'forgot_password': request_validator.forgot_password_request(event),
        'resend_otp': request_validator.resend_otp_request(event),
        'reset_password': request_validator.reset_password_request(event),
        'change_password': request_validator.change_password_request(event),
        'verify_account': request_validator.verify_account_request(event),
        'upvote': request_validator.upvote_request(event),
        'update_profile': request_validator.update_profile_request(event),
    }
    if operation in operations:
        return operations[operation]
    else:
        raise ValueError('Unrecognized operation "{}"'.format(operation))

