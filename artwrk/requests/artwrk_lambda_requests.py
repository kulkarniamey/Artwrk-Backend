from artwrk.schemas.artwrk_schemas import Schemas
from artwrk.config.config import logger




class ValidateRequest:
    def create_user(self,event):
        try:
            Schemas.create_user_schema.validate(event)
            return True
        except Exception as e:
            logger.warning(e)
            return False


    def sign_in(self,event):
        try:
            Schemas.sign_in_schema.validate(event)
            return True
        except Exception as e:
            logger.warning(e)
            return False


    def forgot_password(self,event):
        try:
            Schemas.forgot_password_schema.validate(event)
            return True
        except Exception as e:
            logger.warning(e)
            return False


    def resend_otp(self,event):
        try:
            Schemas.resend_otp_schema.validate(event)
            return True
        except Exception as e:
            logger.warning(e)
            return False


    def upvote(self,event):
        if len(event)==3:
            try:
                event['user_id']
                event['post_id']
            except:
                return False
            return True
        else:
            return False

    def change_password(self,event):
        try:
            Schemas.change_password_schema.validate(event)
            return True
        except Exception as e:
            logger.warning(e)
            return False
    
    def get_posts_by_artists(self,event):
        try:
            Schemas.get_posts_by_artist.validate(event)
            return True
        except Exception as e:
            logger.warning(e)
            return False
    
    def change_password_authenticated(self,event):
        try:
            Schemas.change_password_authenticated_schema.validate(event)
            return True
        except Exception as e:
            logger.warning(e)
            return False


    def get_jobs_by_user(self,event):
        if len(event)==3:
            try:
                event['user_id']
                event['type']
            except:
                return False
            return True
        else:
            return False
        