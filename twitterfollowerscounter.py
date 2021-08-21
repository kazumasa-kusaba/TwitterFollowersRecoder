# -*- coding: utf-8 -*-
import argparse
import logging
import sys
import os
import tweepy
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "utils")
from utils.file_manager import FileManager

log_handler = logging.StreamHandler(sys.stdout)
log_handler.setFormatter(logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s'))
logger = logging.getLogger(__name__)
logger.addHandler(log_handler)

def record_the_number_of_followers(args, logging_level):
    file_manager = FileManager(logging_level)
    config_dict = file_manager.get_json_dict_from_json(os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json"))
    logger.debug(config_dict)

    auth = tweepy.OAuthHandler(config_dict["twitter_api"]["consumer_key"], config_dict["twitter_api"]["consumer_secret"])
    auth.set_access_token(config_dict["twitter_api"]["access_token"], config_dict["twitter_api"]["access_token_secret"])
    api = tweepy.API(auth)

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("command", help="the command you want to run")
    arg_parser.add_argument("target_screen_name", nargs="*", help="screen name of the target name")
    arg_parser.add_argument("-q", "--quiet", required=False, action="store_true", help="do not output log")
    args = arg_parser.parse_args()

    # set logging configuration
    # TODO: change the log level to INFO later
    logging_level = logging.DEBUG
    if args.quiet == True:
        logging_level = logging.CRITICAL
    logger.setLevel(logging_level)

    if args.command == "record_the_number_of_followers":
        record_the_number_of_followers(args, logging_level)
    else:
        logger.critical("%s is invalid command!!" % args.command)
        sys.exit(1)

