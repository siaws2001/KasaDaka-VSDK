from django.db import models

from .vs_element import VoiceServiceElement, VoiceServiceSubElement

class ListCallSessions(VoiceServiceElement):
    _urls_name = 'service-development:list_call_sessions'

    @property
    def redirect(self):
        """
        Returns the actual subclassed object that is redirected to,
        instead of the VoiceServiceElement superclass object (which does
        not have specific fields and methods).
        """
        if self._redirect:
            return VoiceServiceElement.objects.get_subclass(id=self._redirect.id)
        else:
            return None

    def __str__(self):
        return "List callsessions: " + self.name

    def is_valid(self):
        return len(self.validator()) == 0

    is_valid.boolean = True

    def validator(self):
        errors = []
        errors.extend(super(ListCallSessions, self).validator())
        if not self._redirect:
            errors.append('Record %s does not have a redirect element' % self.name)
        return errors