# with open("data_file.json", "w+") as write_file:
#     json.dump(data, write_file)

import json
class StorefrontConfig():
    data: object

    def __int__(self, data):
        self.data=data

class FileController():
    def read_file(self):
        """
        read JSON file
        :return:
        """
        my_file = open("/Users/hainguyen/Documents/workspace_python/PythonTutorial/Modules/data.json", "r")
        print(my_file.read())
        my_file.close()
        pass
    def write_file(self):
        """
        write Json file
        :return:
        """
        my_file = open("/Users/hainguyen/Documents/workspace_python/PythonTutorial/Modules/file_name.json", "w")
        print(my_file.write())
        my_file.close()
