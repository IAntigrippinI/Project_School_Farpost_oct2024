import './EventCard.css'
import heart from './../../images/heart.svg'
import likeIco from './../../images/Likee.png'
import DislikeIco from './../../images/Dislike.png'
import ButtonBuy from './ButtonBuy';


const EventCard = ({ key, props }) => {
    let poster_url = `https://static.vl.ru/afisha/$_217x295`
    return (<>
        <div className="eventcard-card">
            <div className="eventcard-window">
                <div className="eventcard-poster-block">
                    <img className='eventcard-poster' src={props.poster_url} />
                    {/* src={props.poster_url} */}
                    <div className="eventcard-hearh-place">
                        <img className='eventcard-heart' src={heart} />
                    </div>
                </div>
                <div className="eventcard-title">{props.title.slice(0, 45)}</div>
                <div className="eventcard-date">{props.date.replace('T', ' ').slice(5, -10)}</div>
                <div className="eventcard-place">Место проведения</div>
                <div className="eventcard-bottom">
                    <div className="eventcard-btn-buy">
                        <ButtonBuy price={props.price_to} />
                    </div>
                    <div className="eventcard-likes">
                        <img src={likeIco}></img> <div className='eventcard-eval'> {props.likes}</div>
                        <img src={DislikeIco}></img> <div className='eventcard-eval'>{props.dislikes}</div>

                    </div>
                </div>
            </div>
        </div>
    </>);
}

export default EventCard;