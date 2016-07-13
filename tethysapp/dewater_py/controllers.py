from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json

from tethys_sdk.gizmos import *

@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    context = {}

    return render(request, 'dewater_py/home.html', context)
def tool(request):
    """
    Controller for the dewatering tool
    """
    # Define view options
    view_options = MVView(
        projection='EPSG:4326',
        center=[-111.64925, 40.24721],
        zoom=15.5,
        maxZoom=22,
        minZoom=2
    )

    # Define drawing options
    drawing_options = MVDraw(
        controls=['Delete', 'Move', 'Point', 'Box'],
        initial='Box',
        output_format='WKT'
    )

    # Define map view options
    map_view_options = MapView(
            height='600px',
            width='100%',
            controls=['ZoomSlider', 'Rotate', 'FullScreen',
                      {'MousePosition': {'projection': 'EPSG:4326'}},
                      {'ZoomToExtent': {'projection': 'EPSG:4326', 'extent': [-130, 22, -65, 54]}}],
            layers=[],
            view=view_options,
            basemap='OpenStreetMap',
            draw=drawing_options,
            legend=True
    )

    # Define Message Box for user feedback
    message_box = MessageBox(name='sampleModal',
                         title='Message Box Title',
                         message='Congratulations! This is a message box.',
                         dismiss_button='Nevermind',
                         affirmative_button='Proceed',
                         width=400,
                         affirmative_attributes='href=javascript:void(0);')

    # Define text input boxes for UI
    k = TextInput(display_text='Average Hydraulic Conductivity',
                  name='k',
                  initial='0.000231',
                  placeholder='e.g. 0.000231',
                  prepend='k =',
                  append='[ft/s]',
                  )
    bedrock = TextInput(display_text='Bedrock Elevation',
                  name='bedrock',
                  initial='0',
                  placeholder='e.g. 0',
                  prepend='Elev. =',
                  append='[ft]',
                  )
    iwte = TextInput(display_text='Initial Water Table Elevation',
                  name='iwte',
                  initial='100',
                  placeholder='e.g. 100',
                  prepend='Elev. =',
                  append='[ft]',
                  )
    q = TextInput(display_text='Total Combined Flow',
                  name='q',
                  initial='2',
                  placeholder='e.g. 2',
                  prepend='Q =',
                  append='[cfs]',
                  )
    dwte = TextInput(display_text='Desired Water Table Elevation',
                  name='dwte',
                  initial='70',
                  placeholder='e.g. 70',
                  prepend='Elev. =',
                  append='[ft]',
                  )

    execute = Button(display_text='Calculate Water Table Elevations',
                     attributes='onclick=app.verify()',
                     submit=True,
                     classes='btn-success')

    instructions = Button(display_text='Instructions',
                     attributes='onclick=app.dewater()',
                     submit=True)

    context = { 'page_id' : '1', 'map_view_options': map_view_options,
                'message_box':message_box,
                'k':k,
                'bedrock':bedrock,
                'iwte':iwte,
                'q':q,
                'dwte':dwte,
                'execute':execute,
                'instructions':instructions}

    return render(request, 'dewater_py/DewateringTool.html', context)

def generate_water_table(request):

    get_data = request.GET

    pXCoords = get_data['pXCoords']
    print pXCoords
    pYCoords = get_data['pYCoords']
    print pYCoords
    wXCoords = get_data['wXCoords']
    print wXCoords
    wYCoords = get_data['wYCoords']
    print wYCoords
    cellSide = get_data['cellSide']
    print cellSide
    waterTable = []

    # lat_list = numpy.arange(pXCoords[0], pXCoords[2], cellSide)
    # lon_list = numpy.arange(pYCoords[0], pYCoords[2], cellSide)

    # Create water table raster grid

    # This code builds the grid with the bounding box being the perimeter drawn by the user
    for long in xrange(pXCoords[0]-cellSide, pXCoords[2]+cellSide, cellSide):
        for lat in range(pYCoords[0]-cellSide, pYCoords[2]+cellSide, cellSide):
            waterTable.append({
                'type': 'Feature',
                'geometry': {
                    'type': 'Polygon',
                    'coordinates': [
                                    [   [long,lat],
                                        [long + cellSide, lat],
                                        [long + cellSide, lat + cellSide],
                                        [long, lat + cellSide],
                                        [long,lat]
                                    ]
                                   ]
                    },
                    'properties': {
                        'elevation' : elevationCalc(long,lat,wXCoords,wYCoords,cellSide),
                    }
            })

    test = json.dumps(waterTable)
    print test

    return JsonResponse({
        "sucess": "Data analysis complete!",
        "local_Water_Table": json.dumps(waterTable)
    })
    # context = {}
    #
    # return render(request, 'dewater/DewateringTool.html', context)

# Assign elevations to raster grid
def elevationCalc (long, lat, wXCoords,wYCoords,cellSide):
    wtElevation = 0.0


    return (wtElevation)



def user(request):
    """
    Controller for the software license page.
    """
    context = {'page_id' : '2'}

    return render(request, 'dewater_py/user.html', context)

def tech(request):
    """
    Controller for the software license page.
    """
    context = {'page_id' : '3'}

    return render(request, 'dewater_py/tech.html', context)

def license(request):
    """
    Controller for the software license page.
    """
    context = {'page_id' : '4'}

    return render(request, 'dewater_py/license.html', context)
