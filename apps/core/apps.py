from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.core'
    verbose_name = 'Core & Pages'

    def ready(self):
        import sys
        if sys.version_info >= (3, 14):
            self._patch_template_context()

    @staticmethod
    def _patch_template_context():
        """
        Monkey-patch Django 5.1's BaseContext.__copy__ for Python 3.14+.

        Django's original does `copy(super())` which fails because Python 3.14
        changed super() proxy objects to disallow __dict__ assignment.
        We replace it with a version that manually constructs the copy.
        """
        try:
            from django.template.context import BaseContext, Context, RenderContext

            def _base_context_copy(self):
                duplicate = self.__class__.__new__(self.__class__)
                duplicate.dicts = self.dicts[:]
                return duplicate

            def _context_copy(self):
                duplicate = self.__class__.__new__(self.__class__)
                duplicate.dicts = self.dicts[:]
                # Copy Context-specific attributes
                for attr in (
                    'autoescape', 'use_l10n', 'use_tz',
                    'template_name', 'render_context',
                    '_current_app', 'template',
                ):
                    if hasattr(self, attr):
                        try:
                            setattr(duplicate, attr, getattr(self, attr))
                        except AttributeError:
                            pass
                return duplicate

            BaseContext.__copy__ = _base_context_copy
            Context.__copy__ = _context_copy
        except ImportError:
            pass
