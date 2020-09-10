from data_loader import DataLoader
from algorithms import Mapping


def main():
    loader = DataLoader('test_cases/')
    tasks, cores = loader.load('small')
    mapping = Mapping(tasks, cores)
    mapping.run()


if __name__ == "__main__":
    main()
