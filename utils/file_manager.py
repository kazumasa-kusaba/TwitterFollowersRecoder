# -*- coding: utf-8 -*-
import os
import json
import csv

class FileManager():
    def get_json_dict_from_json(self, json_file_path):
        data = self.__read_file(json_file_path)
        json_dicts = json.loads(data)
        return json_dicts

    def update_csv_file(self, directory_path, screen_name, timestamp, friends_count, followers_count):
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
        with open(os.path.join(directory_path, screen_name + ".csv"), "a", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, friends_count, followers_count])
    
    def __read_file(self, file_path):
        with open(file_path, "r", encoding="utf8") as f:
            data = f.read()
            return data

    def __write_file(self, file_path, data):
        with open(file_path, "w", encoding="utf8") as f:
            f.write(data)

