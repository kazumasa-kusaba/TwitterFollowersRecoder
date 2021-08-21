# -*- coding: utf-8 -*-
import sys
import logging
import json

class FileManager():
    def __init__(self, logging_level):
        log_handler = logging.StreamHandler(sys.stdout)
        log_handler.setFormatter(logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s'))
        self.logger = logging.getLogger(__name__)
        self.logger.addHandler(log_handler)
        self.logger.setLevel(logging_level)
    
    def get_json_dict_from_json(self, json_file_path):
        data = self.__read_file(json_file_path)
        json_dicts = json.loads(data)
        return json_dicts
    
    def __read_file(self, file_path):
        with open(file_path, "r", encoding="utf8") as f:
            data = f.read()
            return data

    def __write_file(self, file_path, data):
        with open(file_path, "w", encoding="utf8") as f:
            f.write(data)

