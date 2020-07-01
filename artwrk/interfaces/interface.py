import boto3
from abc import ABC,abstractmethod

class DAL_abstract(ABC):

#----------------------------------------------------------------------------------------------------
    
    @abstractmethod
    def create_user(self,username,email,password,type):
        pass
        #Returns a response 200_OK if the credentials are valid, else return 403_Forbidden
#     @abstractmethod
#     def sign_in(self,username_or_email,password,type):
#         pass
#         #Returns 200_OK with a token if credentials are valid, else return 403_Forbidden
# #-----------------------------------------------------------------------------------------------------    
#     #Seperate Model for Profile

#     @abstractmethod
#     def update_profile(self,user_id,profile_id,**update_args):
#         pass
#         #update Profile with arguments in kwargs
    
#     @abstractmethod
#     def get_profile(self,user_id,profile_id):
#         pass
#         #Returns a Json object with all the attributes in profile
# #------------------------------------------------------------------------------------------------------
#     @abstractmethod
#     def get_posts_by_artists(self,user_id):
#         pass
#         #Pass primary key as "user_id" and sort_key begins_with "post"
#         #returns json object for all jobs posted by the recruiter
# # ------------------------------------------------------------------------------------------------------

#     @abstractmethod
#     def get_jobs_by_recruiter(self,user_id):
#         pass
#         #Pass primary key as "user_id" and sort_key begins_with "jobs"
#         #returns json object for all jobs posted by the recruiter
#     @abstractmethod
#     def get_jobs_by_artist(self,user_id):
#         pass
#         #Pass primary key as "user_id" and sort_key begins_with "jobs"
#         #returns json object for all jobs applied by the user
#     @abstractmethod
#     def upvote(self,user_id_of_upvoter,post_id):
#         pass 
#         #increment the upvote variable by 1 and add user_id to the upvoters list
    @abstractmethod
    def get_posts_by_artists(self,user_id):
        pass
#         #Pass primary key as "user_id" and sort_key begins_with "post"
#         #returns json object for all jobs posted by the recruiter
# # ------------------------------------------------------------------------------------------------------

    @abstractmethod
    def get_jobs_by_user(self,user_id,type):
        pass


