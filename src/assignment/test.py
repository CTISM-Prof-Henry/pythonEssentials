import unittest

class Testador(unittest.TestCase):

	def test_main(self):
		try:
			from assignment import main as other_main
		except Exception as e:
			raise Exception('Existe algum erro no código-fonte. ' 
				'Certeza que escreveu tudo certo?')
		self.assertEqual(2, other_main(), 'O código-fonte está errado!')

def main():
	unittest.main()

if __name__ == '__main__':
	main()