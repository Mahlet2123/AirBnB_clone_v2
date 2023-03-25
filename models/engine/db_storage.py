#!/usr/bin/python3
"""The driving power of relational databses"""
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv
from sqlalchemy import create_engine, MetaData


class DBStorage():
    """ This class comprises the ORM methods that helps us
    to interact with our detabase """

    __classNames = [
            User,
            State,
            City,
            Place,
            Amenity,
            Review
            ]

    __engine = None
    __session = None

    def __init__(self):
        """ This is how we get conneted to the database.
        The four environmental variables are used for
        robust security """

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'
            .format(getenv("HBNB_MYSQL_USER"),
                    getenv("HBNB_MYSQL_PWD"),
                    getenv("HBNB_MYSQL_HOST"),
                    getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True)

    def all(self, cls=None):
        #query to fetch all objects related to cls if cls
        #is not None. Otherwise fetch all
        obj_dict = {}

        if cls:
            obj_dict.update(session.query(cls))
        else:
            for key in DBStorage.__classNames:
                for row in self.__session.query(key):
                    obj_dict.update({'{}.{}'.
                                    format(type(row).__name__, row.id,): row})
        return obj_dict

    def new(self, obj):
        """ Adding the obj to the database """
        self.__session.add(obj)

    def save(self):
        """ commiting all changes to a database """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete a session object if not None """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ To Create all the tables on the database """
        from sqlalchemy.orm import sessionmaker
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(
                bind=self.__engine, expire_on_commit=False
                )
        self.__session = Session()

    def close(self):
        """ calls remove()
        """
        self.__session.close()

    def classes_dict(self):
        """collection of classes"""
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.amenity import Amenity
        from models.state import State
        from models.review import Review

        classes_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review,
        }
        return classes_dict
