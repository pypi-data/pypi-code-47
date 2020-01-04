class SplunkCimGenerator(object):

    def generate(self, input: bytes) -> Graph:

        # Parse the bytes
        return Graph()


generator = GraphGenerator(SplunkCimGenerator())

generator.run(event, context)