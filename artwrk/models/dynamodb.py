from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute,NumberAttribute,ListAttribute,MapAttribute
from pynamodb.indexes import GlobalSecondaryIndex, AllProjection
from artwrk.config.config import AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY,AWS_REGION,DYNAMODB_HOST,TABLE_NAME

class GSI(GlobalSecondaryIndex):
    """
    This class represents a global secondary index
    """
    class Meta:
        # index_name is optional, but can be provided to override the default name
        index_name = 'Gsi1'
        read_capacity_units = 2
        write_capacity_units = 2
        # All attributes are projected
        projection = AllProjection()
        region = AWS_REGION
        aws_access_key_id = AWS_ACCESS_KEY_ID
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY
        host = DYNAMODB_HOST

    # This attribute is the hash key for the index
    # Note that this attribute must also exist
    # in the model
    compositekey = UnicodeAttribute(hash_key=True)
    id = UnicodeAttribute(range_key=True)

class GSIModel(Model):
    
    class Meta:
        table_name = TABLE_NAME
        region = AWS_REGION
        aws_access_key_id = AWS_ACCESS_KEY_ID
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY
        host = DYNAMODB_HOST
    id = UnicodeAttribute(hash_key=True)
    compositekey = UnicodeAttribute(range_key=True)
    url = UnicodeAttribute(null=True)
    time = UnicodeAttribute(null=True)
    content = UnicodeAttribute(null=True)
    voters = MapAttribute(null=True)
    applicants = MapAttribute(null=True)
    date_time = UnicodeAttribute(null=True)
    hiring_type= UnicodeAttribute(null=True)
    jobTitle=UnicodeAttribute(null=True)
    companyTitle=UnicodeAttribute(null=True)
    Description=UnicodeAttribute(null=True)
    recruiter_id=UnicodeAttribute(null=True)
    date_time=UnicodeAttribute(null=True)
    vote_count=NumberAttribute(null=True)
    Title=UnicodeAttribute(null=True)
    index=GSI()

class User(Model):
    class Meta:
        table_name = TABLE_NAME
        region = AWS_REGION
        aws_access_key_id = AWS_ACCESS_KEY_ID
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY
        host = DYNAMODB_HOST
    id = UnicodeAttribute(hash_key=True)
    type = UnicodeAttribute(null=True)
    compositekey = UnicodeAttribute(range_key=True)
    email = UnicodeAttribute(null=True)
    password = UnicodeAttribute(null=True)
    name = UnicodeAttribute(null=True)
    profile_pic= UnicodeAttribute(null=True)
    otp=UnicodeAttribute(null=True)
    username=UnicodeAttribute(null=True)
    email_verification=UnicodeAttribute(null=True)
    following = MapAttribute(null=True)
    followers = MapAttribute(null=True)
    vote_count = NumberAttribute(null=True)    
    awards_recognition = ListAttribute(null=True)
    facebook_link = UnicodeAttribute(null=True)
    twitter_link = UnicodeAttribute(null=True)
    phone= UnicodeAttribute(null=True)
    user_id=UnicodeAttribute(null=True)
    voters = MapAttribute(null=True)  
    search=UnicodeAttribute(null=True)
    key=UnicodeAttribute(null=True)
    Description=UnicodeAttribute(null=True)
    url=UnicodeAttribute(null=True)
    companyTitle = UnicodeAttribute(null=True)
    jobTitle = UnicodeAttribute(null=True)
    applicants = MapAttribute(null=True)
    applied_jobs = MapAttribute(null=True)
    rated_by  =MapAttribute(null=True)
    liked_posts = ListAttribute(null=True)
    artist_score=NumberAttribute(null=True)
    timeline = ListAttribute(null=True)
    Title = UnicodeAttribute(null=True)

class Artist(User):
    class Meta:
        table_name = TABLE_NAME
        region = AWS_REGION
        aws_access_key_id = AWS_ACCESS_KEY_ID
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY
        host = DYNAMODB_HOST
    artist_type= UnicodeAttribute(null=True)
    artist_score=NumberAttribute(null=True)
    employer_history = ListAttribute(null=True)
    education_history = ListAttribute(null=True)
    skill_tags = ListAttribute(null=True)
    current_employer =UnicodeAttribute(null=True)
    certificates = ListAttribute(null=True)
    resume = UnicodeAttribute(null=True)
    applied_jobs=MapAttribute(null=True)
    rated_by = MapAttribute(null=True)
    rate=NumberAttribute(null=True)
    profile_pic= UnicodeAttribute(null=True)


