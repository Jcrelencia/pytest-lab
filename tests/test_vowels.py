from problems.vowels import count_vowels

def test_count_vowels_in_word():
    # Arrange
    word = "banana"

    # Act
    result = count_vowels(word)

    # Assert
    assert result == 3

def test_has_no_vowel():
    #Arrange
    word = "try"

    #Act
    result = count_vowels(word)

    #Assert
    assert result == 0
    

