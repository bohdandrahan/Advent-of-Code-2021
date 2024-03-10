class Input_Reader():
    def __init__(self, file_path):
        self.file = open(file_path)
        self.convert_to_list()

    def convert_to_list(self):

        self.data = []

        for i, line in enumerate(self.file):
            self.data.append([int(each.strip()) for each in line.split()])

    def get_data(self):
        return self.data
