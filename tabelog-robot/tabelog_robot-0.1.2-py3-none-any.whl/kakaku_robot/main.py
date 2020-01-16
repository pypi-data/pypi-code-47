import argparse
import logging
from kakaku_robot.site.ranking import Ranking

def main():
    parser = argparse.ArgumentParser(description="kakaku robot")

    # args params
    parser.add_argument('-f', '--function', nargs='*', choices=['all_category_ranking'], help="functions")
    parser.add_argument('-d', '--dump_path', help="result dump path", required=True)
    args = parser.parse_args()
    print(args)
    
    for f in args.function:
        if f == "all_category_ranking":
            output_path = f"{args.dump_path}/kakau_rank.csv"
            print(f"all_category_ranking output to {output_path}")
            result = Ranking().all_category_ranking(pandas=True)
            result.to_csv(output_path)
            
if __name__ == "__main__":
    main()