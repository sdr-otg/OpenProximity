#    OpenProximity2.0 is a proximity marketing OpenSource system.
#    Copyright (C) 2009,2008 Naranjo Manuel Francisco <manuel@aircable.net>
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation version 2 of the License.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
from models import *
from django.contrib import admin

class SettingAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')

admin.site.register(Setting, SettingAdmin)

class DongleAdmin(admin.ModelAdmin):
    list_display = ( 'address', 'name', 'enabled' )

class RemoteDongleAdmin(admin.ModelAdmin):
    list_display = ( 'address', 'name', 'local_dongle', 'priority', 'enabled' )

class RemoteDongleInline(admin.TabularInline):
    model = RemoteScannerBluetoothDongle
    fk_name = 'local_dongle'
    fields = ('address', 'name','priority', 'enabled')
    extra = 7
    template = 'op/tabular_remotescanner.html'
        
class ScannerDongleAdmin(admin.ModelAdmin):
    inlines = [ RemoteDongleInline ]
    list_display = ( 'address', 'name', 'priority', 'enabled' )

admin.site.register(ScannerBluetoothDongle, ScannerDongleAdmin)
admin.site.register(RemoteScannerBluetoothDongle, RemoteDongleAdmin)
admin.site.register(UploaderBluetoothDongle, DongleAdmin)

class CampaignFileAdmin(admin.StackedInline):
    model = CampaignFile
    date_hierarchy = None


class MarketingCampaignAdmin(admin.ModelAdmin):
    fieldsets = (
	(None, {
	    'fields': ('name', 'enabled', 'service', 'rejected_count','tries_count'),
	}),
	('Timing Filters', {
	    'classes': ('collapse', ),
	    'fields': ('start', 'end')
	}),
	('Extra Filter Settings', {
	    'classes': ('collapse', ),
	    'fields': ('name_filter', 'addr_filter', 'devclass_filter')
	}),
    )
    
    inlines = [ CampaignFileAdmin, ]
    
    list_display = ( 'name', 
			'service', 
			'start',
			'end', 
			'name_filter', 
			'addr_filter', 
			'devclass_filter',
			'enabled'
		)
    list_filter = ( 'service', 
			'start', 
			'end', 
			'name_filter', 
			'addr_filter',
			'devclass_filter',
			'enabled'
		)
			
    ordering = [ 'name', 'service', 'start', 'end' ]


admin.site.register(MarketingCampaign, MarketingCampaignAdmin)
