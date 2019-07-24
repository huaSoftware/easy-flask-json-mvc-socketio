# coding: utf-8
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.schema import FetchedValue
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class HtComment(Base):
    __tablename__ = 'ht_comments'

    id = Column(Integer, primary_key=True)
    msg = Column(String(100), nullable=False, server_default=FetchedValue())
    user_id = Column(Integer)
    article_id = Column(Integer, nullable=False)
    add_time = Column(Integer, nullable=False)


class HtImgShard(Base):
    __tablename__ = 'ht_img_shard'

    id = Column(Integer, primary_key=True)
    uuid = Column(String(100), nullable=False, server_default=FetchedValue())
    imgString = Column(Text, nullable=False)
    index = Column(Integer, nullable=False)


class HtLog(Base):
    __tablename__ = 'ht_logs'

    id = Column(Integer, primary_key=True)
    type = Column(Integer, nullable=False, server_default=FetchedValue())
    level = Column(Integer, nullable=False, server_default=FetchedValue())
    data = Column(Text, nullable=False)
    create_time = Column(Integer, nullable=False)


class HtSuggest(Base):
    __tablename__ = 'ht_suggest'

    add_time = Column(Integer, nullable=False)
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, nullable=False)
    message = Column(String(255, 'utf8_unicode_ci'), nullable=False)


class HtUser(Base):
    __tablename__ = 'ht_users'

    id = Column(Integer, primary_key=True)
    name = Column(String(255, 'utf8_unicode_ci'), unique=True)
    email = Column(String(255, 'utf8_unicode_ci'), nullable=False, unique=True)
    tel = Column(String(20, 'utf8_unicode_ci'), unique=True)
    password = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    status = Column(Integer, nullable=False)
    remember_token = Column(String(100, 'utf8_unicode_ci'))
    created_at = Column(Integer)
    updated_at = Column(Integer)
    url_path = Column(String(300, 'utf8_unicode_ci'))
    real_path = Column(String(300, 'utf8_unicode_ci'))
