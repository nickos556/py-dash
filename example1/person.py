from atom.api import Atom, Str, Value, Int, Unicode, observe, Bool


class Person(Atom):
    first_name = Unicode()
    last_name = Unicode()
    age = Int(0)
    debug = Bool(False)

    @observe('age')
    def debug_print(self, change):
        """
        Prints out a debug message whenever the person's age changes.

        """
        if self.debug:
            templ = "{first} {last} is {age} years old."
            s = templ.format(
                first=self.first_name, last=self.last_name, age=self.age,
            )
            print s
