from datetime import date
from server.app import app, db
from server.models.user import User
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance

with app.app_context():
    print("🌱 Seeding database...")

    # Clear existing data
    Appearance.query.delete()
    Episode.query.delete()
    Guest.query.delete()
    User.query.delete()

    # Users
    admin = User(username="admin")
    admin.set_password("password")

    user2 = User(username="james")
    user2.set_password("123456")

    user3 = User(username="sarah")
    user3.set_password("letmein")

    db.session.add_all([admin, user2, user3])

    # Guests
    guest1 = Guest(name="Zendaya", occupation="Actress")
    guest2 = Guest(name="Trevor Noah", occupation="Comedian")
    guest3 = Guest(name="Bill Gates", occupation="Philanthropist")
    guest4 = Guest(name="Taylor Swift", occupation="Musician")

    db.session.add_all([guest1, guest2, guest3, guest4])

    # Episodes
    episode1 = Episode(date=date(2025, 6, 1), number=1)
    episode2 = Episode(date=date(2025, 6, 2), number=2)
    episode3 = Episode(date=date(2025, 6, 3), number=3)
    episode4 = Episode(date=date(2025, 6, 4), number=4)

    db.session.add_all([episode1, episode2, episode3, episode4])
    db.session.commit()

    # Appearances
    appearance1 = Appearance(rating=5, guest_id=guest1.id, episode_id=episode1.id)
    appearance2 = Appearance(rating=4, guest_id=guest2.id, episode_id=episode2.id)
    appearance3 = Appearance(rating=3, guest_id=guest3.id, episode_id=episode3.id)
    appearance4 = Appearance(rating=5, guest_id=guest1.id, episode_id=episode4.id)
    appearance5 = Appearance(rating=4, guest_id=guest4.id, episode_id=episode4.id)

    db.session.add_all([appearance1, appearance2, appearance3, appearance4, appearance5])

    db.session.commit()
    print("✅ Done seeding!")
