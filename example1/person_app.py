
import enaml
from enaml.qt.qt_application import QtApplication
from person import Person

if __name__ == '__main__':
    with enaml.imports():
        from person_view import PersonView

    john = Person(first_name='John', last_name='Doe', age=42)
    john.debug = True

    app = QtApplication()
    view = PersonView(person=john)
    view.show()

    app.start()
