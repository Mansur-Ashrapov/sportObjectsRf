import { Component } from "react";
import { Clusterer } from "@pbe/react-yandex-maps";
import axios from "axios";

import ObjectPoint from "./ObjectPointComponent";

const base_url = "http://localhost:8000";

class PointsContainer extends Component {
    constructor(props) {
        super(props);
        this.state = {
            pointsData: null
        }
    } 

    componentDidMount() {
        axios.get(base_url + "/sport-objects/points/ru")
            .then( res => {
                    const points = res.data
                    this.setState({ pointsData: points })
                }
            )
        return null
    }

    render () {
        return (
            <Clusterer
                options={{
                preset: "islands#invertedVioletClusterIcons",
                groupByCoordinates: false,
                }}
            >
                { this.state.pointsData === null ? this.setState({ pointsData: [] }) : this.state.pointsData.map((point) => (
                    <ObjectPoint point={point} OnClickPlaceMark={this.props.OnClickPlaceMark}/>
                ))}
            </Clusterer>
        )
    }
}

export default PointsContainer;