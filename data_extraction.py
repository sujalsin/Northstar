import json


class data_extraction:

    def __init__(self, filename):
        self.filename = filename

    def title_author(self):
        final_output = {}
        with open(self.filename) as f:
            data = json.load(f)
        for i in data:
            final_output[i["title"]] = i["authors"]

        return final_output

    def author_name(self):
        final_output = []
        with open(self.filename) as f:
            data = json.load(f)
            for i in data:
                final_output.append(i['authors'])
        return final_output