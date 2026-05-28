from marshmallow import Schema, fields

class PaginadoOutputModel(Schema):
	page = fields.Int()
	per_page = fields.Int()
	total = fields.Int()
	has_next = fields.Bool()
	item_count = fields.Method('item_counter')

	def item_counter(self, obj) -> int:
		try:
			return len(obj.items)
		except:
			return None