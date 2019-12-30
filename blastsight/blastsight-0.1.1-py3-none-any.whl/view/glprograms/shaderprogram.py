#!/usr/bin/env python

#  Copyright (c) 2019 Gabriel Sanhueza.
#
#  Distributed under the MIT License.
#  See LICENSE for more info.

import pathlib

from qtpy.QtGui import QOpenGLShader
from qtpy.QtGui import QOpenGLShaderProgram


class ShaderProgram:
    def __init__(self, widget):
        self.base_name = None
        self.widget = widget
        self.shader_program = None
        self.shader_dir = f'{pathlib.Path(__file__).parent.parent}/drawables/shaders'
        self.uniform_locs = {}
        self.drawables = []
        self.transparents = []

    def setup(self) -> None:
        if self.shader_program:
            return

        self.shader_program = QOpenGLShaderProgram(self.widget.context())
        self.setup_shaders()

        self.add_uniform_loc('model_view_matrix')
        self.add_uniform_loc('proj_matrix')

    def setup_shaders(self) -> None:
        # Placeholders to avoid early garbage collection
        vs = self.enable_vertex_shader()
        fs = self.enable_fragment_shader()

        self.shader_program.link()

    def _enable_shader(self, shader_type, filename: str):
        shader = QOpenGLShader(shader_type)
        shader.compileSourceFile(f'{self.shader_dir}/{self.base_name}/{filename}')
        self.shader_program.addShader(shader)
        return shader

    def enable_vertex_shader(self, filename='vertex.glsl'):
        return self._enable_shader(QOpenGLShader.Vertex, filename)

    def enable_fragment_shader(self, filename='fragment.glsl'):
        return self._enable_shader(QOpenGLShader.Fragment, filename)

    def enable_geometry_shader(self, filename='geometry.glsl'):
        return self._enable_shader(QOpenGLShader.Geometry, filename)

    def add_uniform_loc(self, loc_str) -> None:
        self.uniform_locs[loc_str] = self.shader_program.uniformLocation(loc_str)

    def update_uniform(self, loc_str, *values) -> None:
        self.shader_program.setUniformValue(self.uniform_locs[loc_str], *values)

    def set_drawables(self, drawables):
        self.drawables = [d for d in drawables if d.alpha >= 0.99]
        self.transparents = [d for d in drawables if d.alpha < 0.99]

        for drawable in self.drawables:
            drawable.initialize()

        for drawable in self.transparents:
            drawable.initialize()

    def bind(self) -> None:
        self.shader_program.bind()

    def recreate(self) -> None:
        pass

    def inner_draw(self, drawables):
        for drawable in drawables:
            drawable.draw()

    def draw(self):
        self.inner_draw(self.drawables)

    def redraw(self):
        self.inner_draw(self.transparents)
