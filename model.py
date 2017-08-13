import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

LIFE = 0
WORK_BUSINESS = 1
EDUCATION = 2

TIMELINE_ENTRY_CLASS = {
    LIFE: "",
    WORK_BUSINESS: "timeline-inverted",
    EDUCATION: ""
}

TIMELINE_ICON = {
    LIFE: "fa fa-user",
    WORK_BUSINESS: "fa fa-briefcase",
    EDUCATION: "fa fa-university"
}

TIMELINE_HEADING_STYLE = {
    LIFE: "text-danger",
    WORK_BUSINESS: "text-primary",
    EDUCATION: "text-warning"
}


class Timeline(Base):
    __tablename__ = "timelines"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    date_from = Column(Date, nullable=False)
    date_to = Column(Date, nullable=False)
    event_type = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    image_url = Column(String)

class File(Base):
    __tablename__ = "files"
    id = Column(Integer, primary_key=True)
    file_name = Column(String, nullable=False)
    question_entry_id = Column(Integer, ForeignKey('question_entries.id'))
    question_entry = relationship("QuestionEntry", backref="attachments")
    download_uri = Column(String, nullable=False)

class QuestionReplyAssociation(Base):
    __tablename__ = "question_reply_relations"
    id = Column(Integer, primary_key=True)
    question_entry_id = Column(Integer, ForeignKey('question_entries.id'))
    reply_id = Column(Integer, ForeignKey('replies.id'))
    question = relationship("QuestionEntry", backref="reply_links")
    reply = relationship("Reply", backref="question_links")

class QuestionEntry(Base):
    __tablename__ = "question_entries"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)
    last_update_date = Column(Date, nullable=False)

class Reply(Base):
    __tablename__ = "replies"
    id = Column(Integer, primary_key=True)
    token = Column(String(8))
    receiver_name = Column(String)
    about = Column(String)
    question_entries = relationship("QuestionEntry", backref="replies",
                                    secondary="question_reply_relations")

