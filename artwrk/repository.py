from .interfaces.interface import DAL_abstract
from .models.dynamodb import UserModel
from .config.config import logger
import random
import jwt

class User_Repository(DAL_abstract):
    def delete_user(self,user_id,email):
        unique_email='email#'+email
        user=self.get_object(unique_email,'unique_email')
        user1=self.get_object(user_id,'profile')
        if user and user1:
            user.delete()
            user1.delete()
            return True
        else:
            return False

    
    def create_user(self,username,email,password,type):
        id= type+"_"+username
        unique_email="email#"+email
        otp=str(random.randint(100000,999999))
        test_email=self.get_object(unique_email,'unique_email')
        test_id=self.get_object(id,'profile')
        if not test_email and not test_id:
            with UserModel.batch_write() as batch:
                    batch.save(UserModel(id=id,compositekey="profile",email=email,password=password,otp=otp,username=username))
                    batch.save(UserModel(id=unique_email,compositekey="unique_email",password=password,userid=id))
            return {"email":email,"otp":otp,'username':username}
        else:
            logger.warning("Username or email_id already exists")
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
                        {'username':user.username,'user_id': user.id,'user_type': type,'verified':user.verified},
                        'secret',
                        algorithm='HS256'
                        )
                    print(token.decode('UTF-8'))
                    token=jwt.decode(token,'secret',algorithms=['HS256'])
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

    def change_password_authenticated(self,user_id,old_password,new_password):
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

    def change_password(self,username,password,type,recieved_otp):
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
                    actions.append(UserModel.password.set(value))
                if key=="verified":
                    actions.append(UserModel.verified.set(value))
                if key=="otp":
                    actions.append(UserModel.otp.set(value))
            user.update(actions)
            return True
        else:
            return False
    
    def upvote(self,id,post_id,upvoter_id):
        post=self.get_object(id,post_id)
        upvoter=self.get_object(upvoter_id,"profile")
        actions=[]
        flag=1
        if post:        
            liked_by=post.liked_by
            for i in liked_by:
                if upvoter_id==i:
                    flag=0
            if flag==1:
                upvoteCount=post.upvote+1
                liked_by[upvoter_id]=upvoter.username
                actions.append(UserModel.upvote.set(upvoteCount))
                actions.append(UserModel.liked_by.set(liked_by))
                post.update(actions)
                return True
            else:
                return False
        else:
            return False

    def get_object(self,id,compositekey):
        try:
            object=UserModel.get(id,compositekey)
            return object
        except:
            logger.warning("No data found with id : "+id+"and composite key : "+compositekey)
            return False
    
    def get_posts_by_artists(self,id):
        data = []
        try:
            user=UserModel.query(id,UserModel.compositekey.startswith('post'))
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
                user=UserModel.query(id,UserModel.compositekey.startswith('post'))
            if type=="recruiter":
                user=UserModel.query(id,UserModel.compositekey.startswith('job'))
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
