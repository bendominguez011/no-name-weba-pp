from app import db
from models import User, Posts, Community, Comments

db.session.rollback()
db.create_all()
u = User('ben', '_apples1')
u2 = User('user', '_apples1')
db.session.add_all([u, u2])
c = Community('powerlifting', password=None, founder=u, FAQ=None, description='a community for powerlifters')
db.session.add(c)
post = Posts("Title", "This is a body", author=u, community=c)
post2 = Posts("Title", "This is a second body", author=u2, community=c)
db.session.add_all([post, post2])
comment = Comments("This is a comment", author=u2, post=post)
db.session.add(comment)
db.session.commit()
