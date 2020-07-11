from artwrk.schemas.artwrk_schemas import Schemas
from artwrk.config.config import logger
from artwrk.service import User_Service


user=User_Service()
class ValidateRequest:
    def create_user(self,event):
        try:
            Schemas.create_user_schema.validate(event)
            return user.create_user(event)
            
        except Exception as e:
            logger.warning(e)
            return False


    def sign_in(self,event):
        try:
            Schemas.sign_in_schema.validate(event)
            return user.sign_in(event)
        except Exception as e:
            logger.warning(e)
            return False


    def forgot_password(self,event):
        try:
            Schemas.forgot_password_schema.validate(event)
            return user.forgot_password(event)
        except Exception as e:
            logger.warning(e)
            return False


    def resend_otp(self,event):
        try:
            Schemas.resend_otp_schema.validate(event)
            return user.resend_otp(event)
        except Exception as e:
            logger.warning(e)
            return False

    def reset_password(self,event):
        try:
            Schemas.reset_password_schema.validate(event)
            return user.reset_password(event)
        except Exception as e:
            logger.warning(e)
            return False
    
    def change_password(self,event):
        try:
            Schemas.change_password_schema.validate(event)
            return user.change_password(event)
        except Exception as e:
            logger.warning(e)
            return False
    
    def delete_user(self,event):
        try:
            return user.delete_user(event)
        except Exception as e:
            logger.warning(e)
            return False

    def upvote(self,event):
        try:
            return user.upvote(event)
        except Exception as e:
            logger.warning(e)
            return False
        
    def send_notification(self,event):
        try:
            return user.send_notification(event)
        except Exception as e:
            logger.warning(e)
            return False