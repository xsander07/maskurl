"""
maskurl by scrazzz.

:copyright: (c) 2021 scrazzz
:license: MIT, see LICENSE for more details.

"""

__title__ = 'maskurl'
__author__ = 'scrazzz'
__license__ = 'MIT'
__copyright__ = 'Copyright 2021 scrazzz'
__version__ = '0.1.0'

import urllib.parse as uparse
from platform import python_version
import requests

class c:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

if python_version().startswith('2', 0):
    print(
        f'{c.WARNING} You are using Python {python_version()}\n'
        f'Please use Python 3.x{c.ENDC}'
    )
    exit(1)

maskurl = f"""
{c.BLUE}--------------------{c.ENDC}

        MASKURL

{c.CYAN}VERSION:{c.ENDC} 0.1.0
{c.CYAN}MADE-BY:{c.ENDC} scrazzz
{c.CYAN}GITHUB-:{c.ENDC} https://github.com/scrazzz/maskurl

{c.BLUE}--------------------{c.ENDC}

"""
print(maskurl)

def prompt():
    main_url = input(f'{c.GREEN}[1]{c.ENDC} Enter your main URL:\n- ')
    if not main_url.startswith('http://'):
        if not main_url.startswith('https://'):
            print(f'\n{c.FAIL}[ ! ] Invalid URL [ ! ]{c.ENDC}')
            prompt()

    mask_main_url = input(f'\n{c.GREEN}[2]{c.ENDC} Enter a link to mask your main URL. Example: https://google.com, https://amazon.com, https://ebay.com, etc.. :\n- {c.ENDC}')
    if not mask_main_url.startswith('http://'):
        if not mask_main_url.startswith('https://'):
            print(f'{c.FAIL}[ ! ] Invalid MASK URL (http or https link Required) [ ! ]{c.ENDC}\n')
            prompt()

    final_mask = input(
        f"\n{c.GREEN}[3]{c.ENDC} Edit your masked URL (Use words with hyphens or dots Only). Example: free-vbucks, important-survey, free.coupon, etc.. \n"
        f"{c.WARNING}[+] Do NOT include slash (/) here. Example: free/money, hot/videos-here, etc... It will mess up the link and redirect to somewhere you did not intent to.{c.ENDC}\n- "
    )
    if '/' in final_mask:
        print(f'\n{c.FAIL}[ ! ] Do NOT include slash (/) in the above step. It will mess up the link and redirect to somewhere you did not intent to. Start over again. [ ! ]{c.ENDC}')
        exit(1)

    r = requests.get(f'https://is.gd/create.php?format=json&url={uparse.quote(main_url)}')

    if r.status_code != 200:
        print(f'{c.FAIL}[ ! ] Unknown error occured. Status Code: {r.status_code} [ ! ]{c.ENDC}')
        exit(1)

    try:
        js_url = r.json()['shorturl'].strip('https://')
        print(f'\n{c.CYAN}[ + ] Here is your masked URL:{c.ENDC}\n- {mask_main_url}-{final_mask}@{js_url}')
        exit()
    except Exception as e:
        print(f"\n{c.FAIL}[ ! ] An unknown exception has occured. Did you enter a valid URL?{c.ENDC}")
        exit(1)

if __name__ == '__main__':
    try:
        prompt()
    except KeyboardInterrupt:
        exit()
