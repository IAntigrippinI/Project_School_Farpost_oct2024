import './ButtonBuy.css'

const ButtonBuy = ({ price }) => {
    return (
        <button className="eventcard-btn-btn-buy">
            {/* {price == 0 ? бесплатно : от {price}} */}
            {price == 0 ? <div>Бесплатно</div> : <div>от {price}</div>}
        </button>
    );
}

export default ButtonBuy;