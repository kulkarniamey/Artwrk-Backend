from schema import Schema, And, Use, Optional
from artwrk.config.config import logger

class Schemas:

    Account = Schema(
        {   
            'operation':And(Use(str)),
            Optional('username'):  And(Use(str)),
            Optional('type'): And(str, Use(str.lower),
            lambda s: s in ('artist', 'recruiter')),
            Optional('otp'):And(Use(str),lambda s: len(s)==6),
            Optional('email'):And(Use(str)),
            Optional('password'):And(str,lambda s: len(s)>6),
            Optional('old_password'):And(str,lambda s: len(s)>6),
            Optional('new_password'):And(str,lambda s: len(s)>6),
            Optional('username'):And(Use(str)),
            Optional('user_id'):And(Use(str)),
        })
    Profile = Schema(
        {
            'operation':And(Use(str)),
            Optional('authorizationToken'):And(Use(str)),
            Optional('type'): And(str, Use(str.lower)),
            Optional('current_employer'):And(Use(str)),
            Optional('username'):And(Use(str)),
            Optional('facebook_link'):And(Use(str)),
            Optional('twitter_link'):And(Use(str)),
            Optional('employer_history'):And(Use(str)),
            Optional('education_history'):And(Use(str)),
            Optional('skill_tags'):And(Use(str)),
            Optional('awards_recognition'):And(Use(str)),
            Optional('name'):And(Use(str)),
            Optional('phone'):And(Use(str)),
            Optional('id'):And(Use(str)),
            Optional('user_id'):And(Use(str)),
            Optional('other_id'):And(Use(str)),
            Optional('artist_type'):And(Use(str)),
            Optional('email_verification'):And(Use(str)),
            Optional('otp'):And(Use(str),lambda s: len(s)==6),
            Optional('company_type'):And(Use(str)),
            Optional('admin_verification'):And(Use(str)),
            Optional('post_id'):And(Use(str)),
            Optional('activity'):And(Use(str)),
            Optional('recruiter_id'):And(Use(str)),

        }
    )
    
    Post = Schema(
        {
            'operation':And(Use(str)),
            Optional('authorizationToken'):And(Use(str)),
            Optional('post_id'):And(Use(str)),
            Optional('id'):And(Use(str)),
            Optional('time'):And(Use(str)),
            Optional('content'):And(Use(str)),
            Optional('url'):And(Use(str)),
            Optional('voters'):And(Use(str)),
            Optional('vote_count'):And(Use(str)),
        }
    )
    
    Job = Schema(
        {
            'operation':And(Use(str)),
            'authorizationToken':And(Use(str)),
            Optional('recruiter_id'):And(Use(str)),
            Optional('id'):And(Use(str)),
            Optional('job_id'):And(Use(str)),
            Optional('user_id'):And(Use(str)),
            Optional('time'):And(Use(str)),
            Optional('content'):And(Use(str)),
            Optional('url'):And(Use(str)),
            Optional('applicants'):And(Use(str)),
            Optional('hiring_type'):And(Use(str)),
        }
    )
    
