from parser import Param
from optimizer import GA

PARAM_FILE = "param.in"

if __name__ == "__main__":
	p = Param(PARAM_FILE)
	ga = GA(p)
	ga.run()
	
