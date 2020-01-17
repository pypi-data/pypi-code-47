import argparse
import logging
from kakakucom.site.ranking import Ranking
from catscore.lib.time import get_today_date

def main():
    parser = argparse.ArgumentParser(description="kakaku robot")

    # args params
    parser.add_argument('-f', '--function', nargs='*', choices=['all_category_ranking'], help="functions")
    parser.add_argument('-d', '--dump_path', help="result dump path", required=True)
    args = parser.parse_args()
    print(args)
    
    for f in args.function:
        if f == "all_category_ranking":
            output_path = f"{args.dump_path}/kakaku/kakau_rank_{get_today_date()}.csv"
            print(f"all_category_ranking output to {output_path}")
            result = Ranking().all_category_ranking(pandas=True)
            result.to_csv(output_path)
            
if __name__ == "__main__":
    main()