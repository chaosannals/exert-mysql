from sly import Lexer, Parser


class CreateTableLexer(Lexer):
    '''
    '''

    K_CREATE = r'CREATE'
    K_TABLE = r'TABLE'
    K_NOT = r'NOT'
    K_NULL = r'NULL'
    K_AUTO_INCREMENT = r'AUTO_INCREMENT'
    K_COLLATE = r'COLLATE'
    K_COMMENT = r'COMMENT'
    K_CURRENT_TIMESTAMP = r'CURRENT_TIMESTAMP'
    K_UNIQUE = r'UNIQUE'
    K_KEY = r'KEY'
    K_DEFAULT = r'DEFAULT'
    K_ENGINE = r'ENGINE'
    K_CHARSET = r'CHARSET'

    ID = r'`.+?`'
    ID2 = r'\w+'
    TEXT = r'\'.*?\''
    LPAREN = r'\('
    RPAREN = r'\)'
    COMMA = r','
    EQUAL = r'='
    NUMBER = r'\d+'

    T_INT = r'int'
    T_VARCHAR = r'varchar'
    T_BINARY = r'binary'
    T_DATETIME = r'datetime'

    ignore = ' \t'
    ignore_newline = r'[\r\n]+'
    tokens = {
        K_CREATE,
        K_TABLE,
        K_NOT,
        K_NULL,
        K_AUTO_INCREMENT,
        K_COLLATE,
        K_COMMENT,
        K_CURRENT_TIMESTAMP,
        K_UNIQUE,
        K_KEY,
        K_DEFAULT,
        K_ENGINE,
        K_CHARSET,

        ID,
        ID2,
        TEXT,
        LPAREN,
        RPAREN,
        COMMA,
        EQUAL,
        NUMBER,

        T_INT,
        T_VARCHAR,
        T_BINARY,
        T_DATETIME,
    }

    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print(f"Illegal character '{t.value[0]}'")
        self.index += 1


class CreateTableParser(Parser):
    '''
    '''

    tokens = CreateTableLexer.tokens

    def __init__(self):
        self.names = {}

    @_('K_CREATE K_TABLE identifier LPAREN fdef')
    def statement(self):
        '''
        '''

    @_('ID')
    def identifier(self, p):
        return p.ID

    @_('ID2')
    def identifier(self, p):
        return p.ID2

    @_('T_INT')
    def ftype(self, p):
        return p.T_INT

    @_('T_INT LPAREN NUMBER RPAREN')
    def ftype(self, p):
        return f'{p.T_INT} ({p.NUMBER})'

    @_('T_VARCHAR LPAREN NUMBER RPAREN')
    def ftype(self, p):
        return f'{p.T_VARCHAR} ({p.NUMBER})'

    @_('identifier ftype ')
    def fdef(self, p):
        return f'{p.identifier} {p.ftype}'
