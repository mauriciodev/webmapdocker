#!/usr/bin/python3
import uuid, json
import zipfile
from osgeo import ogr, osr

class GeoImporter:
    def __init__(self, connection_string):
        self.connection_string = connection_string
    
    def importVectorFile(self, inputPath, epsg=4326, metadata_uuid='', schema_name='unknown', max_scale=10000000):
        
        with zipfile.ZipFile(inputPath,"r") as zip_ref:    
            relativepath, = zipfile.Path(zip_ref).iterdir() #get the root folder
        inputDS=ogr.Open(f"/vsizip/{relativepath.filename}")
        
        if metadata_uuid=='': metadata_uuid=str(uuid.uuid4())
        
        #connectionString = "PG:dbname='%s' user='%s' password='%s'" % (database,usr,pw)
        outDataSource = ogr.Open(self. connection_string)
        
        srs = osr.SpatialReference()
        srs.ImportFromEPSG(epsg)
        
        outLayerA = outDataSource.CreateLayer('polygons',srs, ogr.wkbMultiPolygon25D , ["OVERWRITE=YES"])
        outLayerL = outDataSource.CreateLayer('lines',srs, ogr.wkbMultiLineString25D , ["OVERWRITE=YES"])
        outLayerP = outDataSource.CreateLayer('points',srs, ogr.wkbMultiPoint25D , ["OVERWRITE=YES"])
        
        for layer in [outLayerA,outLayerL,outLayerP]:
            lname = layer.GetName()
            newField = ogr.FieldDefn("class_name", ogr.OFTString)
            newField.SetWidth(128)
            layer.CreateField(newField)

            newField = ogr.FieldDefn("schema_name", ogr.OFTString)
            newField.SetWidth(128)
            layer.CreateField(newField)

            sql=f"alter table {lname} \
                add column attribute_data jsonb, \
                add column metadata_uuid uuid, \
                add column max_visible_scale bigint;"
            outDataSource.ExecuteSQL(sql)
            
            outDataSource.ExecuteSQL(f"CREATE UNIQUE INDEX IF NOT EXISTS {lname}_class_idx ON lname (class_name)");
            outDataSource.ExecuteSQL(f"CREATE UNIQUE INDEX IF NOT EXISTS {lname}_schema_idx ON lname (schema_name)");
            
        
        del outDataSource 
        outDataSource = ogr.Open(self.connection_string, 1)
        layerMap={ogr.wkbMultiPolygon25D:"polygons", ogr.wkbMultiLineString25D:"lines", ogr.wkbMultiPoint25D:"points", ogr.wkbPolygon25D:"polygons", ogr.wkbLineString25D:"lines", ogr.wkbPoint25D:"points",  ogr.wkbPolygonZM:'polygons',   ogr.wkbLineStringZM:"lines", ogr.wkbPointZM:"points"}
        
        for layer in inputDS:
            class_name=layer.GetName()
            #Still need to find which of the 3 layers
            #print(layer.GetGeomType())
            outLayer = outDataSource.GetLayerByName(layerMap[layer.GetGeomType()])
            featureDefn = outLayer.GetLayerDefn()
            
            
            feat = layer.GetNextFeature()
            while feat is not None:
                jsondata=feat.ExportToJson()
                #converting from json string to python object so that we can get only the attributes later
                d=json.loads(jsondata) 
                attributes=json.dumps(d['properties'])
                #creating new feature
                feature = ogr.Feature(featureDefn)
                #copying the geometry to the new feature
                g=feat.GetGeometryRef().Clone()
                g.FlattenTo2D()
                g.Set3D(True)
                g.SetMeasured(False)
                if (g.GetGeometryType() == ogr.wkbPolygon25D):
                    g=ogr.ForceToMultiPolygon(g)
                if (g.GetGeometryType() == ogr.wkbPoint25D):
                    g=ogr.ForceToMultiPoint(g)
                if (g.GetGeometryType() == ogr.wkbLineString25D) or (g.GetGeometryType() == ogr.wkbLineString25D):
                    g=ogr.ForceToMultiLineString(g)
                        
                feature.SetGeometry(g)
                #storing the class name and the json attribute
                feature.SetField("class_name", class_name)
                feature.SetField("schema_name", schema_name)
                feature.SetField("attribute_data",attributes )
                feature.SetField("metadata_uuid",metadata_uuid )
                feature.SetField("max_visible_scale",max_scale )
                
                #saving on the database
                outLayer.CreateFeature(feature)
                feature = None
                feat = layer.GetNextFeature()
            feat=None
            
        
        del outLayer
        del outDataSource



        
