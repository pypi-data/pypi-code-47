from ofxReaderBR.writer.IWriterController import IWriterController


class BSWriterController(IWriterController):
    def write(self, data, factory, outputFilename=''):
        return data
