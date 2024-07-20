

def main() -> None:
	class fib:
		def __init__(self) -> None:
			self.x = 0
			self.y = 1
			self.z = 1
		
		def __iter__(self):
			return self

		def __next__(self) -> int:
			self.z = self.y + self.x
			self.x = self.y
			self.y = self.z
			return self.x

	my_fib = fib().__iter__()

	for _ in range(100):
		print(my_fib.__next__())


if __name__ == '__main__':
	main()