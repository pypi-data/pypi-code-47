import os
import csv
import argparse
import utils


def simimgs(in_csv_path: str, out_csv_path: str):
    """This function, simimgs, is the main entrypoint for the script.

        Read through an input csv file, in_csv_path, that contains a list of image path paris, compute their
        similarity score and record the time it takes to run this computation. For each valid pair of images,
        write out the similarity score and running time in an output file, out_csv_path.

    Args:
        in_csv_path: The first parameter.
        out_csv_path: The second parameter.
    """

    try:
        with open(in_csv_path, 'rt', encoding='utf-8') as csv_in:
            with open(out_csv_path, 'wt', encoding='utf-8', newline='') as csv_out:
                csv_reader = csv.reader(csv_in, delimiter=',')
                csv_writer = csv.writer(csv_out, delimiter=',')
                next(csv_reader)  # skip input csv header
                csv_writer.writerow(['image1', 'image2', 'similar', 'elapsed'])

                for line_numb, row in enumerate(csv_reader, start=1):
                    im1_path, im2_path = row[0], row[1]
                    invalid_paths = list(filter(lambda path: not os.path.exists(path), [im1_path, im2_path]))
                    if len(invalid_paths) > 0:
                        print("Invalid line {} in input csv".format(line_numb))
                        if im1_path in invalid_paths:
                            print("--- Image 1 has an invalid path: {}".format(im1_path))
                        if im2_path in invalid_paths:
                            print("--- Image 2 has an invalid path: {}".format(im2_path))
                        continue
                    else:
                        similarity_score, run_time = utils.timed_call(utils.get_similarity, [im1_path, im2_path])
                        csv_writer.writerow([im1_path, im2_path, similarity_score, run_time])
    # TODO
    except Exception as e:
        print('Error: ', e)


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('input_csv_path', metavar='input_csv_path',
                        help='file path to the input csv file')
    parser.add_argument('output_csv_path', metavar='out_csv_path',
                        help='file path to the output csv file')
    args = parser.parse_args()
    simimgs(args.input_csv_path, args.output_csv_path)


if __name__ == '__main__':
    main()
