import itertools
import math

def find_numbers(numbers, target):
        """
        Function to find which numbers together make up the target number using any of the four operators.
        """
        results = []
        # Sort the array in descending order
        numbers = sorted(numbers, reverse=True)

        # Iterate over all possible combinations of numbers
        for i in range(2, len(numbers) + 1):

            for combo in itertools.combinations(numbers, i):

                # Iterate over all four operators
                for operator in ['+', '-', '*', '/']:

                    # Check the combination based on the current operator
                    if operator == '+':
                        if sum(combo) == target:
                            results.append((combo, operator))

                    elif operator == '-':
                        for perm in itertools.permutations(combo):
                            if perm[0] - sum(perm[1:]) == target:
                                results.append((combo, operator))

                    elif operator == '*':
                        if math.prod(combo) == target:
                            results.append((combo, operator))

                    elif operator == '/':
                        for perm in itertools.permutations(combo):
                            if len(set(perm[1:])) == 1 and perm[0] / perm[1] == target:
                                results.append((combo, operator))

        # remove results with combination of operators
        results = [(numbers, operator)
                    for numbers, operator in results if len(set(operator)) == 1]

        # Print the results clearly
        if results:
            print(
                "\n\n*************************************************************************")
            print(
                f"The following combinations of numbers make up the target number of {target}:\n")
            for r in results:
                print(f"{r[0]} using {r[1]}\n")
        else:
            print(
                "\n\n*************************************************************************")
            print(
                f"No combination of numbers make up the target number of {target} using any of the four operators with a single operator.")

numbers = [18, 2, 15, 20, 30]
target = 15

find_numbers(numbers, target)
