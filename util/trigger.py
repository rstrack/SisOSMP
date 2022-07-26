class Trigger(object):

    def __init__(self, table, name, when, trigger_op, cond, logic, safe=True):
        self.create = 'create trigger' + (' if not exists' if safe else '')
        self.tablename = table
        self.name = name
        self.when = when
        self.trigger_op = trigger_op
        self.cond = cond
        self.logic = logic

    def create_trigger(self, cursor):
        cursor.execute(f"""
        {self.create} {self.name} {self.when} {self.trigger_op}
        on {self.tablename}
        for each row
        begin
            if {self.cond} then
                set {self.logic};
            end if;
        end""")