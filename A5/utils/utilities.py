from repository.repository import Repository
from domain.plane import Plane
from domain.passenger import Passenger

class Utilities:
    def __init__(self, repo: Repository):
        self.__repo = repo

    @staticmethod
    def filter_data(data, filter_func=None):
        """
        Filter data based on a provided filter function.

        Args:
            data (list): The list of objects to be filtered.
            filter_func (callable, optional): A function to filter elements in the list.

        Returns:
            list: A filtered list of objects.
        """
        if filter_func:
            return [item for item in data if filter_func(item)]
        return data


    @staticmethod
    def sort_data(data, sort_key=None, order_func=None):
        """
        Sort data based on a provided sort key and a comparison function.

        Args:
            data (list): The list of objects to be sorted.
            sort_key (callable, optional): A function to extract a comparison key for sorting.
            order_func (callable, optional): A function that takes two arguments and returns True
                                            if the first argument should come before the second.

        Returns:
            list: A sorted list of objects.
        """
        if not sort_key or not order_func:
            return data

        n = len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if not order_func(sort_key(data[j]), sort_key(data[j + 1])):
                    data[j], data[j + 1] = data[j + 1], data[j]

        return data
    
    @staticmethod 
    def generalized_backtracking(data, k, is_valid_group):
        """
        Generalized backtracking function to form groups based on constraints.

        Args:
            data (list): The list of items to group.
            k (int): The size of each group.
            is_valid_group (callable): A function that takes the current group and a new item
                                    and returns True if the item can be added to the group.

        Returns:
            list: A list of valid groups.
        """
        group_list = []

        def backtrack(group, index):
            if len(group) == k:
                group_list.append(group.copy())
                return

            for i in range(index, len(data)):
                if is_valid_group(group, data[i]):
                    group.append(data[i])
                    backtrack(group, i + 1)
                    group.pop()

        backtrack([], 0)
        return group_list