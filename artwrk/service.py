from .repository import User_Repository
from email.mime.multipart import MIMEMultipart
from .config.config import email,password,smtp_host
from email.mime.text import MIMEText
import smtplib
server=smtplib.SMTP_SSL(smtp_host,465)
server.login(email,password)


class User_Service(User_Repository):
    def delete_user(self,event):
        deleted=User_Repository.delete_user(self,event['user_id'],event['email'])
        if deleted:
            return{
                "statusCode":200,
                }
        else:
            return{
                "statusCode":409,
                }
    def create_user(self,event):
        response=User_Repository.create_user(self,event['username'],event['email'],event['password'],event['type'])
        if response:
            message="Hey "+response['username']+",\n\n Thank you for registering with ArtWrk!\n\n Your OTP is :"+response['otp']
            to=response['email']
            subject="Registration Successful"
            self.send_mail(to,subject,message)
            return{
                "statusCode":200,
                }
        else:
            return {
                "statusCode":409,
                }
        
    def sign_in(self,event):
        token=User_Repository.sign_in(self,event['username'],event['password'],event['type'])
        if token:
            return{
                "statusCode":200,
                "token":token
                }
        else:
            return{
                "statusCode":409
                }
    
    def resend_otp(self,event):
        response=User_Repository.generate_otp(self,event['username'],event['type'])
        if response:
            message="Hey "+response['username']+",\n\n Your OTP is :"+response['otp']
            to=response['email']
            subject="ArtWrk OTP"
            self.send_mail(to,subject,message)
            return{
                "statusCode":200,
                }
        else:
            return{
                "statusCode":409,
                }

    def forgot_password(self,event):
        response=User_Repository.generate_otp(self,event['username'],event['type'])
        if response:
            message="Hey "+response['username']+",\n\n Your OTP for changing password is :"+response['otp']
            to=response['email']
            subject="Forgot Password"
            self.send_mail(to,subject,message)
            return{
                "statusCode":200,
                }
        else:
            return{
                "statusCode":409,
                }

    
    def verify_account(self,username,type,otp):
        verified=User_Repository.verify_account(self,username,type,otp)
        if verified:
            return{
                "statusCode":200,
                }
        else:
            return{
                "statusCode":409,
                }

    def change_password_authenticated(self,event):
        changed=User_Repository.change_password_authenticated(self,event['user_id'],event['old_password'],event['new_password'])
        if changed:
            return{
                "statusCode":200,
                }
        else:
            return{
                "statusCode":409,
                }
    
    def change_password(self,event):
        changed=User_Repository.change_password(self,event['username'],event['password'],event['type'],event['otp'])
        if changed:
            return{
                "statusCode":200,
                }
        else:
            return{
                "statusCode":409,
                }

    
    def update_profile(self,id,**kwargs):
        updated=User_Repository.update_profile(self,id,**kwargs)
        if updated:
            return{
                "statusCode":200,
                }
        else:
            return{
                "statusCode":409,
                }

    
    def upvote(self,id,post_id):
        upvoted=User_Repository.upvote(self,id,post_id)
        if upvoted:
            return{
                "statusCode":200,
                }
        else:
            return{
                "statusCode":409,
                }


    def send_mail(self,to,subject,message):
            msg = MIMEMultipart()
            msg['From']="alumnijnec@gmail.com"
            msg['To']= to
            msg['Subject']=subject
            msg.attach(MIMEText(message, 'plain'))
            server.send_message(msg)
    
    def get_posts_by_artists(self,id):
        got=User_Repository.get_posts_by_artists(self,id)
        if got:
            return{
                "statusCode":200,
            }
        else:
            return{
                "statusCode":409
            }

    def get_jobs_by_user(self,id,type):
        got=User_Repository.get_jobs_by_user(self,id,type)
        if got:
            return{
                "statusCode":200,
            }
        else:
            return{
                "statusCode":409
            }
            