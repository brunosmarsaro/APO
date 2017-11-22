class Param:
	def __init__(self, file):
		self.file = file
		self.run()

	def run(self):
		fp = open(self.file, "r")
		for line in fp:
			if "individuos" in line:
				i = line.index(':')				
				self.n_individuos = int(line[(i+1):])
			elif "geracoes" in line:
				i = line.index(':')				
				self.n_geracoes = int(line[(i+1):])
			elif "crossover" in line:
				i = line.index(':')				
				self.p_crossover = float(line[(i+1):])
			elif "mutacao" in line:
				i = line.index(':')				
				self.p_mutacao = float(line[(i+1):])
			elif "antenas" in line:
				i = line.index(':')				
				self.n_antenas = int(line[(i+1):])
			elif "Largura" in line:
				i = line.index(':')				
				self.largura = float(line[(i+1):])
			elif "Altura" in line:
				i = line.index(':')				
				self.altura = float(line[(i+1):])
		fp.close()

