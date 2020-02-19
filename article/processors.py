class PostProcessor:
    @staticmethod
    def process_code(text):
        # TODO
        text = text.replace("<source>", "<textarea>")
        text = text.replace("</source>", "</textarea>")
        return text

    @staticmethod
    def process(text):
        text = PostProcessor.process_code(text)
        return text
