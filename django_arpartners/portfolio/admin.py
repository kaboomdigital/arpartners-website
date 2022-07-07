from django.contrib import admin
from .models import Partner, Project, Contact, Directie,SiteContent, ProjectDetail, ProjectImages


class ProjectDetailInline(admin.TabularInline):
    model = ProjectDetail
    extra = 0
    ordering = ('-project', 'table_row_number', )


class ProjectImagesInline(admin.TabularInline):
    model = ProjectImages
    extra = 0
    ordering = ('-project', 'order_id',)


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectDetailInline, ProjectImagesInline]
    search_fields = ['name', ]
    list_display = ('name', 'project_status', 'url', 'created_date', 'order_id', 'published', )
    list_editable = ('project_status', 'order_id', 'published', )
    list_filter = ('project_status', 'city', 'created_date', 'published')
    ordering = ('name', )
    fieldsets = (
        ('Project info', {
            'fields':
                 (('name', 'url'), 'description', 'thumbnail', ('project_status', 'order_id', 'created_date'), 'published', ),
            'description':
                ('The "Url" can consist of lower case characters only. Also, only characters, dashes and underscores are allowed.'),
            }),
        ('Address', {
            'fields':
                (('street_name', 'house_number'), ('zipcode', 'city'), ('district', 'neighborhood'))
            }),
        ('Object details', {
            'fields':
                (('residential_houses', 'non_residential', 'parking_spots'), 'total_floor_area', 'real_estate_broker', )
            }),
    )


class ProjectDetailAdmin(admin.ModelAdmin):
    search_fields = ['project__name', ]
    save_as = True
    ordering = ('-project', 'table_row_number', )
    list_display = ('project', 'table_row_number', 'table_row_label', 'table_row_floor', 'table_row_area', )
    list_editable = ('table_row_number', 'table_row_label', 'table_row_floor', 'table_row_area', )
    list_filter = ('project', )
    fieldsets = (
        ('Select project', {
            'fields':
                ('project',),
            'description':
                ('Select the project you want to add a data-table to'),
        }),
        ('Appartement/floor details', {
            'fields':
                 ('table_row_number', ('table_row_label', 'table_row_floor', 'table_row_area'), ),
            'description':
                ('Tip: first add the number of needed rows with only the "Table row number" filled in. Then in the overview page modify the label, floor and area all in the same page. Use "Save as new" button to quickly create new entries with same project name already selected'),
            }),
    )


class ProjectImagesAdmin(admin.ModelAdmin):
    search_fields = ['project__name', ]
    ordering = ('-project', 'order_id',)
    list_display = ('project', 'order_id', 'image', )
    list_editable = ('order_id', 'image', )
    list_filter = ('project', )
    fieldsets = (
        ('Select project', {
            'fields':
                 ('project', ),
            'description':
                ('Select the project you want to add an image to'),
            }),
        ('Project image', {
            'fields':
                ('image', 'order_id'),
            'description':
                (
                'Please select a valid image type. The Order ID determines in which order the images are displayed on the website'),
            }),
        ('Description', {
            'fields':
                ('image_description', ),
            'description':
                ('Optionally add a description for this image.'),
        }),
    )


class PartnerAdmin(admin.ModelAdmin):
    list_display = ('partner', 'link', )
    list_editable = ('link', )
    ordering = ('partner', )
    fieldsets = (
        ('Add a new partner', {
            'fields':
                 ('partner', 'link', ),
            }),
    )


class SiteContentAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Home', {
            'fields':
                 ('home_header', 'home_copy', 'home_organisatie', 'home_directie', 'home_projecten', 'home_investeren'),
            }),
        ('Organisatie', {
            'fields':
                ('organisatie_header', 'organisatie_header_text', 'organisatie_content_text'),
            }),
        ('Directie', {
            'fields':
                ('directie_header', 'directie_header_text'),
            }),
        ('Projecten', {
            'fields':
                ('projecten_header', 'projecten_header_text', ),
            }),
        ('Investeren', {
            'fields':
                ('investeren_header', 'investeren_header_text', 'investeren_content_text', 'investeren_content_text_afm'),
            }),
        ('Partners', {
            'fields':
                ('partners_header', 'partners_header_text'),
            }),
        ('Contact', {
            'fields':
                ('contact_header', ),
            }),
    )


# Register your models here.
admin.site.register(Project, ProjectAdmin)
# admin.site.register(ProjectDetail, ProjectDetailAdmin)
# admin.site.register(ProjectImages, ProjectImagesAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Contact)
admin.site.register(Directie)
admin.site.register(SiteContent, SiteContentAdmin)

admin.site.site_header = 'ARPartners.nl administration'
