import json
import os
import random


def get_file_path(file_name):
    """Gets the full path to a file relative to the project directory.

    Args:
      file_name: The name of the file.

    Returns:
      The full path to the file.
    """

    project_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(project_dir, "..", "data", file_name)
    return file_path


class ActivationCodeManager:

    @classmethod
    def get_random_activation_code(cls, file_path):
        """Reads activation codes from a JSON file and returns a random one.

        Args:
            file_path: The path to the JSON file.

        Returns:
            A random activation code.
        """
        activation_code_file = get_file_path(file_path)

        with open(activation_code_file, 'r') as f:
            data = json.load(f)
            activation_codes = data['activation-codes']
            return random.choice(activation_codes)


    @classmethod
    def delete_activation_code(cls, file_path, code_to_delete):

        activation_code_file = get_file_path(file_path)

        with open(activation_code_file, 'r') as f:
            data = json.load(f)
            activation_codes = data.get('activation-codes', [])

        if code_to_delete not in activation_codes:
            raise ValueError(f"Activation code '{code_to_delete}' not found in the list.")

        # Remove the code from the list
        activation_codes.remove(code_to_delete)

        # Write the updated list back to the file
        with open(activation_code_file, 'w') as f:
            data['activation-codes'] = activation_codes
            json.dump(data, f, indent=4)
            print(f"Activation code '{code_to_delete}' has been deleted.")