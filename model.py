import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
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
    __tablename__ = "timeline"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    date_from = Column(Date, nullable=False)
    date_to = Column(Date, nullable=False)
    event_type = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    image_url = Column(String)

