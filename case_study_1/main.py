from typing import Set, List, Iterable, Dict
from components.component import Component


def order_components(components: Iterable[Component]) -> List[Component]:

    raise NotImplementedError


if __name__ == "__main__":

    # A preconstructed and unordered set of components has been created. The numbering of said components
    # corresponds to that of the diagram provided in Case Study 1, Question 1.

    components: Set[Component] = {
        Component(
            downstream_components=["C02", "C03", "C04"],
            unique_identifier="C01"
        ),
        Component(
            downstream_components=["C05"],
            unique_identifier="C02"
        ),
        Component(
            downstream_components=[],
            unique_identifier="C03"
        ),
        Component(
            downstream_components=["C06"],
            unique_identifier="C04"
        ),
        Component(
            downstream_components=["C07", "C08"],
            unique_identifier="C05"
        ),
        Component(
            downstream_components=["C09"],
            unique_identifier="C06"
        ),
        Component(
            downstream_components=["C10"],
            unique_identifier="C07"
        ),
        Component(
            downstream_components=["C10"],
            unique_identifier="C08"
        ),
        Component(
            downstream_components=["C11", "C12"],
            unique_identifier="C09"
        ),
        Component(
            downstream_components=[],
            unique_identifier="C10"
        ),
        Component(
            downstream_components=[],
            unique_identifier="C11"
        ),
        Component(
            downstream_components=[],
            unique_identifier="C12"
        )
    }


    # Each component is computed in the following loop.
    # The implementation of your ordering algorithm required by Case Study 1, Question 1 will be showcased
    # here.

    for component in order_components(components):

        component.compute()