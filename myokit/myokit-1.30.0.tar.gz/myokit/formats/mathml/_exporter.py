#
# Exports to MathML based formats.
#
# This file is part of Myokit.
# See http://myokit.org for copyright, sharing, and licensing details.
#
from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals

import os

from lxml import etree

import myokit
from ._ewriter import MathMLExpressionWriter


class XMLExporter(myokit.formats.Exporter):
    """
    This :class:`Exporter <myokit.formats.Exporter>` generates an XML file
    containing a model's equations, encoded in Content MathML. This is an XML
    format containing the bare equations, without any formatting. It can be
    used to exchange equations with MathML supporting applications.
    """
    def info(self):
        import inspect
        return inspect.getdoc(self)

    def model(self, path, model, protocol=None):
        """
        Export the model to an xml document.
        """
        path = os.path.abspath(os.path.expanduser(path))

        # Create model xml element
        root = etree.Element('math')
        root.attrib['xmlns'] = 'http://www.w3.org/1998/Math/MathML'

        # Create expression writer
        writer = MathMLExpressionWriter()
        writer.set_mode(presentation=False)
        writer.set_time_variable(model.time())

        # Write equations
        for var in model.variables(deep=True):
            writer.eq(var.eq(), root)

        # Write xml to file
        doc = etree.ElementTree(root)
        doc.write(path, encoding='utf-8', method='xml')

        # Pretty output
        if True:
            import xml.dom.minidom as m
            xml = m.parse(path)
            with open(path, 'wb') as f:
                f.write(xml.toprettyxml(encoding='utf-8'))

    def supports_model(self):
        """
        Returns ``True``.
        """
        return True


class HTMLExporter(myokit.formats.Exporter):
    """
    This :class:`Exporter <myokit.formats.Exporter>` generates a HTML file
    displaying a model's equations. The equations are encoded using
    Presentation MathML. This format can be viewed in most modern browsers, but
    is less suitable as an exchange format.
    """
    def info(self):
        import inspect
        return inspect.getdoc(self)

    def model(self, path, model, protocol=None):
        """
        Export to a html document.
        """
        # Get model name
        try:
            name = model.meta['name']
        except KeyError:
            name = 'Generated model'

        # Create model html element
        html = etree.Element('html')
        head = etree.SubElement(html, 'head')
        title = etree.SubElement(head, 'title')
        title.text = name
        body = etree.SubElement(html, 'body')
        heading = etree.SubElement(body, 'h1')
        heading.text = name

        # Create expression writer
        writer = MathMLExpressionWriter()
        writer.set_mode(presentation=True)
        writer.set_time_variable(model.time())

        # Write equations, per component
        for component in model.components():
            div = etree.SubElement(body, 'div')
            div.attrib['class'] = 'component'
            heading = etree.SubElement(div, 'h2')
            heading.text = component.qname()
            for var in component.variables(deep=True):
                div2 = etree.SubElement(div, 'div')
                div2.attrib['class'] = 'variable'
                math = etree.SubElement(div2, 'math')
                math.attrib['xmlns'] = 'http://www.w3.org/1998/Math/MathML'
                writer.eq(var.eq(), math)

        # Write xml to file
        doc = etree.ElementTree(html)
        doc.write(path, encoding='utf-8', method='xml')

        # Pretty output
        if True:
            import xml.dom.minidom as m
            xml = m.parse(path)
            with open(path, 'wb') as f:
                f.write(xml.toprettyxml(encoding='utf-8'))

    def supports_model(self):
        """
        Returns ``True``.
        """
        return True
