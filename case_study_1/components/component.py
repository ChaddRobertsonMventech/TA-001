from typing import List


class Component:


    def __init__(self, downstream_components: List[str], unique_identifier: str):
        
        self.downstream_components = downstream_components
        self.unique_identifier = unique_identifier


    def compute(self):

        print(f"Component {self.unique_identifier} computed successfully")


if __name__ == "__main__":

    pass