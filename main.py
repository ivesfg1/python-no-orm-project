from database.migrations import create_tables
from database.orm import Note

create_tables()

Note.clear()

print(Note.all())

Note.insert("Teste1")
Note.insert("Teste2")

print(Note.all())

print(Note.get("title", "Teste1"))

Note.delete("title", "Teste1")
print(Note.all())
