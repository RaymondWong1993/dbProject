import datetime
from sqlalchemy import exc, Table, Column, Integer, String, ForeignKey, Sequence, DateTime, Text, text
from sqlalchemy.ext.declarative import declarative_base
from flask import g
from user import User

class Business(User):
    __tablename__ = 'yummy_business'

    id = Column(Integer,ForeignKey('yummy_user.id') , primary_key=True)
    image = Column(String(512), default='')
    address = Column(String(512), default='')
    joinTime = Column(DateTime, default=datetime.datetime.now())

    __mapper_args__ = {
        'polymorphic_identity': __tablename__,
    }

    def __repr__(self):
        return "<Business" + str(self.__dict__) + ">"

    def save(self):
        try:
            g.session.add(self)
            g.session.commit()
        except exc.IntegrityError as e:
            code, msg = e.orig
            if code == 1062:
                raise BusinessRepetitionException
            else:
                raise Exception

    def modify(self, **kwargs):
        if not hasattr(self, 'id'):
            raise BusinessNotExistException

        g.session.add(self)
        for k in kwargs.keys():
            self.__setattr__(k, kwargs[k])

        g.session.commit()

    @classmethod
    def init(cls):
        User.metadata.drop_all(g.conn)
        User.metadata.create_all(g.conn)

    @classmethod
    def queryById(cls, id=None):
        if not id:
            return None

        result = g.session.query(cls).filter_by(id=id).first()
        if not result:
            g.session.expunge(result)
        return result

    @classmethod
    def queryByUsername(cls, username=None):
        if not username:
            return None

        result = g.session.query(cls).filter_by(username=username).first()
        if not result:
            g.session.expunge(result)
        return result

    @classmethod
    def queryByName(cls, name=None):
        if not name:
            return None

        result = g.session.query(cls).filter_by(name=name).first()
        if not result:
            g.session.expunge(result)
        return result

    @classmethod
    def queryAll(cls):
        results =  g.session.query(cls).all()
        if not results:
            g.session.expunge(results)
        return results

    @classmethod
    def deleteById(cls, id=None):
        if not id:
            raise BusinessNotExistException

        result = g.session.query(cls).filter_by(id=id).first()
        if not result:
            raise BusinessNotExistException

        g.session.delete(result)
        g.session.commit()

    @classmethod
    def deleteByUsername(cls, username=None):
        if not username:
            raise BusinessNotExistException

        result = g.session.query(cls).filter_by(username=username).first()
        if not result:
            raise BusinessNotExistException

        g.session.delete(result)
        g.session.commit()

    @classmethod
    def deleteAll(cls):
        g.session.query(cls).delete()
        g.session.commit()

class BusinessNotExistException(Exception): pass
class BusinessRepetitionException(Exception): pass
