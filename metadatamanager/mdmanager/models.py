from django.db import models
import uuid
# Create your models here.

class metadata(models.Model):
    fileIdentifier = models.UUIDField(
         default = uuid.uuid4,
         editable = True)
    title = models.TextField(blank=False)
    xml = models.TextField(blank=False)

    def __str__(self):
         return f"{self.title} {self.fileIdentifier}"


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
    anytext_tsvector = models.TextField(blank=True, null=True)  # This field type is a guess.
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        db_table = 'records'
