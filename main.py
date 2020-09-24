import sys
from data_loader import DataLoader
from algorithms import Mapping


def main():
    if len(sys.argv) < 2:
        print("Missing parameters")
        return
    name = sys.argv[1]
    temprature = sys.argv[2] if len(sys.argv) > 2 else 10000
    loader = DataLoader('test_cases/')
    tasks, cores = loader.load(name)
    mapping = Mapping(tasks, cores, int(temprature))
    solution = mapping.run()
    loader.dump(name + "_solution", solution)


if __name__ == "__main__":
    main()
