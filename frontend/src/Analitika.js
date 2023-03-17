import React, { Component } from 'react';
import { BarChart, Bar, XAxis, YAxis } from 'recharts';

import './diagramm.css'


const base_url = "http://localhost:8000";

const setAct = (val) => {
    return {
        isLoaded: val.isLoaded,
        active: !val.active,
        reg: val.reg,
        obl: val.obl
    }
}

class Financies extends Component {
    constructor(props) {
        super(props);
        this.state = {
            isLoaded: false,
            active: true,
            reg: [],
            obl: []
          };
    }   

    componentDidMount() {
        fetch(base_url + "/sport-objects/finance/")
       .then(res => res.json())
       .then((result) => {
            this.setState({
                isLoaded: true,
                active: true,
                reg: result[0],
                obl: result[1]
            })
       })
    }

    render() {
        const Names = () => {
            let i = 0
            return this.state.reg.map((req) => {
                const res = (<p>{i}. {req.name}<br/></p>)
                i = i + 1
                return res
            })
        }
        const renderCustomBarLabel = ({ payload, x, y, width, height, value }) => {
            return <text x={x + width / 2} y={y} fill="#666" textAnchor="middle" dy={-6}>{`${value}`}</text>;
          };

        const styles = {
            position: "absolute",
            zIndex: 4,
        }

        const {isLoaded} = this.state;
        if (!isLoaded) {
            return (
                <div className={this.state.active ? 'diagramm active': 'diagramm'}>
                    <p>Loading...</p>;
                </div>
            )
        } else {
        return (
            <div>
                <div className={this.state.active ? 'diagramm active': 'diagramm'}>
                    <p>Общее финансирование в округах</p>       
                        <BarChart width={900} height={300} data={this.state.reg} style={styles} margin={{ top: 40, right: 0, bottom: 5, left: 50 }}>
                            <XAxis />
                            <YAxis />
                            <Bar dataKey="uv" barSize={30} fill="#8884d8" label={renderCustomBarLabel}/>
                        </BarChart>
                        <div className='names'><Names/></div>
                    </div>
                <button className={!this.state.active ? 'dbutton':'dbutton active'}  onClick={() => {this.setState(setAct(this.state, this.setState))}}>{this.state.active ? '<':'>'}</button>
            </div>
        )
        }
    }
}

export default Financies;