from model.model import Model 
from ui.View import View
from presenter.presenter import Presenter



try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
        pass

 
def main() -> None:
    '''Build the application.'''
    
    model = Model()
    view = View()
    presenter = Presenter(model,view)
    presenter.RunUI()


if __name__ == "__main__":
    main()