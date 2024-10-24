import './MainPage.css'
import burger from './../../../images/burger.png'
import heart from './../../../images/heart.svg'

import axios from 'axios';
import { useState, useEffect } from 'react';
import ButtonAddEvent from "./../../../components/main/Header/ButtonAddEvent";
import SearchLine from './../../../components/main/Header/SearchLine';
import CategoryFilter from './../../../components/main/Header/CategoryFilter';
import EventCard from '../../../components/main/EventCard';
import { api } from '../../../backend';

const MainPage = () => {
    const [category, setCategory] = useState(0)
    const [events, setEvents] = useState([])
    const [eventsByCategory, setEventsByCategory] = useState([])
    const [page, setPage] = useState(1)

    let categories = ['Концерты', "Впечатления", "Театры", "Детям", "Городское событие"]

    function fetchRec() {
        axios.get(`${api}/events?per_page=5`).then((resp) => {
            setEvents(resp.data)
        })
    }

    function fechCategory() {
        axios.get(`${api}/events?category=${category}&page=${page}&per_page=15`).then((resp) => {
            setEventsByCategory(resp.data)
        })
    }


    function ClickCat(e) {
        if (category == e.target.innerText) {
            setCategory(0)
        }
        else {

            setCategory(e.target.innerText)

        }
    }

    useEffect(fetchRec, [])
    useEffect(() => { fechCategory(); }, [category])
    return (
        <>
            <div className="main-page">
                <div className="header">
                    <div className="header-menu">
                        <div className="left-menu">
                            <div className="burger">
                                <img src={burger} />
                            </div>
                            <div className="place"> <div className="text-16-orange">Афиша</div>  <div className="text-9">Владивосток</div> </div>
                        </div>
                        <div className="items">
                            <div className="add-event-btn">
                                <ButtonAddEvent />
                            </div>
                            <div className="favorite">
                                <img src={heart} />
                            </div>
                        </div>
                    </div>
                    <div className="search-line">
                        <SearchLine />
                    </div>
                    <div className="categories">
                        {/* Концерты Впечатления Театры Детям Городское событие */}
                        {categories.map((el, key) => {
                            return <div onClick={ClickCat} className='header-cat-filter'><CategoryFilter key={key} text={el} /></div>
                        })}
                    </div>
                    <div className="header-choose-date-block">
                        <button className='header-choose-date-btn'>Выбрать дату</button>
                    </div>
                    <div className="header-calender">
                        Тут календарь
                    </div>


                </div>
                {category == 0 ?
                    <div className="events-block">
                        Название какоето
                        <div className="events-category-block">
                            {events.map((el, key) => { return <EventCard key={key} props={el} /> })}
                        </div>
                        Название какоето
                        <div className="events-category-block">
                            {events.map((el, key) => { return <EventCard key={key} props={el} /> })}
                        </div>
                        Название какоето
                        <div className="events-category-block">
                            {events.map((el, key) => { return <EventCard key={key} props={el} /> })}
                        </div>
                        Название какоето
                        <div className="events-category-block">
                            {events.map((el, key) => { return <EventCard key={key} props={el} /> })}
                        </div>
                    </div>
                    : <>
                        <h3>{category}</h3>
                        <div className="table-events">
                            {eventsByCategory.map((el, key) => {
                                // console.log(el)
                                return (<div className="event-cat-table"><EventCard props={el} /></div>)
                            })}
                        </div>

                    </>
                }
            </div>
        </>
    );
}

export default MainPage;