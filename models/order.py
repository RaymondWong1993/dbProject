import datetime
from sqlalchemy import exc, Table, Column, Integer, String, ForeignKey, Sequence, DateTime, Text, text
from sqlalchemy.ext.declarative import declarative_base
from flask import g

Base = declarative_base()

class Order(Base):
    __tablename__ = 'yummy_order'

    id = Column(Integer, Sequence('yummy_order_seq'), primary_key=True)
    createTime = Column(DateTime, default=datetime.datetime.now())
    totalPrice = Column(Integer, default=0)
    status = Column(Integer, default=0)
    items = Column(Text, default='')
    business_id = Column(Integer)
    customer_id = Column(Integer)

    def __repr__(self):
        return "<Order" + str(self.__dict__) + ">"

    def save(self):
        try:
            g.session.add(self)
            g.session.commit()
        except exc.IntegrityError as e:
            code, msg = e.orig
            if code == 1062:
                raise OrderRepetitionException
            else:
                raise Exception

    def modify(self, **kwargs):
        if not hasattr(self, 'id'):
            raise OrderNotExistException

        g.session.add(self)
        for k in kwargs.keys():
            self.__setattr__(k, kwargs[k])

        g.session.commit()

    def addItem(self, id=None):
        if not id:
            return False

        g.session.add(self)
        self.items = self.items + ',' + str(id)
        g.session.commit()
        return True

    def getItems(self):
        return self.items.split(',')

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
    def queryByBusinessId(cls, id=None):
        if not id:
            return None

        results = g.session.query(cls).filter_by(business_id=id).all()
        g.session.expunge_all()
        return results

    @classmethod
    def queryByCustomerId(cls, id=None):
        if not id:
            return None

        results = g.session.query(cls).filter_by(customer_id=id).all()
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
            raise OrderNotExistException

        result = g.session.query(cls).filter_by(id=id).first()
        if not result:
            raise OrderNotExistException

        g.session.delete(result)
        g.session.commit()

    @classmethod
    def deleteAll(cls):
        g.session.query(cls).delete()
        g.session.commit()

class OrderNotExistException(Exception): pass
class OrderRepetitionException(Exception): pass