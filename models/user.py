import datetime
from sqlalchemy import exc, Table, Column, Integer, String, ForeignKey, Sequence, DateTime, Text, text
from sqlalchemy.ext.declarative import declarative_base
from flask import g

Base = declarative_base()

class User(Base):
    __tablename__ = 'yummy_user'

    id = Column(Integer, Sequence('yummy_user_seq'), primary_key=True)
    username = Column(String(32), unique=True)
    hashpw = Column(String(60))
    salt = Column(String(29))
    name = Column(String(64), default='', unique=True)
    describe = Column(String(1024), default='')
    contact = Column(String(128), default='')
    type = Column(String(32), default=__tablename__)

    __mapper_args__ = {
        'polymorphic_identity': __tablename__,
        'polymorphic_on': type,
        'with_polymorphic': '*',
    }

    # def __init__(self, **kwargs):
    #     self.__dict__ = kwargs

    def __repr__(self):
        return "<User" + str(self.__dict__) + ">"

    def save(self):
        try:
            g.session.add(self)
            g.session.commit()
        except exc.IntegrityError as e:
            code, msg = e.orig
            if code == 1062:
                raise UserRepetitionException
            else:
                raise Exception

    def modify(self, **kwargs):
        if not hasattr(self, 'id'):
            raise UserNotExistException

        g.session.add(self)
        for k in kwargs.keys():
            ## Haven't understand that self.__dict__[k] = kwargs[k] doesn't work.
            self.__setattr__(k, kwargs[k])

        g.session.commit()

    @classmethod
    def init(cls):
        Base.metadata.drop_all(g.conn)
        Base.metadata.create_all(g.conn)

    @classmethod
    def queryById(cls, id=None):
        if not id:
            return None

        result = g.session.query(cls).filter_by(id=id).first()
        if result:
            g.session.expunge(result)
        return result

    @classmethod
    def queryByUsername(cls, username=None):
        if not username:
            return None

        result = g.session.query(cls).filter_by(username=username).first()
        if result:
            g.session.expunge(result)

        return result

    @classmethod
    def queryByName(cls, name=None):
        if not name:
            return None

        result = g.session.query(cls).filter_by(name=name).first()
        if result:
            g.session.expunge(result)
        return result

    @classmethod
    def queryAll(cls):
        results = g.session.query(cls).all()
        if results:
            g.session.expunge_all()
        return results

    @classmethod
    def deleteById(cls, id=None):
        if not id:
            raise UserNotExistException

        result = g.session.query(cls).filter_by(id=id).first()
        if not result:
            raise UserNotExistException

        g.session.delete(result)
        g.session.commit()

    @classmethod
    def deleteByUsername(cls, username=None):
        if not username:
            raise UserNotExistException

        result = g.session.query(cls).filter_by(username=username).first()
        if not result:
            raise UserNotExistException

        g.session.delete(result)
        g.session.commit()

    @classmethod
    def deleteAll(cls):
        g.session.query(cls).delete()
        g.session.commit()

class UserNotExistException(Exception): pass
class UserRepetitionException(Exception): pass
