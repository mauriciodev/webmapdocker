import Map from 'ol/Map.js';
import OSM from 'ol/source/OSM.js';
import TileLayer from 'ol/layer/Tile.js';
import TileWMS from 'ol/source/TileWMS.js';
import View from 'ol/View.js';
import MousePosition from 'ol/control/MousePosition.js';
import {createStringXY} from 'ol/coordinate.js';
import {ZoomToExtent, ZoomSlider, ScaleLine, Rotate, FullScreen, OverviewMap, defaults as defaultControls} from 'ol/control.js';
//import  from 'ol/control/OverviewMap.js';
//import  from 'ol/control/FullScreen.js';
//import ScaleLine from 'ol/control/ScaleLine.js';

var mapExtent=[-125, -55, 0, 15];
var bdgexHost="https://bdgex.eb.mil.br/"

const layers = [
    new TileLayer({
      source: new OSM(),
    }),
    new TileLayer({
    extent: mapExtent,
    source: new TileWMS({
      url: bdgexHost+'mapcache',
      params: {'LAYERS': 'ctm25', 'TILED': true},
      serverType: 'geoserver',
      attributions: '© <a href="'+bdgexHost+'"> BDGEx </a>',
      // Countries have transparency, so do not fade tiles:
      transition: 0,
      }),
    }),
  ]

const map = new Map({
  layers: layers,
  controls: defaultControls().extend([
    new ZoomToExtent({
      extent: mapExtent,
    }),
    new ZoomSlider(),
    new OverviewMap(),
    new FullScreen(),
    new ScaleLine(),
    new Rotate(),
  ]),
  target: 'map',
  view: new View({
    projection: 'EPSG:4326',
    center: [0, 0],
    zoom: 2,
  }),
});
