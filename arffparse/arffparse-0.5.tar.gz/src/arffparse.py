import argparse

parser = argparse.ArgumentParser(description="ARFF parsing tool")
parser.add_argument("input", help="path for input ARFF file")
parser.add_argument("-o", "--out", help="name of output file")
parser.add_argument("-v", "--verbose", help="display more info", action="store_true")
parser.add_argument(
    "-t", "--test", help="run post write validation checks", action="store_true",
)

args = parser.parse_args()
verbose = args.verbose


def read_file(file_path):
    with open(file_path, "r") as f:
        return f.read()


def print_verbose(msg, end="\n"):
    if verbose:
        print(msg, end=end)


def main():

    input_path = args.input
    output_path = args.out if args.out else None

    print_verbose("using input file %s" % input_path)

    data = read_file(input_path)

    if not output_path:
        # use relation name with no spaces
        for line in data.split("\n"):
            if line.startswith("@relation"):
                output_path = line.split(" ")[1].replace(" ", "-") + ".csv"
                break

    print_verbose("using output file %s" % output_path)

    # build attributes
    print_verbose("parsing attributes")

    attributes = [line for line in data.split("\n") if line.startswith("@attribute")]
    attributes = [attr.replace("\t", " ") for attr in attributes]
    attributes = [attr.split(" ")[1] + "," for attr in attributes]
    attributes[-1] = attributes[-1].rstrip(",")
    attributes.append("\n")

    total_attributes = len(attributes) - 1  # dont count \n
    print_verbose("%d attributes found" % total_attributes)

    # build data
    print_verbose("parsing data rows")

    data_rows = []
    found = False
    for line in data.split("\n"):

        if line.startswith("%"):
            continue

        if found:
            line += "\n"
            data_rows.append(line)

        if line.startswith("@data"):
            found = True

    print_verbose("writing to %s" % output_path)

    # output data
    with open(output_path, "w+") as f:
        f.writelines(attributes)
        f.writelines(data_rows)

    print_verbose("finished writing")

    if args.test:
        print_verbose("running tests")
        print_verbose("validation CSV format ..", end=" ")
        with open(output_path, "r") as f:
            for line_n, line in enumerate(f.readlines()[1:-1]):
                if len(line.split(",")) != total_attributes:
                    print(
                        "ERROR: Something went wrong, number of attributes "
                        "do not match rows in data"
                    )
                    print("line %s appears to be invalid" % line_n)
                    print(line)
                    exit()
        print_verbose("OK")

    print_verbose("Done")


if __name__ == "__main__":
    main()
