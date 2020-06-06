from pytonik.Editor.Resolver import *

class _Fragment(object):

    def __init__(self, raw_text):

        self.raw = raw_text
        
        self.clean = self.clean_fragment()
        
        

    def clean_fragment(self):

        if self.raw[:2] in (VAR_TOKEN_START, BLOCK_TOKEN_START):

            return self.raw.strip()[2:-2].strip()

        return self.raw

    @property
    def type(self):
        raw_start = self.raw[:2]
        if raw_start == VAR_TOKEN_START:
            return VAR_FRAGMENT
        elif raw_start == BLOCK_TOKEN_START:

            block = str('end{}'.format(self.clean[3:9]))
            
            return CLOSE_BLOCK_FRAGMENT if self.clean[:9] == block else OPEN_BLOCK_FRAGMENT

        elif raw_start == COMMENT_TOKEN_START:
            if self.clean.find(TRANSLATOR_COMMENT_MARK):
                self.clean[2:-2].strip()
            return CLOSE_COMMENT_FRAGMENT
        else:

            return TEXT_FRAGMENT

