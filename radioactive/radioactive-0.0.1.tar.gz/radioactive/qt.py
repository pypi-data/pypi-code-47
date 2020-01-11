def register_lineedit(editor, model, key):
    def update_model(t):
        model[key] = t
    editor.textChanged.connect(update_model)
    register_property(editor, 'text', model, key)

def register_property(widget, prop, model, key, adapter=str):
    def update(model, key, value):
        widget.setProperty(prop, adapter(value))
    model.subscribe(key, update)
    update(model, key, model[key])


def demo():
    from PyQt5 import Qt
    from radioactive.model import Dict

    data = dict(name='Hello!', version='1.2.3')
    state = Dict(data)
    state['title'] = f'{state["name"]} - {state["version"]}'
    def title(model, key, value):
        model['title'] = f'{model["name"]} - {model["version"]}'
    state.subscribe('name', title)
    state.subscribe('version', title)

    app = Qt.QApplication([])
    w = Qt.QWidget()
    layout = Qt.QGridLayout(w)

    labelName = Qt.QLabel()
    editorName = Qt.QLineEdit()
    layout.addWidget(Qt.QLabel('Name:'), 0, 0)
    layout.addWidget(editorName, 0, 1)
    layout.addWidget(labelName, 0, 2)
    register_property(labelName, 'text', state, 'name')
    register_lineedit(editorName, state, 'name')

    for i in range(1, 3):
        labelVersion = Qt.QLabel()
        editorVersion = Qt.QLineEdit()
        layout.addWidget(Qt.QLabel('Version:'), i, 0)
        layout.addWidget(editorVersion, i, 1)
        layout.addWidget(labelVersion, i, 2)
        register_property(labelVersion, 'text', state, 'version')
        register_lineedit(editorVersion, state, 'version')

    def reset():
        state.update(data)

    btn = Qt.QPushButton('Reset')
    btn.clicked.connect(reset)
    layout.addWidget(btn, 3, 0, 1, 3)
    register_property(w, 'windowTitle', state, 'title')

    w.show()
    app.exec_()


if __name__ == '__main__':
    demo()
