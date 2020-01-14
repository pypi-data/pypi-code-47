from flask import Flask, request;
from qdatabase import QDatabase;
from qhilbertspace import QHilbertspace;


class QServer():



	def __init__(self, quantumics=None):
		self.app = Flask(__name__);
		self.quantumics = quantumics



	async def build(self):
		

		@self.app.route("/train")
		async def train(data):
			data = json.dump(data);
			model_id = self.quantumics.config.database['models'].insert()
			try:
				model = self.quantumics.system.operator.train(data['inputD'], data['outputD']);
				return self.quantumics.config.database['models'].update(model_id, model.to_json());
			except Exception as e:
				self.quantumics.config.database['models'].remove({"_id": model_id});
				return {"status":"404", "error":str(e)};



		@self.app.route("/insert")
		def insert(data):
			data = json.dump(data)
			return self.quantumics.config.database.insert(data['dataset']);



		@self.app.route("/delete")
		def delete(data):
			data = json.dump(data)
			return self.quantumics.config.database.remove(data['dataset']);
		


		@self.app.route("/evaluate")
		def evaluate(data):
			data = json.dump(data)
			return self.quantumics.system.operator.evaluate(data['inputD']);



		@self.app.route("/fit")
		def fit(data):
			return self.evaluate(data);



		@self.app.route("/test")
		def test(data):
			data = json.dump(data)
			return self.quantumics.system.operator.test(data['inputD'], data['outputD']);

		

	def run(self):
		self.build();
		return self.app.run();



	def start(self):
		return self.run();