class Recruiter(User):
    class Meta:
        table_name = TABLE_NAME
        region = AWS_REGION
        aws_access_key_id = AWS_ACCESS_KEY_ID
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY
        host = DYNAMODB_HOST
    admin_verification=UnicodeAttribute(null=True)
    company_type= UnicodeAttribute(null=True)
    address = UnicodeAttribute(null=True)
    profile_pic=UnicodeAttribute(null=True)


class Post(Model):
    class Meta:
        table_name = TABLE_NAME
        region = AWS_REGION
        aws_access_key_id = AWS_ACCESS_KEY_ID
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY
        host = DYNAMODB_HOST
    id = UnicodeAttribute(hash_key=True)
    compositekey = UnicodeAttribute(range_key=True)
    url = UnicodeAttribute(null=True)
    time = UnicodeAttribute(null=True)
    Description=UnicodeAttribute(null=True)
    vote_count = NumberAttribute(null=True)
    voters = MapAttribute(null=True)
    resume = UnicodeAttribute(null=True)
    applied_jobs=MapAttribute(null=True)
    rated_by = MapAttribute(null=True)
    rate=NumberAttribute(null=True)
    profile_pic= UnicodeAttribute(null=True)
    Title = UnicodeAttribute(null=True)
    artist_id = UnicodeAttribute(null=True)

class Job(Model):
    class Meta:
        table_name = TABLE_NAME
        region = AWS_REGION
        aws_access_key_id = AWS_ACCESS_KEY_ID
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY
        host = DYNAMODB_HOST
    id = UnicodeAttribute(hash_key=True)
    compositekey = UnicodeAttribute(range_key=True)
    url = UnicodeAttribute(null=True)
    time = UnicodeAttribute(null=True)
    content = UnicodeAttribute(null=True)
    applicants = MapAttribute(null=True)
    hiring_type= UnicodeAttribute(null=True)
    Description=UnicodeAttribute(null=True)
    companyTitle = UnicodeAttribute(null=True)
    jobTitle = UnicodeAttribute(null=True)

class Notification(Model):
    class Meta:
        table_name = TABLE_NAME
        region = AWS_REGION
        aws_access_key_id = AWS_ACCESS_KEY_ID
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY
        host = DYNAMODB_HOST
        
    id = UnicodeAttribute(hash_key=True)
    compositekey = UnicodeAttribute(range_key=True)
    time = UnicodeAttribute(null=True)
    notification = UnicodeAttribute(null=True)
    flag = NumberAttribute(null=True)
    link_id = UnicodeAttribute(null=True)

class Score_vote(Model):
    class Meta:
        table_name = 'scoring_table'
        region = 'ap-south-1'
        aws_access_key_id = 'AKIAVFG6GGAGG3ZN2STD'
        aws_secret_access_key = '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'
        host = 'https://dynamodb.ap-south-1.amazonaws.com'
    id = UnicodeAttribute(hash_key=True)
    compositekey = UnicodeAttribute(range_key=True)
    url = UnicodeAttribute(null=True)
    time = UnicodeAttribute(null=True)
    caption = UnicodeAttribute(null=True)
    vote_count = NumberAttribute(null=True)
    voters = MapAttribute(null=True)  
    post_id=UnicodeAttribute(null=True)  


# class ViewIndex(GlobalSecondaryIndex):
#     #This class represents a global secondary index
#     class Meta:
#         index_name = 'compositekey-id-index'
#         read_capacity_units = 1
#         write_capacity_units = 1
#         # All attributes are projected
#         projection = AllProjection()

#     view = NumberAttribute(default=0, hash_key=True)

# class TestModel(Model):
#     #A test model that uses a global secondary index
#     class Meta:
#         table_name = 'Artwrk'
#         region = 'ap-south-1'
#         aws_access_key_id = 'AKIAVFG6GGAGG3ZN2STD'
#         aws_secret_access_key = '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'
#         host = 'https://dynamodb.ap-south-1.amazonaws.com'
#     forum = UnicodeAttribute(hash_key=True)
#     thread = UnicodeAttribute(range_key=True)
#     view_index = ViewIndex()
#     view = NumberAttribute(default=0)
