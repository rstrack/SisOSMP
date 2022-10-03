# Fetch More Example - Lazy Table Edition
# Ported to PyQt4 by Darryl Wallace, 2009 - wallacdj at gmail.com

from controller.orcamentoController import OrcamentoController
from controller.clienteController import ClienteController
import sys
from PyQt6 import QtGui, QtCore, QtWidgets

class InfiniteScrollTableModel(QtCore.QAbstractTableModel):
    numberPopulated = QtCore.pyqtSignal(int, int)
    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.numRows= len(data)   
        self.numColumns=len(data[0]) if self.numRows>0 else 0
        self._data=data
        self.horizontalHeaders = [''] * len(self._data)
    #__init__

    def setRowCount(self, rows: int) -> None:
        self.beginResetModel()
        self.numRows = rows
        self.endResetModel()
        self.dataChanged.emit(QtCore.QModelIndex(),QtCore.QModelIndex())

    def setColumnCount(self, columns: int) -> None:
        self.beginResetModel()
        self.numColumns = columns
        self.endResetModel()
        self.dataChanged.emit(QtCore.QModelIndex(),QtCore.QModelIndex())

    def removerColunas(self, colunas: list):
        self.beginResetModel()
        for linha in self._data:
            for coluna in colunas:
                if coluna in linha:
                    del linha[coluna]
        self.endResetModel()

    def colunasDesejadas(self, colunas:list):
        self.beginResetModel()
        for dict in self._data:
            self._data[self._data.index(dict)] = {key: (dict[key] if key in dict else None) for key in colunas}
        self.endResetModel()

    def setHeaderData(self, section: int, orientation: QtCore.Qt.Orientation, value, role: int = ...) -> bool:
        if orientation == QtCore.Qt.Orientation.Horizontal and role in (QtCore.Qt.ItemDataRole.DisplayRole, QtCore.Qt.ItemDataRole.EditRole):
            try:
                self.horizontalHeaders[section] = value
                return True
            except:
                return False
        return super().setHeaderData(section, orientation, value, role)

    def setHorizontalHeaderLabels(self, list):
        try:
            self.horizontalHeaders = [''] * len(list)
            for i in range(len(list)):
                self.horizontalHeaders[i] = list[i]
            return True
        except:
            return False
    
    def headerData(self, section, orientation, role=QtCore.Qt.ItemDataRole.DisplayRole):
        if orientation == QtCore.Qt.Orientation.Horizontal and role == QtCore.Qt.ItemDataRole.DisplayRole:
            try:
                return self.horizontalHeaders[section]
            except:
                pass
        return super().headerData(section, orientation, role)

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

    def updateData(self, data):
        self.beginResetModel()
        self._data = data
        self.endResetModel()
        self.dataChanged.emit(QtCore.QModelIndex(),QtCore.QModelIndex())

    def addData(self, data):
        self.beginResetModel()
        if len(self._data) == 1:
            self._data = data
        else: self._data.extend(data)
        self.endResetModel()
    
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
#InfiniteScrollTableModel

#classe pra testes
class Window(QtWidgets.QWidget):
    
    def __init__(self, data, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        
        self.model = InfiniteScrollTableModel(data, parent=self)
        
        view=QtWidgets.QTableView()
        view.setModel(self.model)
        
        layout=QtWidgets.QGridLayout()
        layout.addWidget(view, 0, 0, 1, 2)
        
        self.setLayout(layout)
        
        self.resize(400, 600)
    #__init__
    
    def updateLog(self, rows, columns):
        self.logViewer.append("{} rows added. {} columns added".format(rows, columns))
    #updateLog
#Window

if __name__=='__main__':
    qApp=QtWidgets.QApplication(sys.argv)
    rep = ClienteController()
    data = rep.listarClientes()
    data = list(reversed(data))
    fetchMoreWindow=Window(data)
    r = fetchMoreWindow.model.setHorizontalHeaderLabels(['idCliente', 'nome', 'documento'])
    fetchMoreWindow.model.colunasDesejadas(['idCliente', 'nome', 'documento'])
    fetchMoreWindow.show()
    qApp.exec()