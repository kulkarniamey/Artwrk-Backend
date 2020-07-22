<<<<<<< HEAD
from artwrk.requests.artwrk_lambda_requests import RequestHandler
import jwt

request_handler=RequestHandler()
def lambda_handler(event, context):
    operation=event['operation']
    if operation=='create_user':
        return request_handler.create_user_request(event)
    if operation=='delete_user':
        return request_handler.delete_user_request(event)
    if operation=='sign_in':
        return request_handler.sign_in_request(event)
    if operation=='forgot_password':
        return request_handler.forgot_password_request(event)
    if operation=='reset_password':
        return request_handler.reset_password_request(event)
    if operation=='resend_otp':
        return request_handler.resend_otp_request(event)
    if operation=='change_password':
        return request_handler.change_password_request(event)
    if operation=='verify_account':
        return request_handler.verify_account_request(event)
    if operation=='update_profile':
        return request_handler.update_profile_request(event)
    if operation=='verify_delete_recruiter':
        return request_handler.verify_delete_recruiter(event)
    if operation=='get_unverified_recruiter_list':
        return request_handler.get_unverified_recruiter_list(event)
    if operation=='get_posts_by_user':
        return request_handler.get_posts_by_user(event)
    if operation=='get_all_jobs_by_user':
        return request_handler.get_all_jobs_by_user(event)
    if operation=='vote':
        return request_handler.vote(event)
    if operation=='get_post':
        return request_handler.get_post(event)
    if operation=='connect_to_users':
        return request_handler.connect_to_users(event)
    if operation=='get_all_notifications':
        return request_handler.get_all_notifications(event)
    if operation=='apply_job':
        return request_handler.apply_job(event)
    if operation=='get_profile':
        return request_handler.get_profile(event)
    if operation=='get_all_jobs':
        return request_handler.get_all_jobs()        
=======
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
>>>>>>> 6bbd8089ac681d551324d66efe5520cedcbc3d9b
    else:
        return "INVALID OPERATION"    


<<<<<<< HEAD
a=lambda_handler({"operation":"get_all_jobs","authorizationToken":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoicmVjcnVpdGVyX2FydHdyayIsInVzZXJfdHlwZSI6ImFydGlzdCIsImV4cCI6MTU5NTM4NzIyOX0.wO_orRm1dHN3r8vWf2sF0cgrRGpfl5I-j0nnBVKWAtA"},"context")
=======
# a=lambda_handler({"operation":"get_profile","authorizationToken":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoicmVjcnVpdGVyX2FydHdyayIsInVzZXJfdHlwZSI6ImFydGlzdCIsImV4cCI6MTU5NTM4NzIyOX0.wO_orRm1dHN3r8vWf2sF0cgrRGpfl5I-j0nnBVKWAtA"},"context")

a=lambda_handler({
    "operation":"update_profile",
    "authorizationToken":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoicHJhc2hhbnQiLCJ1c2VyX3R5cGUiOiJhcnRpc3QiLCJleHAiOjE1OTQ5NDEzMzl9.7jvoJBNaR3OmCGFuglJPju1cNKxvWgoSKG9wEy6HyW0",
    "id":"artist_prashant123",
    "name":"Prashant Dolawat",
    "facebook_link":"abcd",
    "twitter_link":"defg",
    "employer_history":["Artwrk11334"],
    "skill_tags":["ASP.NET","C++"],
    "awards_recognition":["6* Codechef"],
    "education_history":["1"],
    "current_employer":"Infosys",
},"context")
>>>>>>> 6bbd8089ac681d551324d66efe5520cedcbc3d9b
print(a)