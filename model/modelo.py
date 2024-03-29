from peewee import *

DATABASE_NAME = "dbpasetto"
USER = "user"
PASSWORD = "pswd123"
PORT = 3306

SIGLAESTADOS = "'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'"

db = MySQLDatabase(
    DATABASE_NAME, user=USER, password=PASSWORD, host="localhost", port=PORT
)


class BaseModel(Model):
    class Meta:
        database = db


class Cidade(BaseModel):
    idCidade = AutoField()
    nome = CharField(max_length=50, null=False)
    uf = CharField(
        max_length=2, null=False, constraints=[Check(f"UF in ({SIGLAESTADOS})")]
    )


class Marca(BaseModel):
    idMarca = AutoField()
    nome = CharField(max_length=50, null=False)


class Veiculo(BaseModel):
    idVeiculo = AutoField()
    modelo = CharField(max_length=30, null=False)
    ano = CharField(max_length=4, constraints=[Check("ano > 1900")], null=True)
    placa = CharField(
        max_length=7,
        unique=True,
        constraints=[Check("CHAR_LENGTH(placa)=7")],
        null=False,
    )
    marca = ForeignKeyField(Marca, backref="marcas", null=False)


class Cliente(BaseModel):
    idCliente = AutoField()
    nome = CharField(max_length=80, null=False)
    tipo = CharField(
        max_length=1, null=False, constraints=[Check("tipo in ('0','1','2')")]
    )
    documento = CharField(max_length=14, null=True, unique=True)
    cep = CharField(max_length=8, null=True, constraints=[Check("CHAR_LENGTH(cep)=8")])
    endereco = CharField(max_length=80, null=True)
    numero = CharField(max_length=6, null=True, constraints=[Check("numero>=0")])
    bairro = CharField(max_length=50, null=True)
    cidade = ForeignKeyField(Cidade, backref="cidades", null=True)

    class Meta:
        constraints = [
            Check(
                "CHAR_LENGTH(documento)=11 and tipo='0' or CHAR_LENGTH(documento)=14 and tipo='1' or tipo='2'"
            )
        ]


class Veiculo_Cliente(BaseModel):
    veiculo = ForeignKeyField(
        Veiculo, backref="veiculos", null=False, on_delete="CASCADE"
    )
    cliente = ForeignKeyField(
        Cliente, backref="clientes", null=False, on_delete="CASCADE"
    )

    class Meta:
        primary_key = CompositeKey("veiculo", "cliente")


class Peca(BaseModel):
    idPeca = AutoField()
    descricao = CharField(max_length=80, null=False)
    un = CharField(max_length=5, null=False)
    valor = DoubleField(constraints=[Check("valor>=0")], null=False)


class Servico(BaseModel):
    idServico = AutoField()
    descricao = CharField(max_length=80, null=False)
    valor = DoubleField(constraints=[Check("valor>=0")], null=False)


class Orcamento(BaseModel):
    idOrcamento = AutoField()
    dataOrcamento = DateField(constraints=[SQL("DEFAULT (CURRENT_DATE)")], null=False)
    cliente = ForeignKeyField(Cliente, backref="clientes", null=False)
    veiculo = ForeignKeyField(Veiculo, backref="veiculos", null=False)
    km = CharField(max_length=6, constraints=[Check("km>0")], null=False)
    valorTotal = DoubleField(constraints=[Check("valorTotal>=0")], null=False)
    dataAprovacao = DateField(null=True)
    status = CharField(
        max_length=1,
        constraints=[SQL("DEFAULT '0'"), Check("status in ('0','1','2','3')")],
        null=False,
    )
    observacoes = CharField(max_length=200, null=True)


"""status:
0 = Aguardando aprovação
1 = Reprovado
2 = Aprovado
3 = Finalizado
"""


class ItemPeca(BaseModel):
    peca = ForeignKeyField(Peca, backref="pecas")
    orcamento = ForeignKeyField(Orcamento, backref="orcamentos", on_delete="CASCADE")
    qtde = FloatField(null=False)
    valor = DoubleField(constraints=[Check("valor>=0")], null=False)

    class Meta:
        primary_key = CompositeKey("peca", "orcamento")


class ItemServico(BaseModel):
    servico = ForeignKeyField(Servico, backref="servicos", null=False)
    orcamento = ForeignKeyField(
        Orcamento, backref="orcamentos", null=False, on_delete="CASCADE"
    )
    qtde = IntegerField(null=False)
    valor = DoubleField(constraints=[Check("valor>=0")], null=False)

    class Meta:
        primary_key = CompositeKey("servico", "orcamento")


class Fone(BaseModel):
    cliente = ForeignKeyField(
        Cliente, backref="clientes", null=False, on_delete="CASCADE"
    )
    fone = CharField(
        max_length=14,
        null=False,
        unique=True,
        constraints=[Check("CHAR_LENGTH(fone)>=8")],
    )

    class Meta:
        primary_key = CompositeKey("cliente", "fone")


def create_tables(cursor):
    models = BaseModel.__subclasses__()
    db.create_tables(models)
    cursor.execute(
        """CREATE TRIGGER `tr_set_data_aprovacao`
BEFORE UPDATE ON `orcamento`
FOR EACH ROW
begin
    if new.status='2' and old.status='0' then
        set new.dataAprovacao=curdate();
    end if;
end"""
    )
