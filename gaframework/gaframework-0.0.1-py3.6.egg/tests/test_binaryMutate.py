from unittest import TestCase
from GaPy.binary_mutate import *


class TestBinaryMutate(TestCase):

    def test__mutate_gene(self):

        mutate = BinaryMutate(1.0)
        self.assertEqual(1.0, mutate._p == 1.0)

        gene = True
        m_gene = mutate._mutate_gene(gene)
        self.assertFalse(m_gene)

        gene = False
        m_gene = mutate._mutate_gene(gene)
        self.assertTrue(m_gene)

    def test__mutate_chromosome(self):

        mutate = BinaryMutate(1.0)
        chromosome = Chromosome()

        mutate = BinaryMutate(1.0)

        # create set 16 genes to true
        for i in range(16):
            chromosome.genes.append(True)

        # with a probability of 1.0, all genes should be mutated
        mutate._mutate_chromosome(chromosome)

        self.assertEqual("0000000000000000", str(chromosome))


