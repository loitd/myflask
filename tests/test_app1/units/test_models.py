import pytest
from app1.models.users import User

def test_init_db(db):
    """Test if init_db works"""
    # with app.app_context():
    _row = db.session.query(User).filter_by(email="admin@myflask.com").first()
    assert _row is not None #existed
    assert _row.email == "admin@myflask.com"
    
