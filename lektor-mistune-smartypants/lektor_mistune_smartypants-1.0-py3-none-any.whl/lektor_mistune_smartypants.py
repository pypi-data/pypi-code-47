# -*- coding: utf-8 -*-
from lektor.pluginsystem import Plugin
import smartypants
import jinja2

class MistuneSmartypantsPlugin(Plugin):
	name = 'mistune-smartypants'
	description = u'Adds curly quotes to your markdown paragraphs and headings.'

	def on_markdown_config(self, config, **extra):
		"""Adds a mixin to the Mistune parser to add curly quotes"""
		class SmartyPantsMixin(object):
			def paragraph(ren, text):
				return super().paragraph(smartypants.smartypants(text))
			def header(self, text, level, raw=None):
				return super().header(smartypants.smartypants(text), level, raw)
		config.renderer_mixins.append(SmartyPantsMixin)

	def on_setup_env(self, **extra):
		"""Adds the `smartypants` filter to all jinja2 templates"""
		def smartypants_filter(text):
			return jinja2.Markup(smartypants.smartypants(jinja2.escape(text)))
		self.env.jinja_env.filters['smartypants'] = smartypants_filter
