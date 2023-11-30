class PascalTriangleException(Exception):
	def __init__(self, message: str = "") -> None:
		super().__init__(message)

class PascalTriangle:
	def __init__(self) -> None:
		self.__n: int = -1
		self.__bin_coefs: dict[tuple[int, int], int] = dict()
		self.__bin_coefs_rows: dict[int, str] = dict()
		self.__built: bool = False

	def build(self, n: int) -> None:
		if not self.__check_n_is_valid(n):
			raise PascalTriangleException("N is not valid! Must be great or equal to zero!")

		self.__n = n
		self.__calculate_bin_coefs()
		self.__built = True

	def show(self, spaces: bool = True) -> None:
		if not self.__built:
			raise PascalTriangleException("Triangle is not built! Call build() first!")

		self.__transform_bin_coefs_into_strings(spaces)

		print("Pascal's triangle for N={}:".format(self.__n))
		for row_number in range(self.__n + 1):
			print(self.__bin_coefs_rows[row_number])

	def __check_n_is_valid(self, n: int) -> bool:
		return n >= 0

	def __calculate_bin_coefs(self) -> None:
		self.__bin_coefs[(0, 0)] = 1
		for n in range(1, self.__n + 1):
			self.__bin_coefs[(n, 0)] = 1
			self.__bin_coefs[(n, n)] = 1
			for k in range(1, n):
				self.__bin_coefs[(n, k)] = self.__bin_coefs[(n - 1, k - 1)] + self.__bin_coefs[(n - 1, k)]

	def __transform_bin_coefs_into_strings(self, spaces: bool) -> None:
		if not spaces:
			for n in range(self.__n + 1):
				row_str: str = ""
				for k in range(n + 1):
					row_str += " " + str(self.__bin_coefs[(n, k)])
				self.__bin_coefs_rows[n] = row_str
			return

		max_length: int = self.__coef_maximum_length()
		for n in range(self.__n + 1):
			coef_str: str = str(self.__bin_coefs[(n, 0)])
			row_str: str = " " * ((self.__n - n) * max_length) + " " * (max_length - len(coef_str)) + coef_str
			for k in range(1, n + 1):
				spaces = " " * max_length
				coef_str = str(self.__bin_coefs[(n, k)])
				term = " " * (max_length - len(coef_str)) + coef_str
				row_str += spaces + term
			self.__bin_coefs_rows[n] = row_str

	def __coef_maximum_length(self) -> int:
		max_length: int = 1
		for n in range(self.__n + 1):
			for k in range(n + 1):
				max_length = max(max_length, self.__count_digits(self.__bin_coefs[(n, k)]))
		return max_length

	def __count_digits(self, number: int) -> int:
		res: int = 0
		while number != 0:
			res += 1
			number //= 10
		return res

def main() -> None:
	print("Enter N:")

	N: int = -1
	while (N < 0):
		N_input = input()
		try:
			N = int(N_input)
		except Exception as e:
			print("Can not interpret \"{}\" as number. Please, enter valid value:".format(N_input))

	print("Do you want to make pretty output? [yes/no]")
	pretty_output_answer: str = input()
	while (pretty_output_answer != "yes" and pretty_output_answer != "no"):
		print("Unknown answer \"{}\". Please, enter \"yes\" or \"no\"".format(pretty_output_answer))
		pretty_output_answer = input()
	pretty_output_switch: bool = True if pretty_output_answer == "yes" else False

	pt: PascalTriangle = PascalTriangle()
	pt.build(N)
	pt.show(pretty_output_switch)

main()
