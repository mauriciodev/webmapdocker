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

import MVT from 'ol/format/MVT.js';
import VectorTileLayer from 'ol/layer/VectorTile.js';
import VectorTileSource from 'ol/source/VectorTile.js';
import {Fill, Icon, Stroke, Style, Text} from 'ol/style.js';

var mapExtent=[-125, -55, 0, 15];
var bdgexHost="https://bdgex.eb.mil.br/"

const layers = [
    new TileLayer({
      source: new OSM(),
    }),
    //new TileLayer({
    //extent: mapExtent,
    //source: new TileWMS({
    //  url: 'http://localhost/mapcache',
    //  params: {'LAYERS': 'trecho_drenagem_l', 'TILED': true},
    //  serverType: 'geoserver',
    //  attributions: '© <a href="'+bdgexHost+'"> BDGEx </a>',
    //  // Countries have transparency, so do not fade tiles:
    //  transition: 0,
    //  }),
    //}),
    new VectorTileLayer({
      declutter: true,
      source: new VectorTileSource({
        format: new MVT(),
        url:
          //'https://{a-d}.tiles.mapbox.com/v4/mapbox.mapbox-streets-v6/' +
          //'{z}/{x}/{y}.vector.pbf?access_token=' +
          //key,
          'http://localhost/mapcache/gmaps/trecho_drenagem_l_g@g/{z}/{x}/{y}.mvt'
      }),
      //style: createMapboxStreetsV6Style(Style, Fill, Stroke, Icon, Text),
    }),
  ]

const map = new Map({
  layers: layers,
  controls: defaultControls().extend([
    //new ZoomToExtent({
    //  extent: mapExtent,
    //}),
    new ZoomSlider(),
    new OverviewMap(),
    new FullScreen(),
    new ScaleLine(),
    new Rotate(),
  ]),
  target: 'map',
  view: new View({
    //projection: 'EPSG:4326',
    center: [0, 0],
    zoom: 2,
  }),
});
