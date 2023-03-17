import { Component } from 'react';
import { Placemark } from '@pbe/react-yandex-maps';

class ObjectPoint extends Component {


    render () {
        return (
            <Placemark 
                key={this.props.point.id} 
                modules={['geoObject.addon.balloon']}
                geometry={[this.props.point.coor_y, this.props.point.coor_x]}
                properties={{
                balloonContentHeader: '',
                balloonContentBody: this.props.point.name,
                balloonContentFooter: ''
                }}
                options={{
                preset: 'islands#yellowStretchyIcon',
                }}
                onClick={() => this.props.OnClickPlaceMark(this.props.point)} 
          />
        )
    }
}

export default ObjectPoint;