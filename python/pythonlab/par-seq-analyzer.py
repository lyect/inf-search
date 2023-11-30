class ParenthesisSequenceAnalyzerException(Exception):
	def __init__(self, message: str = "") -> None:
		super().__init__(message)

class ParenthesisSequenceAnalyzer:
	def __init__(self) -> None:
		pass

	def analyze_string(self, seq: str) -> bool:
		return self.__analyze_sequence(seq)

	def analyze_file(self, filepath: str) -> bool:
		try:
			f = open(filepath, "r")
		except FileNotFoundError:
			raise ParenthesisSequenceAnalyzerException(f"File {filepath} not found!")
		except OSError:
			raise ParenthesisSequenceAnalyzerException(f"OS error occurred trying to open {filepath}")
		except Exception:
			raise ParenthesisSequenceAnalyzerException(f"Unexpected error opening {filepath}")
		else:
			with f:
				return self.__analyze_sequence(f.read().strip())

	def __analyze_sequence(self, seq: str) -> bool:
		nLeftParenthesis: int = 0

		for par in seq:
			if par == "(":
				nLeftParenthesis += 1
			elif par == ")":
				nLeftParenthesis -= 1
			else:
				raise ParenthesisSequenceAnalyzerException("Only \"(\" or \")\" must be used in the sequnce!")

		return nLeftParenthesis == 0

def main() -> None:
	print("Do you want to read from terminal or from file? [term/file]")
	mode_answer: str = input()
	while (mode_answer != "term" and mode_answer != "file"):
		print("Unknown answer \"{}\". Please, enter \"term\" or \"file\"".format(mode_answer))
		mode_answer = input()
	mode_switch: bool = True if mode_answer == "term" else False

	analyzer: ParenthesisSequenceAnalyzer = ParenthesisSequenceAnalyzer()

	if mode_switch:
		print("Enter sequence:")
		seq: str = input()
		if analyzer.analyze_string(seq):
			print("\033[92mCorrect sequence!\033[0m")
		else:
			print("\033[91mIncorrect sequence!\033[0m")
	else:
		print("Enter filepath:")
		filepath: str = input()
		if analyzer.analyze_file(filepath):
			print("\033[92mCorrect sequence!\033[0m")
		else:
			print("\033[91mIncorrect sequence!\033[0m")

main()