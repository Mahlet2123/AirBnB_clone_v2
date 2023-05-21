#!/usr/bin/python3
""" The database storage module """
from sqlalchemy import create_engine, MetaData, text
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from os import getenv


class DBStorage:
    """DBStorage class"""

    __classNames = [State, City, User, Place, Review, Amenity]

    __engine = None
    __session = None

    def __init__(self):
        """constructor"""
        url = "mysql+mysqldb://{}:{}@{}/{}".format(
            getenv("HBNB_MYSQL_USER"),
            getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"),
            getenv("HBNB_MYSQL_DB"),
        )

        self.__engine = create_engine(url, pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            # drop all tables
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
        query on the current database session (self.__session)
        all objects depending of the class name (argument cls)
        """
        r_dict = {}
        if cls:
            for obj in self.__session.query(cls).all():
                # objs -> list of returned objects
                key = "{}.{}".format(type(obj).__name__, obj.id)
                r_dict[key] = obj
        else:
            for cls in DBStorage.__classNames:
                for obj in self.__session.query(cls).all():
                    # objs -> list of returned objects
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    r_dict[key] = obj
        return r_dict

    def my_all(self, cls=None):
        # query to fetch all objects related to cls if cls
        # is not None. Otherwise fetch all
        list_obj = []
        if not cls:
            for obj in DBStorage.__classNames:
                list_obj += self.__session.query(obj)
        else:
            list_obj = self.__session.query(cls)

        # return the dictionary reperesentation
        # return {v.__class__.__name__ + '.' + v.id: v for v in list_obj
        return {type(v).__name__ + "." + v.id: v for v in list_obj}

    def new(self, obj):
        """add the object to the current
        database session (self.__session)"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current
        database session (self.__session)"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current OOAdatabase session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database (feature of SQLAlchemy)"""
        from sqlalchemy.orm import sessionmaker

        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()

    def classes_dict(self):
        """collection of classes"""

        classes_dict = {
            "BaseModel": BaseModel,
            "State": State,
            "City": City,
            "User": User,
            "Place": Place,
            "Review": Review,
            "Amenity": Amenity
        }
        return classes_dict

    def close(self):
        """ method on the private session attribute (self.__session) """
        self.__session.close()
