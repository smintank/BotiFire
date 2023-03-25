import defaults as df

DB_NAME: str = 'shifts.db'
DB_PATH: str = 'db'


DELETE_DB: bool = True

message: dict[str, str] = {
    'start': df.START_MESSAGE,
    'help': df.HELP_MESSAGE,
    'name_err': df.NAME_CHECK_ERROR_MESSAGE,
    'surname_err': df.SURNAME_CHECK_ERROR_MESSAGE
}
