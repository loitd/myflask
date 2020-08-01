import os

class Const(object):
    MSG_USER_NOTFOUND = "Username and password combination not found"
    MSG_BLANK_FIELDS_SUBMITTED = "No blank field(s) please"
    MSG_USER_EXISTED = "Email already exists"
    _GH_CLIENT_KEY = os.environ.get("GH_CLIENT_KEY")
    _GH_CLIENT_SECRET = os.environ.get("GH_CLIENT_SECRET")
    _GG_CLIENT_ID = os.environ.get("GG_CLIENT_ID")
    _GG_CLIENT_SECRET = os.environ.get("GG_CLIENT_SECRET")
    _GG_DISCOVERY_URL="https://accounts.google.com/.well-known/openid-configuration"