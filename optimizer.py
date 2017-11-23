from math import exp, sqrt, pi
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
		print(self.fitness_function(self.populacao[0][0]))
		

	def run(self):
		while(True):
			# Evaluation
			#for i in range(self.n_geracoes):
			break

	def fitness_function(self, individuo):
		return ((self.area_coberta(individuo)**2)*(self.sumpot(individuo))*(self.med_dist_antenas(individuo)))/(self.n_antenas)

	def area_coberta(self, individuo): #TODO
		area_total = 0
		for antena in individuo:
			r = self.get_raio(antena)
			area_total += pi*r**2
		
		area_total = (area_total/(self.altura*self.largura))*100
		return area_total

	def get_raio(self, antena):
		# CONSTANTES
		la = 30
		gr = 20
		gt = 25
		pr = 3
		pt = antena.pot

		r = 1/(((4*pi)/la) * (sqrt(pr/(pt*gr*gt))))
		return r

	def med_dist_antenas(self, individuo):
		if self.n_antenas == 1: 
			return 1
		dist_total = 0
		for antena in individuo:
			for dif_antena in [x for x in individuo if x != antena]:
				dist_total += sqrt((antena.x - dif_antena.x)**2 + (antena.y - dif_antena.y)**2)

		n_dists = ((self.n_antenas*(self.n_antenas - 1))/2)
		dist_total = (dist_total/2)/n_dists

		return dist_total

	def sumpot(self, individuo):
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

		individuo = (individuo,0)
		return individuo

class Antena:
	def __init__(self, x, y, pot):
		self.x = x
		self.y = y
		self.pot = pot
