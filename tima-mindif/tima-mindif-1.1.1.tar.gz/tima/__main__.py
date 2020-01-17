import argparse
import sys
import os
from loguru import logger
from . import utils

# from .tima_mindif_processor import tima_mindif_processor as tima14
from .tima_mindif_processor import tima_mindif_processor


@logger.catch
def main():
    parser = argparse.ArgumentParser(description="Process TIMA data")
    parser.add_argument("project_path", type=str, help="Path to the TIMA project")
    parser.add_argument("mindif_root", type=str, help="Path to the MinDif root")
    parser.add_argument(
        "--output",
        "-o",
        dest="output",
        default="./",
        type=str,
        help="Path to the desired output folder",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Prints more information about app progress.",
    )
    parser.add_argument("--thumbs", action="store_true", help="Create thumbnails.")
    args = parser.parse_args()

    logger_config = {
        "handlers": [
            {
                "sink": sys.stdout,
                "level": "INFO" if not args.verbose else "DEBUG",
                "format": "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
                "<level>{message}</level>",
            }
        ]
    }
    logger.configure(**logger_config)

    utils.create_thumbnail = True if args.thumbs else False

    if not os.path.exists(args.project_path):
        logger.error("Could not find: {}", args.project_path)
        return

    if not os.path.exists(args.mindif_root):
        logger.error("Could not find: {}", args.mindif_root)
        return

    tima_mindif_processor(
        args.project_path, args.mindif_root, args.output,
    )


if __name__ == "__main__":
    main()
