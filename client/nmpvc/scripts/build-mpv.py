
import types

from kwking_helper.logging import CL


Code = """

class MPV:
    def __init__(self):
        ...

    def _run_method(self, name: str, *args, **kwargs):
        ...

    def _set_prop(self, prop: str, value):
        ...

    def _get_prop(self, prop: str):
        ...

"""

TemplateProperty = """

    @property
    def {name}(self):
        return self._get_prop({name})

    @{name}.setter
    def {name}(self, value):
        self._set_prop('{name}', value)

"""



class BuildMPV:
    def __init__(self, out: str):
        self.out = out

        self.logger = CL(
            'debug', __name__, _format="[{level}] {message}"
        )

        self.code = Code

    def run(self):
        import mpv

        player = mpv.MPV()

        for name in dir(player):
            try:
                attr = getattr(player, name)
            except RuntimeError as ex:
                self.logger.error(f"{ex.args[2][1].decode()}: {ex.args[0]}")
                continue

            if name[0] == '-':
                continue

            if isinstance(attr, types.MethodType):
                # @todo: generate method
                ...

            else:
                self.code += TemplateProperty.format(name=name)

    def save(self):
        # @todo: write to file
        with open(self.out, 'w') as file:
            file.write(self.code)


if __name__ == "__main__":
    build = BuildMPV('nmpvc.py')
    build.run()
    build.save()
