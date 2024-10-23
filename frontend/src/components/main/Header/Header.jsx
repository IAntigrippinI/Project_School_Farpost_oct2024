import './Header.css'
import burger from './../../../images/burger.png'
import heart from './../../../images/heart.svg'
import ButtonAddEvent from './ButtonAddEvent';

const Header = () => {
    return (
        <>
            <div className="header">
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
        </>
    );
}

export default Header;