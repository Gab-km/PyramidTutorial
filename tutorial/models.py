from pyramid.security import (
    Allow,
    Everyone,
    )

from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Page(Base):
    """The SQLAlchemy declarative model class for a page object."""
    __tablename__ = 'pages'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    data = Column(Text)

    def __init__(self, name, data):
        self.name = name
        self.data = data

class RootFactory:
    __acl__ = [(Allow, Everyone, 'view'),
                (Allow, 'group:editors', 'edit')]
    def __init__(self, request):
        pass