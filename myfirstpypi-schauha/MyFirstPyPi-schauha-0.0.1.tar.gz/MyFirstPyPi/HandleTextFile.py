class GetLines:
    def file_len(fname):
        num_lines = sum(1 for line in open('fname'))
        return num_lines
