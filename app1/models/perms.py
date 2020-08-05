# To read more about Flask-Principle:
# - https://pythonhosted.org/Flask-Principal/
# - https://github.com/mickey06/Flask-principal-example
# - https://github.com/mickey06/Flask-principal-example/blob/master/FPrincipals.py
# - https://github.com/mattupstate/flask-principal/

from flask_principal import Principal, Permission, RoleNeed, identity_loaded
from flask_login import current_user

# Needs
admin_need = RoleNeed('admin')
editor_need = RoleNeed('editor')
user_need = RoleNeed('user')

# Create Permissions
admin_perm = Permission(admin_need)
editor_perm = Permission(editor_need)
user_perm = Permission(user_need)

# @identity_loaded.connect_via(app)
@identity_loaded.connect
def on_identity_loaded(sender, identity):
    needs = []
    if current_user.is_authenticated:
        _roles = current_user.getRoles()
        if "admin" in _roles:
            needs.append(admin_need)
        elif "editor" in _roles:
            needs.append(editor_need)
        elif "user" in _roles:
            needs.append(user_need)
    
    for need in needs:
        identity.provides.add(need)