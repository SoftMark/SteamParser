class Collector:
    kwargs = {}

    @classmethod
    def collect(cls, **kwargs):
        print("Old data:", cls.kwargs)
        print("Got *kwargs:", kwargs)
        cls.kwargs.update(kwargs)
        print("Updated! New data:", cls.kwargs)
        print("------------------")


names = ["Larry", "Jake", "Victor", "Dan"]
names_dict = {i: name for i, name in enumerate(names)}

for key in names_dict:
    Collector.collect(key=names_dict[key])
#names_tuples = [(i,name) for i, name in enumerate(names)]






#Collector.collect(*list(enumerate(names)))



#Collector.collect(name=name)

# def tester(*args, **kwargs):
#     print("args:", args)
#     print("kwargs:", kwargs)
#
#
#




#Collector.show()
#
#
# tester(1, "a", 7, emp1="Larry", emp2="Jake", args=8)
#

# my_d = {"a": "1"}
# my_d.update({"b":2})
# print(my_d)