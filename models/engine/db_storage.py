#!/usr/bin/python3
"""defines the db storage system"""
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
import os
from dotenv import load_dotenv


""" load variable from env file """
load_dotenv()


class DBStorage:
    """Represents a database storage engine.

    Attributes:
        __engine (sqlalchemy.Engine): The working SQLAlchemy engine.
        __session (sqlalchemy.Session): The working SQLAlchemy session.
    """

    __engine = None
    __session = None

    def __init__(self):
        """Initialize a new Storage instance."""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(
                                          os.environ.get("HBNB_MYSQL_USER"),
                                          os.environ.get("HBNB_MYSQL_PWD"),
                                          os.environ.get("HBNB_MYSQL_HOST"),
                                          os.environ.get("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if os.environ.get("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects and return dictionaries"""
        all_classes = [State, City, User, Place, Review, Amenity]

        if cls is None:
            objs = []
            for table_class in all_classes:
                objs.extend(self.__session.query(table_class).all())
        else:
            if isinstance(cls, str):
                cls = eval(cls)
            objs = self.__session.query(cls).all()
        result_dict = {"{}.{}".format(type(o).__name__, o.id): o for o in objs}
        return result_dict

    def new(self, obj):
        """adds a new object to the to the database"""
        if obj not in self.__session:
            self.__session.add(obj)

    def save(self, obj):
        """this saves the changes and commits them to the database"""

        self.__session.commit()

    def delete(self, obj):
        """delet from database"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_expire = sessionmaker(
            bind=self.__engine, expire_on_commit=True)
        Session = scoped_session(session_expire)
        self.__session = Session()

    def close(self):
        """Close the sqlalchemy sessions"""
        self.__session.close()
