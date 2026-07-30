from problems.calc import add


def test_add_positive():
    # Arrange
    a, b = 2, 3
    # Act
    result = add(a, b)
    # Assert
    assert result == 5


def test_add_negative():
    # Arrange
    a, b = -1, -1
    # Act
    result = add(a, b)
    # Assert
    assert result == -2
