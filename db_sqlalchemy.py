import os
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Watchlist(db.Model):
    __tablename__ = 'watchlist'
    id = db.Column(db.Integer, primary_key=True)
    entity_type = db.Column(db.String(50), nullable=False)
    value = db.Column(db.String(255), nullable=False)
    threat_level = db.Column(db.String(50), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

class Complaint(db.Model):
    __tablename__ = 'complaint'
    id = db.Column(db.Integer, primary_key=True)
    complaint_no = db.Column(db.String(100))
    category = db.Column(db.String(100))
    state = db.Column(db.String(100))
    ioc_list = db.Column(db.Text)
    status = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class AuditLog(db.Model):
    __tablename__ = 'audit_log'
    id = db.Column(db.Integer, primary_key=True)
    action = db.Column(db.String(255), nullable=False)
    target = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_ip = db.Column(db.String(50))