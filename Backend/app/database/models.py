import sqlalchemy as SA
from sqlalchemy import MetaData

metadata = MetaData()

SportObject = SA.Table(
    'sport_objects',
    metadata,
    SA.Column('id', SA.Integer, primary_key=True, autoincrement=False),
    SA.Column('name_ru', SA.String, default=None),
    SA.Column('name_en', SA.String, default=None),
    SA.Column('is_active', SA.Boolean, default=None),
    SA.Column('short_description_ru', SA.String, default=None),
    SA.Column('detail_description_ru', SA.String, default=None),
    SA.Column('short_description_en', SA.String, default=None),
    SA.Column('detail_description_en', SA.String, default=None),
    SA.Column('municipality', SA.String, default=None),
    SA.Column('subject_of_federation', SA.String, default=None),
    SA.Column('matter', SA.String, default=None),
    SA.Column('city_ru', SA.String, default=None),
    SA.Column('city_en', SA.String, default=None),
    SA.Column('address_ru', SA.String, default=None),
    SA.Column('address_en', SA.String, default=None),
    SA.Column('oktmo', SA.BigInteger, default=None),
    SA.Column('fcp', SA.String, default=None),
    SA.Column('action', SA.String, default=None),
    SA.Column('action_start_date', SA.Date, default=None),
    SA.Column('action_compliton_date', SA.Date, default=None),
    SA.Column('full_finance', SA.Float, default=None),
    SA.Column('working_hours', SA.String, default=None),
    SA.Column('working_hours_sat', SA.String, default=None),
    SA.Column('working_hours_sun', SA.String, default=None),
    SA.Column('area', SA.String, default=None),
    SA.Column('email', SA.String, default=None),
    SA.Column('type', SA.String, default=None),
    SA.Column('phone', SA.String, default=None),
    SA.Column('url', SA.String, default=None),
    SA.Column('kinds_of_sports', SA.String, default=None),
    SA.Column('coor_x', SA.Float),
    SA.Column('coor_y', SA.Float),
    SA.Column('curator_id', SA.Integer, SA.ForeignKey('curator.id'), default=None)
)



Curator = SA.Table(
    'curator',
    metadata,
    SA.Column('id', SA.Integer, primary_key=True),
    SA.Column('name_ru', SA.String, default=None),
    SA.Column('address_ru', SA.String, default=None),
    SA.Column('name_en', SA.String, default=None),
    SA.Column('address_en', SA.String, default=None),
    SA.Column('phone', SA.String, default=None),
)