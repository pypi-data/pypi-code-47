"""A simple cli-based profiler for Python"""

__version__ = '0.2'

from .main import profile, profile_recursive, Profiler

__all__ = ['profile', 'profile_recursive', 'Profiler']
