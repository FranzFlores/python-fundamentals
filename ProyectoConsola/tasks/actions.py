import tasks.note as model

class Actions:
    def create(self, user):
        print("Crear una nueva nota")
       
        title = input("Titulo: ")
        description = input("Descripcion: ")
        
        note = model.Note(user[0], title, description)
        save = note.save()

        if save[0] >= 1:
            print("\nNota creada exitosamente")
        else:
            print("\nNo se pudo crear la nota")	 

    def list_notes(self, user):
        print("\nTus notas")
        notes = model.Note(user[0],"","").list_notes()
        print(notes)
        for note in notes:
            print("\n********************************************************")
            print("\nTitulo: {}".format(note[2]))
            print("Descripcion: {}".format(note[3]))
            print("\n********************************************************")
    
    def delete(self, user):
        print("\nEliminar Nota")
        title = input("Titulo: ")
        note = model.Note(user[0], title, "")
        delete = note.delete()
        if delete[0] >= 1:
            print("\nNota eliminada exitosamente")
        else:
            print("\nNo se pudo eliminar la nota")