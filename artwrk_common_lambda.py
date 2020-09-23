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
    if operation=='rate_post':
        return request_handler.rate_post(event)
    if operation=='get_post':
        return request_handler.get_post(event)
    if operation=='get_job':
        return request_handler.get_job(event)
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
    if operation=='get_all_posts':
        return request_handler.get_all_posts()
    if operation=='mark_as_read':
        return request_handler.mark_as_read(event)
    if operation=='get_searched_profile':
        return request_handler.get_searched_profile(event)   
    if operation=='delete_post':
        return request_handler.delete_post(event)  
    if operation=='delete_job':
        return request_handler.delete_job(event)
    if operation=='get_all_posts':
        return request_handler.get_all_posts()  
    if operation=='update_timeline':
        return request_handler.update_timeline(event)
    if operation=='get_timeline':
        return request_handler.get_timeline(event)
    if operation=='update_post':
        return request_handler.update_post(event)
    else:
        return "INVALID OPERATION"   
    
     


# a=lambda_handler({"operation":"get_all_jobs","authorizationToken":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoicmVjcnVpdGVyX2FydHdyayIsInVzZXJfdHlwZSI6ImFydGlzdCIsImV4cCI6MTU5NTM4NzIyOX0.wO_orRm1dHN3r8vWf2sF0cgrRGpfl5I-j0nnBVKWAtA"},"context")
# print(a)