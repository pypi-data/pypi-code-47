#!/usr/bin/python
# coding: utf8

# Copyright 2019 Skiply

from __future__ import unicode_literals


from .base import db_session, SkiplyBase

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy import and_, or_


class PowerSupply(SkiplyBase):
    ''' Device '''
    __tablename__ = 'so_power_supply'
    
    id = Column(Integer, primary_key=True, autoincrement=True)

    power_time = Column('time', DateTime, nullable=False)
    power_voltage = Column('voltage', Integer, nullable=False)
    power_voltage_idle = Column('voltage_idle', Integer, nullable=False)
    power_voltage_percentage = Column('voltage_percentage', Integer, nullable=False)

    device_id = Column('device_id', Integer, nullable=False)
    device_skiply_id = Column('device_name', String(255))

    def __init__(self, power_time, power_voltage, device_id, device_skiply_id):
        self.power_time = power_time
        self.power_voltage = power_voltage

        self.device_id = device_id
        self.device_skiply_id = device_skiply_id

    def __repr__(self):
        return '<Power Supply %s - %s>' % (self.power_time, self.power_voltage)

def get_powerSupply(powerSupply_id):
    session = db_session()
    try:
        results = session.query(PowerSupply).filter(PowerSupply.id == powerSupply_id).first()
    except:
        print("DB Request get_powerSupply(powerSupply_id) Failed")
        results = None
    finally:
        session.close()

    return results

def get_powerSupply_with_level_under(power_threshold, power_threshold_percent):
    session = db_session()
    try:
        results = session.query(PowerSupply).filter(or_(and_(PowerSupply.power_voltage <= power_threshold, PowerSupply.power_voltage > 0), and_(PowerSupply.power_voltage_percentage <= power_threshold_percent, PowerSupply.power_voltage_percentage > 0))).group_by(PowerSupply.device_skiply_id).all()
    except:
        print("DB Request get_powerSupply(powerSupply_id) Failed")
        results = None
    finally:
        session.close()

    return results