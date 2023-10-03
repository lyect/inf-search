class AlphabetException(Exception):
	def __init__(self, message: str = "") -> None:
		super().__init__(message)

class CaesarDeciphererException(Exception):
	def __init__(self, message: str = "") -> None:
		super().__init__(message)

class Alphabet:
	def __init__(self, name: str, alphabet: str) -> None:
		self.__name: str = name
		self.__lowercase: str = alphabet.lower()
		self.__uppercase: str = alphabet.upper()
		self.__length: int = len(alphabet)

	def get_name(self) -> str:
		return self.__name

	def lowercase_contains(self, letter: str) -> bool:
		return letter in self.__lowercase

	def uppercase_contains(self, letter: str) -> bool:
		return letter in self.__uppercase

	def contains(self, letter: str) -> bool:
		return self.lowercase_contains(letter) or self.uppercase_contains(letter)

	def get_lowercase_letter(self, index: int) -> str:
		if index >= self.__length:
			raise AlphabetException("Lowercase index out of range!")
		return self.__lowercase[index]

	def get_uppercase_letter(self, index: int) -> str:
		if index >= self.__length:
			raise AlphabetException("Uppercase index out of range!")
		return self.__uppercase[index]

	def get_lowercase_index(self, letter: str) -> int:
		if len(letter) != 1:
			raise AlphabetException("Tried to get lowercase index of non-only letter!")
		if not self.lowercase_contains(letter):
			raise AlphabetException("Lowercase does not contain letter \"{}\"".format(letter))
		return self.__lowercase.index(letter)

	def get_uppercase_index(self, letter: str) -> int:
		if len(letter) != 1:
			raise AlphabetException("Tried to get uppercase index of non-only letter!")
		if not self.uppercase_contains(letter):
			raise AlphabetException("Uppercase does not contain letter \"{}\"".format(letter))
		return self.__uppercase.index(letter)

	def get_length(self) -> int:
		return self.__length

RUS_ALPHABET = Alphabet("rus", "абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
ENG_ALPHABET = Alphabet("eng", "abcdefghijklmnopqrstuvwxyz")

class CaesarDecipherer:
	def __init__(self, lang: str, shift: int) -> None:
		self.__lang = lang
		if self.__lang == RUS_ALPHABET.get_name():
			self.__alphabet = RUS_ALPHABET
			self.__shift = shift % RUS_ALPHABET.get_length()
		elif self.__lang == ENG_ALPHABET.get_name():
			self.__alphabet = ENG_ALPHABET
			self.__shift = shift % ENG_ALPHABET.get_length()
		else:
			raise CaesarDeciphererException("\"{}\" is unknown lang!");

	def __decipher_lowercase_letter(self, letter: str) -> str:
		letter_index = self.__alphabet.get_lowercase_index(letter)
		shifted_letter_index = (letter_index + self.__shift) % self.__alphabet.get_length()
		return self.__alphabet.get_lowercase_letter(shifted_letter_index)

	def __decipher_uppercase_letter(self, letter: str) -> str:
		letter_index = self.__alphabet.get_uppercase_index(letter)
		shifted_letter_index = (letter_index + self.__shift) % self.__alphabet.get_length()
		return self.__alphabet.get_uppercase_letter(shifted_letter_index)

	def __decipher(self, text: str) -> str:
		result: str = ""
		for letter in text:
			if not self.__alphabet.contains(letter):
				raise CaesarDeciphererException(
					"Decipherer got unknown letter \"{}\" for language \"{}\"".format(letter, self.__lang))

			deciphered_letter: str = ""
			if letter.islower():
				deciphered_letter = self.__decipher_lowercase_letter(letter)	
			elif letter.isupper():
				deciphered_letter = self.__decipher_uppercase_letter(letter)
			else:
				raise CaesarDeciphererException("Letter \"{}\" is not lowercase or uppercase!".format(letter))

			result += deciphered_letter
		return result
	
	def decipher(self, filepath: str) -> str:
		try:
			f = open(filepath, "r", encoding="utf-8")
		except FileNotFoundError:
			raise CaesarDeciphererException(f"File {filepath} not found!")
		except OSError:
			raise CaesarDeciphererException(f"OS error occurred trying to open {filepath}")
		except Exception:
			raise CaesarDeciphererException(f"Unexpected error opening {filepath}")
		else:
			with f:
				return self.__decipher(f.read().strip())

def main() -> None:
	print("Enter filepath:")
	filepath: str = input()
	
	print("Enter shift:")
	shift: int = int(input())

	print("Do you want to use Russian or English language? [rus/eng]")
	lang_answer: str = input()
	while (lang_answer != "rus" and lang_answer != "eng"):
		print("Unknown answer \"{}\". Please, enter \"rus\" or \"eng\"".format(lang_answer))
		lang_answer = input()

	cs: CaesarCipherer = CaesarDecipherer(lang_answer, shift)
	ans: str = cs.decipher(filepath)

	print("Deciphered text: \"{}\"".format(ans))
	
main()