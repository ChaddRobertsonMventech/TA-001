from typing import Set, List, Iterable
from components.component import Component


def generate_sample_space(components: Iterable[Component], sample_count: int) -> List[Set[Component]]:

    raise NotImplementedError


if __name__ == "__main__":

    # A preconstructed and unordered set of components has been created. The numbering of said components
    # corresponds to that of the diagram provided in Case Study 1, Question 1.

    components: Set[Component] = {
        Component(
            parameters={"a": 5, "b": 10, "c": 25},
            sample_allocation={},
            unique_identifier="C01"
        ),
        Component(
            parameters={"d": 8, "e": 12, "f": 16},
            sample_allocation={"e": (2, 98)},
            unique_identifier="C02"
        ),
        Component(
            parameters={"g": 1, "h": 11, "i": 23},
            sample_allocation={"h": (5, 20)},
            unique_identifier="C03"
        )
    }


    # Each component is computed in the following loop.
    # The implementation of your ordering algorithm required by Case Study 1, Question 1 will be showcased
    # here.

    sample_space: List[Set[Component]] = generate_sample_space(components=components)

    for i, sample in enumerate(sample_space):

        print(f"Sample {i}:")
        
        for j, component in enumerate(sample):

            print(component.parameters)