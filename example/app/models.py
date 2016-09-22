# -*- coding: utf-8 -*-
# Copyright (c) 2013 by Pablo Martín <goinnn@gmail.com>
#
# This software is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this software.  If not, see <http://www.gnu.org/licenses/>.

from django.db import models
from django.utils.translation import gettext as _

from multiselectfield import MultiSelectField

CATEGORY_CHOICES = (
    (1, 'Handbooks and manuals by discipline'),
    (2, 'Business books'),
    (3, 'Books of literary criticism'),
    (4, 'Books about literary theory'),
    (5, 'Books about literature')
)

TAGS_CHOICES = (
    ('sex',         _('Sex')),
    ('work',        _('Work')),
    ('happy',       _('Happy')),
    ('food',        _('Food')),
    ('field',       _('Field')),
    ('boring',      _('Boring')),
    ('interesting', _('Interesting')),
    ('huge',        _('Huge')),
    ('nice',        _('Nice')),
)

PROVINCES = (
    ('AB', _("Alberta")),
    ('BC', _("British Columbia")),
)

STATES = (
    ('AK', _("Alaska")),
    ('AL', _("Alabama")),
    ('AZ', _("Arizona")),
)

PROVINCES_AND_STATES = (
    (_("Canada - Provinces"), PROVINCES),
    (_("USA - States"),       STATES),
)


class Book(models.Model):
    title = models.CharField(max_length=200)
    categories = MultiSelectField(choices=CATEGORY_CHOICES,
                                  max_choices=3,
                                  #default='1,5')
                                  default=1)
    tags = MultiSelectField(choices=TAGS_CHOICES,
                            null=True, blank=True)
    published_in = MultiSelectField(_("Province or State"), max_length=2, choices=PROVINCES_AND_STATES)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.__str__()
