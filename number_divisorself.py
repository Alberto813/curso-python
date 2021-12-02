def divisors(num):
	divisors = [i for i in range(1,num+1) if num % i == 0]
	return divisors


def run():
	try:
		num = input("ingresa un numero: ")
		print(divisors(int(num)))
	except ValueError:
		print("debes ingresar un numero")


if __name__ == "__main__":
	run()
