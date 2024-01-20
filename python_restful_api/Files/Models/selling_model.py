from peewee import *
from Models.base_model import BaseModel
from Models.contract_model import ContractModel
from Models.furniture_model import FurnitureModel

class SellingModel(BaseModel):
       selling_id = AutoField(column_name='selling_id')
       contract_id = ForeignKeyField(ContractModel, to_field='contract_id')
       furniture_id = ForeignKeyField(FurnitureModel, to_field='furniture_id')
       count = IntegerField(column_name='count', null=True)
       
       class Meta:
              table_name = 'sellings'