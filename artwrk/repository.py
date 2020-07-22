from artwrk.interfaces.interface import DAL_abstract
from artwrk.models.dynamodb import User,Artist,Recruiter,Post,Notification,Job,GSIModel
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

    def validate_unique_constraints(self,username,email):
        unique_email="email#"+email
        test_email=self.get_object(unique_email,'unique_email')
        artist_username=self.get_object("artist_"+username,'profile')
        recruiter_username=self.get_object("recruiter_"+username,'profile') 
        if not test_email and not artist_username and not recruiter_username:
            return True
        else:
            return False     
    
    def create_user(self,username,email,password,type):
        try:
            unique_email="email#"+email
            id= type+"_"+username
            otp=str(random.randint(100000,999999))
            if self.validate_unique_constraints(username,email):
                with User.batch_write() as batch:
                    if type=='artist':
                        batch.save(Artist(id=id,compositekey="profile",email=email,password=password,otp=otp,username=username,email_verification="False",skill_tags=[],education_history=[],employer_history=[],awards_recognition=[],followers={},following={},certificates={},applied_jobs={},artist_score=0))
                        batch.save(User(id=unique_email,compositekey="unique_email",password=password,user_id=id))
                    else:
                        batch.save(Recruiter(id=id,compositekey="profile",email=email,password=password,otp=otp,username=username,email_verification="False",admin_verification="False",awards_recognition=[],followers={},following={}))
                        batch.save(User(id=unique_email,compositekey="unique_email",password=password,user_id=id))
                if type=='recruiter':
                    User_Repository.send_notification(['admin'],username+" has just joined Artwrk. Click to verify his profile.")
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
                        {'user_id': user.id,'user_type': type,'username':user.username,'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=180)},
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
        print(otp)
        id=self.get_userid(username,type)
        if id:
            self.update_profile({"id":id,"otp":otp})
            user=self.get_object(id,'profile')
            print(user.otp)
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
                    print("TRUE")
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
                user=self.update_profile({"id":id,"email_verification":"True"})
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
                user=self.update_profile({"id":user.id,"password":new_password})
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
                user=self.update_profile({"id":id,"password":password})
                if user:
                    return True
            else:
                return False
        else:
            return False

    def get_profile(self,user_id):
        try:
            followers=dict()
            following=dict()
            certificates=dict()
            applied_jobs=dict()            
            if user_id.startswith('artist'):
                user=Artist.get(user_id,'profile')
                for i in user.followers:
                    followers[i]=user.followers[i]
                for i in user.certificates:
                    certificates[i]=user.certificates[i]
                for i in user.following:
                    following[i]=user.following[i]
                for i in user.applied_jobs:
                    applied_jobs[i]=user.applied_jobs[i]
                profile={
                            'user_id': user.id,
                            'username': user.username,
                            'artist_score':user.artist_score,
                            'awards_recognition':user.awards_recognition,
                            'current_employer':user.current_employer,
                            'education_history':user.education_history,
                            'email_verfication':user.email_verification,
                            'employer_history':user.employer_history,
                            'facebook_link':user.facebook_link,
                            'followers':followers,
                            'following':following,
                            'name':user.name,
                            'skill_tags':user.skill_tags,
                            'twitter_link':user.twitter_link,
                            'certificates':certificates,
                            'applied_jobs':applied_jobs,
                            'email':user.email,
                            'artist_type':user.artist_type,

                        }
            elif user_id.startswith("recruiter"):
                user=Recruiter.get(user_id,'profile')
                for i in user.followers:
                    followers[i]=user.followers[i]
                for i in user.following:
                    following[i]=user.following[i]
                profile={
                            'user_id': user.id,
                            'awards_recognition':user.awards_recognition,
                            'email_verfication':user.email_verification,
                            'facebook_link':user.facebook_link,
                            'followers':followers,
                            'following':following,
                            'name':user.name,
                            'twitter_link':user.twitter_link,
                            'email':user.email,
                            'admin_verification':user.admin_verification,
                            'company_type':user.company_type,
                            'address':user.address,
                            
                            }
            return profile
        except Exception as e:
            logger.info(e)
            return False


    def update_profile(self,event):
        try:
            user= self.get_object(event['id'],'profile')
            if user:
                actions=[]
                for key in event:
                    if key == 'id':
                        pass
                    else:
                        if key=="employer_history":
                            actions.append(Artist.employer_history.set(Artist.employer_history.append(event[key])))
                        if key=="education_history":
                            actions.append(Artist.education_history.set(Artist.education_history.append(event[key])))
                        if key=="email_verification":
                            actions.append(Artist.email_verification.set(event[key]))
                        if key=="otp":
                            actions.append(User.otp.set(event[key]))                                
                        if key=="facebook_link":
                            actions.append(User.facebook_link.set(event[key]))
                        if key=="twitter_link":
                            actions.append(User.twitter_link.set(event[key]))
                        if key=="current_employer":
                            actions.append(Artist.current_employer.set(event[key]))
                        if key=="name":
                            actions.append(User.name.set(event[key]))
                        if key=="password":
                            actions.append(Artist.password.set(event[key]))
                        if key=="skill_tags":
                            actions.append(Artist.skill_tags.set(Artist.skill_tags.append(event[key])))
                        if key=="awards_recognition":
                            actions.append(User.awards_recognition.set(User.awards_recognition.append(event[key])))
                user.update(actions)
                return True
        except Exception as e:
            logger.warning(e)
            return False
    def apply_job(self,event):
        try:
            user = self.get_object(event['id'],'profile')
            job= self.get_object(event['recruiter_id'],event['job_id'])
            actions = []
            if job and user:
                job_apply = job.applicants
                job_apply[event['id']]=user.username
                actions.append(Job.applicants.set(job_apply))
                job.update(actions)

                actions = []   
                applied_job = user.applied_jobs
                applied_job[event['recruiter_id']]=event['job_id']
                actions.append(Artist.applied_jobs.set(applied_job))  
                user.update(actions)
                User_Repository.send_notification([event['recruiter_id']],"%s has applied to your job for %s"%(user.username,job.job_title))
                return True
        except Exception as e:
            logger.warning(e)   
            return False

    def connect_to_users(self,event):
        try:
            user1=self.get_object(event['id'],'profile')
            user2=self.get_object(event['other_id'],'profile')
            actions=[]

            if user1 and user2:
                followingg=user2.following
                followingg[event['id']]=user1.username
                actions.append(User.following.set(followingg))
                user2.update(actions)
            
                actions=[]
                follower=user1.followers
                follower[event['other_id']]=user2.username
                actions.append(User.followers.set(follower))
                user1.update(actions)    

                User_Repository.send_notification([event['other_id']],'%s has started following you.'%(user1.username))
                return True
            else:
                print("FAILURE")
                return False
        except Exception as e:
            logger.warning(e)
            return False

    def get_all_notifications(self,event):
        try:
            a = []
            for i in User.query(event['id'],User.compositekey.startswith('notification')):
                a.append(i.notification)
            return a
        except Exception as e:
            logger.warning(e)
            return False


    def get_post(self,event):
        try:
            post = self.get_object(event['id'],event['post_id'])
            if post:
                print(post.caption)
                print(post.url)
                return post
        except Exception as e:
            logger.warning(e)
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
    @classmethod
    def send_notification(self,to,notification):
        flag=0
        compositekey="notification_"+str(datetime.datetime.now().timestamp())
        for i in to:
            with Notification.batch_write() as batch:
                batch.save(Notification(id=i,compositekey=compositekey,notification=notification,flag=flag))          
        return True

    def vote(self,event):
        try:
            post=self.get_object(event['id'],event['post_id'])
            upvoter=self.get_object(event['other_id'],"profile")
            actions=[]
            flag=1
            if post:       
                liked_by=post.voters
                for i in liked_by:
                    if event['other_id']==i:
                        flag=0
                if flag==1:
                    upvoteCount=post.vote_count+1
                    voters = post.voters
                    voters[event['other_id']]=upvoter.username
                    actions.append(Post.vote_count.set(upvoteCount))
                    actions.append(Post.voters.set(voters))
                    post.update(actions)  
                    self.scoring(event['id'])
                    User_Repository.send_notification([event['id']],event['post_id']+" liked by "+event['other_id'])
                    return True 
        except Exception as e:
            logger.warning(e)
            return False


    def scoring(self,id):
        user=self.get_object(id,"profile")
        user_actions=[]
        artist_score=user.artist_score+10
        user_actions.append(Artist.artist_score.set(artist_score))
        user.update(user_actions)


    def get_unverified_recruiter_list(self,event):
        recruiters=[]
        try:
            # profile=self.get_object(id,'profile')
            # if profile.type == "admin" :
            if event['type'] == "admin":
                search=User.query("applications",User.compositekey.startswith('recruiter_'))
            for i in search:
                recruiters.append({
                    'recruiter_id': i.compositekey,
                })
            if recruiters:
                return recruiters
            else :
                return 'no recruiters pending verification'
        except Exception as e:
            logger.warning("Error in obtaining Unverified Recruiter list")
            print(e)
            return False


    def verify_delete_recruiter(self,event):
        try:
            # profile=self.get_object(id,'profile')
            # if profile.type == "admin"
            actions=[]
            if event['type'] == "admin":
                user=self.get_object(event['recruiter_id'],"profile")
                if event['recruiter_id'].startswith("recruiter") :
                    if event['activity'] == "valid" :
                        try:
                            actions.append(Recruiter.admin_verification.set("True"))
                            user.update(actions)
                            search= self.get_object("applications",event['recruiter_id'])
                            search.delete()
                            return True
                        except Exception as e:
                            logger.warning("Error in updating Recruiter Status to Valid")
                            print(e)    
                            return False
                    elif event['activity'] == "delete" :
                        try:
                            unique_email='email#'+user.email
                            user_mail=self.get_object(unique_email,'unique_email')
                            user_mail.delete()
                            user.delete()
                            search= self.get_object("applications",event['recruiter_id'])
                            search.delete()
                            return True
                        except Exception as e:
                            logger.warning("Error in deleting Recruiter Profile")
                            print(e)
                            return False
        except Exception as e:
            logger.warning("Error in updating Recruiter Status")
            print(e)
            return False

    def get_posts_by_user(self,event):
        try:
            a = []
            for i in User.query(event['id'],User.compositekey.startswith('post')):
                a.append(
                    {
                        'id': i.id,
                        'post_id': i.compositekey,
                        'url': i.url,
                    }
                )
            print(a)
            return a
        except Exception as e:
            logger.warning(e)
            return False

    def get_all_jobs_by_user(self,event):
        try:
            a = []
            for i in User.query(event['id'],User.compositekey.startswith('job')):
                a.append(
                    {
                        'id': i.id,
                        'job_id': i.compositekey,
                        'url': i.url,
                    }
                )
            print(a)
            return a
        except Exception as e:
            logger.warning(e)
            return False

    def get_all_jobs(self):
        try:
            a = []
            for i in GSIModel.index.query('job_metadata'):
                a.append(
                    {
                        
                        'job_id': i.id,
                        'url': i.url,
                    }
                )
            print(a)
            return a
        except Exception as e:
            logger.warning(e)
            return False
    