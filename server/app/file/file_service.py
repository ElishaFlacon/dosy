import uuid
import os


class FileService():
    # save file to a static folder
    def save_file(self, file):
        # checking for file availability
        if (not file):
            return

        # generate random name
        filename = f'{uuid.uuid4()}.png'

        # save file
        path = os.path.join(os.environ.get('STATIC_PATH'), filename)
        file.save(path)

        return filename

    def remove_file(self, file):
        if (not file):
            return

        os.remove(f'{os.environ.get("STATIC_PATH")}/{file}')
