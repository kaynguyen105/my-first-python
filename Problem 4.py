from Modules.modify_data import ModifyData
import json
from Modules.modify_data import ModifyData


class StorefrontConfig:
    def __init__(self, data):
        self.data = data

    def update(self, modify_data):
        update_helper(self.data, modify_data)


def update_helper(data, modify_data):
    for key, value in modify_data.items():
        if key in data.keys() and not isinstance(value, dict):
            data[key] = value
        else:
            data[key] = update_helper(data[key], value)
    return data


class FileController:

    def read_file(self, location):
        """
        read JSON file
        :return:
        """
        f = open(location)
        data_str = f.read()
        data = json.loads(data_str)

        store_config = StorefrontConfig(data)
        return store_config

    def write_file(self, storefront_config, file_name):
        """
        write Json file
        :return:
        """
        my_file = open("/Users/hainguyen/Documents/workspace_python/PythonTutorial/Modules/file_name.json", "w")
        my_file.write(json.dumps(storefront_config.data))
        my_file.close()




file_controller = FileController()
config= file_controller.read_file("/Users/hainguyen/Documents/workspace_python/PythonTutorial/Modules/data.json")
config.update(ModifyData.modify_data)
file_controller.write_file(config, "file_name.json")
