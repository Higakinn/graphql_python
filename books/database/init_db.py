
from .db_session import db_session, engine
from .base import Base


def init_db():
    from ..models.genres import Genres
    from ..models.books import Books
    from ..models.characters import Characters

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    fantasy = Genres(name='Fantasy')
    db_session.add(fantasy)
    political_fiction = Genres(name='Political Fiction')
    db_session.add(political_fiction)
    philosophical_novel = Genres(name='Philosophical Novel')
    db_session.add(philosophical_novel)

    peter_wendy = Books(name='Peter & Wendy', author='J.M. Barrie', genre=fantasy)
    db_session.add(peter_wendy)
    it_cant_happen = Books(name='It Can\'t Happen Here', author='Sinclair Lewis',
                           genre=political_fiction)
    db_session.add(it_cant_happen)
    crooked_kingdom = Books(name='Crooked Kingdom', author='Leigh Bardugo', genre=fantasy)
    db_session.add(crooked_kingdom)
    crime_punishment = Books(name='Crime and Punishment', author='Fyodor Dostoyevsky',
                             genre=philosophical_novel)
    db_session.add(crime_punishment)

    peter_pan = Characters(name='Peter Pan', book=peter_wendy)
    db_session.add(peter_pan)
    wendy_darling = Characters(name='Wendy Darling', book=peter_wendy)
    db_session.add(wendy_darling)
    berzelius_windrip = Characters(name='Berzelius Windrip', book=it_cant_happen)
    db_session.add(berzelius_windrip)
    kaz_brekker = Characters(name='Kaz Brekker', book=crooked_kingdom)
    db_session.add(kaz_brekker)
    inej_ghafa = Characters(name='Inej Ghafa', book=crooked_kingdom)
    db_session.add(inej_ghafa)
    raskolnikov = Characters(name='Raskolnikov', book=crime_punishment)
    db_session.add(raskolnikov)

    db_session.commit()