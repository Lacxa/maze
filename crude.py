
class Crude():
    def __init__(self):
        self.data = {}
        self.counter = 1

    def create(self, info):
        self.data[self.counter] = info
        print(f"Successfully  created {self.counter} --> {info}")
        self.counter += 1


    def read(self, data_id=None):
        if data_id:
            reader = self.data.get(data_id, "Record not found")
            print(reader)

        else:
            print(self.data)

    def update(self, data_id, new):
        if data_id in self.data:
            print(f"{self.data[data_id]} --> {new}")
            self.data[data_id] = new

        else:
            print("No record to update")

    def delete(self, data_id):
        if data_id in self.data:
            del self.data[data_id]

        else:
            print("No data to delete")


result = Crude()
result.create("hello")
result.create("how are you")
result.create("de donde")
result.read(2)
result.update(2, "como estas")
result.read()
result.delete(1)
result.read()
