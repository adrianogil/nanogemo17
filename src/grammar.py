from utils import get_random

class SimpleGrammar:
    def __init__(self):
        self.reset_tags()

    def reset_tags(self):
        self.tags = {}

    def add_tag(self, tag, expression):
        self.tags[tag] = expression
 
    def evaluate(self, text):
        found_tags = self.parse_tags_from(text)

        # print('evaluate - ' + str(found_tags))

        tags_evaluated = self.evaluate_taglist(found_tags)

        text_evaluated = text

        for i in xrange(0, len(tags_evaluated)):
            text_evaluated = text_evaluated.replace("#" + found_tags[i] + "#", tags_evaluated[i])

        return text_evaluated

    def evaluate_taglist(self, tag_list):
        tags_evaluated = []

        for t in tag_list:
            if t in self.tags:
                tagged_text = get_random(self.tags[t])
                tags_evaluated.append(self.evaluate(tagged_text))

        return tags_evaluated

    def parse_tags_from(self, text):
        '''
            Tags are between ##
        '''
        current_tag = ''
        found_tags = []
        inside_tag = False

        for s in text:
            if s == '#':
                if inside_tag:
                    found_tags.append(current_tag)
                current_tag = ''
                inside_tag = not inside_tag
            elif inside_tag:
                current_tag = current_tag + s

        return found_tags
