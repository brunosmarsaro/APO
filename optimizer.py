from math import exp
from random import randint

class GA:
	def __init__(self, param):	
		self.n_individuos = param.n_individuos
		self.n_geracoes = param.n_geracoes
		self.n_antenas = param.n_antenas
		self.p_crossover = param.p_crossover
		self.p_mutacao = param.p_mutacao
		self.largura = param.largura
		self.altura = param.altura

		self.populacao = self.init_populacao() #mudar para uma esttutura de dados onde tem um evaluation value associado ao individuo

	def run(self):
		while(True):
			# Evaluation
			#for i in range(self.n_geracoes):
			pass

	def fitness_function(self, individuo):
		return ((self.area_coberta(individuo)**2)*(exp(-self.sumpot(individuo))))/self.n_antenas

	def area_coberta(self, individuo): #TODO
		return 1

	def sumpot(individuo):
		soma = 0
		for antena in individuo:
			soma += antena.pot
		return soma

	def init_populacao(self):
		populacao = []
		for i in range(self.n_individuos):
			populacao.append(self.gen_individuo())

		return populacao

	def gen_individuo(self):
		individuo = []
		for i in range(self.n_antenas):
			x = randint(0,self.largura)
			y = randint(0,self.altura)
			pot = randint(0,90) #db
			antena = Antena(x,y,pot)
			individuo.append(antena)

		return individuo

class Antena:
	def __init__(self, x, y, pot):
		self.x = x
		self.y = y
		self.pot = pot
