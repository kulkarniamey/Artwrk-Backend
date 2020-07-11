from .repository import User_Repository
from email.mime.multipart import MIMEMultipart
from .config.config import email,password,smtp_host
from botocore.exceptions import ClientError
from email.mime.text import MIMEText
import jwt
import boto3
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
            message="<br><h2>Hey "+response['username']+",<br> Thank you for registering with ArtWrk! </h2><h2>Your OTP is : "+response['otp']+"</h2>"
            to=response['email']
            subject="Registration Successful!!"
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
            message="<br><h2>Hey "+response['username']+",</h2><h2> Your OTP is :"+response['otp']+"</h2>"
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
            message="<br><h2>Hey "+response['username']+",</h2><h2> Your OTP for changing password is :"+response['otp']+"</h2>"
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

    def change_password(self,event):
        changed=User_Repository.change_password(self,event['user_id'],event['old_password'],event['new_password'])
        if changed:
            return{
                "statusCode":200,
                }
        else:
            return{
                "statusCode":409,
                }
    
    def reset_password(self,event):
        changed=User_Repository.reset_password(self,event['username'],event['password'],event['type'],event['otp'])
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
    
    def send_notification(self,event):
        updated=User_Repository.send_notification(self,event['list'],event['notification'])
        if updated:
            return{
                "statusCode":200,
                }
        else:
            return{
                "statusCode":409,
                }

    
    def upvote(self,event):
        upvoted=User_Repository.upvote(self,event['user_id'],event['post_id'],event['upvoter_id'])
        if upvoted:
            return{
                "statusCode":200,
                }
        else:
            return{
                "statusCode":409,
                }

    
    def send_mail(self,to,subject,message):
        SENDER = "ArtWrk <artwrk.inbox@gmail.com>"
        RECIPIENT = to
        AWS_REGION = "ap-south-1"
        SUBJECT = subject
        BODY_TEXT = ("message"
                    )

        BODY_HTML = """<html>
        <head><style>.a{height:600px;width:600px;color:white;border:2px solid black;padding:20px;background-image: url('https://harpersbazaar.my/wp-content/uploads/2020/01/6.Shaq-Koyok-confession-of-palm-oil-1-1.jpg');}</style></head>
        <body><div class="a">
        <center><h1>"""+subject+"""</h1></center>
        """+message+"""</div>
        </body>
        </html>
            """   
        CHARSET = "UTF-8"
        client = boto3.client('ses',region_name=AWS_REGION)

        try:
            response = client.send_email(
                Destination={
                    'ToAddresses': [
                        RECIPIENT,
                    ],
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': CHARSET,
                            'Data': BODY_HTML,
                        },
                        'Text': {
                            'Charset': CHARSET,
                            'Data': BODY_TEXT,
                        },
                    },
                    'Subject': {
                        'Charset': CHARSET,
                        'Data': SUBJECT,
                    },
                },
                Source=SENDER,

            )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print("Email sent! Message ID:"),
            print(response['MessageId'])

    

    
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
            