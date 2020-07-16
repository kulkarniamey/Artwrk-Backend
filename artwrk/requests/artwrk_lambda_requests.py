from artwrk.schemas.artwrk_schemas import Schemas
from artwrk.config.config import logger
from artwrk.service import Service

Service=Service()
class RequestValidator:
    def create_user_request(self,event):
        try:
            Schemas.Account.validate(event)
            return Service.create_user(event)
            
        except Exception as e:
            logger.warning(e)
            return False


    def sign_in_request(self,event):
        try:
            Schemas.Account.validate(event)
            return Service.sign_in(event)
        except Exception as e:
            logger.warning(e)
            return False


    def forgot_password_request(self,event):
        try:
            Schemas.Account.validate(event)
            return Service.forgot_password(event)
        except Exception as e:
            logger.warning(e)
            return False


    def resend_otp_request(self,event):
        try:
            Schemas.Account.validate(event)
            return Service.resend_otp(event)
        except Exception as e:
            logger.warning(e)
            return False

    def reset_password_request(self,event):
        try:
            Schemas.Account.validate(event)
            return Service.reset_password(event)
        except Exception as e:
            logger.warning(e)
            return False
    
    def change_password_request(self,event):
        try:
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
