"""Demonstrate merge sort and visualize a list before and after sorting."""

import matplotlib.pyplot as plt


EXAMPLE_VALUES = [54, 26, 93, 17, 77, 31, 44, 55, 20]


def merge(left_values: list[int], right_values: list[int]) -> list[int]:
    """Merge two sorted lists into one sorted list.

    Args:
        left_values: The sorted left half.
        right_values: The sorted right half.

    Returns:
        A sorted list containing all values from both input lists.
    """
    merged_values = []
    left_index = 0
    right_index = 0

    while left_index < len(left_values) and right_index < len(right_values):
        if left_values[left_index] <= right_values[right_index]:
            merged_values.append(left_values[left_index])
            left_index += 1
        else:
            merged_values.append(right_values[right_index])
            right_index += 1

    merged_values.extend(left_values[left_index:])
    merged_values.extend(right_values[right_index:])

    return merged_values


def merge_sort(values: list[int]) -> list[int]:
    """Sort a list of integers using the merge sort algorithm.

    The input list is not modified. A new sorted list is returned.

    Args:
        values: The list of integers to sort.

    Returns:
        A new list containing the same values in ascending order.
    """
    if len(values) <= 1:
        return values.copy()

    middle_index = len(values) // 2
    left_half = merge_sort(values[:middle_index])
    right_half = merge_sort(values[middle_index:])

    return merge(left_half, right_half)


def plot_values(values: list[int], title: str) -> None:
    """Plot the values of a list as a line chart.

    Args:
        values: The list of integers to plot.
        title: The title of the plot.
    """
    positions = range(len(values))

    plt.figure()
    plt.plot(positions, values, marker="o")
    plt.title(title)
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.grid(True)
    plt.show()


def main() -> None:
    """Run the merge sort example and show the plots."""
    unsorted_values = EXAMPLE_VALUES
    sorted_values = merge_sort(unsorted_values)

    plot_values(unsorted_values, "Values before merge sort")
    plot_values(sorted_values, "Values after merge sort")


if __name__ == "__main__":
    main()