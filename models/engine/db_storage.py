#!/usr/bin/python3
""" The database storage module """
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv


class DBStorage():
    """ """
    __engine = None
    __session = None


    def __init__(self):
        """ constructor """
        url = 'mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_DB'))

        self.__engine = create_engine(url, pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            #drop all tables
            Base.metadata.drop_all(bind=self.__engine)


    def all(self, cls=None):
        """
        query on the current database session (self.__session)
        all objects depending of the class name (argument cls)
        """
        r_dict = {}
        objs = []
        if cls:
            class_name = self.classes_dict()[cls]
            objs = self.__session.query(class_name).all()
            # objs -> list of returned objects
        else:
            for name in self.classes_dict().values():
                class_objs = self.__session.query(name).all()
                objs.extend(class_objs)

        for class_obj in objs:
            key = '{}.{}'.format(type(class_obj), class_obj.id)
            r_dict[key] = class_obj
        return r_dict

    def new(self, obj):
        """ add the object to the current
        database session (self.__session) """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current
        database session (self.__session) """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session obj if not None """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ create all tables in the database (feature of SQLAlchemy) """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()

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
