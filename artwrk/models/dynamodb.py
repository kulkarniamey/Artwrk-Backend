from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute,NumberAttribute,ListAttribute,MapAttribute

class User(Model):
    class Meta:
        table_name = 'new'
        region = 'us-east-1'
        aws_access_key_id = 'AKIAVFG6GGAGG3ZN2STD'
        aws_secret_access_key = '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'
        host = 'https://dynamodb.us-east-1.amazonaws.com'
    id = UnicodeAttribute(hash_key=True)
    compositekey = UnicodeAttribute(range_key=True)
    email = UnicodeAttribute(null=True)
    password = UnicodeAttribute(null=True)
    userid=UnicodeAttribute(null=True)
    name = UnicodeAttribute(null=True)
    profile_pic= UnicodeAttribute(null=True)
    otp=UnicodeAttribute(null=True)
    username=UnicodeAttribute(null=True)
    email_verification=UnicodeAttribute(null=True)
    following = MapAttribute(null=True)
    followers = MapAttribute(null=True)
    awards_recognition = ListAttribute(null=True)
    facebook_link = UnicodeAttribute(null=True)
    twitter_link = UnicodeAttribute(null=True)
    phone= UnicodeAttribute(null=True)
    

class Artist(User):
    artist_type= UnicodeAttribute(null=True)
    artist_score=NumberAttribute(null=True)
    employer_history = ListAttribute(null=True)
    education_history = ListAttribute(null=True)
    skill_tags = ListAttribute(null=True)
    current_employer =UnicodeAttribute(null=True)


class Recruiter(User):
    admin_verification=UnicodeAttribute(null=True)
    company_type= UnicodeAttribute(null=True)
    address = UnicodeAttribute(null=True)

class Post(Model):
    class Meta:
        table_name = 'new'
        region = 'us-east-1'
        aws_access_key_id = 'AKIAVFG6GGAGG3ZN2STD'
        aws_secret_access_key = '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'
        host = 'https://dynamodb.us-east-1.amazonaws.com'
    id = UnicodeAttribute(hash_key=True)
    compositekey = UnicodeAttribute(range_key=True)
    url = UnicodeAttribute(null=True)
    time = UnicodeAttribute(null=True)
    caption = UnicodeAttribute(null=True)
    vote_count = NumberAttribute(null=True)
    voters = MapAttribute(null=True)

class Job(Model):
    class Meta:
        table_name = 'new'
        region = 'us-east-1'
        aws_access_key_id = 'AKIAVFG6GGAGG3ZN2STD'
        aws_secret_access_key = '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'
        host = 'https://dynamodb.us-east-1.amazonaws.com'
    id = UnicodeAttribute(hash_key=True)
    compositekey = UnicodeAttribute(range_key=True)
    url = UnicodeAttribute(null=True)
    time = UnicodeAttribute(null=True)
    content = UnicodeAttribute(null=True)
    applicants = MapAttribute(null=True)
    hiring_type= UnicodeAttribute(null=True)

class Notification(Model):
    class Meta:
        table_name = 'new'
        region = 'us-east-1'
        aws_access_key_id = 'AKIAVFG6GGAGG3ZN2STD'
        aws_secret_access_key = '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'
        host = 'https://dynamodb.us-east-1.amazonaws.com'
    id = UnicodeAttribute(hash_key=True)
    compositekey = UnicodeAttribute(range_key=True)
    time = UnicodeAttribute(null=True)
    notification = UnicodeAttribute(null=True)
    flag = NumberAttribute(null=True)