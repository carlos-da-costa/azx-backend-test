# declare all models/tables as instances of Model
# the Model will also provied schema to validate http requests
# and format query results 

from dal import Model, Column, ColumnType

task = Model(
    'task', 
    [
        Column('title', ColumnType.string, required=True),
        Column('description', ColumnType.string, required=True),
        Column('due_date', ColumnType.date),
        Column('done', ColumnType.boolean),
    ]
)
