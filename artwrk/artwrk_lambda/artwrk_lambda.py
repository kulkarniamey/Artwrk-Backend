from artwrk.service import User_Service
from artwrk.requests.artwrk_lambda_requests import ValidateRequest
import jwt
user=User_Service()
validate_request=ValidateRequest()
def lambda_handler(event, context):
    operation=event['operation']
    if operation=='create_user':
        if validate_request.create_user(event):
            return user.create_user(event['username'],event['email'],event['password'],event['type'])
        else:
            return {"statusCode":403}
    if operation=='sign_in':
        if validate_request.sign_in(event):
            return user.sign_in(event['username'],event['password'],event['type'])
        else:
            return {"statusCode":403}
    if operation=='forgot_password':
        if validate_request.forgot_password(event):
            return user.forgot_password(event['username'],event['type'])
        else:
            return {"statusCode":403}
    if operation=='resend_otp':
        if validate_request.resend_otp(event):
            return user.resend_otp(event['username'],event['type'])
        else:
            return {"statusCode":403}
    if operation=='change_password':
        if validate_request.change_password(event):
            return user.change_password(event['username'],event['password'],event['type'],event['otp'])
        else:
            return {"statusCode":403}
    if operation=='upvote':
        if validate_request.upvote(event):
            return user.upvote(event['user_id'],event['post_id'])
        else:
            return {"statusCode":403}
    if operation=="delete_user":
        return user.delete_user(event['user_id'],event['email'])

    if operation=="get_posts_by_artists":
        if validate_request.get_posts_by_artists(event):
            return user.get_posts_by_artists(event['user_id'])
        else:
            return {"statusCode":403}
    
    if operation=="change_password_authenticated":
        if validate_request.change_password_authenticated(event):
            return user.change_password_authenticated(event['user_id'],event['old_password'],event['new_password'])
        else:
            return {"statusCode":403}
            
    if operation=="get_jobs_by_user":
        if validate_request.get_jobs_by_user(event):
            return user.get_jobs_by_user(event['user_id'],event['type'])
        else:
            return {"statusCode":403}


