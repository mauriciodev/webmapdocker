from django.db import models
import uuid
# Create your models here.




class Records(models.Model):
    identifier = models.TextField(primary_key=True)
    typename = models.TextField()
    schema = models.TextField()
    mdsource = models.TextField()
    insert_date = models.TextField()
    xml = models.TextField()
    anytext = models.TextField()
    metadata = models.TextField(blank=True, null=True)
    metadata_type = models.TextField()
    language = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    title_alternate = models.TextField(blank=True, null=True)
    abstract = models.TextField(blank=True, null=True)
    edition = models.TextField(blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)
    keywordstype = models.TextField(blank=True, null=True)
    themes = models.TextField(blank=True, null=True)
    parentidentifier = models.TextField(blank=True, null=True)
    relation = models.TextField(blank=True, null=True)
    time_begin = models.TextField(blank=True, null=True)
    time_end = models.TextField(blank=True, null=True)
    topicategory = models.TextField(blank=True, null=True)
    resourcelanguage = models.TextField(blank=True, null=True)
    creator = models.TextField(blank=True, null=True)
    publisher = models.TextField(blank=True, null=True)
    contributor = models.TextField(blank=True, null=True)
    organization = models.TextField(blank=True, null=True)
    securityconstraints = models.TextField(blank=True, null=True)
    accessconstraints = models.TextField(blank=True, null=True)
    otherconstraints = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    date_revision = models.TextField(blank=True, null=True)
    date_creation = models.TextField(blank=True, null=True)
    date_publication = models.TextField(blank=True, null=True)
    date_modified = models.TextField(blank=True, null=True)
    format = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    crs = models.TextField(blank=True, null=True)
    geodescode = models.TextField(blank=True, null=True)
    denominator = models.TextField(blank=True, null=True)
    distancevalue = models.TextField(blank=True, null=True)
    distanceuom = models.TextField(blank=True, null=True)
    wkt_geometry = models.TextField(blank=True, null=True)
    servicetype = models.TextField(blank=True, null=True)
    servicetypeversion = models.TextField(blank=True, null=True)
    operation = models.TextField(blank=True, null=True)
    couplingtype = models.TextField(blank=True, null=True)
    operateson = models.TextField(blank=True, null=True)
    operatesonidentifier = models.TextField(blank=True, null=True)
    operatesoname = models.TextField(blank=True, null=True)
    degree = models.TextField(blank=True, null=True)
    classification = models.TextField(blank=True, null=True)
    conditionapplyingtoaccessanduse = models.TextField(blank=True, null=True)
    lineage = models.TextField(blank=True, null=True)
    responsiblepartyrole = models.TextField(blank=True, null=True)
    specificationtitle = models.TextField(blank=True, null=True)
    specificationdate = models.TextField(blank=True, null=True)
    specificationdatetype = models.TextField(blank=True, null=True)
    platform = models.TextField(blank=True, null=True)
    instrument = models.TextField(blank=True, null=True)
    sensortype = models.TextField(blank=True, null=True)
    cloudcover = models.TextField(blank=True, null=True)
    bands = models.TextField(blank=True, null=True)
    links = models.TextField(blank=True, null=True)
    contacts = models.TextField(blank=True, null=True)
    # anytext_tsvector = models.TextField(blank=True, null=True)  # This field type is a guess.
    # wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'records'


from owslib.csw import CatalogueServiceWeb
from metadatamanager import settings

class product(models.Model):
    #fileIdentifier = models.UUIDField(
         #default = uuid.uuid4,
         #editable = True)
    xmlFile = models.FileField(upload_to="metadata")
    dataFile = models.FileField(upload_to="data")
    csw_record = models.OneToOneField(
        Records,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )


    def __str__(self):
        return f"{self.xmlFile} {self.csw_record}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.
        self.CSW_add()


    """Adds the current product to the csw server or csw queue."""
    def CSW_add(self):
        #import to PyCSW
        pass
        #csw = CatalogueServiceWeb(settings.CSW_server)
        #use the uuid to link products to records
        #csw.transaction(ttype='insert', typename='gmd:MD_Metadata', record=open(self.xmlFile.path).read().encode())

    """Deletes the current product from the csw server."""
    def CSW_delete(self):
        pass

    """Updates the current product from the csw server."""
    def CSW_update(self):
        pass

    """Adds the current product to the WMS/WFS server."""
    def Geo_add(self):
        pass

    """Deletes the current product from the WMS/WFS server."""
    def Geo_delete(self):
        pass

    """Updates the current product on the WMS/WFS server."""
    def Geo_update(self):
        pass


#from django.db.models.signals import post_save
#from django.dispatch import receiver

#@receiver(post_save, sender=product)
#def my_handler(sender, **kwargs):
    #sender.CSW_add()
#    print('post save callback')

