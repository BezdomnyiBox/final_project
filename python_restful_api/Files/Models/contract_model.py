from peewee import *
from Models.base_model import BaseModel
from Models.client_model import ClientModel

class ContractModel(BaseModel):
       contract_id = AutoField(column_name='contract_id')
       client_id = ForeignKeyField(ClientModel, to_field='client_id')
       check_in_date = DateField(column_name='check_in_date', null=True)
       check_out_date = DateField(column_name='check_out_date', null=True)    

       class Meta:
              table_name = 'contracts'