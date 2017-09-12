
#======================================================
# AUTHOR: John Spataro
# DESCRIPTION:
#       Qt utilities.
#======================================================

## Imports
 
from PyQt5 import Qt
import formatting as fmt

## Classes

class ListSelectionDialog(Qt.QDialog):

    def __init__(self, items=None, message='',
                 select_multiple=False, parent=None):

        # Init Subclass
        Qt.QDialog.__init__(self, parent)

        # Init Widgets
        self.msg = Qt.QLabel(message)
        self.list_widget = Qt.QListWidget()
        self.ok_button = Qt.QPushButton('OK')

        self.setLayout(Qt.QVBoxLayout())
        
        button_layout = Qt.QHBoxLayout()
        button_layout.addWidget(self.ok_button)

        self.layout().addWidget(self.msg)
        self.layout().addWidget(self.list_widget)
        self.layout().addLayout(button_layout)

        self.ok_button.clicked.connect(self.close)

        # Populate Items
        if items is not None:
            for item in items:
                self.addItem(item)

        # Other setup
        if select_multiple:
            self.list_widget.setSelectionMode(Qt.QAbstractItemView.MultiSelection)

    def addItem(self, item_name):
        self.list_widget.addItem(item_name)

    @property
    def items(self):
        list_items = self.list_widget.selectedItems()
        item_names = [str(x.text()) for x in list_items]
        return item_names

    @items.setter
    def items(self, items):
        for item in items:
            self.addItem(item)
        

    def __enter__(self):
        self.exec_()
        return self

    def __exit__(self, typ, val, tb):
        self.close()
        

class AppLaunch(object):

    def __init__(self, argv):
        self.argv = argv
        self.app = None

    def __enter__(self):

        try:
            app = Qt.QApplication(self.argv)
            app.setStyle('cleanlooks')
            self.app = app
        except RuntimeError:
            print('QApp Exists, continuing...')
            self.app = None

        return None
        

    def __exit__(self, typ, value, tb):

        if self.app is not None:
            self.app.exec_()
        

## Main/Testing

if __name__ == "__main__":

    fmt.section('Main')

    import sys
    
    with AppLaunch(sys.argv):

        with ListSelectionDialog(items=['A','B','C','D'],
                                 select_multiple=True) as win:

            items = win.items
            print('Items Selected: %s' % ','.join(items))

    fmt.section('End')
        
