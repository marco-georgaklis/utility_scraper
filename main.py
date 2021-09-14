import requests
from bs4 import BeautifulSoup

utilities = [
    "find",
    "xargs",
    "grep",
    "rm",
    "echo",
    "ls",
    "sort",
    "chmod",
    "wc",
    "cat",
    "cut",
    "head",
    "mv",
    "chown",
    "cp",
    "mkdir",
    "tr",
    "tail",
    "dirname",
    "rsync"
]


def parse_page(utility):
    """Parses the page for a particular utility in the man7.org man pages
    
    For a given utlity, the function scrapes the html from the man page
    at man7.org and parses the html for the available options for the given
    utility.
    
    :param str utility: The utility we want to find the flags to
    
    :returns a dictionary that maps each corresponding flag to an empty list.
     The format follows:
     
        {
            flag1: [],
            flag2: [],
            flag3: [],
        }
    """

    utility_url = f'https://man7.org/linux/man-pages/man1/{utility}.1.html'
    r = requests.get(utility_url)
    soup = BeautifulSoup(r.text)
    desc = soup.find_all('pre')[2].text
    options = soup.find_all('pre')[4].text
    stripped_options = [line.strip() for line in options.split('\n')]
    flag_lines = list(filter(lambda x: x and x[0] == "-", stripped_options))
    flags = [line.split(" ")[0] for line in flag_lines]
    clean_flags = [f if f[-1] not in punctuation else f[:-1] for f in flags]
    clean_flags = [f if "[" not in f else f.split("[")[0] for f in clean_flags]
    d = {flag: [] for flag in clean_flags}
    return d


def build_utility_structure(utility_list, d=None):
    """Builds a data structure mapping utilities to their flags
    
    For a list of utlities, it parses man7.org for the appropriate flags and
    builds a dictionary mapping the utility to its flags.
    
    :param list utility_list: A list of utlities to 
    :param dictionary d: A dictionary to built the data structure off of.
        Defaults to None.
        
    :returns dictionary that maps each utility to a dictionary that maps
        each flag for the utiltiy to an empty list. Example:
        
        {
            utility1:
                {
                    flag1: [],
                    flag1: [],
                },
            utility2:
                {
                    flag1: [],
                },
        }

    """

    if d is None:
        d = {}

    for utility in utility_list:
        d[utility] = parse_page(utility)

    return d
