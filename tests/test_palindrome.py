from problems.palindrome import is_palindrome
from problems.palindrome import is_palindrome, is_palindrome_list

def test_is_a_palindrome():
    #Arrange
    word = "racecar" 

    #Act
    result = is_palindrome(word)

    #Assert
    assert result == True

def test_is_not_a_palindrome():
    #Arrange
    word = "Jack"

    #Act 
    result = is_palindrome(word)

    #Assert
    assert result == False

def test_is_a_single_character_palindrome():
    #Arrange
    word = "a"

    #Act
    result = is_palindrome(word)

    assert result == True

def test_is_a_palindrome_phrase():
    # Arrange
    word = "never odd or even"
    # Act
    result = is_palindrome(word)
    # Assert
    assert result == True

def test_is_palindrome_list():
    # Arrange
    code = [114, 97, 99, 101, 99, 97, 114]

    # Act
    result = is_palindrome_list(code)

    # Assert
    assert result == True
