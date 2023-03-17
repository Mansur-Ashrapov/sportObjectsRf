import { Component } from 'react';
import axios from 'axios';
import Navbar from './NavigationDesc';

const base_url = "http://localhost:8000";

const setAct = (val) => {
    return { active: !val.active, pointData: val.pointData }
}

class Description extends Component {
    constructor(props) {
        super(props);
        this.state = {
            active: true,
            pointData: props.pointData
        };
    }

    componentDidMount() {
        axios.get(base_url + "/sport-objects/ru&" + this.state.pointData.id + "/")
            .then(res => {
                const data = res.data
                this.setState({ pointData: data })
            });
        console.log(this.context)
    }

     
    render() {
        return (
            <div>
                <button className={this.state.active? 'closeButton active': 'closeButton'} onClick={()=>{this.setState(setAct(this.state))}}>{this.state.active ? '<':'>'}</button>
                <div className={this.state.active? 'description active': 'description'}>
                    <button className='exitButton' onClick={()=>this.props.setCurrentPointData(null)}>{"X"}</button>
                    <Navbar point={this.state.pointData}/>
                </div>
            </div>
        )
    }
}

export default Description;