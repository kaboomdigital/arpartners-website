from django.db import models
from django.utils import timezone
from datetime import date


def generate_thumbnail_name(self, filename):
    url = "images/{}/{}".format(self.url, filename)
    return url


# Create your models here.
class Project(models.Model):
    """ a model for the general project fields """
    PROJECT_STATUS_CHOICES = (
        ('status-gerealiseerd', 'status-gerealiseerd'),
        ('status-in-verkoop-verhuur', 'status-in-verkoop-verhuur'),
        ('status-in-ontwikkeling', 'status-in-ontwikkeling')
    )

    name = models.CharField(max_length=200)
    url = models.SlugField(max_length=100)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to=generate_thumbnail_name)
    published = models.BooleanField(default=False)
    created_date = models.DateField(default=date.today)
    order_id = models.PositiveSmallIntegerField(verbose_name='Order ID', default=1)
    project_status = models.CharField(max_length=30, choices=PROJECT_STATUS_CHOICES, default='in ontwikkeling')

    street_name = models.CharField(max_length=200, blank=True)
    house_number = models.CharField(max_length=200, blank=True)
    zipcode = models.CharField(max_length=7, blank=True)
    city = models.CharField(max_length=50, blank=True)
    district = models.CharField(max_length=50, default='', blank=True)
    neighborhood = models.CharField(max_length=200, blank=True)
    residential_houses = models.IntegerField(blank=True, null=True)
    non_residential = models.IntegerField(blank=True, null=True)
    parking_spots = models.IntegerField(blank=True, null=True)
    total_floor_area = models.IntegerField(blank=True, null=True)
    real_estate_broker = models.CharField(max_length=250, blank=True)

    def get_next(self):
        """
        Get the next object by primary key order
        """
        next = self.__class__.objects.filter(pk__gt=self.pk)
        try:
            return next[0]
        except IndexError:
            return False

    def get_prev(self):
        """
        Get the previous object by primary key order
        """
        prev = self.__class__.objects.filter(pk__lt=self.pk).order_by('-pk')
        try:
            return prev[0]
        except IndexError:
            return False

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projecten'
        ordering = ('name', )

    def __str__(self):
        return self.name


class ProjectDetail(models.Model):
    """ a model for the appartment table project fields """
    project = models.ForeignKey(Project)
    table_row_number = models.PositiveSmallIntegerField(verbose_name='Table row number', default='1')
    table_row_label = models.CharField(max_length=100, verbose_name='Row Label', blank=True, null=True)
    table_row_floor = models.CharField(max_length=50, verbose_name='Floor', blank=True, null=True)
    table_row_area = models.PositiveSmallIntegerField(verbose_name='Area in m2', blank=True, null=True)

    class Meta:
        verbose_name = 'Project Details'
        verbose_name_plural = 'Projecten Details'
        ordering = ('project', 'table_row_number', )

    def __str__(self):
        return '{}'.format('Project Details table row')


def generate_filename(self, filename):
    """ Generate a filename for the project images upload field"""
    url = "images/{}/{}".format(self.project.url, filename)
    return url


class ProjectImages(models.Model):
    project = models.ForeignKey(Project)
    order_id = models.PositiveSmallIntegerField(verbose_name='Order ID', default=1)
    image = models.ImageField(upload_to=generate_filename)
    image_description = models.CharField(max_length=500, blank=True)

    class Meta:
        verbose_name = 'Project Images'
        verbose_name_plural = 'Projecten Images'

    def __str__(self):
        return '{}, {}, {}'.format(self.project, 'Order ID: ' + str(self.order_id), self.image)


class Partner(models.Model):
    partner = models.CharField(max_length=200)
    link = models.URLField(max_length=250)

    class Meta:
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'

    def __str__(self):
        return self.partner


class Contact(models.Model):
    company_name = models.CharField(max_length=250)
    street_name = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=6)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    class Meta:
        verbose_name = 'Contact Details'
        verbose_name_plural = 'Contact Details'

    def __str__(self):
        return self.company_name


class Directie(models.Model):
    name = models.CharField(max_length=100)
    function = models.CharField(max_length=50)
    description = models.TextField()
    linkedin = models.URLField(max_length=250)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    class Meta:
        verbose_name = 'Directie Member'
        verbose_name_plural = 'Directie Members'

    def __str__(self):
        return self.name


class SiteContent(models.Model):
    home_header = models.CharField(max_length=200)
    home_copy = models.CharField(max_length=200)
    home_organisatie = models.TextField()
    home_directie = models.TextField()
    home_projecten = models.TextField()
    home_investeren = models.TextField()
    organisatie_header = models.CharField(max_length=200)
    organisatie_header_text = models.TextField()
    organisatie_content_text = models.TextField()
    directie_header = models.CharField(max_length=200)
    directie_header_text = models.TextField()
    projecten_header = models.CharField(max_length=200)
    projecten_header_text = models.TextField()
    investeren_header = models.CharField(max_length=200)
    investeren_header_text = models.TextField()
    investeren_content_text = models.TextField()
    investeren_content_text_afm = models.TextField()
    partners_header = models.CharField(max_length=200)
    partners_header_text = models.TextField()
    contact_header = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Page Content'
        verbose_name_plural = 'Page Content'

    def __str__(self):
        return 'AR Partners Page Content'
