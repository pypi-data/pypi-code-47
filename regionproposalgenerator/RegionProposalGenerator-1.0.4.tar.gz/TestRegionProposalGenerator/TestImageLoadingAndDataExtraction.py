import RegionProposalGenerator
import unittest

class TestImageLoadingAndDataExtraction(unittest.TestCase):

    def setUp(self):
        self.rpg = RegionProposalGenerator.RegionProposalGenerator(data_image="halfsun.jpg")
        self.rpg.extract_data_pixels_in_bb("halfsun.jpg", [5,5,6,6])

    def test_loaded_image(self):
        print("testing image loading and pixel data extraction")
        self.rpg.displayImage(self.rpg.data_im)
        width,height = self.rpg.data_im.size
        val = self.rpg.extract_data_pixels_in_bb("halfsun.jpg", [5,5,6,6])
        self.assertEqual(width, 150)
        self.assertEqual(height, 49)
        self.assertEqual(str(val[0][0]),'[47  7  8]')

def getTestSuites(type):
    return unittest.TestSuite([
            unittest.makeSuite(TestImageLoadingAndDataExtraction, type)
                             ])                    
if __name__ == '__main__':
    unittest.main()

