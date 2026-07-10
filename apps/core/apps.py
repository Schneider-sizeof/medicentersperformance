from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.core'
    verbose_name = 'Core & Pages'

    def ready(self):
        import sys
        if sys.version_info >= (3, 14):
            try:
                from django.template import Context, BaseContext
                
                def new_base_context_copy(self):
                    dup = self.__class__()
                    dup.dicts = [d.copy() for d in self.dicts]
                    return dup

                def new_context_copy(self):
                    dup = self.__class__()
                    dup.dicts = self.dicts[:]
                    return dup

                BaseContext.__copy__ = new_base_context_copy
                Context.__copy__ = new_context_copy
            except ImportError:
                pass

