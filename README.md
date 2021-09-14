# Linux Man Page Parser

This repository contains a tool for scraping information from the linux man pages and creating a data structure to map
bash utilities to all of their possible flags and corresponding argument types.

Currently, the tool supports 23 of the most popular utilities, stored in the 'utilities' list.

```
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
```
The return dictionary maps utilities to a dictionary of flag name, argument type pairs. The argument types come in a
list as one flag can have multiple corresponding arguments. The return dictionary comes in the format shown below.
```
{
    utility1:
        {
            flag1: [argtype1],
            flag1: [argtype1, argtype2],
        },
    utility2:
        {
            flag1: [],
        },
}
```

