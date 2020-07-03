from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute,NumberAttribute,ListAttribute,MapAttribute

class UserModel(Model):
    class Meta:
        table_name = 'Artwrk'
        region = 'us-east-1'
    id = UnicodeAttribute(hash_key=True)
    compositekey = UnicodeAttribute(range_key=True)
    email = UnicodeAttribute(null=True)
    password = UnicodeAttribute(null=True)
    userid=UnicodeAttribute(null=True)
    otp=UnicodeAttribute(null=True)
    username=UnicodeAttribute(null=True)
    verified=UnicodeAttribute(default="False")
    upvote=NumberAttribute(null=True)
    job_id=UnicodeAttribute(null=True)
    url=UnicodeAttribute(null=True)
    liked_by=MapAttribute(null=True)