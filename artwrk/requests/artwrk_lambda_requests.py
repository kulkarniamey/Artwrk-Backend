from artwrk.schemas.artwrk_schemas import Schemas
from artwrk.config.config import logger
from artwrk.service import Service

Service=Service()
class RequestHandler:
    def create_user_request(self,event):
        try:
            print("Create")
            Schemas.Account.validate(event)
            return Service.create_user(event)
            
        except Exception as e:
            logger.warning(e)
            return False


    def sign_in_request(self,event):
        try:
            print("SIGN")
            Schemas.Account.validate(event)
            return Service.sign_in(event)
        except Exception as e:
            logger.warning(e)
            return e


    def forgot_password_request(self,event):
        try:
            print("FORGOT")
            Schemas.Account.validate(event)
            return Service.forgot_password(event)
        except Exception as e:
            logger.warning(e)
            return False


    def resend_otp_request(self,event):
        try:
            print("Resend")
            Schemas.Account.validate(event)
            return Service.resend_otp(event)
        except Exception as e:
            logger.warning(e)
            return False

    def reset_password_request(self,event):
        try:
            print("Reset")
            Schemas.Account.validate(event)
            return Service.reset_password(event)
        except Exception as e:
            logger.warning(e)
            return False
    
    def change_password_request(self,event):
        try:
            print("CHANGE")
            Schemas.Account.validate(event)
            return Service.change_password(event)
        except Exception as e:
            logger.warning(e)
            return False
    
    def delete_user_request(self,event):
        try:
            Schemas.Account.validate(event)
            return Service.delete_user(event)
        except Exception as e:
            logger.warning(e)
            return False

    def upvote_request(self,event):
        try:
            Schemas.Post.validate(event)
            return Service.upvote(event)
        except Exception as e:
            logger.warning(e)
            return False

    def update_profile_request(self,event):
        try:
            Schemas.Profile.validate(event)
            return Service.update_profile(event)
        except Exception as e:
            logger.warning(e)
            return False

    def verify_account_request(self,event):
        try:
            Schemas.Account.validate(event)
            return Service.verify_account(event)
        except Exception as e:
            logger.warning(e)
            return False
    
    def apply_job(self,event):
        try:
            Schemas.Job.validate(event)
            return Service.apply_job(event)
        except Exception as e:
            logger.warning(e)
            return False

    def connect_to_users(self,event):
        try:
            Schemas.Profile.validate(event)
            return Service.connect_to_users(event)
        except Exception as e:
            logger.warning(e)
            return False

    def get_all_notifications(self,event):
        try:
            Schemas.Profile.validate(event)
            return Service.get_all_notifications(event)
        except Exception as e:
            logger.warning(e)
            return False
    
    def get_post(self,event):
        try:
            Schemas.Profile.validate(event)
            return Service.get_post(event)
        except Exception as e:
            logger.warning(e)
            return False

    def vote(self,event):
        try:
            Schemas.Profile.validate(event)
            return Service.vote(event)
        except Exception as e:
            logger.warning(e)
            return False

    def get_unverified_recruiter_list(self,event):
        try:
            Schemas.Profile.validate(event)
            return Service.get_unverified_recruiter_list(event)
        except Exception as e:
            logger.warning(e)
            return False

    def verify_delete_recruiter(self,event):
        try:
            Schemas.Profile.validate(event)
            return Service.verify_delete_recruiter(event)
        except Exception as e:
            logger.warning(e)
            return False

    def get_all_jobs_by_user(self,event):
        try:
            Schemas.Job.validate(event)
            return Service.get_all_jobs_by_user(event)
        except Exception as e:
            logger.warning(e)
            return False   

    def get_all_jobs(self):
        try:
            return Service.get_all_jobs()
        except Exception as e:
            logger.warning(e)
            return False        
    
    def mark_as_read(self,event):
        try:
            return Service.mark_as_read(event)
        except Exception as e:
            logger.warning(e)
            return False        

    def get_posts_by_user(self,event):
        try:
            Schemas.Post.validate(event)
            return Service.get_posts_by_user(event)
        except Exception as e:
            logger.warning(e)
            return False
    
    def get_profile(self,event):
        try:
            Schemas.Profile.validate(event)
            return Service.get_profile(event)
        except Exception as e:
            logger.warning(e)
            return False
        
    def get_searched_profile(self,event):
        try:
            Schemas.Profile.validate(event)
            return Service.get_searched_profile(event)
        except Exception as e:
            logger.warning(e)
            return False