from artwrk.interfaces.interface import DAL_abstract
from artwrk.models.dynamodb import User,Artist,Recruiter,Post,Notification,Job,GSIModel,Score_vote
from artwrk.config.config import logger
import random
import jwt
import datetime
import boto3
import json
import requests
from requests_aws4auth import AWS4Auth

s3=boto3.resource('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('scoring_table')
region = 'ap-south-1'

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
                        batch.save(Artist(id=id,compositekey="profile",type=type,email=email,password=password,otp=otp,username=username,email_verification="False",skill_tags=[],education_history=[],employer_history=[],awards_recognition=[],followers={},following={},certificates=[],applied_jobs={},artist_score=0,liked_posts=[],profile_pic="https://artwrk-test-upload.s3.ap-south-1.amazonaws.com/default/default.png"))
                        batch.save(User(id=unique_email,compositekey="unique_email",password=password,user_id=id))
                    else:
                        batch.save(Recruiter(id=id,compositekey="profile",type=type,email=email,password=password,otp=otp,username=username,email_verification="False",liked_posts=[],admin_verification="False",awards_recognition=[],followers={},following={},profile_pic="https://artwrk-test-upload.s3.ap-south-1.amazonaws.com/default/default.png"))
                        batch.save(User(id=unique_email,compositekey="unique_email",password=password,user_id=id))
                        batch.save(User(id="applications",compositekey=id))
                        User_Repository.send_notification(['admin'],username+" has just joined Artwrk. Click to verify his profile.")
                return {"email":email,"otp":otp,'username':username}
            else:
                return False
        except Exception as e:
            logger.warning(e)
            return False

    def mark_as_read(self,user_id):
        try:
            for i in Notification.query(user_id,Notification.compositekey.startswith('notification')):
                if i.flag==0:
                    i.update([Notification.flag.set(1)])
            return True
        except Exception as e:
            logger.warning(e)
            return False

    def get_userid(self,username,type):
        if '@' in username:
            email="email#"+username
            user=self.get_object(email,'unique_email')
            if user:
                return user.user_id
            else:
                logger.warning("Email doesn't exists")
                return False

        else:
            id=type+"_"+username
            get=self.get_object(id,'profile')
            if get:
                return get.id
            else:
                logger.warning("User_id doesn't exists")
                return False

    def sign_in(self,username,password,type):
        try:
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
        except Exception as e:
            logger.log(e)
            return False
    
    def generate_otp(self,username,type):
        try:
            otp=str(random.randint(100000,999999))
            id=self.get_userid(username,type)
            if id:
                self.update_profile({"id":id,"otp":otp})
                user=self.get_object(id,'profile')
            if user:
                return {"otp":user.otp,"email":user.email,"username":user.username}
            else:
                return False
        except:
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

            followers={}

            following={}

            certificates=[]

            applied_jobs={}        

            liked_posts = []

            if user_id.startswith('artist'):
                user=Artist.get(user_id,'profile')

                a = user.followers
                for key in a:
                    followers[key]=a[key]

                a = user.following
                for key in a:
                    following[key]=a[key]                

                a = user.applied_jobs
                for key in a:
                    applied_jobs[key]=a[key]

                a = user.liked_posts
                for i in a:
                    liked_posts.append(i)

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
                            
                            'type':user.type,

                            'skill_tags':user.skill_tags,

                            'twitter_link':user.twitter_link,

                            'certificates':user.certificates,

                            'applied_jobs':applied_jobs,

                            'email':user.email,

                            'artist_type':user.artist_type,

                            'profile_pic':user.profile_pic,

                            'liked_posts':liked_posts,

                        }

            elif user_id.startswith("recruiter"):

                user=Recruiter.get(user_id,'profile')

                a = user.liked_posts
                for i in a:
                    liked_posts.append(i)

                a = user.followers
                for key in a:
                    followers[key]=a[key]

                a = user.following
                for key in a:
                    following[key]=a[key]
                    
                profile={
                            'user_id': user.id,
                            'awards_recognition':user.awards_recognition,
                            'email_verfication':user.email_verification,
                            'facebook_link':user.facebook_link,
                            'followers':followers,
                            'following':following,
                            'name':user.name,
                            'type':user.type,
                            'twitter_link':user.twitter_link,
                            'email':user.email,
                            'admin_verification':user.admin_verification,
                            'company_type':user.company_type,
                            'address':user.address,
                            'username':user.username,
                            'profile_pic':user.profile_pic,
                            'liked_posts':liked_posts,
                            }
            else:

                user=Recruiter.get(user_id,'profile')
                profile={
                            'user_id': user.id,
                            'awards_recognition':[],
                            'email_verfication':user.email_verification,
                            'facebook_link':"fb.com",
                            'followers':{},
                            'following':{},
                            'name':"admin",
                            'type':"admin",
                            'twitter_link':"twitter.com",
                            'email':user.email,
                            'admin_verification':True,
                            'company_type':"admin",
                            'address':"admin",
                            'username':"admin",
                            'profile_pic':user.profile_pic,
                            'liked_posts':[],
                            }                

            return profile

        except Exception as e:
            logger.info(e)
            return e

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
                        if key=="del_skill_tags":
                            actions.append(Artist.skill_tags.remove_indexes(event[key]))
                        if key=="del_awards_recognition":
                            actions.append(User.awards_recognition.remove_indexes(event[key]))
                        if key=="del_employer_history":
                            actions.append(Artist.employer_history.remove_indexes(event[key]))
                        if key=="del_education_history":
                            actions.append(Artist.education_history.remove_indexes(event[key]))
                        if key=="del_certificates":
                            index = event[key]
                            artist=Artist.get(event['id'],'profile')
                            certificate = artist.certificates[event[key]]
                            for key,value in certificate.items():
                                certificate_to_del = value
                            l = certificate_to_del.split('.com/')
                            b = l[1]
                            obj = s3.Object("artwrk-test-upload",b)
                            obj.delete()
                            actions.append(Artist.certificates.remove_indexes(index))
                            
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
                User_Repository.send_notification([event['recruiter_id']],"%s has applied to your job for %s"%(user.username,job.jobTitle))
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
                followerr=user1.followers
                
                following={}
                for key in followingg:
                    following[key]=followingg[key]

                follower={}
                for key in followerr:
                    follower[key]=followerr[key]

                if event['id'] in user2.following and event['other_id'] in user1.followers:
                    
                    del following[event['id']]
                    
                    del follower[event['other_id']]

                    actions=[]
                    actions.append(User.following.set(following))
                    user2.update(actions)

                    actions=[]
                    actions.append(User.followers.set(follower))
                    user1.update(actions)
                    print("remove")

                else:
                    print("1")
                    followingg[event['id']]=user1.username
                    actions.append(User.following.set(followingg))
                    user2.update(actions)

                    actions=[]
                    followerr[event['other_id']]=user2.username
                    actions.append(User.followers.set(followerr))
                    user1.update(actions)
                    
                    User_Repository.send_notification([event['other_id']],'%s has started following you.'%(user1.username))
                
                return True
            else:
                return False
        except Exception as e:
            print("errror")
            logger.warning(e)
            return False

    def get_all_notifications(self,event):
        try:
            a = []
            for i in Notification.query(event['id'],User.compositekey.startswith('notification'),scan_index_forward=False):
                a.append({"notification":i.notification,
                          "flag":i.flag,
                })
            return a
        except Exception as e:
            logger.warning(e)
            return False


    def get_post(self,event):
        try:
            post_meta = self.get_object(event['post_id'],'post_metadata')
            if post_meta:
                post_obj ={}
                post_obj['url'] = post_meta.url
                post_obj['description'] = post_meta.Description
                post_obj['vote_count']=post_meta.vote_count
                post_obj['title']=post_meta.Title

                rated = []
                try:
                    d = post_meta.rated_by
                    
                    for key in d:
                        rated.append({key:d[key]})
                
                except Exception as e:
                    print("error:",e)
                post_obj['rated_by'] = rated

                voter=[]
                try:
                    c = post_meta.voters
                    print("c: ",c)
                    for key in c:
                        b = {}
                        b[key]=c[key]
                        voter.append(b)
                
                except Exception as e:
                    print("e:",e)
                post_obj['voters'] = voter

                return post_obj
        except Exception as e:
            logger.warning(e)
            return False

    def get_job(self,event):
        try:
            job = self.get_object(event['id'],event['job_id'])
            if job:
                job_obj={}
                job_obj['url']=job.url
                job_obj['description']=job.Description
                job_obj['companyTitle'] = job.companyTitle
                job_obj['jobTitle'] = job.jobTitle
                a = job.applicants
                c=0
                for key in a:
                    c+=1
                job_obj['applicants_count'] = c
                return job_obj
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
    

    def get_jobs_by_user(self,id):
        jobs=[]
        try:
            job_list=Job.query(id,User.compositekey.startswith('job'))
            for i in job_list:
                jobs.append({
                    'jobId': i.compositekey,
                    'jobTitle':i.jobTitle, 
                    'companyTitle': i.companyTitle,
                    'description': i.Description,
                    'url': i.url,
                })
            return jobs

        except Exception as e:
            logger.warning(e)

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
            #Getting object of both users
            post=self.get_object(event['id'],event['post_id'])
            user=self.get_object(event['post_id'],'post_metadata')   
            upvoter=self.get_object(event['other_id'],"profile")   
            actions=[]    
            flag=1   
            new={}
            new_rated_by={}
            rated_by = post.rated_by

            if user: 
                #Validating whether the voter already exists      
                liked_by=user.voters      
                for i in liked_by:     
                    if event['other_id']!=i:
                        new[i]=liked_by[i]
                    else:    
                        flag=0
                for i in rated_by:
                    if event['other_id']!=i:
                        new_rated_by[i]=rated_by[i]
                    else:
                        continue

                if flag==0:
                    upvoteCount=user.vote_count-1     
                    voters = user.voters    
                    voters[event['other_id']]=upvoter.username  
                    actions.append(Post.vote_count.set(upvoteCount))   
                    actions.append(Post.voters.set(new)) 
                    user.update(actions)
                    post.update(actions)  
                    liked_posts=upvoter.liked_posts
                    liked_posts.remove(event['post_id'])
                    upvoter.update([User.liked_posts.set(liked_posts)])


                    rate_sum = 0
                    n=0
                    for key in new_rated_by:
                        rate_sum+=new_rated_by[key]
                        n+=1
                    if n!=0:
                        rate = rate_sum/n
                    else:
                        rate=0
                    #updating the ratings.
                    post.update([Artist.rated_by.set(new_rated_by),Artist.rate.set(rate)])
                    user.update([Artist.rated_by.set(new_rated_by),Artist.rate.set(rate)])
                    return True 

                           
                if flag==1:    
                    #Changes in Post metadata
                    liked_posts=upvoter.liked_posts
                    liked_posts.append(event['post_id'])
                    upvoter.update([User.liked_posts.set(liked_posts)])
                    upvoteCount=user.vote_count+1     
                    voters = user.voters    
                    voters[event['other_id']]=upvoter.username  
                    actions.append(Post.vote_count.set(upvoteCount))   
                    actions.append(Post.voters.set(voters)) 
                    
                    #update ratings
                    
                    rated_by[event['other_id']] = 3

                    #calculating the ratings for the post
                    rate_sum = 0
                    n=0
                    for key in rated_by:
                        rate_sum+=rated_by[key]
                        n+=1

                    rate = rate_sum/n

                    #updating the ratings.
                    post.update([Artist.rated_by.set(rated_by),Artist.rate.set(rate)])
                    user.update([Artist.rated_by.set(rated_by),Artist.rate.set(rate)])


                    #For triggering artist score lambda
                    if event['type'] =='artist':  
                        with Score_vote.batch_write() as batch:
                                batch.save(Score_vote(id=event['id'],compositekey='votePost',vote_count=upvoteCount,voters=voters)) 
    
                    #updating all actions 
                    try:    
                        user.update(actions)  
                        post.update(actions)   
                    except:  
                        print("upvoter id already exist")   

                    #Notification to the user 
                    User_Repository.send_notification([event['id']],upvoter.username+" liked your Artwork.")
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
            logger.warning(e)
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
                            logger.warning(e)   
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
                            logger.warning(e)
                            return False
        except Exception as e:
            logger.warning(e)
            return False

    def get_posts_by_user(self,event):
        try:
            a = []
            
            for i in Post.query(event['id'],User.compositekey.startswith('post'),scan_index_forward=False):
                try:
                    c = i.voters
                    voter={}
                    for key in c:
                        voter[key]=c[key]

                except Exception as e:
                    print(e)

                a.append(
                    {
                        'postid':i.compositekey,
                        'description':i.Description,
                        'title':i.Title,
                        'voters': voter,
                        'url': i.url,
                    }
                )
            return a
        except Exception as e:
            logger.warning(e)
            return False


    def get_all_jobs(self):
        try:
            a = []
            for i in GSIModel.index.query('job_metadata',scan_index_forward=False):
                a.append(
                    {
                        'jobId': i.id,
                        'jobTitle':i.jobTitle, 
                        'companyTitle': i.companyTitle,
                        'description': i.Description,
                        'url': i.url,
                        'recruiter_id': i.recruiter_id,
                    }
                )
            return a
        except Exception as e:
            logger.warning(e)
            return False
    
    def get_all_posts(self):
        try:
            a = []
        
            voter=[]
            print(1)
            for i in GSIModel.index.query('post_metadata',scan_index_forward=False):
                
                try:
                    c = i.voters
                    
                    for key in c:
                        b = {}
                        b[key]=c[key]
                        voter.append(b)
                
                except Exception as e:
                    print(e)
                
                

                a.append(
                    {
                        
                        'post_id': i.id,
                        'vote_count':i.vote_count, 
                        'voters': voter,
                        'description': i.Description,
                        'title':i.Title,
                        'url': i.url,
                        'recruiter_id': i.recruiter_id,
                        'date_time': i.date_time,                        
                    }
                )

            return a
        except Exception as e:
            logger.warning(e)
            return False
    

    def get_searched_profile(self,event):
        try:
            region = 'ap-south-1' # e.g. us-east-1
            service = 'es'
            credentials = boto3.Session().get_credentials()
            print("credentials: ",dir(credentials))
            awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)
            print("awsauth :",dir(awsauth ))
            host = 'https://search-search-artwrk-db-erknahlaqc6bdsgglednqkmdgy.ap-south-1.es.amazonaws.com'
            index = 'lambda-index'

            url = host + '/' + index + '/' + '_search'

            headers = { "Content-Type": "application/json" } 
            query = {
                "query": {
                    "match": {
                        "query": event['search']
                    }
                }
            }

            # ES 6.x requires an explicit Content-Type header
            headers = { "Content-Type": "application/json" }

            # Make the signed HTTP request
            r = requests.get(url, auth=awsauth, headers=headers, data=json.dumps(query))
            print(json.dumps(query))

            # Create the response and add some extra content to support CORS
            print("response:", r.text)

            #return r.text
            return True
        except Exception as e:
            logger.warning(e)
            return False

    def delete_post(self,event):
        try:
            #For obtaining key of the post
            post=self.get_object(event['id'],event['post_id'])
            Key=post.key
            
            object=s3.Object("artwrk-test-upload",Key) 
            object.delete()

            #Deleting row from dynamoDB
            with User.batch_write() as batch:
                    batch.delete(User(id=event['id'],compositekey=event['post_id']))
                    batch.delete(User(id=event['post_id'],compositekey='post_metadata'))

            return True
        except Exception as e:
            print(e)

    def delete_job(self,event):
        try:
            #For obtaining key of the job
            job=self.get_object(event['id'],event['job_id'])
            try:
                #If while posting job no image was provided
                Key=job.key
                if Key != "default/default.png":
                    object=s3.Object("artwrk-test-upload",Key) 
                    object.delete()
            except Exception as e:
                print("No image was provided")

            #Deleting row from dynamoDB
            with User.batch_write() as batch:
                    batch.delete(User(id=event['id'],compositekey=event['job_id']))
                    batch.delete(User(id=event['job_id'],compositekey='job_metadata'))
            return True
        except Exception as e:
            print(e)

    #Ratings to particular post is handled by the following function
    def rate_post(self,event):
        try:
            #get objects to be updated.
            post = self.get_object(event['id'],event['post_id'])
            post_meta = self.get_object(event['post_id'],'post_metadata')
            #adding user who rated the post.
            rated_by = post.rated_by
            rated_by[event['user_id']] = event['rate_score']

            #calculating the ratings for the post
            rate_sum = 0
            n=0
            for key in rated_by:
                rate_sum+=rated_by[key]
                n+=1

            rate = rate_sum/n

            #updating the ratings.
            post.update([Artist.rated_by.set(rated_by),Artist.rate.set(rate)])
            post_meta.update([Artist.rated_by.set(rated_by),Artist.rate.set(rate)])

            #sending notification to the host for the post has been .
            User_Repository.send_notification([event['id']],'%s has rated your post %s stars.'%(event['user_id'],event['rate_score']))
            
            return True
        except Exception as e:
            logger.warning(e)
            return False
        
    def update_timeline(self,event):
        try:
            #get user object
            user = self.get_object(event['id'],'profile')
            n =0 
            p =0
            action = []
            #if user wants to add posts to timeline
            if event['to_do'] =='add':
                # this is nothing but a queue like implementaion in Pynamodb ListAttribute of len=10.
                for _ in user.timeline:
                    n+=1
                for _ in event['posts']:
                    p+=1
                if n+p>10:
                    for _ in range(n+p-10):
                        user.update([Artist.timeline.remove_indexes(0)])
                    action.append(Artist.timeline.set(Artist.timeline.append(event['posts'])))
                else:
                    action.append(Artist.timeline.set(Artist.timeline.append(event['posts'])))
                user.update(action)
                return True
            else:
                #if user wants to remove posts from the timeline.
                for j in range(len(event['index'])):
                    event['index'][j]-=j
                print(event['index'])
                for i in event['index']:
                    user.update([Artist.timeline.remove_indexes(i)])
                return True 
        except Exception as e:
            logger.warning(e)
            return False

    #function returns the object of timeline consists of user posts.
    def get_timeline(self,event):
        try:
            user = self.get_object(event['id'],'profile')
            timeline_list = []
            for i in user.timeline:  
                post = self.get_object(i,'post_metadata')
                timeline_list.append(
                    {
                        'postid':i,
                        'description':post.Description,
                        'url': post.url,
                    }
                )
            print(timeline_list)
            return timeline_list
        except Exception as e:
            logger.warning(e)
            return False

    #fuction to update the post's description.
    def update_post(self,event):
        try:
            #get post object to be updated
            post = self.get_object(event['id'],event['post_id'])
            post_meta = self.get_object(event['post_id'],'post_metadata')

            #update the description of given post.
            post.update([Post.Description.set(event['new_description'])])  
            post_meta.update([Post.Description.set(event['new_description'])]) 
            print(post.Description)
            return True
        except Exception as e:
            logger.warning(e)
            return False
