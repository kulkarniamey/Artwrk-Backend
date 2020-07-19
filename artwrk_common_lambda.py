from artwrk.requests.artwrk_lambda_requests import RequestValidator
import jwt

request_validator=RequestValidator()
def lambda_handler(event, context):
    operation=event['operation']
    if operation=='create_user':
        return request_validator.create_user_request(event)
    if operation=='delete_user':
        return request_validator.delete_user_request(event)
    if operation=='sign_in':
        return request_validator.sign_in_request(event)
    if operation=='forgot_password':
        return request_validator.forgot_password_request(event)
    if operation=='reset_password':
        return request_validator.reset_password_request(event)
    if operation=='resend_otp':
        return request_validator.resend_otp_request(event)
    if operation=='change_password':
        return request_validator.change_password_request(event)
    if operation=='verify_account':
        return request_validator.verify_account_request(event)
    if operation=='update_profile':
        return request_validator.update_profile_request(event)
    if operation=='verify_delete_recruiter':
        return request_validator.verify_delete_recruiter(event)
    if operation=='get_unverified_recruiter_list':
        return request_validator.get_unverified_recruiter_list(event)
    if operation=='get_posts_by_user':
        return request_validator.get_posts_by_user(event)
    if operation=='get_all_jobs_by_user':
        return request_validator.get_all_jobs_by_user(event)
    if operation=='vote':
        return request_validator.vote(event)
    if operation=='get_post':
        return request_validator.get_post(event)
    if operation=='connect_to_users':
        return request_validator.connect_to_users(event)
    if operation=='get_all_notifications':
        return request_validator.get_all_notifications(event)
    if operation=='apply_job':
        return request_validator.apply_job(event)
    if operation=='get_profile':
        return request_validator.get_profile(event)
    else:
        return "INVALID OPERATION"    


a=lambda_handler({"operation":"get_profile","authorizationToken":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoicmVjcnVpdGVyX2FydHdyayIsInVzZXJfdHlwZSI6ImFydGlzdCIsImV4cCI6MTU5NTM4NzIyOX0.wO_orRm1dHN3r8vWf2sF0cgrRGpfl5I-j0nnBVKWAtA"},"context")
print(a)