import { useState, useRef, useEffect } from 'react';
import { 
  YMaps, 
  Map,
  ZoomControl,
} from '@pbe/react-yandex-maps';

import Description from "./DescriptionComponent";
import PointsContainer from './PointsContainer';
import Financies from './Analitika';

function App() {
  const map = useRef(null);
  const [zoom, setZoom] = useState(9);
  const [center, setCenter] = useState([61.2185, 66.925]);
  const [oldCenter, setOldCenter] = useState([0,0]);
  const [currentPointData, setCurrentPointData] = useState(null);

  const OnClickPlaceMark = (point) => {
    setZoom(15)

    // для возможности повторного нажатия на метку
    setOldCenter([0,0])
    setCenter([point.coor_y, point.coor_x - 0.0216])

    setCurrentPointData(point)
  }

  useEffect(function ChangeCenter(){
    if (map.current && center !== oldCenter && currentPointData !== null) {
      map.current.setCenter(center, zoom)
    }
  });

  const DescOranalitik = () => {
    let res;
    if (currentPointData !== null) {
      res = <Description setCurrentPointData={setCurrentPointData} pointData={currentPointData} OnClickPlaceMark={OnClickPlaceMark}/>
    }
    else{
      res = <Financies />
    }

    return res
  }


  return (
    <YMaps query={{ mode: 'debug' }}>
      <div className='MapContainer'>
        <Map
          instanceRef={map}
          id='map'
          defaultState={{ center: center, zoom: zoom }}
        >
        <PointsContainer OnClickPlaceMark={OnClickPlaceMark}/>
        <div>
          <DescOranalitik />  
        </div>
        
        <ZoomControl 
          options={{
            position: {
              right: 10,
              left: "auto",
              bottom: 100,
              top: "auto"
            }
        }}/>
        </Map>
      </div>
    </YMaps>
  );
}

export default App;
