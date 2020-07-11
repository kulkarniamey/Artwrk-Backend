from artwrk.requests.artwrk_lambda_requests import ValidateRequest
import jwt

request_handler=ValidateRequest()
def lambda_handler(event, context):
    operation=event['operation']
    operations = {
        'create_user': request_handler.create_user(event),
        'delete_user': request_handler.delete_user(event),
        'sign_in': request_handler.sign_in(event),
        'forgot_password': request_handler.forgot_password(event),
        'resend_otp': request_handler.resend_otp(event),
        'reset_password': request_handler.reset_password(event),
        'change_password': request_handler.change_password(event),
        'upvote': request_handler.upvote(event),
        'send_notification': request_handler.send_notification(event),
    }
    if operation in operations:
        return operations[operation]
    else:
        raise ValueError('Unrecognized operation "{}"'.format(operation))

