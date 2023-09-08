from  .data_manipulation import calculate_average
import pytest

class TestCalculateAverage:

    def test_empty_list(self):
        # Test the function with an empty list
        result = calculate_average([])
        assert result == 0  # Expected result is 0 for an empty list

    def test_list_with_values(self):
        # Test the function with a list of values
        numbers = [1, 2, 3, 4, 5]
        result = calculate_average(numbers)
        assert result == 3.0  # Expected result is the average, which is 3.0

    def test_list_with_negative_values(self):
        # Test the function with a list of negative values
        numbers = [-1, -2, -3, -4, -5]
        result = calculate_average(numbers)
        assert result == -3.0  # Expected result is the average, which is -3.0

    def test_list_with_mixed_values(self):
        # Test the function with a list of mixed positive and negative values
        numbers = [-1, 2, -3, 4, -5]
        result = calculate_average(numbers)
        assert result == -0.6  # Expected result is the average, which is -0.6

    def test_list_with_non_numeric_values(self):
        # Test the function with a list containing non-numeric values
        non_numeric_list = [1, 2, 'three', 4, 5]
        with pytest.raises(TypeError):
            calculate_average(non_numeric_list)  # Should raise a TypeError

    def test_list_with_empty_string(self):
        # Test the function with a list containing an empty string among the numbers
        empty_string_list = [1, 2, '', 4, 5]
        with pytest.raises(TypeError):
            calculate_average(empty_string_list)  # Should raise a TypeError
