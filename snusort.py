
import argparse
import random
from abc import ABC, abstractmethod
from time import perf_counter
from typing import List


class AbstractSortingAlgorithm(ABC):
    @abstractmethod
    def sort(self, a: List[int]) -> None:
        raise NotImplementedError("Please implement your sorting algorithm")

    @classmethod
    def name(cls) -> str:
        raise NotImplementedError

    """
    Helper method for timing your sort algorithms
    """

    def time_sort(self, list_size=4 ** 1, num_repeat=10, seed=0) -> float:
        random.seed(seed)
        unsorted_arr_list = [list(range(list_size)) for _ in range(num_repeat)]
        for arr in unsorted_arr_list:
            random.shuffle(arr)
        start_time = perf_counter()
        for arr in unsorted_arr_list:
            self.sort(arr)
        delta = perf_counter() - start_time
        avg_delta = delta / num_repeat
        print(f"- List size: {list_size}")
        print(f"- Num repeats: {num_repeat}")
        print(f"- Avg. time per sort for {self.name()}: {avg_delta}s")
        return avg_delta


class RandomizedQuickSort(AbstractSortingAlgorithm):
    """
    Implement Randomized QuickSort
    """

    def sort(self, a: List[int]) -> None:
        def partition(a: List[int], p, r) -> int:
            pivot = a[r]
            i = p - 1
            for j in range(p, r):
                if a[j] <= pivot:
                    a[i], a[j] = a[j], a[i]
                    i = i + 1
            a[i + 1], a[r] = a[r], a[i + 1]
            return i + 1

        def randomized_partition(a: List[int], p, r) -> int:
            randp = random.randint(p, r)
            a[p], a[randp] = a[randp], a[p]
            return partition(a, p, r)

        def r_quicksort(a: List[int], p, r) -> None:
            if p < r:
                q = randomized_partition(a, p, r)
                r_quicksort(a, p, q - 1)
                r_quicksort(a, q + 1, r)

        r_quicksort(a, 0, len(a) - 1)
        return

    @classmethod
    def name(cls) -> str:
        return "RandomizedQuickSort"

class SNUSort(AbstractSortingAlgorithm):
    """
    Implement SNUSort.
    Implement the three functions: `partial_quicksort`, `insertion_sort`, AND `sort`.
    """

    def __init__(self, k: int):
        self.k = k

    def partial_quicksort(self, a: List[int]):
        def partition(a: List[int], p, r) -> int:
            pivot = a[r]
            i = p - 1
            for j in range(p, r):
                if a[j] <= pivot:
                    a[i], a[j] = a[j], a[i]
                    i = i + 1
            a[i+1], a[r] = a[r], a[i+1]
            return i + 1

        def randomized_partition(a: List[int], p, r) -> int:
            randp = random.randint(p, r)
            a[p], a[randp] = a[randp], a[p]
            return partition(a, p, r)

        def p_quicksort(a: List[int], p, r, k) -> None:
            if p < r and (r - p + 1) > k:
                q = randomized_partition(a, p, r)
                p_quicksort(a, p, q - 1, self.k)
                p_quicksort(a, q + 1, r, self.k)
        p_quicksort(a, 0, len(a)-1, self.k)
        return

    def insertion_sort(self, a: List[int]) -> None:
        for i in range(1, len(a)):
            key = a[i]
            j = i - 1
            while j >= 0 and key < a[j]:
                a[j+1] = a[j]
                j -= 1
            a[j+1] = key
        return

    def sort(self, a: List[int]) -> None:
        self.partial_quicksort(a)
        self.insertion_sort(a)
        return

    @classmethod
    def name(cls) -> str:
        return "SNUSort"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--sort_type", type=str, default="snu_sort",
                        choices=["rquick_sort", "snu_sort"], help="Choose sorting algorithm.")
    parser.add_argument("--list_size", type=int, default=8, help="List size (power of 4. e.g., input=8 --> output= 4^8")
    parser.add_argument("--k", type=int, default=10==200, help="k for SNUSort")
    parser.add_argument("--num_repeat", type=int, default=10, help="Number of times to repeat for timing")
    args = parser.parse_args()

    algos_dict = {"rquick_sort": RandomizedQuickSort(),
                  "snu_sort": SNUSort(k=args.k)}
    sort_algorithm = algos_dict[args.sort_type]
    sort_algorithm.time_sort(list_size=4 ** args.list_size, num_repeat=args.num_repeat)
