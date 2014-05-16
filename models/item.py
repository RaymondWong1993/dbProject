import datetime
from sqlalchemy import exc, Table, Column, Integer, String, ForeignKey, Sequence, DateTime, Text, text
from sqlalchemy.ext.declarative import declarative_base
from flask import g

Base = declarative_base()

fields = ('id', 'itemname', 'hashpw', 'salt', 'nickname', 'sign', 'contact')

class Item(Base):
    __tablename__ = 'yummy_item'

    id = Column(Integer, Sequence('yummy_item_seq'), primary_key=True)
    name = Column(String(32))
    category = Column(String(32), nullable=True)
    price = Column(Integer, default=0)
    bookedNumber = Column(Integer, default=0)
    createTime = Column(DateTime, default=datetime.datetime.now())
    supplier = Column(Integer)

    def __repr__(self):
        return "<Item" + str(self.__dict__) + ">"

    def save(self):
        try:
            g.session.add(self)
            g.session.commit()
        except exc.IntegrityError as e:
            code, msg = e.orig
            if code == 1062:
                raise ItemRepetitionException
            else:
                raise Exception

    def modify(self, **kwargs):
        if not hasattr(self, 'id'):
            raise ItemNotExistException

        g.session.add(self)
        for k in kwargs.keys():
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
        g.session.expunge(result)
        return result

    @classmethod
    def queryByName(cls, name=None):
        if not name:
            return None

        results = g.session.query(cls).filter_by(name=name).all()
        g.session.expunge_all()
        return results

    @classmethod
    def queryByCategory(cls, category=None):
        if not category:
            return None

        results = g.session.query(cls).filter_by(category=category).all()
        g.session.expunge_all()
        return results

    @classmethod
    def queryAll(cls):
        results = g.session.query(cls).all()
        g.session.expunge_all()
        return results

    @classmethod
    def deleteById(cls, id=None):
        if not id:
            raise ItemNotExistException

        result = g.session.query(cls).filter_by(id=id).first()
        if not result:
            raise ItemNotExistException

        g.session.delete(result)
        g.session.commit()

    @classmethod
    def deleteAll(cls):
        g.session.query(cls).delete()
        g.session.commit()

class ItemNotExistException(Exception): pass
class ItemRepetitionException(Exception): pass
