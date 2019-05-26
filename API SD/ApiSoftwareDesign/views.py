from rest_framework.views import APIView, Response
import datetime
import os
from dateutil import parser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
import json
# Create your views here.
from os import path
import sys
sys.path.append(path.abspath('../group1/helpers'))
from database_manager import Manager
from arguments_manager import manage_arguments
sys.path.append(path.abspath('../group1'))
from container import Container

db_manager = Manager()


from  bson.json_util import dumps

def generate_params():
    return ['mineral_deposit','headers','data_map','block_model' ]



class InsertBlockModel(APIView):
    queryset = ''
    def get(self, request):
        params = generate_params()
        values_params = {}
        for instance in params:
            value = request.GET.get(instance)
            if instance == 'data_map' and value is not None:
               json_acceptable_string = value.replace("'", "\"")
               value = json.loads(json_acceptable_string)
            values_params[instance] = value


        if None not in values_params.values():
            db_manager.insert_new_block_model_with_name(values_params["mineral_deposit"], values_params["headers"] ,values_params["data_map"], values_params["block_model"] )

        all_idex = []
        return Response(all_idex)


"""

def main(args):
	db_manager = Manager()
	manager = Container()
	if args.insert and args.file_input:
		insert(args, db_manager)
	elif args.remove:
		remove(args, db_manager)
	elif args.metrics:
		metrics(args,db_manager, manager)

def insert (args, db_manager):
	if not args.mineral_deposit:
		db_manager.insert_new_mineral_deposit(args.file_input)
	elif not args.block_model:
		db_manager.insert_new_block_model(args.mineral_deposit, args.file_input)
	else:
		db_manager.insert_blocks(args.mineral_deposit, args.block_model, args.file_input)

def remove(args, db_manager):
	db_manager.remove_all_blocks_from_block_model(args.mineral_deposit, args.block_model)

def metrics(args, db_manager, manager):
	if args.mineral_deposit:
		mineral_deposit = db_manager.fetch_mineral_deposit(args.mineral_deposit)
		manager.set_mineral_deposit(mineral_deposit)
		if args.block_model:
			block_model = db_manager.fetch_block_model(args.mineral_deposit, args.block_model)
			blocks = db_manager.get_all_blocks_from_block_model(args.mineral_deposit, args.block_model)
			manager.set_block_model(block_model, blocks)
	manager.interact_with_user()


"""
