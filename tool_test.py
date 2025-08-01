import unittest
from tool import get_lines, parse_and_handle


class ToolTestCase(unittest.TestCase):
    def test(self):
        content = """
            v1: 0, v2: 2 // 1
            v1: 1, v2: 2 // 2
            v1: 2, v2: 2 // 3
            v1: 3, v2: 2 // 4
            v1: 4, v2: 2 // 5
        """
        data = get_lines(content)

        pattern = r"v1: (\d), v2: (\d) // (\d)"
        parse_and_handle(pattern, data, lambda x: (print(x), print(int(x[0]) + int(x[1]) + int(x[2]))))
        print("Hello World!")


if __name__ == "__main__":
    unittest.main()
