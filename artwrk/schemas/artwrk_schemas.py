from schema import Schema, And, Use, Optional
from artwrk.config.config import logger

class Schemas:

    create_user_schema = Schema(
        {   'operation': And(str, Use(str.lower), lambda s: s in ('create_user',)),
            'username':  And(Use(str)),
            'email':And(Use(str)),
            'password':And(str,lambda s: len(s)>6),
            'type': And(str, Use(str.lower),
            lambda s: s in ('artist', 'recruiter'))
        })

    sign_in_schema = Schema(
        {   'operation': And(str, Use(str.lower), lambda s: s in ('sign_in',)),
            'username':  And(Use(str),lambda s: len(s)>4),
            'password':And(str,lambda s: len(s)>6),
            'type': And(str, Use(str.lower),
            lambda s: s in ('artist', 'recruiter'))
        })
    forgot_password_schema = Schema(
        {   'operation': And(str, Use(str.lower), lambda s: s in ('forgot_password',)),
            'username':  And(Use(str)),
            'type': And(str, Use(str.lower),
            lambda s: s in ('artist', 'recruiter'))
        })
    resend_otp_schema = Schema(
        {   'operation': And(str, Use(str.lower), lambda s: s in ('resend_otp',)),
            'username':  And(Use(str)),
            'type': And(str, Use(str.lower),
            lambda s: s in ('artist', 'recruiter'))
        })
    change_password_schema = Schema(
        {   'operation': And(str, Use(str.lower), lambda s: s in ('change_password',)),
            'username':  And(Use(str)),
            'otp':And(Use(str),lambda s: len(s)==6),
            'password':And(str,lambda s: len(s)>6),
            'type': And(str, Use(str.lower),
            lambda s: s in ('artist', 'recruiter'))
        })
    change_password_authenticated_schema = Schema(
        {   'operation': And(str, Use(str.lower), lambda s: s in ('change_password_authenticated',)),
            'user_id':  And(Use(str)),
            'old_password':And(str,lambda s: len(s)>6),
            'new_password':And(str,lambda s: len(s)>6)
        })
    get_posts_by_artist=Schema(
        {   'operation': And(str, Use(str.lower), lambda s: s in ('get_posts_by_artists',)),
            'user_id':  And(Use(str)),
        })

