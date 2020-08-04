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
admin_perm.description = "Administrator permissions"
editor_perm = Permission(editor_need)
user_perm = Permission(user_need)

# @identity_loaded.connect_via(app)
@identity_loaded.connect
def on_identity_loaded(sender, identity):
    needs = []
    if current_user.is_authenticated:
        if current_user.role == "admin":
            needs.append(admin_need)
        elif current_user.role == "editor":
            needs.append(editor_need)
        elif current_user.role == "user":
            needs.append(user_need)
    
    for need in needs:
        identity.provides.add(need)