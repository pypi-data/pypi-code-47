import unittest
from . import gvc_vcf_pipeline



class TestDbsnp(unittest.TestCase):
    

    def test_correct_filename(self):
        gvc_vcf_pipeline.check_dbsnp_format("/disk/db/ref//human.fa",'/disk/db/dbsnp/dbsnp_138-1000G-snp.RS-1000G.1-Y.sort.nonchr')
        
if __name__ == "__main__":
    unittest.main()