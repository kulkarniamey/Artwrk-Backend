from artwrk.repository import User_Repository
from artwrk.config.config import email,password,smtp_host
from botocore.exceptions import ClientError
import boto3
import jwt


class Service(User_Repository):
    def delete_user(self,event):
        deleted=User_Repository.delete_user(self,user_id=event['user_id'],email=event['email'])
        if deleted:
            return{
                "statusCode":200,
                }
        else:
            return{
                "statusCode":409,
                }
    def get_all_jobs(self):
        deleted=User_Repository.get_all_jobs(self)
        if deleted:
            return{
                "statusCode":200,
                "jobs": deleted
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
                "message":"Registration Successful.",
                }
        else:
            return {
                "statusCode":409,
                "message":"Email or Username already exists.",
                }
        
    def sign_in(self,event):
        token=User_Repository.sign_in(self,event['username'],event['password'],event['type'])
        if token:
            return{
                "statusCode":200,
                "token":token,
                "message":"Login successful",
                }
        else:
            return{
                "statusCode":409,
                "message":"Invalid username or password",
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
                "message":"OTP has been sent to email : "+response['email']
                }
        else:
            return{
                "statusCode":409,
                "message":"Invalid username or email.",
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
                "message":"OTP has been sent to the email : "+response['email'],
                }
        else:
            return{
                "statusCode":409,
                "message":"Invalid username or email.",
                }

    
    def verify_account(self,event):
        verified=User_Repository.verify_account(self,event['username'],event['type'],event['otp'])
        if verified:
            return{
                "statusCode":200,
                "message":"Account verification successful."
                }
        else:
            return{
                "statusCode":409,
                "message":"Invalid OTP."
                }

    def change_password(self,event):
        changed=User_Repository.change_password(self,event['user_id'],event['old_password'],event['new_password'])
        if changed:
            return{
                "statusCode":200,
                "message":"Password Changed Successfully."
                }
        else:
            return{
                "statusCode":409,
                "message":"Error in changing password."
                }
    
    def reset_password(self,event):
        changed=User_Repository.reset_password(self,event['username'],event['password'],event['type'],event['otp'])
        if changed:
            return{
                "statusCode":200,
                "message":"Password reset successful."
                }
        else:
            return{
                "statusCode":409,
                "message":"Invalid OTP."
                }

    
    def update_profile(self,event):
        updated=User_Repository.update_profile(self,event)
        if updated:
            return{
                "statusCode":200,
                "profile": User_Repository.get_profile(self,event['id'])
                }
        else:
            return{
                "statusCode":409,
                }

    def apply_job(self,event):
        got = User_Repository.apply_job(self,event)
        if got:
            return{
                "statusCode":200,
            }       
        else:
            return{
                "statusCode":409
            }


    
    def upvote(self,event):
        upvoted=User_Repository.vote(self,event)
        if upvoted:
            return{
                "statusCode":200,
                }
        else:
            return{
                "statusCode":409,
                "message":"User has already voted for the post."
                }

    
    def mark_as_read(self,event):
        marked=User_Repository.mark_as_read(self,event['user_id'])
        if marked:
            return{
                "statusCode":200,
                }
        else:
            return{
                "statusCode":409,
                "message":"Something went wrong."
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
            
    def connect_to_users(self,event):
        got = User_Repository.connect_to_users(self,event)
        if got:
            return{
                "statusCode":200,
            }       
        else:
            return{
                "statusCode":409
            }

    def get_all_notifications(self,event):
        notifications = User_Repository.get_all_notifications(self,event)
        if notifications:
            return{
                "statusCode":200,
                "notifications":notifications
            }       
        else:
            return{
                "statusCode":409
            }

    def get_post(self,event):
        got = User_Repository.get_post(self,event)
        if got:
            return{
                "statusCode":200,
            }       
        else:
            return{
                "statusCode":409
             }
    

    def vote(self,event):
        upvoted=User_Repository.vote(self,event)
        if upvoted:
            return{
                "statusCode":200,
                }
        else:
            return{
                "statusCode":409,
                }

    def get_unverified_recruiter_list(self,event):
        got=User_Repository.get_unverified_recruiter_list(self,event)
        print(got)
        if got and type(got) is list:
            return{
                "statusCode":200,
            }
        elif type(got) is str:
            return{
                "statusCode":204,
            }
        else:
            return{
                "statusCode":409,
            }

    def verify_delete_recruiter(self,event):
        got=User_Repository.verify_delete_recruiter(self,event)
        if got:
            return{
                "statusCode":200,
            }
        else:
            return{
                "statusCode":409
            }

    def get_posts_by_user(self,event):
        post_list=User_Repository.get_posts_by_user(self,event)
        if post_list:
            return{
                "statusCode":200,
                "posts":post_list
            }
        else:
            return{
                "statusCode":409
            }

    def get_all_jobs_by_user(self,event):
        got=User_Repository.get_jobs_by_user(self,event['id'])
        if got:
            return{
                "statusCode":200,
            }
        else:
            return{
                "statusCode":409
            }
        
    def get_profile(self,event):
        try:
            token=event['authorizationToken']
            token=jwt.decode(token,'secret',algorithms=['HS256'])
            got=User_Repository.get_profile(self,token['user_id'])
        except:
            got=User_Repository.get_profile(self,event['user_id'])
        if got:
            return{
                "statusCode":200,
                'profile': got,
            }
        else:
            print(got)
            return{
                "statusCode":409,
                "message":"Invalid User-id"
            }
    
    def get_searched_profile(self,event):
        got=User_Repository.get_searched_profile(self,event)
        if got:
            return{
                "statusCode":200,
            }
        else:
            return{
                "statusCode":409
            }
    