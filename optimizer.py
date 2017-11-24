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
		#print(self.fitness_function(self.populacao[0][0]))

	def run(self):
		cont = 0
		while(True):
			total_fitness = self.avaliar_populacao()
			self.ordenar_populacao()
			if cont == self.n_geracoes:
				break
			cont += 1
			self.selecionar(total_fitness)
			self.mutar()
			
	def selecionar(self, total_fitness): #TODO: verificar e terminar
		norm_fitness = [f[1]/total_fitness for f in self.populacao]
		probs = [sum(norm_fitness[:i+1]) for i in range(len(norm_fitness))]
		
		nova_populacao = []
		cont = 20

		for i in range(cont):
			nova_populacao.append(self.populacao[i])

		while(cont < self.n_individuos):
			r1 = random()
			novo_i1 = self.gen_individuo()
			novo_i2 = self.gen_individuo()
			r2 = random()
			nf1 = nf2 = False
			for (i, individuo) in enumerate(self.populacao):
				if (r1 <= probs[i]  and not nf1):
					novo_i1 = individuo
					nf1 = True
					continue
				if (r2 <= probs[i] and not nf2):
					novo_i2 = individuo
					nf2 = True

				if nf1 and nf2:
					break
			novo_i1, novo_i2 = self.crossover(novo_i1[0], novo_i2[0])
			nova_populacao.append(novo_i1)
			nova_populacao.append(novo_i2)
			cont += 2

		self.populacao = nova_populacao

	def mutar(self):
		for i in range(self.n_individuos):
			if random() < self.p_mutacao:
				self.mutacao(self.populacao[i][0])

	def ordenar_populacao(self):
		self.populacao.sort(key=lambda x: x[1], reverse=True)

	def crossover(self, individuo1, individuo2): #TODO
		i = randint(0, self.n_antenas-1)
		novo_i1 = individuo1[:i] + individuo2[i:]
		novo_i2 = individuo2[:i] + individuo1[i:]

		return [novo_i1,0], [novo_i2,0]

	def mutacao(self, individuo): #TODO: Verificar
		i = randint(0, self.n_antenas-1)
		individuo[i].x = randint(0,self.largura)
		individuo[i].y = randint(0,self.altura)
		individuo[i].pot = randint(1,90)

		return individuo
			
	def avaliar_populacao(self):
		total_fitness = 0
		for i in range (self.n_individuos):
			valor_fitness = self.fitness_function(self.populacao[i][0])
			total_fitness += valor_fitness
			self.populacao[i][1] = valor_fitness
		'''
		for i in range (self.n_individuos):
			valor_fitness = self.populacao[i][1]/total_fitness
			self.populacao[i][1] = valor_fitness
		'''
		return total_fitness

	def fitness_function(self, individuo):
		return ((self.area_coberta(individuo)**3)*(self.sumpot(individuo)))/(self.n_antenas*(self.med_dist_antenas(individuo)))

	def area_coberta(self, individuo): #TODO
		area_total = 0
		for antena in individuo:
			r = self.get_raio(antena)
			area_total += pi*r**2
		
		area_total = (area_total/(self.altura*self.largura))*100

		return area_total

	def get_raio(self, antena):
		# CONSTANTES
		la = 0.125
		gr = 63
		gt = 300
		pr = 0.018 # 18 mW
		pt = antena.pot

		r = 1/(((4*pi)/la) * (sqrt(pr/(pt*gr*gt))))
		#print(r)
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
			antena = Antena(self.largura, self.altura)
			individuo.append(antena)

		individuo = [individuo,0]
		return individuo

class Antena:
	def __init__(self, largura, altura):
		self.x = randint(0,largura)
		self.y = randint(0,altura)
		self.pot = randint(1,90) #db
