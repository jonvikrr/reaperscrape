import argparse

def get_args(): 
    parser = argparse.ArgumentParser(description='ReaperScrape')
    parser.add_argument('-d', '--domain', help='Starting domain')

    return parser.parse_args()