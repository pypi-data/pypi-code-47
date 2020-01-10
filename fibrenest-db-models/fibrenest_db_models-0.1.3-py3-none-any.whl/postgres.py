import enum
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import MACADDR, INET

Base = declarative_base()


class CPEProvTypeENUM(enum.Enum):
    bridge = 'bridge'
    gateway = 'gateway'


class ServiceProvStatusENUM(enum.Enum):
    not_started = 'not_started'
    radius_record_created = 'radius_record_created'
    live = 'live'
    suspended = 'suspended'
    deleted = 'deleted'


def _repr(obj):
    cols = []
    for k in obj.__class__.__dict__.keys():
        if not str(k).startswith('_'):
            cols.append(f'{k}={obj.__getattribute__(k)}')
    return f'<{obj.__class__.__name__}({",".join(cols)})>'


class ONT(Base):
    __tablename__ = 'ont'

    id = Column(Integer, primary_key=True)
    sn = Column(String(length=64), nullable=False, unique=True)
    portid = Column(Integer, nullable=False)
    slotid = Column(Integer, nullable=False)
    frameid = Column(Integer, nullable=False)
    ontid = Column(Integer)
    model = Column(String(length=64))
    netbox_siteid = Column(Integer)
    olt_ip = Column(INET, nullable=False)
    sitename = Column(String(length=256))
    ont_registered = Column(Boolean, nullable=False, default=False, comment='If the ONT is registered on the OLT or not')
    ont_register_datetime = Column(DateTime)
    prov_type = Column(Enum(CPEProvTypeENUM), comment='Provisioning type of the ONT. Valid values: bridge or gateway')
    s_vlan = Column(Integer)
    c_vlan = Column(Integer)
    replacement_for = Column(String(length=64), comment='Serial number of the ONT that this ONT is a replacement for')

    cpe = relationship('CPE', back_populates='ont')

    def __repr__(self):
        return _repr(self)


class CPE(Base):
    __tablename__ = 'cpe'

    id = Column(Integer, primary_key=True)
    mac = Column(MACADDR, unique=True)
    ont_id = Column(Integer, ForeignKey('ont.id'))

    ont = relationship('ONT', back_populates='cpe')
    customer = relationship('CUSTOMER', back_populates='cpe')

    def __repr__(self):
        return _repr(self)


class CUSTOMER(Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True)
    cpe_id = Column(Integer, ForeignKey('cpe.id'))
    billing_sys_id = Column(String(length=128))

    cpe = relationship('CPE', back_populates='customer')
    service = relationship('SERVICE', back_populates='customer')

    def __repr__(self):
        return _repr(self)


class SERVICE(Base):
    __tablename__ = 'service'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    name = Column(String(length=64))
    status = Column(Enum(ServiceProvStatusENUM))
    prov_datetime = Column(DateTime)
    suspend_datetime = Column(DateTime)
    delete_datetime = Column(DateTime)

    customer = relationship('CUSTOMER', back_populates='service')

    def __repr__(self):
        return _repr(self)