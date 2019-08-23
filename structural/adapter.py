class Japanese:
    def __init__(self):
        self.name = "japanese"

    def speak_japanese(self):
        return "konnichiowa"


class British:
    def __init__(self):
        self.name = "british"

    def speak_british(self):
        return "hello"


class Adapter:
    def __init__(self, language,  **kwargs):
        self._language = language
        self.__dict__.update(kwargs)


british = British()
japanese = Japanese()

b_adapter = Adapter(british, speak=british.speak_british)
j_adapter = Adapter(japanese, speak=japanese.speak_japanese)

print(b_adapter.speak())
print(j_adapter.speak())
