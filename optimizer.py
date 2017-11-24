from math import exp, sqrt, pi
from random import randint, random

class GA:
	def __init__(self, param):	
		self.n_individuos = param.n_individuos
		self.n_geracoes = param.n_geracoes
		self.n_antenas = param.n_antenas
		self.p_crossover = param.p_crossover
		self.p_mutacao = param.p_mutacao
		self.largura = param.largura
		self.altura = param.altura

		self.populacao = self.init_populacao()		

	def run(self):
		cont = 0
		while(True):
			self.avaliar_populacao()
			if cont == self.n_geracoes:
				break
			cont += 1
			self.ordenar_populacao()
			self.selecionar()
			# SELECIONAR
			# APLICAR OPERADORES GENETICOS

	def selecionar(self): #TODO: verificar e terminar
		nova_populacao = []
		continua_m = int(0.3*self.n_individuos)
		continua_p = int(0.15*self.n_individuos) + 1
		for i in range(continua_m):
			nova_populacao.append(self.populacao[i])
		for i in range(1, continua_p):
			nova_populacao.append(self.populacao[self.n_individuos - i])


	def ordenar_populacao(self):
		self.populacao.sort(key=lambda x: x[1], reverse=True)

	def crossover(self, individuo1, individuo2): #TODO
		pass

	def mutacao(self, individuo): #TODO: Verificar
		i = randint(0,self.n_antenas-1)
		if random() < 0.3:
			individuo[i].x = randint(0,self.largura)
		if random() < 0.3:
			individuo[i].y = randint(0,self.altura)
		if random() < 0.2:
			individuo[i].pot = randint(1,90)

		return individuo
			
	def avaliar_populacao(self):
		total_fitness = 0
		for i in range (self.n_individuos):
			valor_fitness = self.fitness_function(self.populacao[i][0])
			total_fitness += valor_fitness
			self.populacao[i][1] = valor_fitness

		for i in range (self.n_individuos):
			valor_fitness = self.populacao[i][1]/total_fitness
			self.populacao[i][1] = valor_fitness

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
			pot = randint(1,90) #db
			antena = Antena(x,y,pot)
			individuo.append(antena)

		individuo = [individuo,0]
		return individuo

class Antena:
	def __init__(self, x, y, pot):
		self.x = x
		self.y = y
		self.pot = pot
