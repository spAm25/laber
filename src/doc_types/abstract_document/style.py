class Style():
    def __init__(self,**kvargs):
        self._style_str = r"""%% Auto generated laber style section""" + '\n'
        ## Размер шрифта
        self._style_str += r"\usepackage[14pt]{extsizes}" + '\n' 

    @property
    def style_str(self):
        return self._style_str

