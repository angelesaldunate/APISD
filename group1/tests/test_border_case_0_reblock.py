import unittest
from classes.block_model import BlockModel


class TestReblock(unittest.TestCase):
	def setUp(self):
		name = "v1"
		mineral_deposit = "Zuck small"
		headers =  ["id", "x", "y", "z", "cost", "value", "rock_tonnes", "ore_tonnes"]
		data_map = {"x": "x", "y": "y", "z": "z", "weight": "rock_tonnes", "grade": {"Au":"ore_tonnes"}}
		blocks = [{"_id": {"$oid": "5cb0f608b766f9aa245cb3f0"},
				"mineral_deposit": "Zuck small",
				"block_model": "v1",
				"id": 9369,
				"x": 0,
				"y": 0,
				"z": 0,
				"cost": 56592,
				"value": 135786.28,
				"rock_tonnes": 0,
				"ore_tonnes": 0
				}, {"_id": {"$oid": "5cb0f608b766f9aa245cb3f1"},
				"mineral_deposit": "Zuck small",
				"block_model": "v1",
				"id": 9370,
				"x": 1,
				"y": 0,
				"z": 0,
				"cost": 56592,
				"value": 115580.184,
				"rock_tonnes": 0,
				"ore_tonnes": 0	},
				{"_id": {"$oid": "5cb0f608b766f9aa245cb3f1"},
				"mineral_deposit": "Zuck small",
				"block_model": "v1",
				"id": 9370,
				"x": 0,
				"y": 1,
				"z": 0,
				"cost": 56592,
				"value": 115580.184,
				"rock_tonnes": 0,
				"ore_tonnes": 0	},
				{"_id": {"$oid": "5cb0f608b766f9aa245cb3f1"},
				"mineral_deposit": "Zuck small",
				"block_model": "v1",
				"id": 9370,
				"x": 1,
				"y": 1,
				"z": 0,
				"cost": 56592,
				"value": 115580.184,
				"rock_tonnes": 0,
				"ore_tonnes": 0	}]
		self.block_model = BlockModel(name, mineral_deposit, headers, data_map, 1, 1, 0)
		self.block_model.add_blocks(blocks)
		self.rx = 1
		self.ry = 1
		self.rz = 1







	def test_change_block_quantity(self):
		self.block_model.reblock(self.rx, self.ry, self.rz)
		new_blocks = self.block_model.count_blocks()
		self.assertEqual(new_blocks, 4)


	def test_new_weight(self):
		old_blocks_weight = self.block_model.get_total_weight()
		self.block_model.reblock(self.rx, self.ry, self.rz)
		new_blocks_weight = self.block_model.get_total_weight()
		self.assertEqual(old_blocks_weight, new_blocks_weight)


	def test_new_mineral_percentage(self):
		old_mineral_weight = self.block_model.get_total_mineral_weight()
		self.block_model.reblock(self.rx, self.ry, self.rz)
		new_mineral_weight = self.block_model.get_total_mineral_weight()
		self.assertEqual(old_mineral_weight, new_mineral_weight)

