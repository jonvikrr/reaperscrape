import pyfiglet

from config.args import get_args
from utils.logginig import logger

def show_banner():
    banner = pyfiglet.figlet_format('ReaperScrape')
    print(f'\n{banner}\n')    

def main():
    show_banner()
    logger.info('Current ReaperScrape version v1.0')

    args = get_args    

    if not args.domain:
        logger.error('Program exiting: no domain provided')
    else:
        logger.info(f'Crawling pages for {args.domain}')

if __name__ == '__main__':
    main()

args = get_args()