import './SearchLine.css'
import findIcon from './../../../images/find-ico.png'

const SearchLine = () => {
    return (<div className='searchline-component'>
        <div className="searchline-input-block">
            <input className='searchline-input'></input>
        </div>
        <div className="searchline-ico-block">
            <img src={findIcon} className='searchline-ico'></img>
        </div>
    </div>
    );
}

export default SearchLine;