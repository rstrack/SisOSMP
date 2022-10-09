from PyQt6 import QtCore, QtWidgets

class InfiniteScrollTableModel(QtCore.QAbstractTableModel):
    numberPopulated = QtCore.pyqtSignal(int, int)
    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.numRows= len(data)   
        self.numColumns=len(data[0]) if self.numRows>0 else 0
        self._data=data
        self.horizontalHeaders = [''] * len(self._data)
        self.headerAlignment = [QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter] * len(self._data)

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
        elif orientation == QtCore.Qt.Orientation.Horizontal and role == QtCore.Qt.ItemDataRole.TextAlignmentRole:
            try:
                return self.headerAlignment[section]
            except:
                return False
        return super().setHeaderData(section, orientation, value, role)

    def setHeaderAlignment(self, section, alignment):
        try:
            self.headerAlignment[section] = alignment
            return True
        except:
            return False

    def setHorizontalHeaderLabels(self, list):
        try:
            self.horizontalHeaders = [''] * len(list)
            self.headerAlignment = [QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter] * len(list)
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
        elif role == QtCore.Qt.ItemDataRole.TextAlignmentRole and orientation == QtCore.Qt.Orientation.Horizontal:
            return self.headerAlignment[section]
        return super().headerData(section, orientation, role)

    def rowCount(self, parent):
        """
        parent=QModelIndex
        """
        return self.numRows 
    
    def columnCount(self, parent):
        """
        parent=QModelIndex
        """
        return self.numColumns  
    
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
    
    def fetchMore(self, index):
        """
        Index=QModelIndex
        """
        maxFetch=20 # max de linhas renderizadas por vez
        
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

class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, align: QtCore.Qt.AlignmentFlag) -> None:
        super().__init__()
        self.alignmentFlag = align

    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = self.alignmentFlag
