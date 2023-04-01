import lexicon.lexicon_ru as lexicon

DB_NAME: str = 'shifts.db'
DB_PATH: str = 'db'


DELETE_DB: bool = True

message: dict[str, str] = {
    'start': lexicon.START_MESSAGE,
    'help': lexicon.HELP_MESSAGE,
    'name_err': lexicon.NAME_CHECK_ERROR_MESSAGE,
    'surname_err': lexicon.SURNAME_CHECK_ERROR_MESSAGE
}
