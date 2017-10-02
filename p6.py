class TextProcessor:
    def __init__(self, test_string):
        self.test_string = ''

        def count_alphabet():
            count = 0
            for letter in test_string:
                count += 1
                return count

        def vowel_capitalization():
            to_upper = ['a', 'e', 'i', 'o', 'u']
            array = []
            for c in test_string:
                if c in to_upper:
                    c = c.upper()
                array.append(c)
            print(''.join(array))

        def concat(new_string):
            ''.join(test_string, new_string)

        def search(sub):
            try:
                test_string.find(sub)
            except ValueError:
                print(-1)

               
