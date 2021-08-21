# TwitterFollowersCounter
A tool for counting the number of Twitter friends and followers and recording as CVS file on a regular basis.

## Features
This tool can:  
* retrieve the number of friends and followers using Twitter API.  
* record them as CSV file on a regulary basis using cron.  

# Installation
Just clone this and start using it.  
```console
git clone https://github.com/kazumasa-kusaba/TwitterFollowersCounter.git
```

## Dependencies
* [tweepy](https://github.com/tweepy/tweepy)
  
Just do:  
```console
$ pip install tweepy
```

# Usage
```
usage: twitterfollowerscounter.py [-h] [-q] command [target_screen_name [target_screen_name ...]]

positional arguments:
  command             the command you want to run
  target_screen_name  screen name of the target name

optional arguments:
  -h, --help          show this help message and exit
  -q, --quiet         do not output log
```

## Commands
| Command Name | Description |
|--------------|-------------|
| record       | - Retrieve the number of friends and followers of any user specified by the arguments and record them as CSV file.<br>- The CSV files will be saved in `/result` direcotry.<br>- The CSV format is `"datetime, friends_count, followers_count"`. |

# License
```
MIT License

Copyright (c) 2021 Kazumasa Kusaba

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

