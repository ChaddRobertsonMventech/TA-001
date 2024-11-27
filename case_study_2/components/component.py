from typing import Dict, Tuple


class Component:


    def __init__(self, parameters: Dict[str, float], sample_allocation: Dict[str, Tuple[float, float]], unique_identifier: str):

        self.parameters = parameters
        self.sample_allocation = sample_allocation
        self.unique_identifier = unique_identifier


if __name__ == "__main__":

    pass