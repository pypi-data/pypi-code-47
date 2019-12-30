from StarkLego.lego_builders.model.blocks import TwoXTwoBlock
from StarkLego.lego_builders.model.dimensions import StarkDimensions

const = {
            "3003.DAT": TwoXTwoBlock,
        }

class FileNameToLdrawBlockMapper():
   
    @staticmethod
    def map(filename):
        print(const.get(filename))
        return const.get(filename)

