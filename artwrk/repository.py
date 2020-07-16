from artwrk.interfaces.interface import DAL_abstract
from artwrk.models.dynamodb import User,Artist,Recruiter,Post,Notification
from artwrk.config.config import logger
import random
import jwt
import datetime
class User_Repository(DAL_abstract):
    def delete_user(self,user_id,email):
        unique_email='email#'+email
        email=self.get_object(unique_email,'unique_email')
        profile=self.get_object(user_id,'profile')
        if email and profile:
            profile.delete()
            email.delete()
            return True
        else:
            return False

    
    def create_user(self,username,email,password,type):
        try:
            id= type+"_"+username
            unique_email="email#"+email
            otp=str(random.randint(100000,999999))
            test_email=self.get_object(unique_email,'unique_email')
            artist_username=self.get_object("artist_"+username,'profile')
            recruiter_username=self.get_object("recruiter_"+username,'profile')
            if not test_email and not artist_username and not recruiter_username:
                with User.batch_write() as batch:
                    if type=='artist':
                        batch.save(Artist(id=id,compositekey="profile",email=email,password=password,otp=otp,username=username,email_verification="False",skill_tags=[],education_history=[],employer_history=[],awards_recognition=[],followers=[],following=[]))
                    else:
                        batch.save(Recruiter(id=id,compositekey="profile",email=email,password=password,otp=otp,username=username,email_verification="False",admin_verification="False",awards_recognition=[],followers=[],following=[]))
                    batch.save(User(id=unique_email,compositekey="unique_email",password=password,userid=id))
                if type=='recruiter':
                    User_Repository.send_notification(self,['admin'],username+" has just joined Artwrk. Click to verify his profile.")
                return {"email":email,"otp":otp,'username':username}
            else:
                return False
        except Exception as e:
            logger.warning(e)
            return False


    def get_userid(self,username,type):
        if '@' in username:
            email="email#"+username
            user=self.get_object(email,'unique_email')
            if user:
                logger.warning("Email doesn't exists")
                return False
            else:
                return user.userid
        else:
            id=type+"_"+username
            get=self.get_object(id,'profile')
            if get:
                return id
            else:
                logger.warning("User_id doesn't exists")
                return False

    def sign_in(self,username,password,type):
        id=self.get_userid(username,type)
        if id:
            user=self.get_object(id,'profile')
            if user:
                if password==user.password:
                    token = jwt.encode(
                        {'user_id': user.id,'user_type': type,'verified':user.verified,'exp':datetime.datetime.utcnow()+datetime.timedelta(seconds=60)},
                        'secret',
                        algorithm='HS256'
                        )
                    token=token.decode('UTF-8')
                    return token
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def generate_otp(self,username,type):
        otp=str(random.randint(100000,999999))
        id=self.get_userid(username,type)
        if id:
            self.update_profile(id,otp=otp)
            user=self.get_object(id,'profile')
        if user:
            return {"otp":user.otp,"email":user.email,"username":user.username}
        else:
            return False
    
    
    def verify_otp(self,username,type,recieved_otp):
        id=self.get_userid(username,type)
        if id:
            user=self.get_object(id,'profile')
            if user:
                if recieved_otp==user.otp:
                    return True
                else:
                    return False
        else:
            return False

    def verify_account(self,username,type,recieved_otp):
        id=self.get_userid(username,type)
        status=self.verify_otp(username,type,recieved_otp)
        if status:
            if id:
                user=self.update_profile(id,verified="True")
                if user:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def change_password(self,user_id,old_password,new_password):
        user=self.get_object(user_id,'profile')
        if user:
            if user.password==old_password:
                user=self.update_profile(user.id,password=new_password)
                return True
            else:
                logger.warning("Passwords didn't match!")
                return False
        else:
            return False

    def reset_password(self,username,password,type,recieved_otp):
        id=self.get_userid(username,type)
        status=self.verify_otp(username,type,recieved_otp)
        if status:
            if id:
                user=self.update_profile(id,password=password)
                if user:
                    return True
            else:
                return False
        else:
            return False

    def update_profile(self,id,**kwargs):
        user=self.get_object(id,'profile')
        if user:
            actions=[]
            for key,value in kwargs.items():
                if key=="password":
                    actions.append(User.password.set(value))
                if key=="verified":
                    actions.append(User.email_verification.set(value))
                if key=="otp":
                    actions.append(User.otp.set(value))
            user.update(actions)
            return True
        else:
            return False
    
    def upvote(self,id,post_id,upvoter_id):
        post=self.get_object(id,post_id)
        user=self.get_object(id,"profile")
        upvoter=self.get_object(upvoter_id,"profile")
        user_actions=[]
        actions=[]
        flag=1
        if post and user and upvoter:        
            liked_by=post.liked_by
            for i in liked_by:
                if upvoter_id==i:
                    flag=0
            if flag==1:
                upvoteCount=post.upvoteno+1
                artist_score=user.artist_score+10
                liked_by[upvoter_id]=upvoter.username
                user_actions.append(Artist.artist_score.set(artist_score))
                actions.append(Post.vote_count.set(upvoteCount))
                actions.append(Post.voters.set(liked_by))
                post.update(actions)
                user.update(user_actions)
                return True
            else:
                return False
        else:
            return False

    def get_object(self,id,compositekey):
        try:
            object=User.get(id,compositekey)
            return object
        except:
            logger.warning("No data found with id : "+id+" and composite key : "+compositekey)
            return False
    
    def get_posts_by_artists(self,id):
        data = []
        try:
            user=User.query(id,User.compositekey.startswith('post'))
            for i in user:
                data.append({
                    'id': i.id,
                    'post_id': i.compositekey,
                    'url': i.url
                })
            return data
        except Exception as e:
            logger.warning(e)
            return False

    def get_jobs_by_user(self,id,type):
        jobs=[]
        try:
            if type=="artist":
                user=User.query(id,User.compositekey.startswith('post'))
            if type=="recruiter":
                user=User.query(id,User.compositekey.startswith('job'))
            for i in user:
                jobs.append({
                    'id': i.id,
                    'post_id': i.compositekey,
                    'url': i.url
                })
            return jobs
        except Exception as e:
            logger.warning("Error in obtaining Jobs")
            print(e)

    def send_notification(self,to,notification):
        flag=0
        compositekey="notification_"+str(datetime.datetime.now().timestamp())
        for i in to:
            with Notification.batch_write() as batch:
                batch.save(Notification(id=i,compositekey=compositekey,notification=notification,flag=flag))          
        return True
