import matplotlib.pyplot as plt

from parserf import Param
from optimizer import GA

PARAM_FILE = "param.in"


def print_area(ga):
	circulos = []
	for antena in ga.populacao[0][0]:
		r = ga.get_raio(antena)
		print(r)
		circulo = plt.Circle((antena.x, antena.y), r, edgecolor='black')
		circulos.append(circulo)
	fig, ax = plt.subplots()
	ax.set_xlim((0, ga.largura))
	ax.set_ylim((0, ga.altura))
	for circulo in circulos:
		ax.add_artist(circulo)

	fig.savefig('plot.png')

if __name__ == "__main__":
	p = Param(PARAM_FILE)
	ga = GA(p)
	ga.run()
	print(ga.populacao[0][1])
	for antena in ga.populacao[0][0]:
		print(antena.x, antena.y, antena.pot)
	print_area(ga)
