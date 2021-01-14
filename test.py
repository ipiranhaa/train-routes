import unittest

from graph import Graph
from calculator import calculate
from exception import Error, RouteNotFound


class TestTrainRoute(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestTrainRoute, self).__init__(*args, **kwargs)
        mocked_csv = [
            ["A", "B", "5"],
            ["B", "C", "5"],
            ["C", "D", "7"],
            ["A", "D", "15"],
            ["E", "F", "5"],
            ["F", "G", "5"],
            ["G", "H", "10"],
            ["H", "I", "10"],
            ["I", "J", "5"],
            ["G", "J", "20"],
        ]

        self.graph = Graph()
        self.total_weight = 0

        for row in mocked_csv:
            self.graph.add_edge(row[0], row[1], int(row[2]))
            self.total_weight += int(row[2])

    def test_all_edges(self):
        self.assertEqual(self.graph.edges["A"], ["B", "D"])
        self.assertEqual(
            self.graph.edges["B"], ["A", "C"],
        )
        self.assertEqual(
            self.graph.edges["C"], ["B", "D"],
        )
        self.assertEqual(
            self.graph.edges["D"], ["C", "A"],
        )
        self.assertEqual(
            self.graph.edges["E"], ["F"],
        )
        self.assertEqual(
            self.graph.edges["F"], ["E", "G"],
        )
        self.assertEqual(
            self.graph.edges["G"], ["F", "H", "J"],
        )
        self.assertEqual(
            self.graph.edges["H"], ["G", "I"],
        )
        self.assertEqual(
            self.graph.edges["I"], ["H", "J"],
        )
        self.assertEqual(
            self.graph.edges["J"], ["I", "G"],
        )

    def test_total_weight(self):
        self.assertEqual(sum(self.graph.times.values()), self.total_weight * 2)

    def test_A_to_B(self):
        self.assertEqual(calculate(self.graph, "A", "B"), (0, 5))

    def test_A_to_C(self):
        self.assertEqual(calculate(self.graph, "A", "C"), (1, 10))

    def test_E_to_J(self):
        self.assertEqual(calculate(self.graph, "E", "J"), (2, 30))

    def test_A_to_D(self):
        self.assertEqual(calculate(self.graph, "A", "D"), (0, 15))

    def test_A_to_J(self):
        with self.assertRaises(RouteNotFound) as context:
            calculate(self.graph, "A", "J")
        self.assertTrue("No routes from A to J" in str(context.exception))

    def test_empty_input(self):
        with self.assertRaises(Error) as context:
            calculate(self.graph, "", "")
        self.assertTrue(
            "Please input the getting on and off station." in str(context.exception)
        )


if __name__ == "__main__":
    unittest.main()
