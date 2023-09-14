import argparse
import csv

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--csv_path",
        type=str
    )
    parser.add_argument(
        "--row",
        type=int,
        default=0,
    )
    parser.add_argument(
        "--column",
        type=int,
        default=0,
    )
    return parser.parse_args()


def main():
    args = parse_args()

    with open(args.csv_path, 'r') as file:
        table = list(csv.reader(file))
    output = table[args.row][args.column]
    print(output)


if __name__ == '__main__':
    main()