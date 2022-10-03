# Fetch More Example - Lazy Table Edition
# Ported to PyQt4 by Darryl Wallace, 2009 - wallacdj at gmail.com

import sys
from PyQt6 import QtGui, QtCore, QtWidgets

class LazyTableModel(QtCore.QAbstractTableModel):
    numberPopulated = QtCore.pyqtSignal(int, int)
    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.numRows=0    
        self.numColumns=0
        self._data=data
    #__init__
    
    def rowCount(self, parent):
        """
        parent=QModelIndex
        """
        return self.numRows
    #rowCount    
    
    def columnCount(self, parent):
        """
        parent=QModelIndex
        """
        return self.numColumns
    #columnCount    
    
    def data(self, index, role=QtCore.Qt.ItemDataRole.DisplayRole):
        """
        index=QModelIndex
        """
        if not index.isValid():
            return QtCore.QVariant()
        
        if index.row()>=self.numRows or index.row()<0 or index.column()>=self.numColumns or index.column()<0:
            return QtCore.QVariant()
        
        if role==QtCore.Qt.ItemDataRole.DisplayRole:
            return QtCore.QVariant(list(self._data[index.row()].values())[index.column()])
        elif role==QtCore.Qt.ItemDataRole.BackgroundRole:
            return QtCore.QVariant(QtWidgets.QApplication.palette().base())
            
        return QtCore.QVariant()
    #data
    
    def canFetchMore(self, index):
        """
        index=QModelIndex
        """
        if self.numRows<len(self._data) or self.numColumns<len(self._data[0].keys()):
            return True
        else:
            return False
    #canFetchMore
    
    def fetchMore(self, index):
        """
        Index=QModelIndex
        """
        maxFetch=10     #maximum number of rows/columns to grab at a time.
        
        remainderRows=len(self._data)-self.numRows
        rowsToFetch=min(maxFetch, remainderRows)
        
        if rowsToFetch>0:
            self.beginInsertRows(QtCore.QModelIndex(), self.numRows, self.numRows+rowsToFetch-1)
            self.endInsertRows()
            self.numRows+=rowsToFetch
        
        remainderColumns=len(self._data[0].keys())-self.numColumns
        columnsToFetch=min(maxFetch, remainderColumns)
        if columnsToFetch>0:
            self.beginInsertColumns(QtCore.QModelIndex(), self.numColumns, self.numColumns+columnsToFetch-1)
            self.endInsertColumns()
            self.numColumns+=columnsToFetch
        
        self.numberPopulated.emit(rowsToFetch, columnsToFetch)
    #fetchMore
#LazyTableModel

class Window(QtWidgets.QWidget):
    
    def __init__(self, data, parent=None):
        """
        Data is any 2-d numpy array
        """
        QtWidgets.QWidget.__init__(self, parent)
        
        self.model = LazyTableModel(data, parent=self)
        
        view=QtWidgets.QTableView()
        view.setModel(self.model)
        
        self.logViewer=QtWidgets.QTextBrowser()
        self.logViewer.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred))
        
        self.model.numberPopulated.connect(self.updateLog)
        
        layout=QtWidgets.QGridLayout()
        layout.addWidget(view, 0, 0, 1, 2)
        layout.addWidget(self.logViewer, 1, 0, 1, 2)
        
        self.setLayout(layout)
        
        self.setWindowTitle("Fetch More Example - Table Edition")
        self.resize(400, 600)
    #__init__
    
    def updateLog(self, rows, columns):
        self.logViewer.append("{} rows added. {} columns added".format(rows, columns))
    #updateLog
#Window

if __name__=='__main__':
    qApp=QtWidgets.QApplication(sys.argv)
    data = []
    for i in range(1000):
        dict = {}
        for i in range(10):
            dict[f'{i}'] = i
        data.append(dict)
    fetchMoreWindow=Window(data)
    fetchMoreWindow.show()
    qApp.exec()