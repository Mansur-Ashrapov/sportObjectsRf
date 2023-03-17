import { Component} from 'react';

import './nav.css';


class Navbar extends Component {
    constructor(props) {
        super(props);
        this.state = {
            page: 1
        }
    }

    render () {
        const View = () => {
            if (this.state.page === 1) {
                return (
                    <div className='content'>
                        <a>{this.props.point.short_description}</a><br/>
                        <a>{this.props.point.detail_description}</a>
                    </div>
                )
            } else if (this.state.page === 2) {
                return (
                    <div className='content'>
                        <a>{this.props.point.kinds_of_sports}</a><br/>
                        <a>{this.props.point.type}</a>
                    </div>
                )
            } else {
                console.log(this.props.point)
                return (
                    
                    <div className='content'>
                        <a>Рабочие часы: { this.props.point.working_hours === null ? "информация отсутствует" : this.props.point.working_hours}</a><br/>
                        <a>Рабочие часы по выходным: { this.props.point.working_hours_sat === null ? "информация отсутствует" : this.props.point.working_hours_sat}</a><br/>
                        <a>Телефон: { this.props.point.phone === null ? "информация отсутствует" : this.props.point.phone}</a><br/>
                        <a>Почта: { this.props.point.email === null ? "информация отсутствует" : this.props.point.email}</a><br/>
                        <a>Адрес: { this.props.point.address === null ? "информация отсутствует" : this.props.point.address}</a><br/>
                        <a>Сайт: { this.props.point.url === null ? "информация отсутствует" : this.props.point.url}</a><br/>
                    </div>
                )
            }
        }

        return (
            <div>
                <button className={ this.state.page === 1? 'navbutton one active' : 'navbutton one'} onClick={()=>this.setState({page: 1})}>Описание</button>
                <button className={ this.state.page === 2? 'navbutton two active' : 'navbutton two'} onClick={()=>this.setState({page: 2})}>Спорт</button>
                <button className={ this.state.page === 3? 'navbutton active' : 'navbutton'} onClick={()=>this.setState({page: 3})}>Контакты</button>
                <View/>
            </div>
        )
    }
}

export default Navbar;