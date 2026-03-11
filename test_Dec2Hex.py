import unittest                          # used for using unit test methods
import subprocess                        # used for running another program in terminal

class TestDec2Hex(unittest.TestCase):

    def run_script(self, num):           # method to run Dec2Hex.py with different numbers
        result = subprocess.run(
            ["python3", "Dec2Hex.py", str(num)],
            capture_output=True,
            text=True
        )
        result = result.stdout.strip().lower()
        return result.split()[-1]        # gets the last word (the hex value)

    def expected_hex(self, num):
        if num < 0:
            return "-" + hex(-num)[2:]   # handles negative numbers properly
        return hex(num)[2:]              # removes the "0x"

    def test_basic_numbers(self):        # testing different scenarios
        self.assertEqual(self.run_script(10), self.expected_hex(10))
        self.assertEqual(self.run_script(-15), self.expected_hex(-15))
        self.assertEqual(self.run_script(16), self.expected_hex(16))
        self.assertEqual(self.run_script(255), self.expected_hex(255))
        self.assertEqual(self.run_script(0), self.expected_hex(0))

    def test_many_numbers(self):         # testing many numbers in a loop
        for i in range(1000):
            self.assertEqual(self.run_script(i), self.expected_hex(i))

    def test_invalid_inputs(self):       # testing for invalid inputs
        invalid_inputs = ["abc", "10.5", "@", " "]

        for value in invalid_inputs:
            result = subprocess.run(
                ["python3", "Dec2Hex.py", value],
                capture_output=True,
                text=True
            )
            self.assertIn("please provide a valid integer", result.stdout.strip().lower())


if __name__ == "__main__":
    unittest.main()
