import datetime

from affo_sms_service.extensions import db

__all__ = ["SMSMessage"]


class SMSMessage(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    from_ = db.Column(db.String(20))
    to = db.Column(db.String(20))
    body = db.Column(db.String(918))
    gateway = db.Column(db.String(20))
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
