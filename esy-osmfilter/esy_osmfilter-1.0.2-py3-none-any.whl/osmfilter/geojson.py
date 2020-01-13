
# Experimental Module to export Ways and Nodes to GeoJson
# %%
'''
Sample of use:
filename='test.geojson'
export_geojson(Elements['pipeline']['Way'],Data,filename,jsontype='Line')
filename2='test2.geojson'
export_geojson(Elements['pipeline']['Node'],Data,filename2,jsontype='Point')
''' 
import json
def get_ref_properties(element):
    
    # for ref in element['tags']:
    #     print(ref)
    # print('--')
    print(element['tags'])
    return element['tags']

#%%
def get_ref_coordinates(element,Data):
    longs=[]
    lats=[]
    coordinates=[]
    for ref in element['refs']:
        longs.append(Data['Node'][str(ref)]['lonlat'][0])
        lats.append(Data['Node'][str(ref)]['lonlat'][1])
    for coords in zip(longs,lats):
        coordinates.append(list(coords))    
    return coordinates

def get_coordinates(element):
    coordinates=element['lonlat']
    return coordinates

#%%

def create_GeoJson_Points(elements,Data):    
    feature=[]
    for element in elements:
        feature.append({'type'        : 'Feature',
                        'geometry'    : 
                       {'type'        : 'Point',
                        'coordinates' : get_coordinates(elements[element])},
                        'properties'  : get_ref_properties(elements[element])})
                                  
    return feature  


def create_GeoJson_Lines(elements,Data):    
    feature=[]
    for element in elements:
        feature.append({'type'        : 'Feature',
                        'geometry'    : 
                       {'type'        : 'LineString',
                        'coordinates' : get_ref_coordinates(elements[element],Data)},
                        'properties'  : get_ref_properties(elements[element])})                   
    return feature  

def export_geojson(Elements,Data,filename,jsontype='Line'):
    ### Elements=Elements['pipeline']['Way']
    if jsontype=='Point' or jsontype=='Node':
        collection=create_GeoJson_Points(Elements,Data)
        output={'type': 'FeatureCollection','features': collection}
        open(filename,"w").write(json.dumps(output,indent=4))
    elif jsontype=='Line' or jsontype=='LineString':
        collection=create_GeoJson_Lines(Elements,Data)
        output={'type': 'FeatureCollection','features': collection}
        open(filename,"w").write(json.dumps(output,indent=4))
    else:
        print('No such jsontype')
    



    
    
